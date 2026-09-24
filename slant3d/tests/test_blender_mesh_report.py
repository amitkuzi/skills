from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


SCRIPT = Path(__file__).parents[1] / "scripts" / "blender_mesh_report.py"
SPEC = importlib.util.spec_from_file_location("blender_mesh_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BlenderMeshReportTests(unittest.TestCase):
    def test_connected_components_counts_islands_and_isolated_vertices(self) -> None:
        self.assertEqual(3, MODULE._connected_components(5, [(0, 1), (1, 2)]))
        self.assertEqual(1, MODULE._connected_components(3, [(0, 1), (1, 2), (2, 0)]))
        self.assertEqual(0, MODULE._connected_components(0, []))

    def test_non_finite_number_is_rejected(self) -> None:
        self.assertIsNone(MODULE._number(float("nan")))
        self.assertIsNone(MODULE._number(float("inf")))

    def test_regular_python_requires_blender(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Blender"):
            MODULE._load_blender()

    def test_obj_import_preserves_raw_coordinate_axes(self) -> None:
        called = {}

        def obj_import(**kwargs):
            called.update(kwargs)
            return {"FINISHED"}

        bpy = SimpleNamespace(
            ops=SimpleNamespace(
                wm=SimpleNamespace(obj_import=obj_import),
                import_scene=SimpleNamespace(obj=None),
            )
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "part.obj"
            path.write_text("v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n", encoding="utf-8")
            settings = MODULE._import_source(bpy, path)
            self.assertEqual("Y", called["forward_axis"])
            self.assertEqual("Z", called["up_axis"])
            self.assertEqual("Y", settings["forward_axis"])

    def test_obj_import_blocks_external_material_library(self) -> None:
        bpy = SimpleNamespace(
            ops=SimpleNamespace(
                wm=SimpleNamespace(obj_import=lambda **_: {"FINISHED"}),
                import_scene=SimpleNamespace(obj=None),
            )
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe.obj"
            path.write_text(
                "v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\nmtllib //server/share/file.mtl\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "mtllib"):
                MODULE._import_source(bpy, path)

    def test_loose_edges_are_counted_as_non_manifold(self) -> None:
        mesh = SimpleNamespace(
            edges=(
                SimpleNamespace(vertices=(0, 1)),
                SimpleNamespace(vertices=(1, 2)),
                SimpleNamespace(vertices=(2, 0)),
                SimpleNamespace(vertices=(3, 4)),
            ),
            polygons=(SimpleNamespace(vertices=(0, 1, 2)),),
        )
        counts = MODULE._edge_use_counts(mesh)
        self.assertEqual(0, counts[(3, 4)])
        self.assertEqual(4, sum(count != 2 for count in counts.values()))


if __name__ == "__main__":
    unittest.main()
