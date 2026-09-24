from __future__ import annotations

import importlib.util
import json
import math
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from types import SimpleNamespace


SCRIPT = Path(__file__).parents[1] / "scripts" / "freecad_geometry_report.py"
SPEC = importlib.util.spec_from_file_location("freecad_geometry_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FakeShape:
    ShapeType = "Solid"
    Solids = (1,)
    Shells = (1,)
    Faces = (1, 2, 3, 4, 5, 6)
    Wires = tuple(range(6))
    Edges = tuple(range(12))
    Vertexes = tuple(range(8))
    Area = 600.0
    Volume = 1000.0
    BoundBox = SimpleNamespace(
        XMin=0,
        YMin=0,
        ZMin=0,
        XMax=10,
        YMax=10,
        ZMax=10,
        XLength=10,
        YLength=10,
        ZLength=10,
    )

    @staticmethod
    def isNull() -> bool:
        return False

    @staticmethod
    def isValid() -> bool:
        return True


class FreeCadGeometryReportTests(unittest.TestCase):
    def test_environment_handoff_requires_both_paths(self) -> None:
        original_input = MODULE.os.environ.get("SLANT3D_FREECAD_INPUT")
        original_output = MODULE.os.environ.get("SLANT3D_FREECAD_OUTPUT")
        try:
            MODULE.os.environ["SLANT3D_FREECAD_INPUT"] = "part.FCStd"
            MODULE.os.environ.pop("SLANT3D_FREECAD_OUTPUT", None)
            with self.assertRaisesRegex(RuntimeError, "Both"):
                MODULE._arguments_from_environment()
            MODULE.os.environ["SLANT3D_FREECAD_OUTPUT"] = "report.json"
            self.assertEqual(
                ["part.FCStd", "--output", "report.json"],
                MODULE._arguments_from_environment(),
            )
        finally:
            if original_input is None:
                MODULE.os.environ.pop("SLANT3D_FREECAD_INPUT", None)
            else:
                MODULE.os.environ["SLANT3D_FREECAD_INPUT"] = original_input
            if original_output is None:
                MODULE.os.environ.pop("SLANT3D_FREECAD_OUTPUT", None)
            else:
                MODULE.os.environ["SLANT3D_FREECAD_OUTPUT"] = original_output

    def test_shape_summary_is_stable_and_numeric(self) -> None:
        summary = MODULE.summarize_shape(FakeShape())
        self.assertIsNotNone(summary)
        self.assertEqual(1, summary["solids"])
        self.assertEqual(6, summary["faces"])
        self.assertEqual(1000.0, summary["volume"])
        self.assertEqual(10.0, summary["bound_box"]["xlength"])

    def test_non_finite_numbers_are_omitted_from_strict_json(self) -> None:
        self.assertIsNone(MODULE._number(math.nan))
        self.assertIsNone(MODULE._number(math.inf))
        shape = FakeShape()
        shape.Area = math.nan
        summary = MODULE.summarize_shape(shape)
        self.assertIsNone(summary["area"])
        json.dumps(summary, allow_nan=False)

    def test_lazy_shape_failure_is_recorded_without_aborting_document(self) -> None:
        class LazyShape(FakeShape):
            @property
            def Solids(self):
                raise RuntimeError("unresolved add-on shape")

        obj = SimpleNamespace(
            Name="Lazy",
            Label="Lazy",
            TypeId="Part::Feature",
            State=(),
            PropertiesList=("Shape",),
            Shape=LazyShape(),
            Mesh=None,
        )
        report = MODULE.summarize_document(SimpleNamespace(Name="Doc", Objects=(obj,)), Path("part.FCStd"), True)
        self.assertEqual(1, report["freecad"]["object_count"])
        self.assertTrue(report["objects"][0]["analysis_errors"])

    def test_unresolved_object_shape_is_recorded_without_aborting_document(self) -> None:
        class LazyObject:
            Name = "LazyObject"
            Label = "LazyObject"
            TypeId = "Part::Feature"
            State = ()
            PropertiesList = ("Shape",)
            Mesh = None

            @property
            def Shape(self):
                raise RuntimeError("missing workbench")

        report = MODULE.summarize_document(
            SimpleNamespace(Name="Doc", Objects=(LazyObject(),)), Path("part.FCStd"), True
        )
        self.assertTrue(report["objects"][0]["analysis_errors"])

    def test_unknown_proxy_shape_is_not_a_printable_candidate(self) -> None:
        obj = SimpleNamespace(
            Name="Proxy",
            Label="Proxy",
            TypeId="Part::FeaturePython",
            State=(),
            PropertiesList=("Shape",),
            Shape=SimpleNamespace(),
            Mesh=None,
        )
        report = MODULE.summarize_document(SimpleNamespace(Name="Doc", Objects=(obj,)), Path("part.FCStd"), True)
        item = report["objects"][0]
        self.assertFalse(item["printable_candidate"])
        self.assertEqual("auxiliary", item["geometry_role"])
        self.assertTrue(item["analysis_errors"])

    def test_document_summary_counts_types_and_invalid_shapes(self) -> None:
        valid = SimpleNamespace(
            Name="Box",
            Label="Box",
            TypeId="PartDesign::Feature",
            State=("UpToDate",),
            PropertiesList=("Label", "Shape"),
            Shape=FakeShape(),
            Mesh=None,
        )

        class InvalidShape(FakeShape):
            @staticmethod
            def isValid() -> bool:
                return False

        invalid = SimpleNamespace(
            Name="Broken",
            Label="Broken",
            TypeId="Part::Feature",
            State=("Invalid",),
            PropertiesList=("Shape",),
            Shape=InvalidShape(),
            Mesh=None,
        )
        document = SimpleNamespace(Name="Doc", Objects=(valid, invalid))
        report = MODULE.summarize_document(document, Path("part.FCStd"), False)
        self.assertEqual(2, report["freecad"]["object_count"])
        self.assertFalse(report["freecad"]["recompute_call_completed"])
        self.assertEqual(1, report["freecad"]["invalid_shape_count"])
        self.assertEqual(1, report["freecad"]["object_error_state_count"])

    def test_document_summary_separates_instances_bodies_and_feature_history(self) -> None:
        body = SimpleNamespace(
            Name="Body",
            Label="Body",
            TypeId="PartDesign::Body",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
        )
        pad = SimpleNamespace(
            Name="Pad",
            Label="Pad",
            TypeId="PartDesign::Feature",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(body,),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
        )
        body.OutList = (pad,)
        source = SimpleNamespace(
            Name="Source",
            Label="Source",
            TypeId="Part::Feature",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
        )
        link = SimpleNamespace(
            Name="Instance",
            Label="Instance",
            TypeId="App::Link",
            State=(),
            PropertiesList=("LinkedObject", "Shape"),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=source,
            Placement=None,
            ViewObject=None,
            getTypeIdOfProperty=lambda name: "App::PropertyLink" if name == "LinkedObject" else "Part::PropertyPartShape",
        )
        sketch = SimpleNamespace(
            Name="Sketch",
            Label="Sketch",
            TypeId="Sketcher::SketchObject",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(body,),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
        )
        document = SimpleNamespace(Name="Assembly", Objects=(body, pad, source, link, sketch))
        report = MODULE.summarize_document(document, Path("assembly.FCStd"), True)
        roles = {item["name"]: item["geometry_role"] for item in report["objects"]}
        self.assertEqual("part-body", roles["Body"])
        self.assertEqual("feature-history", roles["Pad"])
        self.assertEqual("source-definition", roles["Source"])
        self.assertEqual("assembly-instance", roles["Instance"])
        self.assertEqual("design-reference", roles["Sketch"])
        self.assertEqual(2, report["freecad"]["printable_candidate_count"])
        instance = next(item for item in report["objects"] if item["name"] == "Instance")
        self.assertEqual("Source", instance["linked_object"])

    def test_linked_body_is_source_definition_not_duplicate_print_candidate(self) -> None:
        document = SimpleNamespace(Name="Assembly", FileName="assembly.FCStd")
        body = SimpleNamespace(
            Name="Body",
            Label="Body",
            TypeId="PartDesign::Body",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
            Document=document,
        )
        link = SimpleNamespace(
            Name="Instance",
            Label="Instance",
            TypeId="App::Link",
            State=(),
            PropertiesList=("LinkedObject", "Shape"),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=body,
            Placement=None,
            ViewObject=None,
            Document=document,
            getTypeIdOfProperty=lambda name: "App::PropertyLink" if name == "LinkedObject" else "Part::PropertyPartShape",
        )
        document.Objects = (body, link)
        report = MODULE.summarize_document(document, Path("assembly.FCStd"), True)
        roles = {item["name"]: item["geometry_role"] for item in report["objects"]}
        self.assertEqual("source-definition", roles["Body"])
        self.assertEqual("assembly-instance", roles["Instance"])
        self.assertEqual(1, report["freecad"]["printable_candidate_count"])
        instance = next(item for item in report["objects"] if item["name"] == "Instance")
        link_info = next(item for item in instance["link_properties"] if item["property"] == "LinkedObject")
        self.assertFalse(link_info["external"])
        self.assertEqual("Assembly", link_info["target_details"][0]["document_name"])

    def test_visibility_and_placement_scope_are_explicit(self) -> None:
        global_placement = SimpleNamespace(
            Base=SimpleNamespace(x=1, y=2, z=3),
            Rotation=SimpleNamespace(Q=(0, 0, 0, 1)),
        )
        obj = SimpleNamespace(
            Name="Placed",
            Label="Placed",
            TypeId="Part::Feature",
            State=(),
            PropertiesList=("Shape",),
            Shape=FakeShape(),
            Mesh=None,
            InList=(),
            OutList=(),
            LinkedObject=None,
            Placement=None,
            ViewObject=None,
            getGlobalPlacement=lambda: global_placement,
        )
        report = MODULE.summarize_document(SimpleNamespace(Name="Doc", Objects=(obj,)), Path("part.FCStd"), True)
        item = report["objects"][0]
        self.assertEqual("unavailable-in-headless-analysis", item["visibility"]["source"])
        self.assertIsNone(item["local_placement"])
        self.assertEqual(1.0, item["global_placement"]["base"]["x"])

    def test_regular_python_reports_missing_freecad_runtime(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "FreeCADCmd"):
            MODULE._load_document(Path("part.FCStd"))

    def test_analysis_error_is_written_to_requested_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bad.step"
            output = Path(directory) / "report.json"
            source.write_text("not step", encoding="utf-8")
            with unittest.mock.patch.object(MODULE, "analyze", side_effect=RuntimeError("Cannot open STEP file")):
                self.assertEqual(2, MODULE.main([str(source), "--output", str(output)]))
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("Cannot open STEP file", payload["error"])

    def test_stpz_materializes_one_bounded_step_member(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "part.stpz"
            payload = b"ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\nENDSEC;\nEND-ISO-10303-21;"
            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("nested/part.step", payload)
            with MODULE._materialized_import_source(archive_path) as extracted:
                self.assertEqual(".step", extracted.suffix)
                self.assertEqual(payload, extracted.read_bytes())
                extracted_path = extracted
            self.assertFalse(extracted_path.exists())

    def test_stpz_rejects_multiple_step_members(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "part.stpz"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("one.step", b"one")
                archive.writestr("two.stp", b"two")
            with self.assertRaisesRegex(ValueError, "exactly one"):
                with MODULE._materialized_import_source(archive_path):
                    pass


if __name__ == "__main__":
    unittest.main()
