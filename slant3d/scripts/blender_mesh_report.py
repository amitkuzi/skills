#!/usr/bin/env python3
"""Read-only Blender geometry report for STL and OBJ mesh inputs."""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


SUPPORTED_SUFFIXES = {".stl", ".obj"}
MAX_OBJ_SCAN_BYTES = 64 * 1024 * 1024
MAX_OBJ_LINE_BYTES = 1024 * 1024


def _number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _connected_components(vertex_count: int, edge_vertices: Iterable[tuple[int, int]]) -> int:
    if vertex_count <= 0:
        return 0
    parents = list(range(vertex_count))

    def find(value: int) -> int:
        while parents[value] != value:
            parents[value] = parents[parents[value]]
            value = parents[value]
        return value

    for left, right in edge_vertices:
        if not (0 <= left < vertex_count and 0 <= right < vertex_count):
            continue
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parents[right_root] = left_root
    return len({find(index) for index in range(vertex_count)})


def _edge_use_counts(mesh: Any) -> Counter[tuple[int, int]]:
    counts: Counter[tuple[int, int]] = Counter()
    for edge in mesh.edges:
        counts[tuple(sorted(int(index) for index in edge.vertices))] = 0
    for polygon in mesh.polygons:
        vertices = tuple(int(index) for index in polygon.vertices)
        for index, left in enumerate(vertices):
            right = vertices[(index + 1) % len(vertices)]
            counts[tuple(sorted((left, right)))] += 1
    return counts


def _local_bounds(mesh: Any) -> dict[str, list[float]] | None:
    coordinates = [tuple(_number(value) for value in vertex.co) for vertex in mesh.vertices]
    if not coordinates or any(value is None for point in coordinates for value in point):
        return None
    axes = tuple(zip(*coordinates))
    return {
        "minimum": [min(axis) for axis in axes],
        "maximum": [max(axis) for axis in axes],
    }


def _world_bounds(obj: Any) -> dict[str, list[float]] | None:
    try:
        points = [obj.matrix_world @ type(obj.location)(corner) for corner in obj.bound_box]
        axes = tuple(zip(*((point.x, point.y, point.z) for point in points)))
        minimum = [_number(min(axis)) for axis in axes]
        maximum = [_number(max(axis)) for axis in axes]
    except (AttributeError, RuntimeError, TypeError, ValueError):
        return None
    if any(value is None for value in minimum + maximum):
        return None
    return {"minimum": minimum, "maximum": maximum}


def summarize_mesh_object(obj: Any) -> dict[str, Any]:
    mesh = obj.data
    edge_counts = _edge_use_counts(mesh)
    edge_vertices = [tuple(int(index) for index in edge.vertices) for edge in mesh.edges]
    polygons = tuple(mesh.polygons)
    dimensions = [_number(value) for value in obj.dimensions]
    transform = [[_number(value) for value in row] for row in obj.matrix_world]
    return {
        "name": str(obj.name),
        "vertices": len(mesh.vertices),
        "edges": len(mesh.edges),
        "polygons": len(polygons),
        "triangles_after_import": sum(max(len(polygon.vertices) - 2, 0) for polygon in polygons),
        "boundary_edges": sum(count == 1 for count in edge_counts.values()),
        "non_manifold_edges": sum(count != 2 for count in edge_counts.values()),
        "loose_edges": sum(count == 0 for count in edge_counts.values()),
        "edges_with_more_than_two_faces": sum(count > 2 for count in edge_counts.values()),
        "degenerate_polygons": sum((_number(polygon.area) or 0.0) <= 0.0 for polygon in polygons),
        "connected_components": _connected_components(len(mesh.vertices), edge_vertices),
        "material_slots": len(obj.material_slots),
        "dimensions": dimensions,
        "world_bounds": _world_bounds(obj),
        "source_coordinate_bounds": _local_bounds(mesh),
        "matrix_world": transform,
        "mirrored_transform": bool(obj.matrix_world.determinant() < 0),
    }


def _load_blender() -> Any:
    try:
        import bpy  # type: ignore[import-not-found]
    except ImportError as error:
        raise RuntimeError("Run this script with Blender in background mode") from error
    return bpy


