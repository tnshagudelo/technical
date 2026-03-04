# Test Automation Best Practices

## Principles

1. **Automate the right things** – automate repetitive, stable, regression-prone scenarios. Leave exploratory testing manual.
2. **Tests are first-class code** – review them like production code; avoid duplication, keep them readable.
3. **Fast feedback** – unit tests in < 5 min, integration < 10 min, E2E < 30 min.
4. **Independent tests** – each test must be able to run alone in any order.
5. **Deterministic** – flaky tests are worse than no tests. Fix or delete them.

---

## Framework Selection Guide

| Need | Recommended Tool |
|------|----------------|
| Unit / integration (JS/TS) | Jest |
| Unit / integration (Python) | pytest |
| Unit / integration (Java) | JUnit 5 + Mockito |
| API testing | Postman / Newman, Supertest, RestAssured |
| E2E Web | Playwright (preferred), Cypress |
| E2E Mobile | Appium, Detox |
| Performance | k6 (simple), Gatling (advanced) |
| Contract | Pact |

---

## Project Structure (JavaScript / TypeScript example)

```
tests/
├── unit/
│   └── services/
│       └── user-service.test.ts
├── integration/
│   └── api/
│       └── users.test.ts
└── e2e/
    ├── fixtures/         # Test data and helpers
    ├── pages/            # Page Object Models
    └── specs/
        └── login.spec.ts
```

---

## Page Object Model (POM) Pattern

Use POM for E2E tests to keep test logic separate from UI selectors.

```ts
// pages/LoginPage.ts
import { Page } from '@playwright/test';

export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.page.fill('[data-testid="email"]', email);
    await this.page.fill('[data-testid="password"]', password);
    await this.page.click('[data-testid="submit"]');
  }
}

// specs/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('should log in with valid credentials', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login('user@example.com', 'P@ssw0rd!');
  await expect(page).toHaveURL('/dashboard');
});
```

---

## CI Integration

- Unit and integration tests run on **every PR**.
- E2E tests run on **merge to main** (or nightly if slow).
- Performance tests run **before every release**.
- Test results and coverage reports are published as CI artifacts.

---

## Reporting

| Metric | Target |
|--------|--------|
| Test pass rate (CI) | ≥ 99 % |
| Flaky test rate | < 1 % |
| Unit test coverage | ≥ 80 % |
| Mean time to detect (MTTD) | < 30 min after merge |

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why it's Harmful | Solution |
|-------------|-----------------|---------|
| `Thread.sleep()` / hard waits | Slow and unreliable | Use explicit waits / polling |
| Tests that depend on other tests | Order-sensitivity causes false failures | Each test is independent |
| Testing implementation details | Breaks on refactors | Test observable behaviour |
| Skipped tests left permanently | Dead code hides real failures | Track with ticket; delete or fix |
| No assertions | "Green" tests that prove nothing | Every test must have at least one assertion |
