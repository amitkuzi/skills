# adhd-hebrew

An [Agent Skill](https://agentskills.io) that formats AI assistant responses for fast scanning and low working-memory load — with first-class support for Hebrew (RTL) prose alongside LTR code, commands, and paths.

Works with Claude (claude.ai, Claude Code, Claude API) and any other agent platform that supports the open Agent Skills standard (Cursor, VS Code, GitHub Copilot, etc.).

## What it does

- Leads every answer with the direct answer, not a preamble
- Structures responses into short, scannable sections (🎯 answer / 🔧 what to do / ✅ result / 👉 next step)
- Keeps Hebrew prose natural for RTL reading while keeping code, commands, file paths, URLs, and identifiers in LTR code blocks
- Uses progressive disclosure — minimum useful explanation first, details tucked under a "פרטים" (details) section
- Recommends one default option instead of listing many alternatives
- Defaults code samples to C# / .NET (configurable — see `SKILL.md`)

## Install

### Claude.ai (Pro / Max / Team / Enterprise)
1. Download or clone this repo, zip the folder.
2. Go to **Settings → Features → Skills** (or **Customize → Skills**) → **+** → **Create skill** → upload the ZIP.

### Claude Code
```bash
git clone https://github.com/<your-username>/adhd-hebrew.git ~/.claude/skills/adhd-hebrew
```

### Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("adhd-hebrew.skill", "rb") as f:
    skill = client.skills.create(name="adhd-hebrew", file=f)
```

### Other Agent Skills-compatible platforms
Follow your platform's skill-loading instructions and point it at this folder — it's a standard `SKILL.md` package with no extra dependencies.

## Example

**Prompt:** "יש לי שגיאת 404 בקריאת API"

**Response style:**
```
### 🎯 הבעיה
כתובת ה-endpoint שגויה או שהשרת לא רץ.

### 🔧 תיקון
1. בדוק את `appsettings.json`
2. ודא שהשרת רץ על הפורט הנכון:
   \`\`\`bash
   curl http://localhost:5000/health
   \`\`\`

### 👉 הצעד הבא
הרץ את הבדיקה למעלה ותגיד לי מה חוזר.
```

## Configuration

Edit `SKILL.md` directly to change:
- Default programming language for code samples (defaults to C# / .NET)
- Emoji anchors for section headers (or remove them)
- Whether to always respond in Hebrew vs. only when the user writes in Hebrew

## License

MIT — see [LICENSE](./LICENSE).

## Contributing

Issues and PRs welcome. Keep changes to `SKILL.md` focused — this skill is intentionally small and dependency-free (no `scripts/`, `references/`, or `assets/` needed).
