# Testing Strategy Best Practices

## The Testing Pyramid

```
          /‾‾‾‾‾‾‾‾‾‾‾‾‾\
         /   E2E Tests    \       ~10 %  – slow, expensive, high confidence
        /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
       / Integration Tests  \    ~20 %  – test interactions between components
      /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
     /      Unit Tests        \  ~70 %  – fast, isolated, numerous
    /___________________________\
```

### Coverage Targets (minimum)

| Level | Target |
|-------|--------|
| Unit | 80 % line coverage |
| Integration | All critical API paths |
| E2E | All happy-path user journeys |

---

## Test Types

### Unit Tests
- Test a single function/class in isolation.
- Mock all external dependencies (DB, HTTP calls, file system).
- Run in < 1 second per suite.
- **Tools**: Jest, JUnit, pytest, NUnit.

### Integration Tests
- Test interactions between two or more modules.
- Use a real (in-memory or Dockerised) database.
- Cover success and failure scenarios for each API endpoint.
- **Tools**: Supertest, RestAssured, pytest + httpx.

### End-to-End (E2E) Tests
- Simulate real user flows through the UI.
- Run against a deployed environment (staging or a dedicated test env).
- Keep suite small and focused on critical journeys.
- **Tools**: Playwright, Cypress.

### Contract Tests
- Validate that producer and consumer agree on the API contract.
- Run automatically when either side changes.
- **Tools**: Pact.

### Performance Tests
- Establish baseline metrics before every release.
- Types: load test, stress test, soak test, spike test.
- Alert when p95 latency > threshold or error rate > 1 %.
- **Tools**: k6, JMeter, Gatling.

---

## Shift-Left Principles

| Practice | Benefit |
|---------|---------|
| Write tests alongside code, not after | Defects found earlier cost 10× less to fix |
| Definition of Done includes tests | No feature is "done" without passing tests |
| QA involved in story refinement | Acceptance criteria = test scenarios |
| Automated tests gate every PR | No broken code reaches main |

---

## Test Data Management

- Use **factories / fixtures** to create test data programmatically.
- Never share state between tests – each test should set up and tear down its own data.
- Do **not** use production data in test environments (privacy / GDPR).
- Seed scripts must be idempotent (safe to run multiple times).

---

## Environments

| Environment | Purpose | Data |
|-------------|---------|------|
| Local (dev) | Feature development, quick feedback | Synthetic |
| CI | Automated test gate on every PR | Synthetic |
| QA / Test | Full regression, exploratory testing | Synthetic (anonymised copy) |
| Staging | UAT, performance tests, final sign-off | Production-like |
| Production | Real users | Real |
