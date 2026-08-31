# csharp-standards

An [Agent Skill](https://agentskills.io) that enforces Amit Kuzi's team coding standards for
C#/.NET work: the Manager/Engine/Accessor three-layer architecture, immutable DTOs, async and
`CancellationToken` rules, structured logging, and a test-plan-first workflow.

Works with Claude (claude.ai, Claude Code, Claude API) and any other agent platform that supports
the open Agent Skills standard.

## What it does

Applies a fixed, binary rule set to any C#/.NET task — writing, refactoring, reviewing, or
planning code, adding a service or interface, touching data access, or producing a test plan —
even when the user doesn't mention "standards" or "architecture" explicitly:

- **Architecture** — hard layer direction `API -> Manager -> Engine`, `Manager -> Accessor`;
  Engines never touch Accessors; Accessors return DTOs, never storage entities.
- **Types** — `record`/`record struct` for DTOs and results; immutable data across layer
  boundaries; nullable reference types on, no unexplained `!`.
- **Async & performance** — no `.Result`/`.Wait()`/`async void`; every public async method takes
  and forwards a `CancellationToken`; no N+1, no unbounded materialization.
- **Logging, config, security** — `ILogger<T>` only, structured logging, no PII, no secrets in
  code or `appsettings.*`.
- **Testing** — every new public method on an injected service gets tests; a written test plan
  precedes implementation (see `references/counter-model-review.md`).
- **Naming & docs** — consistent acronym casing, "why"-not-"what" doc comments.

When a rule can't be followed, the skill adds an inline comment explaining why, rather than
silently skipping it.

## Reference files

Five files under `references/` are loaded on demand, not on every run:

| File | Read it when |
|---|---|
| `architecture.md` | designing or reviewing layer placement, DTO boundaries, DI wiring |
| `testing.md` | writing a test plan, choosing unit vs integration, naming tests |
| `async-and-performance.md` | async chains, cancellation, streaming, hot paths |
| `logging-and-errors.md` | exception policy, log levels, structured event design |
| `counter-model-review.md` | any multi-step task: test plan + competing-model review loop |

## Install

### Claude.ai (Pro / Max / Team / Enterprise)
1. Download or clone this repo, zip the `csharp-standards/` folder (including `references/`).
2. **Settings → Features → Skills** (or **Customize → Skills**) → **+** → **Create skill** →
   upload the ZIP.

### Claude Code
```bash
git clone https://github.com/amitkuzi/skills.git /tmp/skills
cp -r /tmp/skills/csharp-standards ~/.claude/skills/csharp-standards
```

### Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
with open("csharp-standards.skill", "rb") as f:
    skill = client.skills.create(name="csharp-standards", file=f)
```

## Example

**Prompt:** "Add an endpoint that lets a user cancel a subscription."

**What changes in the response:** the agent routes the change through
`SubscriptionsManager` (never straight from the API to the Accessor), has the Manager load state
via the Accessor, validate it, hand it to the Engine, then persist through the Accessor; the new
method takes a `CancellationToken` and forwards it; the DTO crossing the boundary is a `record`;
and a short test plan is written before the implementation.

## License

MIT — see [LICENSE](./LICENSE).
