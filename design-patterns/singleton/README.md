# Singleton Pattern

## Intent

Ensure a class has **only one instance** and provide a global point of access to it.

## When to Use

- A single shared resource is needed (e.g., configuration manager, connection pool, logger).
- You want to control concurrent access to a shared resource.

## When NOT to Use

- When global state makes testing difficult (prefer dependency injection instead).
- In multithreaded contexts without proper synchronisation.

## Structure

```
Client ──► Singleton.get_instance() ──► single shared instance
```

## Trade-offs

| Pros | Cons |
|------|------|
| Controlled access to single instance | Hard to unit test (global state) |
| Lazy initialisation possible | Can hide dependencies |
| Consistent state across application | Violates Single Responsibility Principle |

## Example

See [`python/singleton.py`](python/singleton.py).
