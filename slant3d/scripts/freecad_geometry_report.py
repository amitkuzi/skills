#!/usr/bin/env python3
"""Read-only FreeCAD/Open CASCADE geometry report for FCStd and neutral CAD files."""

from __future__ import annotations

import argparse
import contextlib
import json
import math
import os
import re
import shutil
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any


SUPPORTED_SUFFIXES = {".fcstd", ".step", ".stp", ".stpz", ".iges", ".igs", ".brep", ".brp"}
MAX_STEP_ZIP_MEMBER_BYTES = 256 * 1024 * 1024
MAX_COMPRESSION_RATIO = 200


def _count(value: Any) -> int:
    try:
        return len(value)
    except (TypeError, AttributeError):
        return 0


def _number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _read_attribute(
    value: Any,
    name: str,
    default: Any = None,
    errors: list[str] | None = None,
) -> Any:
    try:
        return getattr(value, name, default)
    except (AttributeError, RuntimeError, TypeError) as error:
        if errors is not None:
            errors.append(f"{name}: {type(error).__name__}: {error}")
        return default


def _bound_box(value: Any) -> dict[str, float] | None:
    if value is None:
        return None
    fields = ("XMin", "YMin", "ZMin", "XMax", "YMax", "ZMax", "XLength", "YLength", "ZLength")
    result: dict[str, float] = {}
    for field in fields:
        number = _number(getattr(value, field, None))
        if number is None:
            return None
        result[field.lower()] = number
    return result


def summarize_shape(shape: Any) -> dict[str, Any] | None:
    if shape is None:
        return None
    read_errors: list[str] = []
    is_null_method = _read_attribute(shape, "isNull", None, read_errors)
    if not callable(is_null_method):
        read_errors.append("isNull: unavailable")
    try:
        is_null = bool(is_null_method()) if callable(is_null_method) else None
    except (AttributeError, RuntimeError, TypeError) as error:
        read_errors.append(f"isNull: {type(error).__name__}: {error}")
        is_null = None
    if is_null:
        return {"is_null": True}
    is_valid_method = _read_attribute(shape, "isValid", None, read_errors)
    if not callable(is_valid_method):
        read_errors.append("isValid: unavailable")
    try:
        is_valid = bool(is_valid_method()) if callable(is_valid_method) else None
    except (AttributeError, RuntimeError, TypeError) as error:
        read_errors.append(f"isValid: {type(error).__name__}: {error}")
        is_valid = None
    result = {
        "is_null": False,
        "is_valid": is_valid,
        "shape_type": str(_read_attribute(shape, "ShapeType", "unknown", read_errors)),
        "solids": _count(_read_attribute(shape, "Solids", (), read_errors)),
        "shells": _count(_read_attribute(shape, "Shells", (), read_errors)),
        "faces": _count(_read_attribute(shape, "Faces", (), read_errors)),
        "wires": _count(_read_attribute(shape, "Wires", (), read_errors)),
        "edges": _count(_read_attribute(shape, "Edges", (), read_errors)),
        "vertices": _count(_read_attribute(shape, "Vertexes", (), read_errors)),
        "area": _number(_read_attribute(shape, "Area", None, read_errors)),
        "volume": _number(_read_attribute(shape, "Volume", None, read_errors)),
        "bound_box": _bound_box(_read_attribute(shape, "BoundBox", None, read_errors)),
    }
    if read_errors:
        result["read_errors"] = read_errors
    return result


def summarize_mesh(mesh: Any) -> dict[str, Any] | None:
    if mesh is None:
        return None
    result: dict[str, Any] = {
        "points": int(getattr(mesh, "CountPoints", 0) or 0),
        "facets": int(getattr(mesh, "CountFacets", 0) or 0),
        "bound_box": _bound_box(getattr(mesh, "BoundBox", None)),
    }
    for name, method_name in (("is_solid", "isSolid"), ("components", "countComponents")):
        method = getattr(mesh, method_name, None)
        if callable(method):
            try:
                result[name] = method()
            except RuntimeError:
                result[name] = None
    return result


def _object_name(value: Any) -> str | None:
    name = getattr(value, "Name", None)
    return str(name) if name else None


