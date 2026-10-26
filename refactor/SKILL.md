---
name: refactor
description: Behavior-preserving refactoring that makes code simple, human, readable, debuggable and maintainable — Clean Code and SOLID (Uncle Bob) applied to every function, public/main/interface functions turned into story-like orchestration functions built from small well-named calls, pure "engine" logic separated from "accessor" I/O (DB, storage, network, screen rendering), and repeated code unified into small helpers. Use whenever the user asks to refactor, clean up, simplify, humanize, untangle, "make readable/maintainable", split a long function, remove duplication, or review code for clean-code/SOLID — in any language — even if they don't name this skill.
license: MIT
metadata:
  version: 1.0.0
  released: 2026-10-26
---

# Refactor — code a human can read like a story

Goal: after this skill runs, a developer who has never seen the code can open any public
function, read it top to bottom like a short paragraph, understand *what* it does, and drill
down only where they need *how*. Behavior does not change.

For C#/.NET, also apply the `csharp-standards` skill: its Manager / Engine / Accessor layers are
the same split described here (Orchestrator ≈ Manager). Where the two disagree, `csharp-standards`
wins for C#.

## Non-negotiables

1. **Behavior-preserving.** Refactoring changes structure, never results, side effects, ordering
   of I/O, error types, or public signatures. A bug you find is reported, not silently fixed — fix
   it only as a separate, named step the user approves.
2. **Safety net first.** Before moving code, run the existing tests. If the code under change has
   no tests — or its tests only run inside a host runtime you can't start — pin current behavior
   with a characterization snapshot (see Workflow step 1). If even that is impossible, say so and
   keep steps smaller.
3. **Small steps, green between each.** One mechanical change (extract, rename, move, inline),
   run tests, next change. Never a big-bang rewrite.
4. **Public contract is frozen** unless the user approves: names, parameters, return types,
   exceptions, file/module exports.
5. **Stay in scope.** Refactor what was asked. Don't reformat unrelated files or chase every smell
   in the repo — list them in the report instead.

## Workflow

Follow these steps in order. Steps 3–6 are the core of the skill.

### 1. Scope and baseline
- Identify target files/functions. Read the surrounding code and match its language idioms,
  naming style and comment density.
- Run tests / build / linter and record the baseline result. Pre-existing failures are noted, not
  hidden.
