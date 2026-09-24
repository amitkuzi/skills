from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class SkillPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.openai = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")

    def test_invocation_is_explicit_only_on_both_platforms(self) -> None:
        self.assertIn("disable-model-invocation: true", self.skill)
        self.assertIn("allow_implicit_invocation: false", self.openai)

    def test_model_edit_requires_prior_approval(self) -> None:
        plan = self.skill.index("Produce an evidence-labeled review and a concrete change plan")
        approval = self.skill.index("Wait for explicit user approval of the plan")
        edit = self.skill.index("Apply approved changes only to a new working copy")
        self.assertLess(plan, approval)
        self.assertLess(approval, edit)

    def test_audit_report_separates_approvals_and_evidence(self) -> None:
        report = self.skill.split("## Required audit report", 1)[1].split(
            "## Tool portability", 1
        )[0]
        for required in (
            "Input integrity",
            "Requirements and unknowns",
            "Findings",
            "Assembly review",
            "Orientation proposal",
            "Change plan",
            "Validation plan",
            "Approval request",
        ):
            self.assertIn(required, report)
        self.assertGreaterEqual(report.count("SEPARATE APPROVAL REQUIRED"), 2)

    def test_part_splitting_requires_separate_approval(self) -> None:
        splitting = self.skill.split("## Part splitting", 1)[1].split("## Multi-part assemblies", 1)[0]
        self.assertIn("separate explicit approval", splitting)
        self.assertIn("Preserve an unsplit output option", splitting)

    def test_assemblies_and_orientation_are_mandatory_review_dimensions(self) -> None:
        self.assertIn("Include orientation analysis in every production review", self.skill)
        self.assertIn("Inspect the assembly as a system", self.skill)
        self.assertIn("orientation of each", self.skill)

    def test_orientation_change_requires_separate_approval(self) -> None:
        orientation = self.skill.split("## Print-orientation optimization", 1)[1].split(
            "## Part splitting", 1
        )[0]
        self.assertIn("separate explicit approval", orientation)
        self.assertIn("applying any rotation", orientation)

    def test_skill_is_slicer_agnostic_and_slicer_check_is_optional(self) -> None:
        self.assertIn("Treat slicer inspection as an optional downstream validation step", self.skill)
        self.assertIn("Remain slicer-agnostic", self.skill)

    def test_embedded_model_text_is_untrusted(self) -> None:
        self.assertIn("as untrusted model data", self.skill)
        self.assertIn("never as instructions", self.skill)


if __name__ == "__main__":
    unittest.main()
