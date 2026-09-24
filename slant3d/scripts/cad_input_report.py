#!/usr/bin/env python3
"""Create a safe, read-only preflight report for common CAD and mesh inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


REPORT_SCHEMA_VERSION = "1.0"
MAX_XML_BYTES = 16 * 1024 * 1024
MAX_OBJ_SCAN_BYTES = 64 * 1024 * 1024
MAX_OBJ_LINE_BYTES = 1024 * 1024
MAX_ASCII_STL_SCAN_BYTES = 64 * 1024 * 1024
MAX_DXF_SCAN_BYTES = 64 * 1024 * 1024
MAX_STEP_ZIP_MEMBER_BYTES = 256 * 1024 * 1024
MAX_COMPRESSION_RATIO = 200
MAX_ZIP_MEMBERS = 10_000
MAX_3MF_COMPONENT_DEPTH = 128
MAX_3MF_COMPONENT_WORK = 100_000
THREE_MF_CORE_NAMESPACE = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
PACKAGE_RELATIONSHIPS_NAMESPACE = "http://schemas.openxmlformats.org/package/2006/relationships"
PACKAGE_CONTENT_TYPES_NAMESPACE = "http://schemas.openxmlformats.org/package/2006/content-types"
THREE_MF_MODEL_CONTENT_TYPE = "application/vnd.ms-package.3dmanufacturing-3dmodel+xml"
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
INKSCAPE_NAMESPACE = "http://www.inkscape.org/namespaces/inkscape"
PROPRIETARY_SUFFIXES = {
    ".sldprt": "solidworks-part",
    ".sldasm": "solidworks-assembly",
    ".f3d": "fusion-design",
    ".f3z": "fusion-assembly",
    ".ipt": "inventor-part",
    ".iam": "inventor-assembly",
    ".catpart": "catia-part",
    ".catproduct": "catia-assembly",
    ".x_t": "parasolid-text",
    ".x_b": "parasolid-binary",
}


@dataclass(frozen=True)
class Fingerprint:
    path: str
    size_bytes: int
    sha256: str
    suffix: str


@dataclass(frozen=True)
class Detection:
    format: str
    confidence: str
    fidelity_tier: str
    units: str
    recommended_backend: str
    details: dict[str, Any]
    warnings: tuple[str, ...]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _xml_namespace(tag: str) -> str | None:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") and "}" in tag else None


def _has_forbidden_xml_declaration(raw: bytes) -> bool:
    # Removing NULs makes ASCII XML keywords visible in UTF-16/UTF-32, both endian orders.
    normalized = raw.replace(b"\x00", b"").upper()
    return b"<!DOCTYPE" in normalized or b"<!ENTITY" in normalized


def _safe_xml_from_zip(archive: zipfile.ZipFile, member: zipfile.ZipInfo) -> ET.Element:
    if member.file_size > MAX_XML_BYTES:
        raise ValueError(f"XML member exceeds {MAX_XML_BYTES} bytes")
    compressed = max(member.compress_size, 1)
    if member.file_size / compressed > MAX_COMPRESSION_RATIO:
        raise ValueError("XML member compression ratio is suspicious")
    raw = archive.read(member)
    if _has_forbidden_xml_declaration(raw):
        raise ValueError("XML document declarations are not accepted")
    return ET.fromstring(raw)


def _inspect_fcstd(archive: zipfile.ZipFile, document: zipfile.ZipInfo) -> Detection:
    warnings: list[str] = []
    details: dict[str, Any] = {
        "container": "zip",
        "members": len(archive.infolist()),
        "has_gui_document": "GuiDocument.xml" in archive.namelist(),
        "has_thumbnail": any(name.lower().startswith("thumbnails/") for name in archive.namelist()),
    }
    confidence = "high"
    fidelity_tier = "native-parametric"
    detected_format = "fcstd"
    try:
        root = _safe_xml_from_zip(archive, document)
        if root.tag != "Document":
            raise ValueError("Document.xml root is not an unnamespaced FreeCAD Document")
        if not root.attrib.get("SchemaVersion", "").isdigit():
            raise ValueError("Document.xml has no plausible numeric SchemaVersion")
        objects = next((node for node in root if node.tag == "Objects"), None)
        object_nodes = [] if objects is None else [node for node in objects if node.tag == "Object"]
        types = Counter(
            node.attrib.get("type", node.attrib.get("typeid", "unknown")) for node in object_nodes
        )
        details.update(
            {
                "schema_version": root.attrib.get("SchemaVersion"),
                "program_version": root.attrib.get("ProgramVersion"),
                "object_count": len(object_nodes),
                "object_types": dict(sorted(types.items())),
            }
        )
    except (ET.ParseError, ValueError, KeyError) as error:
        warnings.append(f"Document.xml metadata was not parsed: {error}")
        confidence = "low"
        fidelity_tier = "detected-only"
        detected_format = "fcstd-candidate"
    return Detection(
        format=detected_format,
        confidence=confidence,
        fidelity_tier=fidelity_tier,
        units="document-defined-or-project-default",
        recommended_backend="FreeCADCmd",
        details=details,
        warnings=tuple(warnings),
    )


def _inspect_3mf(
    archive: zipfile.ZipFile,
    model: zipfile.ZipInfo,
    relationship_valid: bool,
    content_type_valid: bool,
) -> Detection:
    warnings: list[str] = []
    details: dict[str, Any] = {
        "container": "opc-zip",
        "members": len(archive.infolist()),
        "model_member": model.filename,
    }
    units = "unspecified"
    confidence = "high"
    fidelity_tier = "polygon-mesh"
    try:
        root = _safe_xml_from_zip(archive, model)
        if root.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}model":
            raise ValueError("3MF model root does not use the supported Core namespace")
        direct_children = {node.tag for node in root}
        if f"{{{THREE_MF_CORE_NAMESPACE}}}resources" not in direct_children:
            raise ValueError("3MF Core model is missing resources")
        if f"{{{THREE_MF_CORE_NAMESPACE}}}build" not in direct_children:
            raise ValueError("3MF Core model is missing build")
        units = root.attrib.get("unit", "millimeter")
        valid_units = {"micron", "millimeter", "centimeter", "inch", "foot", "meter"}
        if units not in valid_units:
            raise ValueError(f"Unsupported 3MF unit value: {units}")
        required_extensions = tuple(filter(None, root.attrib.get("requiredextensions", "").split()))
        counts = Counter(
            _local_name(node.tag)
            for node in root.iter()
            if node.tag.startswith(f"{{{THREE_MF_CORE_NAMESPACE}}}")
        )
        object_records: list[dict[str, Any]] = []
        geometry_warnings: list[str] = []
        resources = next(
            node for node in root if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}resources"
        )
        for object_node in resources:
            if object_node.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}object":
                continue
            record, record_warnings = _inspect_3mf_object(object_node)
            object_records.append(record)
            geometry_warnings.extend(record_warnings)
        object_ids = [record.get("id") for record in object_records]
        valid_object_ids = {value for value in object_ids if value}
        if len(valid_object_ids) != len(object_ids):
            geometry_warnings.append("3MF object IDs are missing or duplicated.")
        for record in object_records:
            for component in record.get("components", []):
                if component.get("object_id") not in valid_object_ids:
                    geometry_warnings.append(
                        f"3MF object {record.get('id') or '<missing-id>'} references an unknown component object."
                    )
        build = next(node for node in root if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}build")
        object_by_id = {record.get("id"): record for record in object_records if record.get("id")}
        bounds_cache: dict[str, dict[str, list[float]]] = {}
        bounds_budget = {"work": 0}
        bounds_budget_exceeded = False
        for record in object_records:
            resolved_bounds, bounds_error = _resolve_3mf_object_bounds(
                record.get("id"),
                object_by_id,
                set(),
                bounds_cache,
                bounds_budget,
                0,
            )
            record["resolved_bounds"] = resolved_bounds
            if bounds_error:
                if bounds_error not in geometry_warnings:
                    geometry_warnings.append(bounds_error)
                if "analysis budget exceeded" in bounds_error:
                    bounds_budget_exceeded = True
                    break
        if bounds_budget_exceeded:
            for record in object_records:
                record.setdefault("resolved_bounds", None)
        build_items = []
        for node in build:
            if node.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}item":
                continue
            object_id = node.attrib.get("objectid")
            raw_transform = node.attrib.get("transform")
            transform = _parse_3mf_transform(raw_transform)
            record = object_by_id.get(object_id)
            invalid_transform = raw_transform is not None and transform is None
            if object_id not in valid_object_ids:
                geometry_warnings.append("3MF build item references an unknown object ID.")
            if invalid_transform:
                geometry_warnings.append(f"3MF build item for object {object_id} has an invalid transform.")
            local_bounds = None if record is None else record.get("resolved_bounds")
            build_items.append(
                {
                    "object_id": object_id,
                    "transform": transform,
                    "invalid_transform": invalid_transform,
                    "transformed_bounds": _transform_bounds(local_bounds, transform)
                    if not invalid_transform
                    else None,
                }
            )
        if not object_records:
            geometry_warnings.append("3MF package contains no model objects.")
        if not build_items:
            geometry_warnings.append("3MF package contains no build items.")
        if object_records and not any(record.get("representation") == "mesh" for record in object_records):
            geometry_warnings.append("3MF package contains no directly inspectable mesh objects.")
        details.update(
            {
                "object_count": counts["object"],
                "mesh_count": counts["mesh"],
                "components_count": counts["components"],
                "triangle_count": counts["triangle"],
                "build_item_count": counts["item"],
                "required_extensions": required_extensions,
                "start_part_relationship_valid": relationship_valid,
                "model_content_type_valid": content_type_valid,
                "objects": object_records,
                "build_items": build_items,
                "geometry_analysis_complete": not geometry_warnings,
                "component_resolution_work": bounds_budget["work"],
                "component_resolution_budget_exceeded": bounds_budget_exceeded,
            }
        )
        if geometry_warnings:
            warnings.extend(geometry_warnings)
            confidence = "medium"
        if (
            not object_records
            or not build_items
            or not any(record.get("representation") == "mesh" for record in object_records)
            or len(valid_object_ids) != len(object_ids)
            or any(item["object_id"] not in valid_object_ids for item in build_items)
            or bounds_budget_exceeded
        ):
            confidence = "low"
            fidelity_tier = "detected-only"
        if required_extensions:
            warnings.append(
                "3MF declares required extensions; verify each extension before interpreting or converting the model."
            )
            confidence = "low"
            fidelity_tier = "detected-only"
        if not relationship_valid:
            warnings.append("3MF package has no valid StartPart relationship to the model part.")
            confidence = "low"
            fidelity_tier = "detected-only"
        if not content_type_valid:
            warnings.append("3MF package does not declare the required model content type.")
            confidence = "low"
            fidelity_tier = "detected-only"
    except (ET.ParseError, ValueError, KeyError, NotImplementedError) as error:
        warnings.append(f"3MF model metadata was not parsed: {error}")
        confidence = "low"
        fidelity_tier = "detected-only"
    warnings.append(
        "Inspect application-specific 3MF extensions before import; FreeCAD may flatten object hierarchy."
    )
    return Detection(
        format="3mf",
        confidence=confidence,
        fidelity_tier=fidelity_tier,
        units=units,
        recommended_backend="3MF package preflight, then an approved mesh backend",
        details=details,
        warnings=tuple(warnings),
    )


def _parse_3mf_transform(value: str | None) -> list[float] | None:
    if value is None:
        return None
    parts = value.split()
    if len(parts) != 12:
        return None
    try:
        transform = [float(part) for part in parts]
    except ValueError:
        return None
    return transform if all(math.isfinite(number) for number in transform) else None


def _point_bounds(points: list[tuple[float, float, float]]) -> dict[str, list[float]] | None:
    if not points:
        return None
    return {
        "minimum": [min(point[axis] for point in points) for axis in range(3)],
        "maximum": [max(point[axis] for point in points) for axis in range(3)],
    }


def _transform_bounds(
    bounds: dict[str, list[float]] | None,
    transform: list[float] | None,
) -> dict[str, list[float]] | None:
    if bounds is None:
        return None
    matrix = transform or [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    minimum, maximum = bounds["minimum"], bounds["maximum"]
    corners = [
        (x, y, z)
        for x in (minimum[0], maximum[0])
        for y in (minimum[1], maximum[1])
        for z in (minimum[2], maximum[2])
    ]
    transformed = [
        (
            x * matrix[0] + y * matrix[3] + z * matrix[6] + matrix[9],
            x * matrix[1] + y * matrix[4] + z * matrix[7] + matrix[10],
            x * matrix[2] + y * matrix[5] + z * matrix[8] + matrix[11],
        )
        for x, y, z in corners
    ]
    return _point_bounds(transformed)


def _union_bounds(bounds_list: list[dict[str, list[float]]]) -> dict[str, list[float]] | None:
    if not bounds_list:
        return None
    return {
        "minimum": [min(bounds["minimum"][axis] for bounds in bounds_list) for axis in range(3)],
        "maximum": [max(bounds["maximum"][axis] for bounds in bounds_list) for axis in range(3)],
    }


def _resolve_3mf_object_bounds(
    object_id: str | None,
    object_by_id: dict[str, dict[str, Any]],
    stack: set[str],
    cache: dict[str, dict[str, list[float]]],
    budget: dict[str, int],
    depth: int,
) -> tuple[dict[str, list[float]] | None, str | None]:
    if object_id is None or object_id not in object_by_id:
        return None, f"3MF object bounds reference unknown object ID {object_id or '<missing-id>'}."
    if object_id in cache:
        return cache[object_id], None
    budget["work"] += 1
    if depth > MAX_3MF_COMPONENT_DEPTH or budget["work"] > MAX_3MF_COMPONENT_WORK:
        return None, (
            "3MF component analysis budget exceeded "
            f"(maximum depth {MAX_3MF_COMPONENT_DEPTH}, maximum work {MAX_3MF_COMPONENT_WORK}); "
            "component bounds remain unverified."
        )
    if object_id in stack:
        return None, f"3MF component graph contains a cycle at object {object_id}."
    record = object_by_id[object_id]
    if record.get("representation") == "mesh":
        bounds = record.get("bounds")
        if bounds is not None:
            cache[object_id] = bounds
            return bounds, None
        return None, f"3MF mesh object {object_id} has no valid bounds."
    if record.get("representation") != "components":
        return None, f"3MF object {object_id} has no resolvable geometry."
    next_stack = set(stack)
    next_stack.add(object_id)
    component_bounds: list[dict[str, list[float]]] = []
    for component in record.get("components", []):
        child_id = component.get("object_id")
        budget["work"] += 1
        if budget["work"] > MAX_3MF_COMPONENT_WORK:
            return None, (
                "3MF component analysis budget exceeded "
                f"(maximum depth {MAX_3MF_COMPONENT_DEPTH}, maximum work {MAX_3MF_COMPONENT_WORK}); "
                "component bounds remain unverified."
            )
        child_bounds, error = _resolve_3mf_object_bounds(
            child_id,
            object_by_id,
            next_stack,
            cache,
            budget,
            depth + 1,
        )
        if error:
            return None, error
        transformed = _transform_bounds(child_bounds, component.get("transform"))
        if transformed is None:
            return None, f"3MF component {child_id} in object {object_id} has unresolved bounds."
        component_bounds.append(transformed)
    combined = _union_bounds(component_bounds)
    if combined is None:
        return None, f"3MF component object {object_id} contains no resolvable components."
    cache[object_id] = combined
    return combined, None


def _triangle_is_degenerate(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
    third: tuple[float, float, float],
) -> bool:
    ab = tuple(second[index] - first[index] for index in range(3))
    ac = tuple(third[index] - first[index] for index in range(3))
    cross = (
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    )
    return sum(value * value for value in cross) <= 1e-24


def _inspect_3mf_object(object_node: ET.Element) -> tuple[dict[str, Any], list[str]]:
    object_id = object_node.attrib.get("id")
    record: dict[str, Any] = {
        "id": object_id,
        "name": object_node.attrib.get("name"),
        "type": object_node.attrib.get("type", "model"),
    }
    warnings: list[str] = []
    mesh = next(
        (node for node in object_node if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}mesh"),
        None,
    )
    components = next(
        (node for node in object_node if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}components"),
        None,
    )
    if mesh is not None:
        vertices_node = next(
            (node for node in mesh if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}vertices"),
            None,
        )
        triangles_node = next(
            (node for node in mesh if node.tag == f"{{{THREE_MF_CORE_NAMESPACE}}}triangles"),
            None,
        )
        vertices: list[tuple[float, float, float] | None] = []
        invalid_vertices = 0
        if vertices_node is not None:
            for node in vertices_node:
                if node.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}vertex":
                    continue
                try:
                    point = tuple(float(node.attrib[axis]) for axis in ("x", "y", "z"))
                except (KeyError, ValueError):
                    point = None
                if point is None or not all(math.isfinite(value) for value in point):
                    vertices.append(None)
                    invalid_vertices += 1
                else:
                    vertices.append(point)
        edge_use: Counter[tuple[int, int]] = Counter()
        triangles = 0
        invalid_triangles = 0
        degenerate_triangles = 0
        used_vertices: set[int] = set()
        parents = list(range(len(vertices)))

        def find(index: int) -> int:
            while parents[index] != index:
                parents[index] = parents[parents[index]]
                index = parents[index]
            return index

        def union(first: int, second: int) -> None:
            left, right = find(first), find(second)
            if left != right:
                parents[right] = left

        if triangles_node is not None:
            for node in triangles_node:
                if node.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}triangle":
                    continue
                triangles += 1
                try:
                    indexes = tuple(int(node.attrib[key]) for key in ("v1", "v2", "v3"))
                except (KeyError, ValueError):
                    invalid_triangles += 1
                    continue
                if (
                    len(set(indexes)) != 3
                    or any(index < 0 or index >= len(vertices) for index in indexes)
                    or any(vertices[index] is None for index in indexes)
                ):
                    invalid_triangles += 1
                    continue
                points = [vertices[index] for index in indexes]
                assert all(point is not None for point in points)
                typed_points = [point for point in points if point is not None]
                if _triangle_is_degenerate(*typed_points):
                    degenerate_triangles += 1
                for first, second in zip(indexes, indexes[1:] + indexes[:1]):
                    edge_use[tuple(sorted((first, second)))] += 1
                    union(first, second)
                used_vertices.update(indexes)
        valid_points = [point for point in vertices if point is not None]
        record.update(
            {
                "representation": "mesh",
                "vertex_count": len(vertices),
                "invalid_vertex_count": invalid_vertices,
                "triangle_count": triangles,
                "invalid_triangle_count": invalid_triangles,
                "degenerate_triangle_count": degenerate_triangles,
                "boundary_edge_count": sum(count == 1 for count in edge_use.values()),
                "non_manifold_edge_count": sum(count > 2 for count in edge_use.values()),
                "connected_components": len({find(index) for index in used_vertices}),
                "bounds": _point_bounds(valid_points),
            }
        )
        if invalid_vertices or invalid_triangles:
            warnings.append(
                f"3MF object {object_id or '<missing-id>'} contains invalid vertices or triangle references."
            )
        if degenerate_triangles:
            warnings.append(
                f"3MF object {object_id or '<missing-id>'} contains degenerate triangles."
            )
        if not vertices or not triangles:
            warnings.append(f"3MF object {object_id or '<missing-id>'} has empty mesh geometry.")
        if record["boundary_edge_count"]:
            warnings.append(
                f"3MF object {object_id or '<missing-id>'} has {record['boundary_edge_count']} boundary edges."
            )
        if record["non_manifold_edge_count"]:
            warnings.append(
                f"3MF object {object_id or '<missing-id>'} has {record['non_manifold_edge_count']} non-manifold edges."
            )
    elif components is not None:
        component_records = []
        invalid_transforms = 0
        for node in components:
            if node.tag != f"{{{THREE_MF_CORE_NAMESPACE}}}component":
                continue
            raw_transform = node.attrib.get("transform")
            transform = _parse_3mf_transform(raw_transform)
            if raw_transform is not None and transform is None:
                invalid_transforms += 1
            component_records.append(
                {"object_id": node.attrib.get("objectid"), "transform": transform}
            )
        record.update(
            {
                "representation": "components",
                "components": component_records,
                "invalid_transform_count": invalid_transforms,
            }
        )
        if invalid_transforms:
            warnings.append(f"3MF object {object_id or '<missing-id>'} has invalid component transforms.")
    else:
        record["representation"] = "none"
        warnings.append(f"3MF object {object_id or '<missing-id>'} has neither mesh nor components.")
    return record, warnings


def _resolve_3mf_model(
    archive: zipfile.ZipFile,
    members: dict[str, zipfile.ZipInfo],
) -> tuple[zipfile.ZipInfo | None, bool]:
    relationship = members.get("_rels/.rels")
    if relationship is None:
        fallback = next((entry for name, entry in members.items() if name.endswith("3dmodel.model")), None)
        return fallback, False
    try:
        root = _safe_xml_from_zip(archive, relationship)
    except (ET.ParseError, ValueError, KeyError, NotImplementedError):
        return None, False
    for node in root.iter():
        if node.tag != f"{{{PACKAGE_RELATIONSHIPS_NAMESPACE}}}Relationship":
            continue
        relation_type = node.attrib.get("Type", "").lower()
        target = node.attrib.get("Target", "").replace("\\", "/").lstrip("/").lower()
        if relation_type.endswith("/3dmodel") and ".." not in Path(target).parts:
            return members.get(target), target in members
    fallback = next((entry for name, entry in members.items() if name.endswith("3dmodel.model")), None)
    return fallback, False


def _has_3mf_model_content_type(
    archive: zipfile.ZipFile,
    member: zipfile.ZipInfo,
    model_name: str,
) -> bool:
    try:
        root = _safe_xml_from_zip(archive, member)
    except (ET.ParseError, ValueError, KeyError, NotImplementedError):
        return False
    if root.tag != f"{{{PACKAGE_CONTENT_TYPES_NAMESPACE}}}Types":
        return False
    normalized_model = "/" + model_name.replace("\\", "/").lstrip("/").lower()
    for node in root:
        if node.tag == f"{{{PACKAGE_CONTENT_TYPES_NAMESPACE}}}Default":
            if (
                node.attrib.get("Extension", "").lower() == "model"
                and node.attrib.get("ContentType", "").lower() == THREE_MF_MODEL_CONTENT_TYPE
            ):
                return True
        if node.tag == f"{{{PACKAGE_CONTENT_TYPES_NAMESPACE}}}Override":
            if (
                node.attrib.get("PartName", "").replace("\\", "/").lower() == normalized_model
                and node.attrib.get("ContentType", "").lower() == THREE_MF_MODEL_CONTENT_TYPE
            ):
                return True
    return False


def _inspect_stpz(archive: zipfile.ZipFile, entries: list[zipfile.ZipInfo]) -> Detection | None:
    step_entries = [entry for entry in entries if Path(entry.filename).suffix.lower() in {".step", ".stp"}]
    if len(step_entries) != 1:
        return None
    entry = step_entries[0]
    compressed = max(entry.compress_size, 1)
    if entry.file_size > MAX_STEP_ZIP_MEMBER_BYTES or entry.file_size / compressed > MAX_COMPRESSION_RATIO:
        return Detection(
            "stpz-candidate",
            "low",
            "detected-only",
            "unknown",
            "FreeCADCmd",
            {"step_member": entry.filename},
            ("Compressed STEP member exceeds safe preflight limits.",),
        )
    try:
        with archive.open(entry) as stream:
            head = stream.read(1024 * 1024)
            stream.seek(max(entry.file_size - 1024 * 1024, 0))
            tail = stream.read(1024 * 1024)
    except (OSError, RuntimeError, NotImplementedError) as error:
        return Detection(
            "stpz-candidate",
            "low",
            "detected-only",
            "unknown",
            "FreeCADCmd",
            {"step_member": entry.filename},
            (f"Compressed STEP member could not be sampled: {error}",),
        )
    if not _looks_like_step(head, tail):
        if head.lstrip().upper().startswith(b"ISO-10303-21;"):
            return Detection(
                "stpz-candidate",
                "low",
                "detected-only",
                "unknown",
                "FreeCADCmd",
                {"step_member": entry.filename, "uncompressed_size_bytes": entry.file_size},
                ("Compressed STEP envelope is structurally incomplete; require a successful parser load.",),
            )
        return None
    return Detection(
        "stpz",
        "medium",
        "exact-brep",
        "file-defined",
        "FreeCADCmd",
        {"step_member": entry.filename, "uncompressed_size_bytes": entry.file_size},
        ("Compressed STEP envelope was sampled; require a successful FreeCAD/Open CASCADE parse.",),
    )


def _detect_zip(path: Path) -> Detection | None:
    if not zipfile.is_zipfile(path):
        return None
    try:
        with zipfile.ZipFile(path) as archive:
            entries = archive.infolist()
            if len(entries) > MAX_ZIP_MEMBERS:
                return Detection(
                    "suspicious-zip",
                    "high",
                    "unsupported",
                    "unknown",
                    "none",
                    {"members": len(entries)},
                    (f"ZIP contains more than {MAX_ZIP_MEMBERS} members.",),
                )
            normalized_names = [entry.filename.replace("\\", "/").lower() for entry in entries]
            if len(normalized_names) != len(set(normalized_names)):
                return Detection(
                    "suspicious-zip",
                    "high",
                    "unsupported",
                    "unknown",
                    "none",
                    {"members": len(entries)},
                    ("ZIP contains duplicate case-insensitive member names.",),
                )
            members = {name: entry for name, entry in zip(normalized_names, entries)}
            document = members.get("document.xml")
            if document is not None:
                return _inspect_fcstd(archive, document)
            model, relationship_valid = _resolve_3mf_model(archive, members)
            content_types = members.get("[content_types].xml")
            if content_types is not None and model is not None:
                content_type_valid = _has_3mf_model_content_type(
                    archive,
                    content_types,
                    model.filename,
                )
                return _inspect_3mf(archive, model, relationship_valid, content_type_valid)
            stpz = _inspect_stpz(archive, entries)
            if stpz is not None:
                return stpz
            suffix = path.suffix.lower()
            if suffix in PROPRIETARY_SUFFIXES:
                return Detection(
                    PROPRIETARY_SUFFIXES[suffix],
                    "low",
                    "detected-only",
                    "unknown",
                    "installed licensed authoring application or approved importer",
                    {"container": "zip", "members": len(members)},
                    ("Unrecognized ZIP container; the proprietary suffix is only a routing hint.",),
                )
            if suffix in {".3mf", ".fcstd", ".stpz"}:
                return Detection(
                    f"{suffix[1:]}-candidate",
                    "low",
                    "detected-only",
                    "unknown",
                    "format-specific approved parser",
                    {"container": "zip", "members": len(members)},
                    ("ZIP container does not contain the required structure for its declared format.",),
                )
            return Detection(
                "zip-container",
                "high",
                "unsupported",
                "unknown",
                "none",
                {"members": len(members)},
                ("ZIP container is neither a recognized FCStd document nor a valid-looking 3MF package.",),
            )
    except (OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile) as error:
        return Detection(
            "invalid-zip",
            "high",
            "unsupported",
            "unknown",
            "none",
            {},
            (f"ZIP container could not be read: {error}",),
        )


def _valid_iges_record(line: bytes, section: bytes) -> bool:
    return (
        len(line) >= 80
        and line[72:73] == section
        and line[73:80].strip().isdigit()
    )


def _looks_like_iges(head: bytes, tail: bytes) -> bool:
    head_lines = head.splitlines()[:100]
    tail_lines = tail.splitlines()[-100:]
    return any(_valid_iges_record(line, b"S") for line in head_lines) and any(
        _valid_iges_record(line, b"T") for line in tail_lines
    )


def _looks_like_step(head: bytes, tail: bytes) -> bool:
    upper = head.decode("utf-8", errors="ignore").lstrip("\ufeff\x00\t\r\n ").upper()
    tail_upper = tail.decode("utf-8", errors="ignore").upper()
    return (
        upper.startswith("ISO-10303-21;")
        and "HEADER;" in upper
        and "DATA;" in upper
        and "END-ISO-10303-21;" in tail_upper
    )


def _looks_like_brep(head: bytes, tail: bytes) -> bool:
    text = (head + b"\n" + tail).decode("utf-8", errors="ignore")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return (
        len(lines) >= 3
        and lines[0].upper() == "DBREP_DRAWABLESHAPE"
        and lines[1].upper().startswith("CASCADE TOPOLOGY")
        and any(line.upper().startswith("TSHAPES ") for line in lines[2:])
    )


def _looks_like_ascii_dxf(head: bytes, tail: bytes) -> bool:
    def pairs(raw: bytes) -> list[tuple[str, str]]:
        lines = raw.decode("utf-8", errors="ignore").lstrip("\ufeff").splitlines()
        return [(lines[index].strip(), lines[index + 1].strip()) for index in range(0, len(lines) - 1, 2)]

    head_pairs = pairs(head)
    tail_pairs = pairs(tail)
    return (
        bool(head_pairs)
        and head_pairs[0] == ("0", "SECTION")
        and any(code == "2" and value.upper() in {"HEADER", "CLASSES", "TABLES", "BLOCKS", "ENTITIES", "OBJECTS"}
                for code, value in head_pairs[:20])
        and any(code == "0" and value.upper() == "EOF" for code, value in tail_pairs[-20:])
    )


DXF_UNITS = {
    0: "unitless",
    1: "inch",
    2: "foot",
    3: "mile",
    4: "millimeter",
    5: "centimeter",
    6: "meter",
    7: "kilometer",
    8: "microinch",
    9: "mil",
    10: "yard",
    11: "angstrom",
    12: "nanometer",
    13: "micron",
    14: "decimeter",
}


def _read_ascii_dxf_pairs(path: Path) -> tuple[list[tuple[str, str]], list[str]]:
    warnings: list[str] = []
    size = path.stat().st_size
    if size > MAX_DXF_SCAN_BYTES:
        return [], [f"DXF exceeds the {MAX_DXF_SCAN_BYTES}-byte bounded-analysis limit."]
    raw = path.read_bytes()
    if b"\x00" in raw:
        return [], ["Binary or NUL-containing DXF is not supported by the static analyzer."]
    text = raw.decode("utf-8", errors="replace").lstrip("\ufeff")
    lines = text.splitlines()
    if len(lines) % 2:
        warnings.append("DXF has an unmatched trailing group-code line.")
        lines = lines[:-1]
    pairs: list[tuple[str, str]] = []
    invalid_codes = 0
    for index in range(0, len(lines), 2):
        code = lines[index].strip()
        value = lines[index + 1].strip()
        try:
            int(code)
        except ValueError:
            invalid_codes += 1
        pairs.append((code, value))
    if invalid_codes:
        warnings.append(f"DXF contains {invalid_codes} non-numeric group codes.")
    return pairs, warnings


def _dxf_float(value: str) -> float | None:
    try:
        number = float(value)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def _inspect_ascii_dxf(path: Path) -> Detection:
    pairs, warnings = _read_ascii_dxf_pairs(path)
    if not pairs:
        return Detection(
            "dxf-candidate",
            "low",
            "detected-only",
            "unknown",
            "static DXF inspection",
            {"scan_limit_bytes": MAX_DXF_SCAN_BYTES},
            tuple(warnings + ["Require a successful authorized DXF parser load."]),
        )

    sections: set[str] = set()
    section = ""
    header_values: dict[str, list[tuple[str, str]]] = {}
    current_header: str | None = None
    entities: list[tuple[str, list[tuple[str, str]]]] = []
    current_entity: tuple[str, list[tuple[str, str]]] | None = None
    table_layers: set[str] = set()
    current_table_record = ""

    for code, value in pairs:
        upper = value.upper()
        if code == "0" and upper == "SECTION":
            section = "__PENDING__"
            current_entity = None
            continue
        if section == "__PENDING__" and code == "2":
            section = upper
            sections.add(section)
            continue
        if code == "0" and upper == "ENDSEC":
            if current_entity is not None:
                entities.append(current_entity)
                current_entity = None
            section = ""
            continue
        if section == "HEADER":
            if code == "9":
                current_header = upper
                header_values.setdefault(current_header, [])
            elif current_header is not None:
                header_values[current_header].append((code, value))
        elif section == "TABLES":
            if code == "0":
                current_table_record = upper
            elif current_table_record == "LAYER" and code == "2":
                table_layers.add(value)
        elif section == "ENTITIES":
            if code == "0":
                if current_entity is not None:
                    entities.append(current_entity)
                current_entity = (upper, [])
            elif current_entity is not None:
                current_entity[1].append((code, value))
    if current_entity is not None:
        entities.append(current_entity)

    entity_counts = Counter(kind for kind, _ in entities)
    layers = set(table_layers)
    open_profiles = 0
    closed_profiles = 0
    profile_kinds = {"LINE", "ARC", "LWPOLYLINE", "POLYLINE", "SPLINE", "CIRCLE", "ELLIPSE"}
    unsupported_profile_entities: Counter[str] = Counter()
    for kind, values in entities:
        value_map: dict[str, list[str]] = {}
        for code, value in values:
            value_map.setdefault(code, []).append(value)
        layers.update(value_map.get("8", []))
        if kind == "CIRCLE":
            closed_profiles += 1
        elif kind in {"LWPOLYLINE", "POLYLINE", "SPLINE"}:
            try:
                flags = int(value_map.get("70", ["0"])[0])
            except ValueError:
                flags = 0
                warnings.append(f"DXF {kind} has an invalid flags value.")
            if flags & 1:
                closed_profiles += 1
            else:
                open_profiles += 1
        elif kind == "ELLIPSE":
            start = _dxf_float(value_map.get("41", ["0"])[0])
            end = _dxf_float(value_map.get("42", [str(2 * math.pi)])[0])
            if start is not None and end is not None and abs((end - start) - 2 * math.pi) < 1e-6:
                closed_profiles += 1
            else:
                open_profiles += 1
        elif kind in {"LINE", "ARC"}:
            open_profiles += 1
        elif kind not in profile_kinds and kind not in {"VERTEX", "SEQEND"}:
            unsupported_profile_entities[kind] += 1

    units_code = None
    for code, value in header_values.get("$INSUNITS", []):
        if code in {"70", "280"}:
            try:
                units_code = int(value)
            except ValueError:
                warnings.append("DXF $INSUNITS is not numeric.")
            break
    units = DXF_UNITS.get(units_code, "file-defined-or-unknown")
    if units_code in {None, 0}:
        warnings.append("DXF scale is ambiguous because $INSUNITS is missing or unitless.")

    def header_point(name: str) -> list[float] | None:
        coordinates: dict[str, float] = {}
        for code, value in header_values.get(name, []):
            if code in {"10", "20", "30"}:
                number = _dxf_float(value)
                if number is not None:
                    coordinates[code] = number
        if "10" not in coordinates or "20" not in coordinates:
            return None
        return [coordinates["10"], coordinates["20"], coordinates.get("30", 0.0)]

    minimum, maximum = header_point("$EXTMIN"), header_point("$EXTMAX")
    if minimum is None or maximum is None:
        warnings.append("DXF does not provide complete declared $EXTMIN/$EXTMAX bounds.")
    warnings.append("DXF is analysis-only in this skill; no 3D reconstruction or extrusion is permitted.")
    details: dict[str, Any] = {
        "sections": sorted(sections),
        "entity_counts": dict(sorted(entity_counts.items())),
        "layers": sorted(layer for layer in layers if layer),
        "open_profile_candidates": open_profiles,
        "closed_profile_candidates": closed_profiles,
        "declared_bounds": None if minimum is None or maximum is None else {"minimum": minimum, "maximum": maximum},
        "insunits_code": units_code,
        "unsupported_entity_counts": dict(sorted(unsupported_profile_entities.items())),
        "analysis_scope": "static 2D metadata and profile-candidate inspection only",
    }
    confidence = "medium" if any("invalid" in warning.lower() for warning in warnings) else "high"
    return Detection(
        "dxf",
        confidence,
        "2d-reference",
        units,
        "static DXF inspection",
        details,
        tuple(warnings),
    )


def _detect_binary_stl(path: Path, header: bytes) -> tuple[bool, int, str | None]:
    if len(header) < 84:
        return False, 0, None
    triangle_count = struct.unpack("<I", header[80:84])[0]
    expected = 84 + 50 * triangle_count
    actual = path.stat().st_size
    if triangle_count == 0 and expected == actual:
        return False, 0, "Binary STL contains no triangles."
    if len(header) < 134:
        return False, triangle_count, "Binary STL does not contain a complete first triangle record."
    if expected == actual:
        with path.open("rb") as stream:
            stream.seek(84)
            for index in range(triangle_count):
                record = stream.read(50)
                if len(record) != 50:
                    return False, triangle_count, f"Binary STL triangle {index} is truncated."
                values = struct.unpack("<12f", record[:48])
                if not all(math.isfinite(value) for value in values):
                    return False, triangle_count, f"Binary STL triangle {index} contains non-finite coordinates."
        return True, triangle_count, None
    if path.suffix.lower() == ".stl" and actual >= 84:
        return False, triangle_count, f"Binary STL length mismatch: expected {expected}, found {actual}."
    return False, triangle_count, None


def _detect_text_format(head: bytes, tail: bytes) -> Detection | None:
    text = head.decode("utf-8", errors="ignore")
    stripped = text.lstrip("\ufeff\x00\t\r\n ")
    upper = stripped.upper()
    tail_upper = tail.decode("utf-8", errors="ignore").upper()
    if _looks_like_step(head, tail):
        return Detection("step", "high", "exact-brep", "file-defined", "FreeCADCmd", {}, ())
    if _looks_like_iges(head, tail):
        return Detection(
            "iges-candidate",
            "low",
            "detected-only",
            "file-defined-or-unknown",
            "FreeCADCmd",
            {},
            ("IGES envelope markers were found; require a successful parser load and check whether surfaces sew into solids.",),
        )
    if _looks_like_brep(head, tail):
        return Detection("brep", "high", "exact-brep", "document-space", "FreeCADCmd", {}, ())
    if _looks_like_ascii_dxf(head, tail):
        return Detection(
            "dxf",
            "high",
            "2d-reference",
            "file-defined-or-unknown",
            "FreeCAD 2D importer",
            {},
            ("DXF is analysis-only in this skill; no 3D reconstruction or extrusion is permitted.",),
        )
    return None


def _detect_ascii_stl(path: Path) -> Detection | None:
    if path.stat().st_size > MAX_ASCII_STL_SCAN_BYTES:
        return None
    state = "solid"
    facet_count = 0
    with path.open("r", encoding="utf-8", errors="strict") as stream:
        for raw_line in stream:
            line = raw_line.strip()
            if not line:
                continue
            parts = line.split()
            lowered = [part.lower() for part in parts]
            if state == "solid" and lowered[0] == "solid":
                state = "facet"
            elif state == "facet" and lowered[:2] == ["facet", "normal"] and len(parts) == 5:
                try:
                    values = [float(value) for value in parts[2:]]
                except ValueError:
                    return None
                if not all(math.isfinite(value) for value in values):
                    return None
                state = "outer"
            elif state == "outer" and lowered == ["outer", "loop"]:
                state = "vertex1"
            elif state in {"vertex1", "vertex2", "vertex3"} and lowered[0] == "vertex" and len(parts) == 4:
                try:
                    values = [float(value) for value in parts[1:]]
                except ValueError:
                    return None
                if not all(math.isfinite(value) for value in values):
                    return None
                state = {"vertex1": "vertex2", "vertex2": "vertex3", "vertex3": "endloop"}[state]
            elif state == "endloop" and lowered == ["endloop"]:
                state = "endfacet"
            elif state == "endfacet" and lowered == ["endfacet"]:
                facet_count += 1
                state = "facet"
            elif state == "facet" and lowered[0] == "endsolid" and facet_count > 0:
                state = "done"
            else:
                return None
    if state != "done":
        return None
    return Detection(
        "stl-ascii",
        "high",
        "polygon-mesh",
        "unitless",
        "Blender",
        {"facet_count": facet_count, "validated_bytes": path.stat().st_size},
        (),
    )


def _detect_xml(path: Path) -> Detection | None:
    size = path.stat().st_size
    if size == 0 or size > MAX_XML_BYTES:
        return None
    raw = path.read_bytes()
    if _has_forbidden_xml_declaration(raw):
        return Detection(
            "unsafe-xml",
            "high",
            "unsupported",
            "unknown",
            "none",
            {},
            ("XML document declarations are not accepted.",),
        )
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return None
    root_name = _local_name(root.tag).lower()
    if root_name == "svg" and _xml_namespace(root.tag) in {None, SVG_NAMESPACE}:
        return _inspect_svg(root)
    if root_name == "amf":
        return Detection(
            "amf",
            "high",
            "detected-only",
            "file-defined-or-unknown",
            "approved external converter",
            {},
            ("Current FreeCAD documentation lists AMF export but not import; request 3MF, STL, or STEP.",),
        )
    return None


def _parse_svg_length(value: str | None) -> tuple[float | None, str | None]:
    if value is None:
        return None, None
    match = re.fullmatch(
        r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*([a-zA-Z%]*)\s*",
        value,
    )
    if match is None:
        return None, None
    number = float(match.group(1))
    if not math.isfinite(number):
        return None, None
    return number, match.group(2).lower() or None


def _inspect_svg(root: ET.Element) -> Detection:
    warnings: list[str] = []
    width, width_unit = _parse_svg_length(root.attrib.get("width"))
    height, height_unit = _parse_svg_length(root.attrib.get("height"))
    view_box: list[float] | None = None
    raw_view_box = root.attrib.get("viewBox") or root.attrib.get("viewbox")
    if raw_view_box:
        try:
            parsed = [float(value) for value in re.split(r"[\s,]+", raw_view_box.strip())]
        except ValueError:
            parsed = []
        if len(parsed) == 4 and all(math.isfinite(value) for value in parsed):
            view_box = parsed
        else:
            warnings.append("SVG viewBox is invalid or incomplete.")

    element_counts: Counter[str] = Counter()
    layers: list[dict[str, str | None]] = []
    transform_count = 0
    open_profiles = 0
    closed_profiles = 0
    ambiguous_paths = 0
    supported_geometry = {"path", "line", "polyline", "polygon", "rect", "circle", "ellipse"}
    unsupported_geometry = {"text", "image", "use", "foreignObject"}
    unsupported_counts: Counter[str] = Counter()
    for node in root.iter():
        name = _local_name(node.tag)
        element_counts[name] += 1
        if "transform" in node.attrib:
            transform_count += 1
        if name == "g" and node.attrib.get(f"{{{INKSCAPE_NAMESPACE}}}groupmode") == "layer":
            layers.append(
                {
                    "id": node.attrib.get("id"),
                    "label": node.attrib.get(f"{{{INKSCAPE_NAMESPACE}}}label"),
                }
            )
        if name in {"line", "polyline"}:
            open_profiles += 1
        elif name in {"polygon", "rect", "circle", "ellipse"}:
            closed_profiles += 1
        elif name == "path":
            path_data = node.attrib.get("d", "")
            if re.search(r"(?<![A-Za-z])[zZ](?![A-Za-z])", path_data):
                closed_profiles += 1
            elif path_data.strip():
                open_profiles += 1
            else:
                ambiguous_paths += 1
        elif name in unsupported_geometry:
            unsupported_counts[name] += 1

    physical_units = {"mm", "cm", "in", "pt", "pc", "q"}
    declared_units = {unit for unit in (width_unit, height_unit) if unit}
    if not declared_units or not declared_units.issubset(physical_units):
        warnings.append(
            "SVG physical scale is ambiguous unless width and height use compatible physical units and agree with viewBox."
        )
        units = "file-defined-or-unknown"
    elif len(declared_units) > 1:
        warnings.append("SVG width and height use different physical units; normalize scale before use.")
        units = "mixed"
    else:
        units = next(iter(declared_units))
    if transform_count:
        warnings.append("SVG contains transforms; preserve and resolve the transform stack during approved downstream import.")
    if unsupported_counts:
        warnings.append("SVG contains reference or presentation elements that are not converted into profile candidates.")
    if not any(element_counts[name] for name in supported_geometry):
        warnings.append("SVG contains no supported geometric profile elements.")
    warnings.append("SVG is analysis-only in this skill; no 3D reconstruction or extrusion is permitted.")
    return Detection(
        "svg",
        "high",
        "2d-reference",
        units,
        "static XML/SVG inspection",
        {
            "width": width,
            "height": height,
            "width_unit": width_unit,
            "height_unit": height_unit,
            "view_box": view_box,
            "element_counts": dict(sorted(element_counts.items())),
            "layers": layers,
            "transform_count": transform_count,
            "open_profile_candidates": open_profiles,
            "closed_profile_candidates": closed_profiles,
            "ambiguous_path_count": ambiguous_paths,
            "unsupported_element_counts": dict(sorted(unsupported_counts.items())),
            "analysis_scope": "static 2D metadata and profile-candidate inspection only",
        },
        tuple(warnings),
    )


def _standard_freecad_candidates() -> list[Path]:
    candidates: list[Path] = []
    if os.name == "nt":
        roots = {
            value
            for key in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)")
            if (value := os.environ.get(key))
        }
        for root in roots:
            candidates.extend(Path(root).glob("FreeCAD*/bin/FreeCADCmd.exe"))
    elif sys.platform == "darwin":
        candidates.extend(
            [
                Path("/Applications/FreeCAD.app/Contents/Resources/bin/FreeCADCmd"),
                Path.home() / "Applications/FreeCAD.app/Contents/Resources/bin/FreeCADCmd",
            ]
        )
    else:
        candidates.extend([Path("/snap/bin/freecadcmd"), Path("/usr/local/bin/freecadcmd")])
    return candidates


def _version_key(path: Path) -> tuple[int, ...]:
    versions = re.findall(r"\d+", " ".join(part for part in path.parts[-4:]))
    return tuple(int(value) for value in versions) or (0,)


def _find_freecad_backend() -> str | None:
    found = shutil.which("FreeCADCmd") or shutil.which("freecadcmd")
    if found:
        return str(Path(found).resolve())
    installed = [path for path in _standard_freecad_candidates() if path.is_file()]
    return str(max(installed, key=_version_key).resolve()) if installed else None


def _standard_blender_candidates() -> list[Path]:
    candidates: list[Path] = []
    if os.name == "nt":
        roots = {
            value
            for key in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)")
            if (value := os.environ.get(key))
        }
        for root in roots:
            candidates.extend(Path(root).glob("Blender Foundation/Blender*/blender.exe"))
    elif sys.platform == "darwin":
        candidates.extend(
            [
                Path("/Applications/Blender.app/Contents/MacOS/Blender"),
                Path.home() / "Applications/Blender.app/Contents/MacOS/Blender",
            ]
        )
    else:
        candidates.extend([Path("/snap/bin/blender"), Path("/usr/local/bin/blender")])
    return candidates


def _find_blender_backend() -> str | None:
    found = shutil.which("blender")
    if found:
        return str(Path(found).resolve())
    installed = [path for path in _standard_blender_candidates() if path.is_file()]
    return str(max(installed, key=_version_key).resolve()) if installed else None


def _valid_obj_vertex(parts: list[str]) -> bool:
    if len(parts) < 4:
        return False
    try:
        coordinates = [float(value) for value in parts[1:4]]
    except ValueError:
        return False
    return all(math.isfinite(value) for value in coordinates)


def _valid_obj_face(parts: list[str], vertex_count: int) -> bool:
    if len(parts) < 4:
        return False
    try:
        indexes = [int(value.split("/", 1)[0]) for value in parts[1:]]
    except (ValueError, IndexError):
        return False
    return all(
        (1 <= index <= vertex_count) if index > 0 else (1 <= -index <= vertex_count)
        for index in indexes
    )


def _detect_obj(path: Path) -> Detection | None:
    valid_vertices = 0
    valid_faces = 0
    invalid_vertices = 0
    invalid_faces = 0
    external_material_references: list[str] = []
    scanned_bytes = 0
    overlong_line = False
    reached_eof = False
    with path.open("rb") as stream:
        while scanned_bytes < MAX_OBJ_SCAN_BYTES:
            read_limit = min(MAX_OBJ_LINE_BYTES + 1, MAX_OBJ_SCAN_BYTES - scanned_bytes + 1)
            raw_line = stream.readline(read_limit)
            if not raw_line:
                reached_eof = True
                break
            scanned_bytes += len(raw_line)
            if scanned_bytes > MAX_OBJ_SCAN_BYTES:
                break
            if len(raw_line) > MAX_OBJ_LINE_BYTES:
                overlong_line = True
                break
            line = raw_line.decode("utf-8", errors="ignore").strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            keyword = parts[0].lower()
            if keyword == "v":
                if _valid_obj_vertex(parts):
                    valid_vertices += 1
                else:
                    invalid_vertices += 1
            elif keyword == "f":
                if _valid_obj_face(parts, valid_vertices):
                    valid_faces += 1
                else:
                    invalid_faces += 1
            elif keyword == "mtllib":
                external_material_references.append(line[len(parts[0]) :].strip())

    details = {
        "validated_vertex_lines": valid_vertices,
        "range_checked_face_lines": valid_faces,
        "invalid_vertex_lines": invalid_vertices,
        "invalid_face_lines": invalid_faces,
        "external_material_references": external_material_references,
        "validated_bytes": scanned_bytes,
        "full_file_scanned": reached_eof,
    }
    if external_material_references:
        return Detection(
            "obj-candidate",
            "low",
            "detected-only",
            "unitless",
            "none until external material references are removed on an approved working copy",
            details,
            (
                "OBJ declares external mtllib resources; automated import is blocked to prevent unintended local or network file access.",
            ),
        )
    if reached_eof and not overlong_line and valid_vertices >= 3 and valid_faces >= 1:
        if invalid_vertices or invalid_faces:
            return Detection(
                "obj-candidate",
                "low",
                "detected-only",
                "unitless",
                "Blender after repair approval",
                details,
                ("OBJ contains invalid or unresolved vertex/face records; repair requires approval.",),
            )
        return Detection(
            "obj",
            "high",
            "polygon-mesh",
            "unitless",
            "Blender",
            details,
            (),
        )
    if path.suffix.lower() == ".obj" and valid_vertices:
        warnings = ["OBJ face data was not validated within the bounded scan; require a successful parser load."]
        if overlong_line:
            warnings.append(f"OBJ contains a line longer than the {MAX_OBJ_LINE_BYTES}-byte safety limit.")
        return Detection(
            "obj-candidate",
            "low",
            "detected-only",
            "unitless",
            "Blender",
            {**details, "scan_limit_bytes": MAX_OBJ_SCAN_BYTES},
            tuple(warnings),
        )
    if path.suffix.lower() == ".obj" and overlong_line:
        return Detection(
            "obj-candidate",
            "low",
            "detected-only",
            "unitless",
            "Blender",
            {"scan_limit_bytes": MAX_OBJ_SCAN_BYTES, "line_limit_bytes": MAX_OBJ_LINE_BYTES},
            (f"OBJ contains a line longer than the {MAX_OBJ_LINE_BYTES}-byte safety limit.",),
        )
    return None


def detect(path: Path) -> Detection:
    zipped = _detect_zip(path)
    if zipped is not None:
        return zipped
    xml_detection = _detect_xml(path)
    if xml_detection is not None:
        return xml_detection
    with path.open("rb") as stream:
        head = stream.read(1024 * 1024)
        if path.stat().st_size > 1024 * 1024:
            stream.seek(max(path.stat().st_size - 1024 * 1024, 0))
            tail = stream.read(1024 * 1024)
        else:
            tail = head
    binary_stl, triangles, stl_warning = _detect_binary_stl(path, head[:134])
    if binary_stl:
        return Detection(
            "stl-binary",
            "high" if path.suffix.lower() == ".stl" else "medium",
            "polygon-mesh",
            "unitless",
            "Blender",
            {"triangle_count": triangles},
            (),
        )
    try:
        ascii_stl = _detect_ascii_stl(path)
    except (OSError, UnicodeError):
        ascii_stl = None
    if ascii_stl is not None:
        return ascii_stl
    textual = _detect_text_format(head, tail)
    if textual is not None:
        if textual.format == "dxf":
            return _inspect_ascii_dxf(path)
        return textual
    obj = _detect_obj(path)
    if obj is not None:
        return obj
    suffix = path.suffix.lower()
    if suffix in {".brep", ".brp"}:
        return Detection(
            "brep-candidate",
            "low",
            "detected-only",
            "unknown",
            "FreeCADCmd",
            {},
            ("BREP suffix was found, but content detection was inconclusive; require a successful parser load.",),
        )
    if suffix in PROPRIETARY_SUFFIXES:
        return Detection(
            PROPRIETARY_SUFFIXES[suffix],
            "low",
            "detected-only",
            "unknown",
            "installed licensed authoring application or approved importer",
            {},
            ("The suffix is only a routing hint; support requires a successful authorized parser load.",),
        )
    warnings = []
    if stl_warning:
        warnings.append(stl_warning)
    if suffix:
        warnings.append(f"Extension {suffix} did not match recognized file content.")
    else:
        warnings.append("File content was not recognized.")
    return Detection("unknown", "low", "unsupported", "unknown", "none", {}, tuple(warnings))


def analyze(path: Path) -> dict[str, Any]:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Input is not a regular file: {resolved}")
    fingerprint = Fingerprint(
        path=str(resolved),
        size_bytes=resolved.stat().st_size,
        sha256=_sha256(resolved),
        suffix=resolved.suffix.lower(),
    )
    detection = detect(resolved)
    backend_names = {
        "freecadcmd": _find_freecad_backend(),
        "freecad": shutil.which("FreeCAD") or shutil.which("freecad"),
        "blender": _find_blender_backend(),
    }
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "fingerprint": asdict(fingerprint),
        "detection": asdict(detection),
        "available_backends": backend_names,
        "limitations": [
            "This preflight identifies containers and basic structure; it does not prove geometric validity or printability.",
            "Exact CAD topology requires a successful FreeCAD/Open CASCADE parse.",
            "Mesh manifoldness and self-intersection checks require an approved mesh backend.",
        ],
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CAD, mesh, or 2D reference file to inspect")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = analyze(args.input)
    except (OSError, ValueError) as error:
        print(json.dumps({"schema_version": REPORT_SCHEMA_VERSION, "error": str(error)}, indent=2))
        return 2
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output = args.output.expanduser().resolve()
        if output == args.input.expanduser().resolve():
            print(json.dumps({"schema_version": REPORT_SCHEMA_VERSION, "error": "Output must not overwrite input."}, indent=2))
            return 2
        try:
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("x", encoding="utf-8") as stream:
                stream.write(payload + "\n")
        except OSError as error:
            print(json.dumps({"schema_version": REPORT_SCHEMA_VERSION, "error": str(error)}, indent=2))
            return 2
    print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
