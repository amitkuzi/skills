# Architecture — Manager / Engine / Accessor

## Layers

| Layer | Owns | Must NOT |
|---|---|---|
| API / Controller | transport, auth, model binding, HTTP status mapping | contain business logic, touch Accessors |
| Manager | orchestration, data collection, validation, persistence, transaction boundary | contain domain algorithms |
| Engine | domain logic, calculations, rules, transformations — pure over its inputs | touch Accessors, IO, clock, or config directly |
| Accessor (DAL/Repository) | all DB/storage/external-API interaction, entity <-> DTO mapping | contain business rules |

## Dependency direction

```
API ──> Manager ──> Engine
             └───> Accessor
```

Never skip a layer. Never reverse. Engine has no reference to Accessor.

## Canonical Manager method shape

```csharp
public async Task<OrderResult> SubmitAsync(OrderRequest request, CancellationToken ct)
{
    // 1. collect
    var order    = await _orderAccessor.GetAsync(request.OrderId, ct);
    var customer = await _customerAccessor.GetAsync(order.CustomerId, ct);

    // 2. validate
    if (order is null) return OrderResult.NotFound(request.OrderId);
    if (!customer.IsActive) return OrderResult.Rejected("inactive customer");

    // 3. process (pure)
    var processed = _pricingEngine.Apply(order, customer, request.Coupons);

    // 4. persist
    await _orderAccessor.SaveAsync(processed.Order, ct);

    return OrderResult.Ok(processed.Order.Id);
}
```

If a method cannot follow collect -> validate -> process -> persist, keep the deviation and
document it inline, e.g.:

```csharp
// DEVIATION: streaming export — the full result set does not fit in memory, so the Engine
// is invoked per page inside the Accessor's async stream rather than on a pre-collected set.
```

## DTO boundary

- Accessors map storage entities to DTOs internally. EF entities, BSON documents, and generated
  API clients' models never leave the Accessor assembly.
- Cross-boundary types are `record`s with init-only members.
- No inheritance between DTOs and storage entities.

## Dependency injection

- Register interfaces, not concretes. Constructor injection only; no service locator.
- Lifetimes: Accessor = Scoped, Engine = Singleton (must be stateless), Manager = Scoped.
- An Engine that cannot be Singleton is a design smell — it is holding state it should receive as a parameter.
- `IClock` / `TimeProvider` and any randomness are injected, never called statically inside an Engine.

## Placement decision aid

- "It talks to a database, a queue, a file, or another service" -> Accessor.
- "It decides *what* the answer is" -> Engine.
- "It decides *what order things happen in* and what gets saved" -> Manager.
- "It has no domain meaning and is pure syntax sugar" -> extension method in Utils.
