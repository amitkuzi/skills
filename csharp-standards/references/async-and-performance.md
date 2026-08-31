# Async and Performance

## Hard rules

- No `.Result`, `.Wait()`, `GetAwaiter().GetResult()` anywhere in product code.
- No `async void` except event handlers.
- Every public async method takes `CancellationToken ct` as its last parameter and passes it
  to every awaited call. No `CancellationToken.None` unless justified inline.
- Suffix async methods with `Async`.
- Do not wrap synchronous work in `Task.Run` inside server code.

## Cancellation

- Accessors pass `ct` to the driver/HTTP call.
- Long Engine loops call `ct.ThrowIfCancellationRequested()` at a sane interval.
- Background jobs (Hangfire) accept and honor the job cancellation token.

## Data access

- No N+1: batch by key or project the join at the store.
- Always constrain the result set — filter and page at the store, never with `.ToList().Where(...)`.
- Large result sets stream (`IAsyncEnumerable<T>`), they are not materialized into a `List<T>`.
- Read paths that never mutate use no-tracking / projection queries.

## Allocation and hot paths

- Prefer `record struct` for small, short-lived value carriers on measured hot paths only.
- Do not micro-optimize without a benchmark. "Consider performance" means: state the expected
  input size in the PR description, and add a benchmark when a path is expected to be hot.
- `StringBuilder` for loops that build strings; `Span<T>`/`Memory<T>` only where measured.

## Concurrency

- No `lock` around awaits. Use `SemaphoreSlim` with `WaitAsync`.
- Parallel fan-out uses a bounded degree of parallelism, never unbounded `Task.WhenAll` over
  an unbounded collection.
