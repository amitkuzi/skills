# grill-me

An [Agent Skill](https://agentskills.io) that runs a relentless, structured interview to
stress-test a plan, design, decision or idea before you act on it.

Works with Claude (claude.ai, Claude Code, Claude API) and any other agent platform that supports
the open Agent Skills standard.

## Attribution

This skill is **not originally authored by Amit Kuzi**. It is an unmodified copy of
`skills/productivity/grill-me` + `skills/productivity/grilling` from
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT license, © Matt Pocock), kept here
because it's part of Amit's day-to-day toolkit. See [LICENSE](./LICENSE) for the full license
text and provenance note.

## What it does

- Maps the problem as a **design tree** — every decision branches into the decisions that hang
  off it.
- Works the tree in **rounds**: asks every question whose prerequisites are already settled (the
  "frontier") in one batch, each with a recommended answer, then waits for the user.
- Never asks the user for a fact it could look up itself — dispatches a sub-agent or runs the
  lookup directly, and only blocks the questions that genuinely depend on that lookup.
- Recomputes the frontier after each round of answers, until nothing is left unsettled or
  silently assumed.
- Does not act until the user confirms a shared understanding has been reached.

## Install

### Claude.ai (Pro / Max / Team / Enterprise)
1. Download or clone this repo, zip the `grill-me/` folder.
2. **Settings → Features → Skills** (or **Customize → Skills**) → **+** → **Create skill** →
   upload the ZIP.

### Claude Code
```bash
git clone https://github.com/amitkuzi/skills.git /tmp/skills
cp -r /tmp/skills/grill-me ~/.claude/skills/grill-me
```

### Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("grill-me.skill", "rb") as f:
    skill = client.skills.create(name="grill-me", file=f)
```

## Example

**Prompt:** "grill me about this migration plan before I start."

**Response shape:**
```
❓ **Q1** - **Rollback strategy**: If the migration fails halfway, do you want an automatic
rollback or a manual one?

➡️ Automatic rollback — a manual one risks someone forgetting the runbook exists.

❓ **Q2** - **Downtime window**: ...
➡️ ...
```
The agent asks the whole current round, waits for answers, then reshapes the tree and asks the
next round — until every branch is settled.

## License

MIT, © Matt Pocock — see [LICENSE](./LICENSE) for the full text and provenance note.
