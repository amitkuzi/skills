# Visual Manual

Version **1.1.0** · MIT © Amit Kuzi

Creates original LEGO/IKEA-style visual manuals with numbered diagrams, parts/tool inventories,
arrows, checkpoints, and concise captions in a wide rounded hero/status/prerequisite-card layout.
Hebrew **and** English are included by default, with **Hebrew on the right and English on the left**
on desktop and in print.
Request additional languages or explicitly ask for a single language to override the default.
Works for physical assembly and software installation. Default deliverables are **both** a
self-contained HTML manual with inline SVG **and a real PDF exported from it**. Explicit format
requests override this default; unavailable PDF tooling is reported as a partial delivery.

Style precedence: explicit user preference, then established project style, then the user's
brandkit. In this workspace the brandkit is `D:\Development\amitkuzi-brandkit`; its actual palette,
logo, and local fonts are read and embedded when accessible. Unavailable assets are disclosed.

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
it is not a manufacturer-verified assembly guide. Its embedded palette and mark come from the
local brandkit; fonts are named fallbacks until embedded from the discovered kit for a generated
deliverable. Generated manuals replace it with subject-specific diagrams and verified specifications.
