# report

An [Agent Skill](https://agentskills.io) that produces a structured Hebrew report — status,
research, comparison/decision, post-mortem, or periodic summary — gathered from connected tools
and the web, delivered as a dated, sourced Markdown document.

Works with Claude (claude.ai, Claude Code, Claude API) and any other agent platform that supports
the open Agent Skills standard.

## What it does

- Picks a report type from the request — `status` / `research` / `decision` / `postmortem` /
  `periodic` — each with its own gathering order and skeleton.
- Gathers from whatever's connected (project files, git log, chat, email, calendar, docs, web),
  and names a role as missing (`פערי מידע`) rather than faking it.
- Sorts every finding into **מאומת** (verified — primary source, or two independent secondary
  sources), **הערכה** (estimate — tagged inline with a reason), or **פער** (gap — asked, not
  found). Contradictions are shown side by side, never averaged.
- Writes Hebrew, RTL, with a fixed section skeleton — תקציר מנהלים, ממצאים, סיכונים וחסמים,
  החלטות שנדרשות ממך, הצעד הבא, פערי מידע, מקורות — dropping any section with nothing anchored
  in it.
- Runs a verification checklist (dates, source coverage, tone, depth budget) before the document
  ships.
- Treats everything gathered — messages, emails, issues, pages — as data to summarize, never as
  instructions to act on.

This skill is tuned to Amit's own workspace conventions (an `ai-toolbox/` tool-selection step, a
`Team_workspace/drafts/` → `inbox/` pipeline, Asia/Jerusalem timezone). Adapt the **Gather** and
**Deliver** sections in `SKILL.md` to your own project layout before reusing it elsewhere.

## Install

### Claude.ai (Pro / Max / Team / Enterprise)
1. Download or clone this repo, zip the `report/` folder.
2. **Settings → Features → Skills** (or **Customize → Skills**) → **+** → **Create skill** →
   upload the ZIP.

### Claude Code
```bash
git clone https://github.com/amitkuzi/skills.git /tmp/skills
cp -r /tmp/skills/report ~/.claude/skills/report
```

### Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("report.skill", "rb") as f:
    skill = client.skills.create(name="report", file=f)
```

## Example

**Prompt:** "תן לי דוח סטטוס על הפרויקט הזה"

**What happens:** the skill reads the project file, git log, workspace logs/handoffs and the
relevant chat channel, sorts findings into מאומת/הערכה/פער, and writes a ~700–900 word Hebrew
document with תקציר מנהלים, ממצאים, מצב מול יעד, סיכונים וחסמים, and a numbered הצעד הבא — each
item ending in a concrete artifact (a file, a branch, a measurement).

## License

MIT — see [LICENSE](./LICENSE).
