# Logging and Error Handling

## Logging

- Inject `ILogger<T>` (or the platform-appropriate abstraction). No static loggers, no `Console.WriteLine`.
- Structured only — named properties in the message template:

```csharp
_logger.LogInformation("Order {OrderId} submitted for {CustomerId}", order.Id, order.CustomerId);   // yes
_logger.LogInformation($"Order {order.Id} submitted");                                              // no
```

- Property names are stable and PascalCase — they are a query surface, not prose.
- Never log PII (name, email, phone, address, national ID, free-text user content) in the message
  or in properties. Log identifiers, not identities.
- Never log secrets, tokens, connection strings, or full request/response bodies.

## Levels

| Level | Use |
|---|---|
| Trace/Debug | developer diagnostics, off in production |
| Information | business-meaningful transitions (one per operation, not per line) |
| Warning | recoverable, expected-but-notable (retry, validation rejection) |
| Error | operation failed, user impact |
| Critical | process-level failure |

Log an exception once, at the boundary that handles it. Do not log-and-rethrow at every layer.

## Exceptions

- Exceptions are for exceptional conditions. Expected validation failures are a result type
  returned by the Manager, not an exception.
- Never `catch (Exception)` without rethrowing or converting to a domain-meaningful result.
- Never swallow: an empty catch block is a defect.
- Always `throw;` — never `throw ex;` (destroys the stack trace).
- Custom exceptions derive from a single solution-level base and carry structured context.

## Correlation

- Every request/job establishes a correlation id and it flows through the logging scope.
- Accessors log external-call duration and outcome, not payloads.
