# Testing

## When a test is mandatory

- A new public method on an injected service or interface.
- Any change to Engine logic (Engines are pure — they are the cheapest and highest-value tests).
- Any bug fix: first a failing test reproducing the bug, then the fix.
- Any change to a Manager's orchestration order or validation branches.

## Unit vs integration

| Kind | Scope | Doubles |
|---|---|---|
| Unit | Engine (no doubles needed), Manager (Accessors + Engines doubled) | mock only interfaces we own |
| Integration | Accessor against a real store (Testcontainers / Atlas test DB), API through the full pipeline | no mocks of our own code |

Never mock `DbContext`, an HTTP client, a driver, or any third-party type. If the test needs
one, it is an integration test.

## Naming

`MethodName_Scenario_ExpectedOutcome`

```
SubmitAsync_CustomerInactive_ReturnsRejected
Apply_CouponExpired_IgnoresCoupon
```

## Structure

- Arrange / Act / Assert, separated by blank lines, no comments needed.
- One logical assertion per test; use a fluent assertion library for readable failures.
- No `Thread.Sleep`; no shared mutable static state between tests.
- Test data built through a builder or `record` `with`-expression, not copy-pasted literals.

## Test plan per sub-task

Before implementing a sub-task, write a test plan file listing:

1. Method / behavior under test
2. Happy path
3. Validation failures (one row per branch)
4. Edge cases (empty, null, boundary, cancellation)
5. Which cases are unit and which are integration

The test plan is implemented by the counter model — see `counter-model-review.md`.

## Gates

- All tests pass before a PR is opened.
- Coverage does not decrease. New Engine code is covered at line level.
- A PR that changes behavior without touching a test is rejected by default.
