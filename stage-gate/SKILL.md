---
name: stage-gate
description: "Mandatory end-of-stage checkpoint for any multi-stage development mission. Runs a behavior-preserving refactor pass (the `refactor` skill) on the stage's code, then an independent adversarial review AND a usability/main-use-case pass, scores 0-100, fixes and re-tests in a loop until the score clears 90 with no blocker/critical, logs every iteration, then runs a live demo and stops for the human's explicit approval before the next stage starts. Use automatically at the end of every development stage/milestone — do not wait to be asked."
metadata:
  version: 1.1.0
  released: 2026-10-26
---

# Stage gate

A development mission (any project with sequential stages/milestones — Stage 1, Stage 2, a
sprint, a workplan phase) does not advance to its next stage on the strength of "tests pass."
This skill is the checkpoint between stages: it forces an independent review, a real usability
pass, a fix-and-retest loop with a numeric bar, a written log, and a live demo the human must
approve before the mission continues.

This skill composes with, and does not replace, `anthropic-skills:adversary` (the general QA/repair
loop this borrows its scoring rubric from), the `refactor` skill (used for the refactor pass) and
the `run` skill (used for the demo step). Any language-specific standards skill (e.g.
`csharp-standards`) still applies to the refactor pass and to whatever fixes get made.

## When this runs

Automatically, at the end of every development stage/milestone, before any work on the next stage
begins — whether or not the user asked for a review. If a mission's stages aren't explicit, treat
"a bounded chunk of work the user or the project plan calls done" as a stage boundary.

Do not skip this for a stage that "obviously worked" — that is exactly the overstatement failure
mode this exists to catch.

## Guardrails (inherited from `adversary`, restated because they're load-bearing here)

- Independent reviewer, fresh context, no prior involvement in writing the stage's code — give it
  the acceptance criteria and the artifact, not the implementation plan or a desired conclusion.
- Never let scope, acceptance criteria, or unrelated work drift just to raise the score.
- Never auto-retry an external, irreversible, costly, security-sensitive, or user-facing mutation
  (deploy, publish, real send, payment, credentials, production data, `git push`) to "fix" a
  finding — surface it and ask.
- A score reflects demonstrated evidence, not confidence. Don't claim a score based on validation
  that wasn't actually run.
- The approval gate at the end is real: do not start next-stage work — not even "just the setup" —
  until the human has explicitly approved. Silence is not approval.

## Cycle

1. **Establish the stage's acceptance criteria** from whatever governs this mission (a PRD/handoff/
   workplan requirement IDs, the task the user gave, or the stage's own stated exit evidence). Two
   tracks of validation are always in scope, every iteration:
   - **Correctness/adversary track**: correctness, completeness, regressions, security/privacy,
     maintainability, standards compliance (whatever language/architecture skill applies) —
     same as the `adversary` skill's attack surface.
   - **Usability/main-use-case track**: actually exercise the primary user-facing flows this stage
     was supposed to deliver — not unit tests, real end-to-end use. For a CLI: run it as a user
     would. For an API/service: start it and call the real endpoints. For a UI: drive it in a
     browser and complete the golden path plus its obvious edge cases. If a stage has no
     user-facing surface yet (pure backend plumbing), the "usability" track becomes "does the
     next consumer of this code (the next stage, or a documented interface) actually get what it
     needs" — state that explicitly rather than skipping the track silently.
2. **Refactor pass (once per gate, before the first review iteration).** Invoke the `refactor`
   skill on the code this stage added or changed — the stage's diff, nothing outside it:
   - Public / main / interface functions become story-like orchestrations; engine logic is split
     from accessor I/O; repeated code is unified; Clean Code + SOLID applied per function.
   - It is **behavior-preserving**: take the baseline first (tests, plus a characterization
     snapshot where tests are thin), refactor in small green steps, and re-verify with identical
     output before continuing. A refactor that changes behavior is reverted, not "fixed forward".
   - Bugs it uncovers are not fixed inside the refactor — they become findings for step 3.
   - Public contracts the stage committed to (APIs, CLI flags, file formats) stay frozen unless
     the stage's acceptance criteria say otherwise.
   - If the stage has no code (docs, config, research), skip the pass and say so in the log.
   The review tracks then run on the refactored code, so reviewers and the demo see what will
   actually ship. In later iterations, fixes follow the same rules (the `refactor` checklist is
   part of the maintainability attack surface) — don't run a second full refactor pass.
