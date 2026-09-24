from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "run_blender_mesh_report.py"
SPEC = importlib.util.spec_from_file_location("run_blender_mesh_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BlenderLauncherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source = self.root / "part.stl"
        self.source.write_bytes(b"fixture")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_standard_install_is_used_when_path_lookup_fails(self) -> None:
        installed = self.root / "Blender 5.2" / "blender.exe"
        installed.parent.mkdir()
        installed.write_bytes(b"fixture")
        with mock.patch.object(MODULE.shutil, "which", return_value=None), mock.patch.object(
            MODULE, "_standard_blender_candidates", return_value=[installed]
        ):
            self.assertEqual(installed.resolve(), MODULE._find_blender(None))

    def test_output_cannot_equal_or_replace_existing_file(self) -> None:
        with self.assertRaisesRegex(ValueError, "overwrite"):
            MODULE._validate_paths(self.source, self.source)
        output = self.root / "report.json"
        output.write_text("preserve", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "already exists"):
            MODULE._validate_paths(self.source, output)

    def test_nonzero_exit_rejects_even_valid_report(self) -> None:
        output = self.root / "report.json"

        def fake_run(*args, **kwargs):
            report = {
                "schema_version": "1.0",
                "source": str(self.source),
                "blender": {},
                "objects": [{}],
                "limitations": [],
            }
            Path(kwargs["env"]["SLANT3D_BLENDER_OUTPUT"]).write_text(json.dumps(report), encoding="utf-8")
            return SimpleNamespace(returncode=4, stdout="", stderr="failure")

        with mock.patch.object(MODULE.subprocess, "run", side_effect=fake_run):
            with self.assertRaisesRegex(RuntimeError, "code 4"):
                MODULE.run(self.source, output, Path(sys.executable))


if __name__ == "__main__":
    unittest.main()
