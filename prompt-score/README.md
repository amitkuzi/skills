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

## Layout

| Path | Contents |
|------|----------|
| `.claude-plugin/plugin.json` | Mod manifest |
| `hooks/register.tsx` | Hooks: score on submit, chat badge, band + actions menu |
| `hooks/score.ts`, `hooks/score.test.ts` | Scoring rules and test |
| `types/index.d.ts` | `$.state` contract |
| `codex/` | Codex port: `score.mjs`, `skill/prompt-score/SKILL.md`, installers |

Keep `hooks/score.ts` and `codex/score.mjs` in sync when changing the rules.