3. **Run both tracks.** Use an independent agent with fresh context for the adversary track
   (per the guardrail above). The usability track can be run directly — it's execution, not
   judgement-under-bias — but its results still feed the same score.
4. **Score 0-100** using the `adversary` skill's rubric: start at 100, subtract blocker 40 /
   critical 25 / high 12 / medium 5 / low 1 per finding across BOTH tracks combined; never score
   above 90 while any blocker/critical remains open.
5. **Fix every safe, in-scope finding** (both tracks), then re-run whichever validations each fix
   touches — rebuild/retest for code fixes, re-exercise the affected use case for usability fixes.
6. **Log the iteration** (see Logging below) before deciding whether to repeat.
7. **Repeat** steps 3-6 until the score is **> 90** and there is no open blocker/critical. There is
   no fixed minimum iteration count — a stage that scores 95 clean on iteration 1 does not need
   three more iterations manufactured to hit a quota; a stage stuck at 70 needs as many honest
   iterations as it takes. What's mandatory is that every iteration that actually ran gets logged,
   and that the loop does not stop below the bar.
8. **Demo.** Once the bar is cleared, run a live demo of the stage's actual deliverable — start the
   real service/app/CLI (via the `run` skill if the project has one, otherwise the project's own
   documented startup command) and walk through the main use case(s) with real output, not a
   description of what it would do. This is for the human, not for you — show it, don't just say
   it passed.
9. **Stop and ask for approval.** After the demo, explicitly ask the human to approve moving to the
   next stage. Do not begin next-stage work in the same turn as the demo. A vague "looks good" in
   passing does not count if the user's attention was on something else — if there's any doubt,
   ask directly ("approve moving to Stage N+1?").

## Logging

One log file per stage, created on the stage's first gate run and appended to on every iteration —
suggested path `Team_workspace/logs/stage-gate/<stage-id>.md` (adjust to the project's own logging
convention if one already exists, e.g. this project may already have `Team_workspace/logs/`).

The first entry records the refactor pass: files in scope, the function map (public function →
orchestration steps and their roles), duplications unified, baseline vs. after verification with
real output, and anything deliberately not refactored (or "skipped — no code in this stage").

Each iteration entry records:

- Iteration number, timestamp, score.
- Findings from both tracks (severity, evidence, fix applied or why not fixed).
- Real command output for anything re-verified (build/test/manual exercise) — no paraphrasing away
  the evidence.
- Running verdict: still below bar / cleared the bar.

The final entry additionally records the demo's outcome and the human's approval decision
(approved / changes requested / not yet asked).

## Do not

- Do not treat "all unit tests pass" as satisfying the usability track — unit tests and real usage
  are different failure modes; a stage can have 100% green tests and still be unusable end to end.
- Do not run the demo before the score clears 90 — the demo is the reward for a clean bar, not a
  substitute for one.
- Do not silently skip the usability track because the stage "is just backend" — state the
  narrower interpretation (next-consumer readiness) instead of dropping the track.
- Do not proceed to the next stage's work without an explicit approval captured in the log.
- Do not let the refactor pass reach outside the stage's diff, change behavior, or silently fix
  bugs — out-of-scope cleanup goes in a backlog note; bugs go through the scored findings.
- Do not let this gate become the excuse for scope creep — findings get fixed within the stage's
  existing scope; a good idea for later goes in a backlog note, not into this stage's diff.
