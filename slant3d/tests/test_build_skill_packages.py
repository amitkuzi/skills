from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "build_skill_packages.py"
SPEC = importlib.util.spec_from_file_location("build_skill_packages", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BuildSkillPackagesTests(unittest.TestCase):
    def test_builds_separate_explicit_only_manifests(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "packages"
            packages = MODULE.build(output)
            claude_skill = (packages["claude_code"] / "SKILL.md").read_text(encoding="utf-8")
            codex_skill = (packages["codex"] / "SKILL.md").read_text(encoding="utf-8")
            codex_agent = (packages["codex"] / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn("disable-model-invocation: true", claude_skill)
            self.assertNotIn("disable-model-invocation", codex_skill)
            self.assertIn("allow_implicit_invocation: false", codex_agent)
            for package in packages.values():
                manifest = json.loads((package / "package-manifest.json").read_text(encoding="utf-8"))
                self.assertFalse(manifest["implicit_invocation"])
                self.assertIn("references/production-design.md", manifest["files"])
                self.assertIn("scripts/cad_input_report.py", manifest["files"])
                self.assertIn("docs/production-design-best-practices.he.md", manifest["files"])
                self.assertIn(
                    "research/claims/best-practice-traceability-matrix.md", manifest["files"]
                )
                self.assertIn(
                    "research/independent-validation-2026-09-24.md", manifest["files"]
                )
                self.assertIn("tests/behavior-scenarios.md", manifest["files"])
                self.assertIn("tests/behavior-validation-results.md", manifest["files"])

    def test_refuses_to_replace_existing_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "packages"
            output.mkdir()
            with self.assertRaisesRegex(ValueError, "already exists"):
                MODULE.build(output)


if __name__ == "__main__":
    unittest.main()