- **Characterization snapshot** (when tests are missing or can't run): copy the original file to a
  scratch folder, write a small harness that calls the public functions over a corpus of inputs —
  typical cases, empty/whitespace, boundaries (every `>=`/`<` threshold), non-English text, very
  long input — and save the output as JSON. After the refactor, run the same harness on the new file
  and byte-compare. Identical output is the proof of "behavior unchanged".
- Look for **mirrored copies** of the code (ports to another language, duplicated scripts, comments
  like "keep in sync with X"). Either refactor them the same way or list them in the report as
  now structurally out of sync.

### 2. Map every function
For each function in scope, classify it into exactly one role:

| Role | Does | Must not |
|---|---|---|
| **Orchestrator** | Public / main / interface / handler / entry point. Sequences steps by calling other functions. | Contain computation, loops with logic, parsing, string building, or raw I/O. |
| **Engine** | Pure logic: compute, decide, validate, transform, format. Data in → data out. | Touch I/O, clocks, randomness, globals, or mutable shared state. |
| **Accessor** | One external boundary: DB, file/storage, network/API, cache, env/config, clock, screen/UI render, logging sink. | Make business decisions, branch on domain rules, or call engines. |
| **Helper** | Tiny shared utility that removes repetition (e.g. `toCents`, `joinPath`). | Hold business rules or state. |

A function that mixes roles is the main refactoring target — split it.

### 3. Turn public functions into orchestrations (do this first)
Every main / public / exported / interface-implementing function becomes an orchestration that
reads like a story:

```text
function placeOrder(request):
    order        = parseOrderRequest(request)        # engine
    customer     = loadCustomer(order.customerId)    # accessor
    ensureCustomerCanOrder(customer, order)          # engine (throws on violation)
    pricedOrder  = applyDiscounts(order, customer)   # engine
    saveOrder(pricedOrder)                           # accessor
    sendConfirmationEmail(customer, pricedOrder)     # accessor
    return toOrderReceipt(pricedOrder)               # engine
```

Rules for an orchestrator:
- **One level of abstraction.** Every line is a call at the same "altitude". No `for` loop with a
  body of logic, no arithmetic, no string formatting, no SQL, no DOM/console calls inline.
- **Typical shape: load (accessor) → decide/compute (engine) → persist/render (accessor) → return.**
  If a different order is required, add a one-line comment saying why.
- **Short:** aim for ≤ 10–15 lines. Longer means a step is hiding inside — extract it.
- **Named intermediates.** Assign each step's result to a descriptive variable instead of nesting
  calls `a(b(c(x)))`. This reads better and gives every step a breakpoint.
- **Step-down rule.** Callees appear below their caller in the file, in the order they are called,
  so the file reads top-down like a newspaper.
- A one-line doc comment on the orchestrator states the *business* purpose, not the mechanics.
- **Repeated steps of the same shape** (a list of checks, validators, exporters, handlers) become
  a data table of rules plus one loop: `RULES.map(rule => runRule(rule, input))`. Adding a variant
  is then adding a table entry — the orchestrator never grows (Open/Closed).

### 4. Extract engines (pure logic)
- Move each computation, decision, validation and transformation into its own small function.
- Make it **static / free / module-level** where the language allows; it receives everything it
  needs as parameters and returns a value. No hidden reads of `this`, globals, time or randomness —
  pass `now`, `config`, `seed` in.
- Name it as a verb phrase describing the result: `calculateShippingCost`, `isEligibleForRefund`,
  `buildInvoiceLines`. Predicates start with `is/has/can/should`.
- Engines are where the unit tests go — they need no mocks.

### 5. Isolate accessors (I/O)
- Each accessor wraps exactly one external concern and does the minimum: call the resource, map
  the raw result to a plain data object, translate low-level errors into meaningful ones with
  context (`CustomerNotFound(customerId)`, not a bare driver exception).
- Accessors are injected (constructor / parameter / module boundary) rather than created inline,
  so orchestrators can be tested with fakes (Dependency Inversion). Add an interface only where the
  language needs one for substitution or a second implementation is realistic — not by reflex.
- Logging and metrics live at accessor and orchestrator boundaries, not deep in engines.
- Screen rendering counts as I/O: the engine builds a view-model; the accessor/renderer draws it.

### 6. Unify repeated code
- Find blocks repeated (exactly or near-exactly) and extract each into one small, well-named
  helper or engine. Parameterize the differences.
- Apply the **rule of three** as a guide: two copies may stay if merging them hurts clarity;
  three or more get unified.
- Beware **accidental duplication**: code that looks the same but changes for different reasons
  stays separate (Single Responsibility beats DRY).

### 7. Clean Code and SOLID pass on every function in scope
Go through each function and check the list in [references/checklist.md](references/checklist.md).
Highlights:
- **Names** reveal intent; no abbreviations, no `data`, `info`, `tmp`, `handle`, `process`, `do`
  without an object. Rename to fit the role (orchestrator = use case, engine = result, accessor =
  resource + verb: `loadCustomer`, `writeReport`, `renderCart`).
- **Small and does one thing.** If you can extract a function with a name that isn't a restatement
  of the code, it does more than one thing.
- **Arguments:** 0–2 ideal, 3 max; group more into a parameter object. No boolean flag arguments —
  split into two functions.
- **Command–query separation:** a function either changes state or returns information, not both.
- **No hidden side effects.** A function named `checkPassword` does not also start a session.
- **Guard clauses** instead of deep nesting; max ~2 levels of indentation.
- **Errors:** throw/return meaningful errors with context; don't return `null` / magic values for
  failure; don't swallow exceptions.
- **Comments explain *why*,** never restate *what*. Delete commented-out code and comments made
  obsolete by good names.
- **SOLID:** single responsibility per function and class; open for extension without editing
  orchestrators (strategy/map instead of growing `switch`); substitutable implementations; small
  focused interfaces; depend on abstractions at I/O boundaries.
- **Boy Scout ("polite code") rule:** leave every touched function cleaner and kinder to the next
  reader than you found it — consistent formatting, obvious names, no surprises.

### 8. Make it debuggable
- Every orchestration step is its own line with a named result → one breakpoint per step.
- Errors carry the identifiers needed to reproduce (ids, file paths, input sizes — never secrets).
- Avoid clever one-liners, chained ternaries and dense comprehensions where a named helper is
  clearer.

### 9. Verify
- Re-run the same tests / build / linter as the baseline. Results must match or improve.
- Re-read each public function aloud: if it doesn't read like a story, iterate.
- Re-run the characterization harness and byte-compare with the baseline snapshot.
- Type-check / compile with the project's strictest settings.
- Confirm the public contract is unchanged (diff signatures/exports).
- If the project ships releases, a refactor is still a source change: follow the project's
  release/version policy before publishing it.

### 10. Report
Finish with a short report:
- **Function map:** table of public functions → the orchestration steps they now call, with each
  callee's role (Orchestrator / Engine / Accessor / Helper).
- **Duplications unified:** what was merged into which helper.
- **Verification:** baseline vs. after (tests, build, lint) with real output, not claims.
- **Not done / suggested follow-ups:** bugs found but not fixed, smells out of scope, places where
  a rule was deliberately not applied and why.

## When to stop and ask

- The only way to apply a rule changes a public signature or observable behavior.
- No tests exist and characterization tests can't be written (e.g. needs live external systems).
- The code is generated, vendored, or performance-critical where extra calls/allocations matter —
  confirm the trade-off first.

See [references/examples.md](references/examples.md) for before/after examples in Python and
TypeScript.
