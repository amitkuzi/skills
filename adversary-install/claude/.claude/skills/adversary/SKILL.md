---
name: adversary
description: "Run an independent adversarial QA-and-repair loop automatically after creating or materially changing code, documents, presentations, spreadsheets, media, designs, or other user deliverables. Use it before handing off a completed artifact; do not use for simple factual answers or actions that have no reviewable output."
---

# Adversary review loop

Before handing off a reviewable deliverable, subject it to an independent adversarial review and repair loop. This applies by default after producing or materially changing code, documents, spreadsheets, presentations, PDFs, images, videos, websites, designs, data outputs, or configuration.

## Guardrails

- Do not alter user intent, acceptance criteria, or unrelated work just to raise a score.
- Use an independent reviewer/agent with fresh context when delegation is available. Give it the task, acceptance criteria, final artifact, and relevant tests—not the implementation plan, prior scores, or desired conclusion. If delegation is unavailable, perform a clearly separated adversarial pass and actively seek disconfirming evidence.
- Never auto-retry external, irreversible, costly, security-sensitive, or user-facing mutations (deployment, send, publish, delete, payment, credentials, production data). Diagnose and present the needed correction for authorization instead.
- Do not claim a score is based on validation that was not run. A score estimates demonstrated quality, not certainty.

## Cycle

1. Establish acceptance criteria and the relevant validation methods. For code, run targeted tests, lint/type/build checks, and inspect the diff. For documents and visuals, render and inspect the output. For data, check source, calculations, ranges, and edge cases. For video/media, inspect timing, content, export integrity, and playback where available.
2. Have the reviewer attack the output for correctness, completeness, regressions, usability, accessibility, security/privacy, maintainability, and task-specific failures. Return findings as: severity (`blocker`, `critical`, `high`, `medium`, `low`), evidence, impact, and specific repair.
3. Calculate a `0–100` quality score using demonstrated evidence. Start at 100 and subtract: blocker 40, critical 25, high 12, medium 5, low 1. Do not score above 90 when any critical or blocker issue remains.
4. Fix all safe, in-scope findings; rerun the validations affected by each fix. Record what changed and what remains.
5. Repeat the review and repair cycle for at least **four** full iterations, even if an earlier score exceeds 90. Continue past four until the final verified score is at least **90** and there are no blocker or critical findings.

## Stop and handoff

Stop when the criteria above are met, or when a remaining correction requires user authorization, unavailable inputs, or an external irreversible action. In the handoff report provide the final score, the number of iterations, validations actually run, material fixes, and any remaining limitation. Keep the report concise.