def _validate_obj_has_no_external_references(source: Path) -> None:
    if source.stat().st_size > MAX_OBJ_SCAN_BYTES:
        raise ValueError(
            f"OBJ exceeds the {MAX_OBJ_SCAN_BYTES}-byte safe pre-import scan limit"
        )
    scanned = 0
    with source.open("rb") as stream:
        while True:
            raw_line = stream.readline(MAX_OBJ_LINE_BYTES + 1)
            if not raw_line:
                return
            scanned += len(raw_line)
            if len(raw_line) > MAX_OBJ_LINE_BYTES:
                raise ValueError("OBJ contains an overlong line and is not safe to import automatically")
            stripped = raw_line.lstrip().lower()
            if stripped.startswith(b"mtllib") and (
                len(stripped) == 6 or stripped[6:7] in b" \t\r\n"
            ):
                raise ValueError(
                    "OBJ external mtllib references are blocked to prevent unintended file or network access"
                )
            if scanned > MAX_OBJ_SCAN_BYTES:
                raise ValueError("OBJ exceeded the safe pre-import scan limit")


def _import_source(bpy: Any, source: Path) -> dict[str, str]:
    suffix = source.suffix.lower()
    if suffix == ".stl":
        operator = getattr(bpy.ops.wm, "stl_import", None)
        arguments = {"filepath": str(source), "forward_axis": "Y", "up_axis": "Z"}
        if operator is None:
            operator = getattr(getattr(bpy.ops, "import_mesh", None), "stl", None)
            arguments = {"filepath": str(source), "axis_forward": "Y", "axis_up": "Z"}
    elif suffix == ".obj":
        _validate_obj_has_no_external_references(source)
        operator = getattr(bpy.ops.wm, "obj_import", None)
        arguments = {"filepath": str(source), "forward_axis": "Y", "up_axis": "Z"}
        if operator is None:
            operator = getattr(getattr(bpy.ops, "import_scene", None), "obj", None)
            arguments = {"filepath": str(source), "axis_forward": "Y", "axis_up": "Z"}
    else:
        raise ValueError(f"Blender mesh analysis does not accept {suffix or 'extensionless'} input")
    if not callable(operator):
        raise RuntimeError(f"This Blender installation has no enabled {suffix} importer")
    result = operator(**arguments)
    if "FINISHED" not in set(result):
        raise RuntimeError(f"Blender importer returned {sorted(result)}")
    return {
        "forward_axis": "Y",
        "up_axis": "Z",
        "axis_policy": "Preserve source coordinate values; OBJ does not define a universal physical up axis.",
    }


def analyze(source: Path) -> dict[str, Any]:
    resolved = source.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Input is not a regular file: {resolved}")
    if resolved.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise ValueError(f"Blender mesh analysis does not accept {resolved.suffix or 'extensionless'} input")
    bpy = _load_blender()
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    import_settings = _import_source(bpy, resolved)
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    if not mesh_objects:
        raise RuntimeError("Blender import completed without mesh objects")
    units = bpy.context.scene.unit_settings
    return {
        "schema_version": "1.0",
        "source": str(resolved),
        "blender": {
            "version": str(bpy.app.version_string),
            "object_count": len(bpy.context.scene.objects),
            "mesh_object_count": len(mesh_objects),
            "scene_units": {
                "system": str(units.system),
                "length_unit": str(units.length_unit),
                "scale_length": _number(units.scale_length),
            },
            "import_settings": import_settings,
        },
        "objects": [summarize_mesh_object(obj) for obj in mesh_objects],
        "limitations": [
            "STL and OBJ are unitless; scene-space dimensions do not establish physical units without user confirmation.",
            "OBJ defines no universal physical up/forward convention; source coordinates are preserved and orientation intent requires confirmation.",
            "This report does not prove printability, strength, tolerance, or production success.",
            "Boundary and face-use checks do not detect every self-intersection or geometric defect.",
            "The source was imported into a factory-startup temporary Blender process and was not saved or modified.",
        ],
    }


def _arguments_from_environment() -> list[str]:
    source = os.environ.get("SLANT3D_BLENDER_INPUT")
    output = os.environ.get("SLANT3D_BLENDER_OUTPUT")
    if not source or not output:
        raise RuntimeError("Both SLANT3D_BLENDER_INPUT and SLANT3D_BLENDER_OUTPUT are required")
    return [source, "--output", output]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = analyze(args.input)
        payload = json.dumps(report, indent=2, sort_keys=True, allow_nan=False)
        output = args.output.expanduser().resolve()
        if output == args.input.expanduser().resolve():
            raise ValueError("Output must not overwrite input")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8") as stream:
            stream.write(payload + "\n")
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        print(json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2))
        return 2
    print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main(_arguments_from_environment()))
