from __future__ import annotations

import importlib.util
import json
import struct
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "cad_input_report.py"
SPEC = importlib.util.spec_from_file_location("cad_input_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CadInputReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, name: str, content: bytes) -> Path:
        path = self.root / name
        path.write_bytes(content)
        return path

    def test_fcstd_container_and_objects_are_reported(self) -> None:
        path = self.root / "part.FCStd"
        document = b'''<Document SchemaVersion="4" ProgramVersion="1.0">
        <Objects Count="2"><Object type="PartDesign::Body" name="Body"/>
        <Object type="PartDesign::Feature" name="Pad"/></Objects></Document>'''
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("Document.xml", document)
            archive.writestr("GuiDocument.xml", b"<GuiDocument/>")
        report = MODULE.analyze(path)
        self.assertEqual("fcstd", report["detection"]["format"])
        self.assertEqual("native-parametric", report["detection"]["fidelity_tier"])
        self.assertEqual(2, report["detection"]["details"]["object_count"])

    def test_fcstd_rejects_unexpected_xml_namespace(self) -> None:
        path = self.root / "spoof.FCStd"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "Document.xml",
                b'<x:Document xmlns:x="urn:evil" SchemaVersion="4"><x:Objects><x:Object type="evil"/></x:Objects></x:Document>',
            )
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("fcstd-candidate", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_3mf_package_reports_units_and_mesh_counts(self) -> None:
        path = self.root / "part.3mf"
        model = b'''<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
        <resources><object id="1"><mesh><vertices/><triangles><triangle v1="0" v2="1" v3="2"/></triangles></mesh></object></resources>
        <build><item objectid="1"/></build></model>'''
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
                </Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
                </Relationships>''',
            )
            archive.writestr("3D/3dmodel.model", model)
        report = MODULE.analyze(path)
        self.assertEqual("3mf", report["detection"]["format"])
        self.assertEqual("millimeter", report["detection"]["units"])
        self.assertEqual(1, report["detection"]["details"]["triangle_count"])

    def test_3mf_reports_topology_bounds_and_build_transform(self) -> None:
        path = self.root / "tetra.3mf"
        model = b'''<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
        <resources><object id="1"><mesh><vertices>
        <vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/>
        <vertex x="0" y="1" z="0"/><vertex x="0" y="0" z="1"/>
        </vertices><triangles>
        <triangle v1="0" v2="2" v3="1"/><triangle v1="0" v2="1" v3="3"/>
        <triangle v1="1" v2="2" v3="3"/><triangle v1="2" v2="0" v3="3"/>
        </triangles></mesh></object></resources>
        <build><item objectid="1" transform="1 0 0 0 1 0 0 0 1 10 20 30"/></build></model>'''
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>''',
            )
            archive.writestr("3D/3dmodel.model", model)
        detection = MODULE.analyze(path)["detection"]
        mesh = detection["details"]["objects"][0]
        build = detection["details"]["build_items"][0]
        self.assertEqual(0, mesh["boundary_edge_count"])
        self.assertEqual(1, mesh["connected_components"])
        self.assertEqual([0.0, 0.0, 0.0], mesh["bounds"]["minimum"])
        self.assertEqual([11.0, 21.0, 31.0], build["transformed_bounds"]["maximum"])
        self.assertTrue(detection["details"]["geometry_analysis_complete"])

    def test_empty_3mf_is_not_claimed_as_polygon_mesh(self) -> None:
        path = self.root / "empty.3mf"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>''',
            )
            archive.writestr(
                "3D/3dmodel.model",
                b'''<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"><resources/><build/></model>''',
            )
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("detected-only", detection["fidelity_tier"])
        self.assertEqual("low", detection["confidence"])
        self.assertFalse(detection["details"]["geometry_analysis_complete"])

    def test_3mf_component_assembly_resolves_nested_transformed_bounds(self) -> None:
        path = self.root / "assembly.3mf"
        model = b'''<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
        <resources>
        <object id="1"><mesh><vertices>
        <vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/>
        <vertex x="0" y="1" z="0"/><vertex x="0" y="0" z="1"/>
        </vertices><triangles>
        <triangle v1="0" v2="2" v3="1"/><triangle v1="0" v2="1" v3="3"/>
        <triangle v1="1" v2="2" v3="3"/><triangle v1="2" v2="0" v3="3"/>
        </triangles></mesh></object>
        <object id="2"><components>
        <component objectid="1"/><component objectid="1" transform="1 0 0 0 1 0 0 0 1 5 0 0"/>
        </components></object>
        </resources><build><item objectid="2" transform="1 0 0 0 1 0 0 0 1 10 20 30"/></build></model>'''
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>''',
            )
            archive.writestr("3D/3dmodel.model", model)
        detection = MODULE.analyze(path)["detection"]
        assembly = detection["details"]["objects"][1]
        build = detection["details"]["build_items"][0]
        self.assertEqual([0.0, 0.0, 0.0], assembly["resolved_bounds"]["minimum"])
        self.assertEqual([6.0, 1.0, 1.0], assembly["resolved_bounds"]["maximum"])
        self.assertEqual([16.0, 21.0, 31.0], build["transformed_bounds"]["maximum"])
        self.assertTrue(detection["details"]["geometry_analysis_complete"])

    def test_deep_3mf_component_chain_fails_closed_without_zip_misclassification(self) -> None:
        path = self.root / "deep-chain.3mf"
        component_objects = "".join(
            f'<object id="{object_id}"><components><component objectid="{object_id - 1}"/></components></object>'
            for object_id in range(1000, 1, -1)
        )
        mesh_object = '''<object id="1"><mesh><vertices>
        <vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/>
        <vertex x="0" y="1" z="0"/><vertex x="0" y="0" z="1"/>
        </vertices><triangles>
        <triangle v1="0" v2="2" v3="1"/><triangle v1="0" v2="1" v3="3"/>
        <triangle v1="1" v2="2" v3="3"/><triangle v1="2" v2="0" v3="3"/>
        </triangles></mesh></object>'''
        model = (
            '<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"><resources>'
            + component_objects
            + mesh_object
            + '</resources><build><item objectid="1000"/></build></model>'
        ).encode()
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>''',
            )
            archive.writestr("3D/3dmodel.model", model)
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("3mf", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])
        self.assertEqual("low", detection["confidence"])
        self.assertTrue(detection["details"]["component_resolution_budget_exceeded"])
        self.assertTrue(any("analysis budget exceeded" in item for item in detection["warnings"]))

    def test_3mf_default_unit_and_invalid_unit_are_not_silently_accepted(self) -> None:
        def write_3mf(name: str, unit_attribute: str) -> Path:
            path = self.root / name
            model = (
                f'<model {unit_attribute} xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
                '<resources/><build/></model>'
            ).encode()
            relationships = b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
            <Relationship Target="/3D/3dmodel.model" Id="rel0"
            Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>'''
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr(
                    "[Content_Types].xml",
                    b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                    <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
                    </Types>''',
                )
                archive.writestr("_rels/.rels", relationships)
                archive.writestr("3D/3dmodel.model", model)
            return path

        default_unit = MODULE.analyze(write_3mf("default.3mf", ""))["detection"]
        invalid_unit = MODULE.analyze(write_3mf("invalid.3mf", 'unit="banana"'))["detection"]
        self.assertEqual("millimeter", default_unit["units"])
        self.assertEqual("detected-only", invalid_unit["fidelity_tier"])
        self.assertEqual("low", invalid_unit["confidence"])

    def test_3mf_without_start_part_relationship_is_downgraded(self) -> None:
        path = self.root / "missing-relationship.3mf"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
                </Types>''',
            )
            archive.writestr("_rels/.rels", b"<Relationships/>")
            archive.writestr(
                "3D/3dmodel.model",
                b'''<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
                <resources/><build/></model>''',
            )
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("3mf", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_3mf_rejects_wrong_namespace_and_extension_element_spoofing(self) -> None:
        relationships = b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
        <Relationship Target="/3D/3dmodel.model" Id="rel0"
        Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>'''
        content_types = b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
        <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>'''

        def write_model(name: str, model: bytes) -> Path:
            path = self.root / name
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("[Content_Types].xml", content_types)
                archive.writestr("_rels/.rels", relationships)
                archive.writestr("3D/3dmodel.model", model)
            return path

        wrong_namespace = write_model("wrong.3mf", b'<model xmlns="urn:evil"><resources/><build/></model>')
        spoofed_counts = write_model(
            "spoofed.3mf",
            b'''<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
            xmlns:x="urn:evil"><resources><x:object/><x:triangle/></resources><build><x:item/></build></model>''',
        )
        wrong = MODULE.analyze(wrong_namespace)["detection"]
        spoofed = MODULE.analyze(spoofed_counts)["detection"]
        self.assertEqual("detected-only", wrong["fidelity_tier"])
        self.assertEqual(0, spoofed["details"]["object_count"])
        self.assertEqual(0, spoofed["details"]["triangle_count"])
        self.assertEqual(0, spoofed["details"]["build_item_count"])

    def test_3mf_required_extension_blocks_geometry_claims(self) -> None:
        path = self.root / "extension.3mf"
        model = b'''<model requiredextensions="x" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
        xmlns:x="urn:required"><resources/><build/></model>'''
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                b'''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
                <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>''',
            )
            archive.writestr(
                "_rels/.rels",
                b'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                <Relationship Target="/3D/3dmodel.model" Id="rel0"
                Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>''',
            )
            archive.writestr("3D/3dmodel.model", model)
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("detected-only", detection["fidelity_tier"])
        self.assertEqual("low", detection["confidence"])

    def test_utf16_xml_declarations_are_rejected(self) -> None:
        malicious = '''<?xml version="1.0" encoding="UTF-16"?>
        <!DOCTYPE svg [<!ENTITY boom "expanded">]>
        <svg xmlns="http://www.w3.org/2000/svg"><text>&boom;</text></svg>'''.encode("utf-16")
        standalone = self.write("unsafe.svg", malicious)
        self.assertEqual("unsafe-xml", MODULE.analyze(standalone)["detection"]["format"])

        packaged = self.root / "unsafe.3mf"
        model = '''<?xml version="1.0" encoding="UTF-16"?>
        <!DOCTYPE model [<!ENTITY boom "expanded">]>
        <model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
        <resources/><build/></model>'''.encode("utf-16")
        with zipfile.ZipFile(packaged, "w") as archive:
            archive.writestr("[Content_Types].xml", b"<Types/>")
            archive.writestr("_rels/.rels", b"<Relationships/>")
            archive.writestr("3D/3dmodel.model", model)
        detection = MODULE.analyze(packaged)["detection"]
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_svg_namespace_must_be_official_or_absent(self) -> None:
        spoofed = self.write("spoofed.svg", b'<x:svg xmlns:x="urn:not-svg"><x:path/></x:svg>')
        self.assertEqual("unknown", MODULE.analyze(spoofed)["detection"]["format"])

    def test_prose_does_not_spoof_brep_dxf_or_ascii_stl(self) -> None:
        brep = self.write("readme.txt", b"This README mentions CASCADE TOPOLOGY but contains no CAD.")
        dxf = self.write("fake.dxf", b"hello\n0\nSECTION\n2\nENTITIES\nbye")
        stl = self.write("fake.stl", b"solid prose facet normal nonsense vertex nope endsolid")
        self.assertEqual("unknown", MODULE.analyze(brep)["detection"]["format"])
        self.assertEqual("unknown", MODULE.analyze(dxf)["detection"]["format"])
        self.assertEqual("unknown", MODULE.analyze(stl)["detection"]["format"])

    def test_structured_ascii_stl_is_validated(self) -> None:
        path = self.write(
            "part.stl",
            b"solid part\nfacet normal 0 0 1\nouter loop\nvertex 0 0 0\nvertex 1 0 0\nvertex 0 1 0\nendloop\nendfacet\nendsolid part\n",
        )
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("stl-ascii", detection["format"])
        self.assertEqual(1, detection["details"]["facet_count"])

    def test_zip_based_proprietary_suffix_preserves_routing_hint(self) -> None:
        path = self.root / "design.f3d"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("opaque.bin", b"payload")
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("fusion-design", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_compressed_step_is_detected_without_extraction(self) -> None:
        path = self.root / "part.stpz"
        step = b"ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\nENDSEC;\nEND-ISO-10303-21;"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("part.stp", step)
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("stpz", detection["format"])
        self.assertEqual("exact-brep", detection["fidelity_tier"])

    def test_truncated_compressed_step_is_only_a_candidate(self) -> None:
        path = self.root / "truncated.stpz"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("part.stp", b"ISO-10303-21;")
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("stpz-candidate", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_step_requires_content_signature_not_extension(self) -> None:
        valid = self.write("valid.bin", b"ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\nENDSEC;\nEND-ISO-10303-21;")
        spoof = self.write("spoof.step", b"not actually a CAD file")
        self.assertEqual("step", MODULE.analyze(valid)["detection"]["format"])
        self.assertEqual("unknown", MODULE.analyze(spoof)["detection"]["format"])

    def test_binary_stl_length_is_validated(self) -> None:
        triangle = b"\0" * 50
        valid = self.write("part.stl", b"binary".ljust(80, b"\0") + struct.pack("<I", 1) + triangle)
        truncated = self.write("bad.stl", b"binary".ljust(80, b"\0") + struct.pack("<I", 2) + triangle)
        self.assertEqual("stl-binary", MODULE.analyze(valid)["detection"]["format"])
        bad = MODULE.analyze(truncated)["detection"]
        self.assertEqual("unknown", bad["format"])
        self.assertTrue(any("length mismatch" in warning for warning in bad["warnings"]))

    def test_binary_stl_checks_every_triangle_for_non_finite_values(self) -> None:
        finite = struct.pack("<12fH", *([0.0] * 12), 0)
        non_finite = struct.pack("<12fH", float("nan"), *([0.0] * 11), 0)
        path = self.write("nan.stl", b"binary".ljust(80, b"\0") + struct.pack("<I", 2) + finite + non_finite)
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("unknown", detection["format"])
        self.assertTrue(any("triangle 1" in warning for warning in detection["warnings"]))

    def test_empty_binary_stl_is_not_high_confidence_mesh(self) -> None:
        path = self.write("empty.stl", b"empty".ljust(80, b"\0") + struct.pack("<I", 0))
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("unknown", detection["format"])
        self.assertTrue(any("no triangles" in warning for warning in detection["warnings"]))

    def test_obj_and_svg_are_distinguished(self) -> None:
        obj = self.write("part.data", b"v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n")
        svg = self.write("profile.svg", b'<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0"/></svg>')
        self.assertEqual("obj", MODULE.analyze(obj)["detection"]["format"])
        svg_detection = MODULE.analyze(svg)["detection"]
        self.assertEqual("svg", svg_detection["format"])
        self.assertEqual("2d-reference", svg_detection["fidelity_tier"])

    def test_svg_reports_scale_layers_transforms_and_profile_candidates(self) -> None:
        svg = self.write(
            "profiles.svg",
            b'''<svg xmlns="http://www.w3.org/2000/svg"
            xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
            width="100mm" height="50mm" viewBox="0 0 100 50">
            <g inkscape:groupmode="layer" inkscape:label="Cut" id="layer1" transform="translate(1 2)">
            <path d="M0 0 L10 0"/><path d="M0 0 L10 0 Z"/><polygon points="0,0 1,0 0,1"/>
            </g></svg>''',
        )
        detection = MODULE.analyze(svg)["detection"]
        details = detection["details"]
        self.assertEqual("mm", detection["units"])
        self.assertEqual(1, details["open_profile_candidates"])
        self.assertEqual(2, details["closed_profile_candidates"])
        self.assertEqual("Cut", details["layers"][0]["label"])
        self.assertEqual(1, details["transform_count"])

    def test_ascii_dxf_reports_units_layers_extents_and_profiles(self) -> None:
        path = self.write(
            "profiles.dxf",
            b'''0\nSECTION\n2\nHEADER\n9\n$INSUNITS\n70\n4\n9\n$EXTMIN\n10\n0\n20\n0\n30\n0\n9\n$EXTMAX\n10\n100\n20\n50\n30\n0\n0\nENDSEC\n0\nSECTION\n2\nENTITIES\n0\nLINE\n8\nOPEN\n10\n0\n20\n0\n11\n10\n21\n0\n0\nLWPOLYLINE\n8\nCLOSED\n70\n1\n10\n0\n20\n0\n10\n1\n20\n0\n10\n1\n20\n1\n0\nENDSEC\n0\nEOF\n''',
        )
        detection = MODULE.analyze(path)["detection"]
        details = detection["details"]
        self.assertEqual("millimeter", detection["units"])
        self.assertEqual(["CLOSED", "OPEN"], details["layers"])
        self.assertEqual(1, details["open_profile_candidates"])
        self.assertEqual(1, details["closed_profile_candidates"])
        self.assertEqual([100.0, 50.0, 0.0], details["declared_bounds"]["maximum"])

    def test_obj_external_material_reference_and_late_invalid_data_are_rejected(self) -> None:
        path = self.write(
            "unsafe.obj",
            b"v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\nmtllib \\\\attacker\\share\\payload.mtl\nv nan 0 0\nf 1 2 99\n",
        )
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("obj-candidate", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])
        self.assertEqual(1, detection["details"]["invalid_vertex_lines"])
        self.assertEqual(1, detection["details"]["invalid_face_lines"])
        self.assertTrue(detection["details"]["external_material_references"])

    def test_large_obj_and_invalid_obj_are_distinguished(self) -> None:
        vertices = b"v 0 0 0\n" * 140_000
        large = self.write("large.obj", vertices + b"f 1 2 3\n")
        invalid = self.write("invalid.obj", b"v nope\nf nope\n")
        self.assertEqual("obj", MODULE.analyze(large)["detection"]["format"])
        self.assertEqual("unknown", MODULE.analyze(invalid)["detection"]["format"])

    def test_obj_face_indices_must_resolve_to_existing_vertices(self) -> None:
        path = self.write("bad-index.obj", b"v 0 0 0\nv 1 0 0\nv 0 1 0\nf 99 100 101\n")
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("obj-candidate", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_obj_scan_caps_single_line_memory(self) -> None:
        path = self.write("overlong.obj", b"v " + b"0" * (MODULE.MAX_OBJ_LINE_BYTES + 64))
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("obj-candidate", detection["format"])
        self.assertTrue(any("line longer" in warning for warning in detection["warnings"]))

    def test_iges_envelope_is_only_a_candidate_until_parser_load(self) -> None:
        start = b"".ljust(72, b" ") + b"S" + b"      1"
        terminate = b"".ljust(72, b" ") + b"T" + b"      1"
        path = self.write("minimal.igs", start + b"\n" + terminate + b"\n")
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("iges-candidate", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])

    def test_svg_requires_xml_root_not_comment_text(self) -> None:
        commented = self.write("comment.xml", b"<root><!-- <svg></svg> --></root>")
        prefixed = self.write(
            "prefixed.svg",
            b'<svg:svg xmlns:svg="http://www.w3.org/2000/svg"><svg:path/></svg:svg>',
        )
        self.assertEqual("unknown", MODULE.analyze(commented)["detection"]["format"])
        self.assertEqual("svg", MODULE.analyze(prefixed)["detection"]["format"])

    def test_weak_cad_signatures_are_not_high_confidence(self) -> None:
        short_step = self.write("short.step", b"ISO-10303-21;")
        fake_iges = self.write("fake.igs", b" " * 72 + b"S")
        self.assertEqual("unknown", MODULE.analyze(short_step)["detection"]["format"])
        self.assertEqual("unknown", MODULE.analyze(fake_iges)["detection"]["format"])

    def test_proprietary_suffix_is_detected_only(self) -> None:
        path = self.write("part.SLDPRT", b"opaque proprietary payload")
        detection = MODULE.analyze(path)["detection"]
        self.assertEqual("solidworks-part", detection["format"])
        self.assertEqual("detected-only", detection["fidelity_tier"])
        self.assertEqual("low", detection["confidence"])

    def test_standard_blender_install_is_reported_when_path_lookup_fails(self) -> None:
        blender = self.root / "Blender Foundation" / "Blender 5.2" / "blender.exe"
        blender.parent.mkdir(parents=True)
        blender.write_bytes(b"fixture")
        part = self.write("part.obj", b"v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n")
        with mock.patch.object(MODULE.shutil, "which", return_value=None), mock.patch.object(
            MODULE, "_standard_blender_candidates", return_value=[blender]
        ), mock.patch.object(MODULE, "_standard_freecad_candidates", return_value=[]):
            self.assertEqual(str(blender.resolve()), MODULE.analyze(part)["available_backends"]["blender"])

    def test_version_sort_is_numeric_not_lexicographic(self) -> None:
        old = Path("C:/Program Files/FreeCAD 1.9/bin/FreeCADCmd.exe")
        new = Path("C:/Program Files/FreeCAD 1.10/bin/FreeCADCmd.exe")
        self.assertGreater(MODULE._version_key(new), MODULE._version_key(old))

    def test_cli_report_is_json_serializable(self) -> None:
        path = self.write("empty", b"")
        payload = json.dumps(MODULE.analyze(path))
        self.assertIn('"schema_version": "1.0"', payload)

    def test_cli_refuses_to_overwrite_input(self) -> None:
        path = self.write("part.obj", b"v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n")
        self.assertEqual(2, MODULE.main([str(path), "--output", str(path)]))
        self.assertTrue(path.read_bytes().startswith(b"v 0 0 0"))


if __name__ == "__main__":
    unittest.main()
