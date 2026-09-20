# skills

Amit Kuzi's [Agent Skills](https://agentskills.io) — reusable instruction packages for Claude
(and any other Agent-Skills-compatible platform: Cursor, VS Code, GitHub Copilot, etc.).

Each skill is a self-contained folder with a `SKILL.md`, its own `README.md`, and its own
`LICENSE`.

## Skills

| Skill | What it does | License |
|---|---|---|
| [`adhd-hebrew`](./adhd-hebrew) | Ultra-concise, BLUF-first, scannable Hebrew response formatting for an ADHD reader — plus wrong-keyboard-layout (Hebrew/English) decoding. | MIT © Amit Kuzi |
| [`csharp-standards`](./csharp-standards) | Team C#/.NET coding standards — Manager/Engine/Accessor layering, immutable DTOs, async/`CancellationToken` rules, structured logging, test-plan-first workflow. | MIT © Amit Kuzi |
| [`grill-me`](./grill-me) | Relentless, structured interview that stress-tests a plan or decision before you act on it. **Sourced from [mattpocock/skills](https://github.com/mattpocock/skills)**, used unmodified. | MIT © Matt Pocock |
| [`report`](./report) | Produces a structured, sourced Hebrew report (status / research / decision / post-mortem / periodic) from connected tools and the web. | MIT © Amit Kuzi |
| [`stage-gate`](./stage-gate) | Mandatory end-of-stage checkpoint for multi-stage dev missions — adversary + usability review, score-and-fix loop to >90, iteration log, live demo, hard stop for human approval before the next stage. | MIT © Amit Kuzi |

## Install

Every skill folder works the same way:

**Claude.ai** — zip the skill's folder, then **Settings → Features → Skills → + → Create skill**
and upload the ZIP.

**Claude Code**
```bash
git clone https://github.com/amitkuzi/skills.git /tmp/skills
cp -r /tmp/skills/<skill-name> ~/.claude/skills/<skill-name>
```

**Claude API**
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("<skill-name>.skill", "rb") as f:
    skill = client.skills.create(name="<skill-name>", file=f)
```

See each skill's own `README.md` for a usage example and any skill-specific notes.

## Structure

```
skills/
  adhd-hebrew/         SKILL.md, README.md, LICENSE
  csharp-standards/     SKILL.md, README.md, LICENSE, references/*.md
  grill-me/              SKILL.md, README.md, LICENSE
  report/                SKILL.md, README.md, LICENSE
  stage-gate/            SKILL.md, README.md, LICENSE
```

## License

Each skill carries its own `LICENSE`. All are MIT; `grill-me` credits its original author
(Matt Pocock) rather than Amit Kuzi, since it's redistributed unmodified.
