# Core System Design Concepts

A quick-reference glossary of the most important terms you will encounter when designing distributed systems.

---

## Scalability

The ability of a system to handle increased load.

| Type | Description |
|------|-------------|
| **Vertical scaling** (scale up) | Add more resources (CPU, RAM) to a single machine |
| **Horizontal scaling** (scale out) | Add more machines and distribute load across them |

Horizontal scaling is generally preferred for internet-scale systems because vertical scaling hits hardware limits.

---

## Availability vs. Consistency (CAP Theorem)

A distributed system can guarantee at most **two** of the following three properties simultaneously:

- **C**onsistency — every read receives the most recent write
- **A**vailability — every request receives a (non-error) response
- **P**artition tolerance — the system continues operating despite network partitions

In practice, partition tolerance is non-negotiable, so the real trade-off is **CP vs. AP**.

---

## Latency vs. Throughput

- **Latency** — time to complete a single request (milliseconds)
- **Throughput** — number of requests processed per unit of time (requests/second)

Optimising for one can hurt the other; understand the workload before tuning.

---

## Caching

Store expensive computation results close to the consumer to reduce latency and backend load.

| Layer | Example |
|-------|---------|
| Browser cache | HTTP `Cache-Control` headers |
| CDN | Cloudflare, AWS CloudFront |
| Application cache | Redis, Memcached |
| Database query cache | Built-in MySQL query cache |

**Cache invalidation** (knowing when to expire stale data) is one of the hardest problems in distributed systems.

---

## Load Balancing

Distribute incoming traffic across multiple servers to avoid overloading any single node.

- **Round-robin** — requests sent to each server in turn
- **Least connections** — next request goes to the server with fewest active connections
- **Consistent hashing** — routes a given key to the same server (useful for caching)

---

## Replication

Keep copies of data on multiple nodes to improve availability and read throughput.

- **Leader–follower** — one primary accepts writes; replicas serve reads
- **Multi-leader** — multiple nodes accept writes (complex conflict resolution)
- **Leaderless** — clients write to multiple nodes directly (e.g., Amazon Dynamo)

---

## Further Reading

- [CAP theorem explained](https://www.ibm.com/topics/cap-theorem)
- *Designing Data-Intensive Applications* — Martin Kleppmann (Chapter 1–2)
