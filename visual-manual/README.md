# Visual Manual

Version **1.0.0** · MIT © Amit Kuzi

Creates original LEGO/IKEA-style visual manuals with numbered diagrams, parts/tool inventories,
arrows, checkpoints, and concise captions. Hebrew **and** English are included by default.
Request additional languages or explicitly ask for a single language to override the default.
Works for physical assembly and software installation. The default artifact is a self-contained,
printable HTML manual with inline SVG; PDF can be requested when an exporter is available.

## Use

Natural-language requests such as `הכן הוראות הרכבה למדף מהתמונות המצורפות`,
`Create installation instructions for this software`, or `Write an assembly manual`
are discoverable triggers. Explicit invocation: `$visual-manual` in Codex or
`/visual-manual` in Claude Code. Automatic selection depends on the host and model;
installation makes the skill available and allows implicit invocation but cannot guarantee selection.

## Install

Clone this repository, then copy the **whole** `visual-manual` folder to:

- Codex: `~/.codex/skills/visual-manual/`
- Claude Code: `~/.claude/skills/visual-manual/`

For PowerShell, run from the repository root:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE/.codex/skills", "$env:USERPROFILE/.claude/skills" | Out-Null
Copy-Item -Recurse -LiteralPath ./visual-manual -Destination "$env:USERPROFILE/.codex/skills/visual-manual"
Copy-Item -Recurse -LiteralPath ./visual-manual -Destination "$env:USERPROFILE/.claude/skills/visual-manual"
```

These commands assume a fresh installation. For an existing copy, replace only that skill's
folder with the new package. Start a fresh session after installing if the running session does
not discover it. See [Claude Code's official skill documentation](https://code.claude.com/docs/en/skills).

`assets/manual-template.html` is a reusable layout with clearly marked demonstration content;
it is not a manufacturer-verified assembly guide. Generated manuals must replace it with
subject-specific diagrams and verified specifications.
