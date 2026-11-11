# prompt-score

Scores every prompt you send from 1 to 100 for prompt-engineering quality (100 = best
engineered), with an actions menu. A fast offline heuristic (Hebrew and English), not an
LLM judgment.

## Install

From the Plugins screen: add the marketplace, then install.

```
/plugin marketplace add D:/Development/Skills
/plugin install prompt-score@amitkuzi-skills
```

(After pushing, `/plugin marketplace add amitkuzi/skills` also works.)

## Score (100 pts)

Clear goal 15, context 15, constraints 15, output format 15, success criteria / examples 15,
specifics 10, structure 10, length fit 5. Labels: excellent 80+, good 60+, fair 40+, weak.
Messages starting with `/` are not scored.

## Claude Code mod

Where the score shows:

- Right of each prompt in the chat: `[72/100 good]` (needs a surface that draws mod UI).
- Band above the prompt box with an **Actions** menu: breakdown, tips, rewrite (haiku),
  send the rewrite, history, hide.
- Status line: `prompt 72/100`.
- No in-reply score line: the hidden instruction that made the model start its reply with
  `Prompt score: N/100` was removed. Surfaces that draw no mod UI (the desktop Code tab)
  show nothing.

```bash
claude --plugin-dir D:/Development/Skills/prompt-score
claude plugin validate D:/Development/Skills/prompt-score
claude plugin test D:/Development/Skills/prompt-score
```

## Codex

Codex has no mod API, so the port is a skill plus `score.mjs` (same rules as `hooks/score.ts`).

```powershell
powershell -File D:/Development/Skills/prompt-score/codex/install.ps1
```

On Linux/macOS use `sh codex/install.sh`. The skill makes Codex start each reply with the score
line and offer breakdown / tips / rewrite / history. Try it directly:
`node codex/score.mjs "fix it"` (add `--json` for the breakdown).
Not available in Codex: the in-chat badge and the band.

## Microsoft Copilot (Windows)

Microsoft Copilot has no skills or hooks, so the port is a declarative agent whose instructions
embed `copilot/score.py` (same rules as `hooks/score.ts`) and run it with Code Interpreter.

```powershell
powershell -ExecutionPolicy Bypass -File D:/Development/Skills/prompt-score/copilot/install.ps1
```

Work account, no IT: in Microsoft 365 Copilot, Agents > New agent > Skip to configure, paste
`agent-instructions.txt` into Instructions and turn on "Create documents, charts, and code".
Builds `copilot/dist/prompt-score-copilot-<version>.zip` (Microsoft 365 Copilot agent package:
upload it in Teams > Apps > Manage your apps > Upload a custom app) and `consumer-prompt.txt`
(a text-only setup prompt built from `copilot/install-prompt.template.md`, for the personal Copilot app: `-Consumer` copies it to the clipboard and opens Copilot; paste it
as the first message of a chat; Copilot applies the rules in plain words, so its score can differ by a few points).
In the agent, without Code Interpreter the score line is marked `(estimated)`.
To make it permanent in personal Copilot, paste `custom-instructions.txt` into Settings > Personalization >
Custom instructions (`-Consumer` copies it); every new chat is then scored.
For a non-technical user, send only `PromptScore-Copilot-Setup-<version>.zip`: they unzip it and
double-click `START HERE.html`, which walks them through with copy buttons (Hebrew/English).
Step-by-step visual guide (Hebrew + English): `copilot/docs/install-manual.html` / `.pdf`,
rebuilt with `node copilot/docs/build-manual.mjs`.

## Version

`.claude-plugin/plugin.json` holds the version and `releaseDate`; the Copilot package, agent
`about` reply and manual read them from there.

- 0.6.0 (2026-10-27): work accounts without Custom instructions: build the agent yourself in Agent Builder (Agents > New agent > Skip to configure); START HERE.html gives copy buttons for Name, Description and Instructions (`agent-instructions.txt`); Teams upload becomes the fallback.
- 0.5.0 (2026-10-27): permanent setup for personal Copilot: `custom-instructions.txt` (1,366 chars, built from `copilot/custom-instructions.template.md`) goes into Settings > Personalization > Custom instructions and applies to every new chat; the one-chat prompt stays as a backup.
- 0.4.0 (2026-10-27): text-only setup prompt for personal Copilot (plain-language rules, confirmation reply); used by START HERE.html and shipped as `Copilot setup text.txt`.
- 0.3.0 (2026-10-27): one-file setup for non-technical users (`dist/PromptScore-Copilot-Setup-<version>.zip`: START HERE.html with copy buttons, agent package, PDF guide).
- 0.2.0 (2026-10-27): Microsoft Copilot port (`copilot/`): agent package, consumer prompt, installer, visual manual.

## Layout

| Path | Contents |
|------|----------|
| `.claude-plugin/plugin.json` | Mod manifest |
| `hooks/register.tsx` | Hooks: score on submit, chat badge, band + actions menu |
| `hooks/score.ts`, `hooks/score.test.ts` | Scoring rules and test |
| `types/index.d.ts` | `$.state` contract |
| `codex/` | Codex port: `score.mjs`, `skill/prompt-score/SKILL.md`, installers |
| `copilot/` | Microsoft Copilot port: `score.py`, instructions template, `appPackage/` templates, `install.ps1`, `docs/` manual |

Keep `hooks/score.ts`, `codex/score.mjs` and `copilot/score.py` in sync when changing the rules
(`node copilot/parity.mjs` checks the last two).
