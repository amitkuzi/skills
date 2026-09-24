from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "run_freecad_geometry_report.py"
SPEC = importlib.util.spec_from_file_location("run_freecad_geometry_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FreeCadLauncherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source = self.root / "part.FCStd"
        self.source.write_bytes(b"fixture")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_output_cannot_equal_or_replace_an_existing_file(self) -> None:
        with self.assertRaisesRegex(ValueError, "overwrite"):
            MODULE._validate_paths(self.source, self.source)
        existing = self.root / "report.json"
        existing.write_text("preserve", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "already exists"):
            MODULE._validate_paths(self.source, existing)
        self.assertEqual("preserve", existing.read_text(encoding="utf-8"))

    def test_verified_report_rejects_error_payload(self) -> None:
        output = self.root / "report.json"
        output.write_text(json.dumps({"schema_version": "1.0", "error": "bad model"}), encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "bad model"):
            MODULE._load_verified_report(output)

    def test_verified_report_accepts_expected_schema(self) -> None:
        output = self.root / "report.json"
        expected = {
            "schema_version": "1.0",
            "source": str(self.source),
            "freecad": {},
            "objects": [],
            "limitations": [],
        }
        output.write_text(json.dumps(expected), encoding="utf-8")
        self.assertEqual(expected, MODULE._load_verified_report(output))

    def test_verified_report_rejects_schema_only_payload(self) -> None:
        output = self.root / "report.json"
        output.write_text(json.dumps({"schema_version": "1.0"}), encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "required fields"):
            MODULE._load_verified_report(output)

    def test_nonzero_freecad_exit_rejects_even_valid_report(self) -> None:
        output = self.root / "report.json"

        def fake_run(*args, **kwargs):
            report = {
                "schema_version": "1.0",
                "source": str(self.source),
                "freecad": {},
                "objects": [],
                "limitations": [],
            }
            Path(kwargs["env"]["SLANT3D_FREECAD_OUTPUT"]).write_text(json.dumps(report), encoding="utf-8")
            return SimpleNamespace(returncode=7, stdout="", stderr="failure")

        with mock.patch.object(MODULE.subprocess, "run", side_effect=fake_run):
            with self.assertRaisesRegex(RuntimeError, "code 7"):
                MODULE.run(self.source, output, Path(sys.executable))

    def test_zero_exit_without_report_preserves_backend_diagnostic(self) -> None:
        output = self.root / "missing.json"
        completed = SimpleNamespace(
            returncode=0,
            stdout='{"schema_version":"1.0","error":"Cannot open STEP file"}',
            stderr="<Exception> Cannot open STEP file",
        )
        with mock.patch.object(MODULE.subprocess, "run", return_value=completed):
            with self.assertRaisesRegex(RuntimeError, "Cannot open STEP file"):
                MODULE.run(self.source, output, Path(sys.executable))

    def test_standard_install_is_used_when_path_lookup_fails(self) -> None:
        installed = self.root / "FreeCADCmd.exe"
        installed.write_bytes(b"fixture")
        with mock.patch.object(MODULE.shutil, "which", return_value=None), mock.patch.object(
            MODULE, "_standard_freecad_candidates", return_value=[installed]
        ):
            self.assertEqual(installed.resolve(), MODULE._find_freecad_cmd(None))

    def test_standard_install_selection_uses_numeric_version_order(self) -> None:
        older = self.root / "FreeCAD 1.9" / "bin" / "FreeCADCmd.exe"
        newer = self.root / "FreeCAD 1.10" / "bin" / "FreeCADCmd.exe"
        older.parent.mkdir(parents=True)
        newer.parent.mkdir(parents=True)
        older.write_bytes(b"old")
        newer.write_bytes(b"new")
        with mock.patch.object(MODULE.shutil, "which", return_value=None), mock.patch.object(
            MODULE, "_standard_freecad_candidates", return_value=[older, newer]
        ):
            self.assertEqual(newer.resolve(), MODULE._find_freecad_cmd(None))

    def test_diagnostics_are_bounded_and_paths_are_redacted(self) -> None:
        source = str(self.source.resolve())
        lines = [f"warning {index} {source}" for index in range(30)]
        result = MODULE._bounded_diagnostics("\n".join(lines), {source: "<input>"})
        self.assertEqual(20, len(result))
        self.assertTrue(all(source not in line for line in result))
        self.assertTrue(all(len(line) <= 300 for line in result))


if __name__ == "__main__":
    unittest.main()
