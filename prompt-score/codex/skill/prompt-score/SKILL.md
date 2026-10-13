---
name: prompt-score
description: Score every user prompt from 1 to 100 for prompt-engineering quality (goal, context, constraints, output format, success criteria, specifics, structure, length) and offer follow-up actions. Use on every user message while active, or when the user asks to score, grade or improve a prompt.
---

For each user message (skip messages that start with `/`):

1. Run the scorer on the user's exact text and put its one-line output at the very top of the reply:

```
node "$CODEX_HOME/skills/prompt-score/score.mjs" "<the user's prompt>"
```

(`CODEX_HOME` defaults to `~/.codex`.) Example output:
`Prompt score: 72/100 (good) - biggest gap: Output format. Say what the answer should look like: format, language, length.`

2. Then answer the request normally.

## Actions menu

After the score line, add `Actions: breakdown | tips | rewrite | history` only when the score is below 80 or the user asks. Handle the user's pick:

- **breakdown**: run the script with `--json` and show points per category as a short list.
- **tips**: list the tips of every category that lost points (from the `--json` output).
- **rewrite**: rewrite the user's prompt as a well-engineered one (clear goal, context, constraints, output format, success criteria), keeping their intent and language; show it and offer to run it.
- **history**: list the scores given earlier in this conversation and their average.

The score is a fast heuristic from keywords and structure, not a quality judgment; say so if the user asks how it is computed.
