# Per-function checklist

Run this on every function in scope. Each item is yes/no. A "no" is either fixed or listed in the
report with the reason it was kept.

## Role
- [ ] The function has exactly one role: Orchestrator, Engine, Accessor, or Helper.
- [ ] Public / main / exported / interface functions are Orchestrators.
- [ ] Engines do no I/O and read no hidden state (globals, `this` fields that change, time, random).
- [ ] Accessors contain no business decisions and call no engines.

## Orchestrators
- [ ] Reads like a short story; every line is a call at the same level of abstraction.
- [ ] ≤ ~15 lines; no inline loops-with-logic, arithmetic, formatting, SQL, DOM/console calls.
- [ ] Each step's result is in a named variable (one breakpoint per step).
- [ ] Shape is load → decide/compute → persist/render → return, or a comment explains why not.
- [ ] Has a one-line doc comment stating its business purpose.

## Clean Code
- [ ] Name reveals intent and matches the role (use case / result / resource + verb).
- [ ] Does one thing; nothing extractable with a non-trivial name remains inside.
- [ ] ≤ 3 parameters; no boolean flag parameters; related params grouped into an object.
- [ ] Command–query separation: changes state *or* returns data, not both.
- [ ] No hidden side effects beyond what the name promises.
- [ ] Guard clauses; indentation depth ≤ 2.
- [ ] No magic numbers/strings — named constants.
- [ ] Errors are meaningful, carry context, are not swallowed; no `null`/sentinel for failure.
- [ ] Comments say *why*; no commented-out code; no comment that restates the code.
- [ ] Callees sit below their caller in call order (step-down rule).

## SOLID (at function and class level)
- [ ] **S** — one reason to change.
- [ ] **O** — new variants are added by adding code (strategy, map, polymorphism), not by editing a
      growing `if/switch` in an orchestrator.
- [ ] **L** — any implementation of an abstraction can replace another without surprising callers.
- [ ] **I** — interfaces are small and specific to their consumers.
- [ ] **D** — orchestrators depend on injected accessors, not on concrete I/O created inline.

## Duplication
- [ ] No block repeated three or more times; near-duplicates are parameterized helpers.
- [ ] Similar-looking code that changes for different reasons was deliberately left separate.

## Debuggability
- [ ] No dense one-liners, chained ternaries, or deeply nested call expressions.
- [ ] Logs/metrics at boundaries only; error messages include the ids needed to reproduce, never
      secrets or personal data.

## Safety
- [ ] Behavior, public signatures, error types and I/O order are unchanged.
- [ ] Tests/build/lint match or beat the baseline.
