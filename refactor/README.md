# refactor

An [Agent Skill](https://agentskills.io) for behavior-preserving refactoring that makes code
simple, human, readable, debuggable and maintainable.

**Version:** 1.0.0 — **Released:** 2026-10-26 (canonical source: `metadata` in `SKILL.md`)

## What it does

1. **Clean Code + SOLID (Uncle Bob)** applied to every function in scope, via a yes/no checklist
   ([references/checklist.md](references/checklist.md)).
2. **Orchestration-first:** every main / public / interface function becomes a short story of
   well-named calls — load → decide → persist/render → return — one breakpoint per step.
3. **Engine vs. Accessor split:** pure logic (static, data in → data out, unit-testable without
   mocks) is separated from I/O boundaries (DB, storage, network, config, clock, screen render).
4. **Duplication unified** into small helpers (rule of three, without merging code that only
   *looks* alike).
5. **Safety:** baseline tests first (characterization tests if none exist), small green steps,
   frozen public contract, and a final report with real before/after verification.

For C#/.NET it defers to [`csharp-standards`](../csharp-standards) (Manager/Engine/Accessor).

## Example prompts

- "Refactor `OrderService.ts` so it's readable."
- "Clean up this function, it's 200 lines."
- "Apply clean code and SOLID to the `billing/` module."

## Install

**Claude Code**
```bash
cp -r refactor ~/.claude/skills/refactor
```

**Claude.ai** — zip this folder, then **Settings → Features → Skills → + → Create skill**.

## Files

```
refactor/
  SKILL.md                  workflow and rules
  references/checklist.md   per-function yes/no checklist
  references/examples.md    before/after in Python and TypeScript
  README.md, LICENSE
```

## License

MIT © Amit Kuzi
