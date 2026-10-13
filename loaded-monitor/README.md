# loaded-monitor

A Claude Code mod that shows what the session has loaded: plugins and mods, skills,
tools, MCP servers and agents. Open it with `/loaded` (side pane) or the ✻ Loaded
button above the prompt (Ctrl+L).

## Install

From the Plugins screen: add the marketplace, then install.

```
/plugin marketplace add D:/Development/Skills
/plugin install loaded-monitor@amitkuzi-skills
```

(After pushing, `/plugin marketplace add amitkuzi/skills` also works.)

## Status

- v0.1.0: working prototype. Lists everything; no per-item status or menu yet.
- Target UI: [`design/loaded-panel.html`](./design/loaded-panel.html) (amitkuzi brand kit).
  Per item: status (Running / Loaded / Error / Disabled), scope tag, and a ⋯ menu with
  Settings, Tutorial, Info, Remove.

## Origin indicator

Every item is tagged: `●` made by me (green), `○` installed from elsewhere, `·` built-in.
Ownership comes from [`own.json`](./own.json): exact names, plus marketplaces (for `plugin@marketplace`).
Edit that file to change what counts as mine.

## Codex (OpenAI harness)

Codex has no mod API, so the Codex port is a skill plus a script that reads
`~/.codex/skills`, `config.toml` plugins and `mcp_servers`, with the same `●`/`○` marks.

```powershell
powershell -File D:/Development/Skills/loaded-monitor/codex/install.ps1
```

On Linux/macOS use `sh codex/install.sh`. Then ask Codex "what is loaded" (skill `loaded`),
or run `node ~/.codex/skills/loaded/loaded.mjs [--json]`.
Not available in Codex: the pane/button UI and the ⋯ menu.

## Layout

| Path | Contents |
|------|----------|
| `.claude-plugin/plugin.json` | Mod manifest |
| `hooks/hooks.json`, `hooks/register.tsx` | Hooks module (command, pane, band) |
| `types/index.d.ts` | `$.state` contract |
| `design/loaded-panel.html` | UI design mockup |
| `own.json` | Which items are mine |
| `codex/` | Codex port: `loaded.mjs`, `skill/loaded/SKILL.md`, `install.ps1`, `install.sh` |

## Run it

```bash
claude --plugin-dir D:/Development/Skills/loaded-monitor
```

## Open work

- Real status per item (MCP connection state, plugin load errors, disabled flags).
- Map connector UUID names to readable names.
- Split skills from slash commands; Agents list shows 0.
- Build the ⋯ menu and Settings / Tutorial / Info / Remove actions.
