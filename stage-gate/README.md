# stage-gate

An [Agent Skill](https://agentskills.io) that turns "the tests pass" into an actual end-of-stage
checkpoint for multi-stage development missions: independent adversarial review + a real
usability/main-use-case pass, a numeric score with a fix-and-retest loop until it clears 90, a
written iteration log, a live demo, and a hard stop for human approval before the next stage
starts.

Works with Claude (claude.ai, Claude Code, Claude API) and any other agent platform that supports
the open Agent Skills standard.

## What it does

Runs automatically at the end of every development stage/milestone, without being asked:

1. **Two validation tracks, every iteration** — a correctness/adversary track (same attack surface
   as `anthropic-skills:adversary`: correctness, regressions, security, standards compliance) and a
   usability/main-use-case track (actually run the thing and exercise its primary flows, not just
   unit tests).
2. **Score 0-100**, same rubric as `adversary` (blocker -40, critical -25, high -12, medium -5,
   low -1; capped at 90 while a blocker/critical is open).
3. **Fix and re-verify**, then log the iteration (score, findings, evidence, fixes) to a per-stage
   log file.
4. **Repeat until the score clears 90** with no open blocker/critical — no manufactured minimum
   iteration count, but every iteration that ran gets logged.
5. **Demo** the real, running deliverable to the human.
6. **Stop and ask for explicit approval** before any work on the next stage begins.

## Why a separate skill from `adversary`

`adversary` is the general-purpose QA/repair loop for any deliverable. `stage-gate` is specifically
the *stage boundary* of a multi-stage mission: it adds the usability/main-use-case track (a green
test suite is not the same claim as "a user can actually do the thing"), the persistent per-stage
log, the demo step, and — the part that matters most — a real approval gate that blocks starting
the next stage's work. Use `adversary` mid-stage for any deliverable; use `stage-gate` at the
stage's end.

## Install

### Claude.ai (Pro / Max / Team / Enterprise)
1. Download or clone this repo, zip the `stage-gate/` folder.
2. **Settings → Features → Skills** (or **Customize → Skills**) → **+** → **Create skill** →
   upload the ZIP.

### Claude Code
```bash
git clone https://github.com/amitkuzi/skills.git /tmp/skills
cp -r /tmp/skills/stage-gate ~/.claude/skills/stage-gate
```

### Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("stage-gate.skill", "rb") as f:
    skill = client.skills.create(name="stage-gate", file=f)
```

## Example

**Context:** a coding session just finished a stage's implementation (code + unit tests green).

**What changes in the response:** instead of reporting done, the agent runs an independent
reviewer against the stage's acceptance criteria, separately starts the real service/app and
exercises its main use case end to end, scores both tracks together, fixes what's found, re-runs
what each fix touches, logs the iteration to `Team_workspace/logs/stage-gate/<stage-id>.md`,
repeats if still ≤ 90, then — once clear — runs a live demo and asks: "Score is 94/100, no open
issues. Here's the demo. Approve moving to Stage 2?" and waits.

## License

MIT — see [LICENSE](./LICENSE).
