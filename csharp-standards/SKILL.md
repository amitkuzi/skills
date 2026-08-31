---
name: csharp-standards
description: Team coding standards for .NET/C# work — the Manager/Engine/Accessor three-layer architecture, immutable records and DTOs, async and CancellationToken rules, structured logging, testing requirements, and the counter-model review workflow. Use this skill for ANY task that writes, refactors, reviews, or plans C#/.NET code, adds a service or interface, touches data access, or produces a test plan — even when the user does not mention standards, architecture, or conventions explicitly.
---

# C# / .NET Coding Standards

Apply these rules to all C#/.NET work. They are binary — either the code complies or it does not.
When a rule cannot be followed, do not silently skip it: add an inline comment stating exactly why.

## Architecture (hard rules)

1. Dependency direction: `API -> Manager -> Engine` and `Manager -> Accessor`.
   Never skip a layer, never reverse a dependency.
2. **Engine never references an Accessor.** Engines are pure domain logic over data handed to them.
3. Standard Manager flow:
   a. call the Accessor(s) to load the data/state the operation needs
   b. validate that data/state
   c. pass it to the Engine for processing
   d. persist the resulting state through the Accessor
   If this flow is not feasible for a given method, add a comment explaining exactly why.
4. Accessors return DTOs. Storage entities never cross the Accessor boundary.
5. Utils and extension methods are for readability only — never for business logic or state.

## Types and data

6. Prefer `record` / `record struct` for DTOs, results, options, and messages.
7. Data structures crossing a layer boundary are immutable: init-only or constructor-set, no public setters, no mutable collection properties (expose `IReadOnlyList<T>` / `IReadOnlyDictionary<,>`).
8. Nullable reference types enabled. No `!` (null-forgiving) without an inline justification comment.

## Async and performance

9. No `.Result`, no `.Wait()`, no `async void` (event handlers excepted).
10. Every public async method accepts a `CancellationToken` and passes it down the whole chain.
11. No N+1 access patterns; no unbounded materialization of large sets — stream or page.

## Logging, config, security

12. Inject `ILogger<T>` (or the platform-appropriate logging abstraction). Never `Console.WriteLine`, never a static logger.
13. Structured logging only — message templates with named properties, not string interpolation.
14. No PII in log messages or log properties.
15. No secrets or connection strings in code or `appsettings.*` — configuration provider only.

## Testing

16. Every new public method on an injected service/interface gets tests.
17. Every major change updates the affected tests and adds new ones. All tests pass before a PR.
18. Unit tests mock only interfaces we own. Anything crossing DB/HTTP/filesystem is an integration test.
19. Each sub-task gets a written test plan before implementation (see `references/counter-model-review.md`).

## Naming and docs

20. Human-readable names. Acronyms capitalized consistently across the whole solution (pick `Id`/`Api`/`Db` style and never mix).
21. Public types and members are documented; the comment says *why*, not *what*.

## Reference files

Read the relevant file when the task goes deeper than the rules above:

| File | Read it when |
|---|---|
| `references/architecture.md` | designing or reviewing layer placement, DTO boundaries, DI wiring |
| `references/testing.md` | writing a test plan, choosing unit vs integration, naming tests |
| `references/async-and-performance.md` | async chains, cancellation, streaming, hot paths |
| `references/logging-and-errors.md` | exception policy, log levels, structured event design |
| `references/counter-model-review.md` | any multi-step task: test plan + competing-model review loop |
