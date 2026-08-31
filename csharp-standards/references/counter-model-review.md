# Counter-Model Workflow

The implementing agent does not grade its own work. Every non-trivial task runs through a
competing agent (the "counter model") for test authoring and review.

## Roles

| Role | Responsibility |
|---|---|
| Implementor | decomposes the task, writes the production code |
| Counter model | writes the test plan and the tests, reviews the code adversarially |
| Validator | confirms the standards checklist before the deliverable ships |

The counter model should be a different model or a separately-prompted agent with no access to
the implementor's reasoning — only to the requirement and the resulting code.

## Loop, per sub-task

1. **Decompose** — the task is split into sub-tasks, each with one testable outcome.
2. **Test plan** — the counter model writes the test plan for the sub-task
   (see `testing.md`) *before* implementation. It is written against the requirement,
   not against the implementation.
3. **Implement** — the implementor writes production code to satisfy the requirement.
4. **Test implementation** — the counter model implements the planned tests.
5. **Adversarial review** — the counter model reviews the diff against this standards set and
   reports findings as: `[BLOCKER] / [SHOULD] / [NIT]`, each with file, line, and rule number
   from `SKILL.md`.
6. **Iterate** — the implementor resolves every `[BLOCKER]`, and either fixes or explicitly
   rejects each `[SHOULD]` with a reason. Repeat 4–5 until no blockers remain.
7. **Validate** — the Validator runs the checklist below and only then does the output move on.

Search / research sub-tasks follow the same loop: the counter model re-runs the search
independently and reconciles differences before findings are accepted.

## Review checklist

- [ ] Dependency direction respected; Engine does not touch an Accessor
- [ ] Manager follows collect -> validate -> process -> persist, or documents the deviation
- [ ] No storage entity crosses the Accessor boundary
- [ ] Cross-boundary types are immutable records
- [ ] No `.Result` / `.Wait()` / `async void`; `CancellationToken` threaded through
- [ ] `ILogger<T>` injected; structured logging; no PII; no secrets
- [ ] Nullable enabled; every `!` justified inline
- [ ] Tests exist for every new public method on an injected interface
- [ ] Unit tests mock only interfaces we own
- [ ] All tests pass; coverage did not decrease