def _object_names(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [name for item in value if (name := _object_name(item)) is not None]
    name = _object_name(value)
    return [name] if name is not None else []


def _object_values(value: Any) -> list[Any]:
    if value is None:
        return []
    return list(value) if isinstance(value, (list, tuple)) else [value]


def _document_identity(value: Any) -> tuple[str | None, str | None, Any | None]:
    document = _read_attribute(value, "Document", None)
    if document is None:
        return None, None, None
    name = _read_attribute(document, "Name", None)
    file_name = _read_attribute(document, "FileName", None)
    return (str(name) if name else None, str(file_name) if file_name else None, document)


def summarize_placement(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    base = getattr(value, "Base", None)
    rotation = getattr(value, "Rotation", None)
    quaternion = getattr(rotation, "Q", None)
    try:
        quaternion_values = [_number(item) for item in quaternion] if quaternion is not None else None
    except (TypeError, ValueError, RuntimeError):
        quaternion_values = None
    if quaternion_values is not None and any(item is None for item in quaternion_values):
        quaternion_values = None
    base_values = {
        axis: _number(getattr(base, axis, None))
        for axis in ("x", "y", "z")
    }
    if any(number is None for number in base_values.values()):
        base_values = None
    return {"base": base_values, "quaternion": quaternion_values}


def _link_properties(obj: Any) -> list[dict[str, Any]]:
    links: list[dict[str, Any]] = []
    for property_name in getattr(obj, "PropertiesList", ()) or ():
        getter = getattr(obj, "getTypeIdOfProperty", None)
        try:
            property_type = str(getter(property_name)) if callable(getter) else ""
        except RuntimeError:
            property_type = ""
        if "Link" not in property_type and property_name not in {"LinkedObject", "Group"}:
            continue
        try:
            target_values = _object_values(getattr(obj, property_name, None))
        except RuntimeError:
            target_values = []
        source_document_name, source_document_file, source_document = _document_identity(obj)
        target_details = []
        external_values: list[bool] = []
        for target in target_values:
            target_document_name, target_document_file, target_document = _document_identity(target)
            external = None if source_document is None or target_document is None else source_document is not target_document
            if external is not None:
                external_values.append(external)
            target_details.append(
                {
                    "name": _object_name(target),
                    "document_name": target_document_name,
                    "document_file": target_document_file,
                    "external": external,
                }
            )
        links.append(
            {
                "property": str(property_name),
                "property_type": property_type,
                "targets": [item["name"] for item in target_details if item["name"]],
                "target_details": target_details,
                "source_document_name": source_document_name,
                "source_document_file": source_document_file,
                "external": any(external_values) if external_values else None,
            }
        )
    return links


def _geometry_role(
    obj: Any,
    has_geometry: bool,
    linked_target_names: set[str],
    type_by_name: dict[str, str],
) -> tuple[str, bool, str]:
    type_id = str(getattr(obj, "TypeId", "unknown"))
    name = str(getattr(obj, "Name", ""))
    parent_types = {type_by_name[parent] for parent in _object_names(getattr(obj, "InList", ())) if parent in type_by_name}
    design_reference_types = {
        "App::Origin",
        "App::Line",
        "App::Plane",
        "App::Point",
        "PartDesign::Line",
        "PartDesign::Plane",
        "PartDesign::Point",
        "PartDesign::CoordinateSystem",
    }
    if type_id.startswith("Sketcher::") or type_id in design_reference_types:
        return "design-reference", False, "Sketch, datum, origin, axis, plane, or point is reference geometry."
    if type_id == "App::Link" or type_id.endswith("::Link"):
        return "assembly-instance", has_geometry, "Link instance represents a placed assembly occurrence."
    if name in linked_target_names:
        return "source-definition", False, "Geometry is a source definition referenced by one or more Link instances."
    if type_id == "PartDesign::Body":
        return "part-body", has_geometry, "PartDesign Body is the final body-level representation."
    if type_id.startswith("PartDesign::") and "PartDesign::Body" in parent_types:
        return "feature-history", False, "Feature belongs to a PartDesign Body and is not a separate printable part."
    if (
        type_id in {"App::Part", "App::DocumentObjectGroup", "App::DocumentObjectGroupPython"}
        or "Assembly" in type_id
    ):
        return "container", False, "Container or assembly object organizes parts but is not itself a printable part."
    if has_geometry:
        return "standalone-geometry", True, "Top-level geometry is not identified as history, source, or container."
    return "auxiliary", False, "Object has no directly printable shape or mesh."


def summarize_document(document: Any, source: Path, recompute_call_completed: bool) -> dict[str, Any]:
    objects: list[dict[str, Any]] = []
    type_counts: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    invalid_shapes = 0
    error_objects = 0
    document_objects = tuple(getattr(document, "Objects", ()))
    type_by_name = {
        str(getattr(obj, "Name", "")): str(getattr(obj, "TypeId", "unknown"))
        for obj in document_objects
    }
    linked_target_names = {
        target
        for obj in document_objects
        for target in _object_names(_read_attribute(obj, "LinkedObject", None))
    }
    printable_candidates = 0
    for obj in document_objects:
        analysis_errors: list[str] = []
        type_id = str(getattr(obj, "TypeId", "unknown"))
        type_counts[type_id] += 1
        states = tuple(str(item) for item in getattr(obj, "State", ()) or ())
        shape = summarize_shape(_read_attribute(obj, "Shape", None, analysis_errors))
        mesh = summarize_mesh(_read_attribute(obj, "Mesh", None, analysis_errors))
        if shape and shape.get("read_errors"):
            analysis_errors.extend(f"Shape.{item}" for item in shape["read_errors"])
        global_placement = None
        global_placement_method = _read_attribute(obj, "getGlobalPlacement", None, analysis_errors)
        if callable(global_placement_method):
            try:
                global_placement = summarize_placement(global_placement_method())
            except (AttributeError, RuntimeError, TypeError) as error:
                analysis_errors.append(f"getGlobalPlacement: {type(error).__name__}: {error}")
        view_object = _read_attribute(obj, "ViewObject", None)
        if view_object is not None:
            visibility = {
                "value": _read_attribute(view_object, "Visibility", None, analysis_errors),
                "source": "gui-view-object",
            }
        else:
            visibility = {"value": None, "source": "unavailable-in-headless-analysis"}
        has_shape_geometry = bool(
            shape
            and shape.get("is_null") is not True
            and any((shape.get("solids", 0), shape.get("shells", 0), shape.get("faces", 0)))
        )
        has_geometry = has_shape_geometry or bool(mesh and mesh.get("facets", 0))
        role, printable_candidate, role_reason = _geometry_role(
            obj,
            has_geometry,
            linked_target_names,
            type_by_name,
        )
        role_counts[role] += 1
        printable_candidates += int(printable_candidate)
        if shape and shape.get("is_valid") is False:
            invalid_shapes += 1
        normalized_states = {re.sub(r"[^a-z]", "", state.lower()) for state in states}
        if any(state not in {"uptodate", "touched"} for state in normalized_states):
            error_objects += 1
        objects.append(
            {
                "name": str(getattr(obj, "Name", "")),
                "label": str(getattr(obj, "Label", "")),
                "type_id": type_id,
                "states": states,
                "visibility": visibility,
                "local_placement": summarize_placement(_read_attribute(obj, "Placement", None, analysis_errors)),
                "global_placement": global_placement,
                "parents": _object_names(getattr(obj, "InList", ())),
                "children": _object_names(getattr(obj, "OutList", ())),
                "linked_object": _object_name(getattr(obj, "LinkedObject", None)),
                "link_properties": _link_properties(obj),
                "geometry_role": role,
                "printable_candidate": printable_candidate,
                "role_reason": role_reason,
                "property_names": sorted(str(name) for name in getattr(obj, "PropertiesList", ()) or ()),
                "shape": shape,
                "mesh": mesh,
                "analysis_errors": analysis_errors,
            }
        )
    return {
        "schema_version": "1.0",
        "source": str(source),
        "freecad": {
            "document_name": str(getattr(document, "Name", "")),
            "object_count": len(objects),
            "object_types": dict(sorted(type_counts.items())),
            "geometry_roles": dict(sorted(role_counts.items())),
            "printable_candidate_count": printable_candidates,
            "link_instance_count": role_counts["assembly-instance"],
            "body_count": role_counts["part-body"],
            "recompute_call_completed": recompute_call_completed,
            "invalid_shape_count": invalid_shapes,
            "object_error_state_count": error_objects,
        },
        "objects": objects,
        "limitations": [
            "This report does not prove printability, strength, tolerances, or physical production success.",
            "Safe mode can leave add-on-defined objects unresolved; do not disable it without explicit approval.",
            "Imported neutral CAD normally lacks the source application's feature history.",
            "Printable-candidate roles are conservative heuristics; confirm intended parts and instances before editing.",
        ],
    }


def _load_document(source: Path) -> tuple[Any, Any]:
    try:
        import FreeCAD as App  # type: ignore[import-not-found]
        import Part  # type: ignore[import-not-found]
    except ImportError as error:
        raise RuntimeError("Run this script with FreeCADCmd or FreeCAD console mode") from error
    if source.suffix.lower() == ".fcstd":
        document = App.openDocument(str(source))
    else:
        document = App.newDocument("Slant3DAnalysis")
        Part.insert(str(source), document.Name)
    return App, document


@contextlib.contextmanager
def _materialized_import_source(source: Path):
    if source.suffix.lower() != ".stpz":
        yield source
        return
    try:
        archive = zipfile.ZipFile(source)
    except (OSError, zipfile.BadZipFile) as error:
        raise ValueError(f"Invalid STPZ container: {error}") from error
    with archive:
        step_members = [
            member
            for member in archive.infolist()
            if not member.is_dir() and Path(member.filename).suffix.lower() in {".step", ".stp"}
        ]
        if len(step_members) != 1:
            raise ValueError("STPZ must contain exactly one STEP/STP member")
        member = step_members[0]
        compressed = max(member.compress_size, 1)
        if member.file_size > MAX_STEP_ZIP_MEMBER_BYTES:
            raise ValueError("STPZ STEP member exceeds the safe extraction size limit")
        if member.file_size / compressed > MAX_COMPRESSION_RATIO:
            raise ValueError("STPZ STEP member compression ratio is suspicious")
        with tempfile.TemporaryDirectory(prefix="slant3d-stpz-") as directory:
            extracted = Path(directory) / f"model{Path(member.filename).suffix.lower()}"
            with archive.open(member) as source_stream, extracted.open("xb") as target_stream:
                shutil.copyfileobj(source_stream, target_stream, length=1024 * 1024)
            if extracted.stat().st_size != member.file_size:
                raise ValueError("STPZ STEP member extraction size mismatch")
            yield extracted


def analyze(source: Path) -> dict[str, Any]:
    resolved = source.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Input is not a regular file: {resolved}")
    if resolved.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise ValueError(f"FreeCAD geometry analysis does not accept {resolved.suffix or 'extensionless'} input")
    app: Any | None = None
    document: Any | None = None
    try:
        with _materialized_import_source(resolved) as import_source:
            app, document = _load_document(import_source)
            try:
                document.recompute()
                recompute_call_completed = True
            except RuntimeError:
                recompute_call_completed = False
            return summarize_document(document, resolved, recompute_call_completed)
    finally:
        if app is not None and document is not None:
            try:
                app.closeDocument(document.Name)
            except RuntimeError:
                pass


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    return parser


def _arguments_from_environment() -> list[str] | None:
    """Read paths passed by the safe launcher without exposing them to FreeCAD argv parsing."""
    source = os.environ.get("SLANT3D_FREECAD_INPUT")
    output = os.environ.get("SLANT3D_FREECAD_OUTPUT")
    if source is None and output is None:
        return None
    if not source or not output:
        raise RuntimeError("Both SLANT3D_FREECAD_INPUT and SLANT3D_FREECAD_OUTPUT are required")
    return [source, "--output", output]


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = analyze(args.input)
    except (OSError, RuntimeError, ValueError) as error:
        error_payload = json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2)
        if args.output:
            output = args.output.expanduser().resolve()
            if output != args.input.expanduser().resolve() and not output.exists():
                try:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    with output.open("x", encoding="utf-8") as stream:
                        stream.write(error_payload + "\n")
                except OSError:
                    pass
        print(error_payload)
        return 2
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output = args.output.expanduser().resolve()
        if output == args.input.expanduser().resolve():
            print(json.dumps({"schema_version": "1.0", "error": "Output must not overwrite input."}, indent=2))
            return 2
        try:
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("x", encoding="utf-8") as stream:
                stream.write(payload + "\n")
        except OSError as error:
            print(json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2))
            return 2
    print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
elif "FreeCAD" in sys.modules:
    # FreeCADCmd imports script files instead of executing them as __main__.
    try:
        environment_arguments = _arguments_from_environment()
        if environment_arguments is not None:
            main(environment_arguments)
    except RuntimeError as error:
        print(json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2))
