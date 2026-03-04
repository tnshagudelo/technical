# Test Plan Template

> **Instructions:** Replace every `<REPLACE_*>` placeholder with real content, then remove this line.

---

## 1. Overview

| Field | Value |
|-------|-------|
| **Project** | `<REPLACE_PROJECT_NAME>` |
| **Version / Release** | `<REPLACE_VERSION>` |
| **Prepared by** | `<REPLACE_AUTHOR>` |
| **Date** | `<REPLACE_DATE>` |
| **Status** | Draft / In Review / Approved |

---

## 2. Objectives

`<REPLACE_OBJECTIVES>`
_Example: Validate that the user registration flow works end-to-end and that no PII is leaked in API responses._

---

## 3. Scope

### In scope
- `<REPLACE_IN_SCOPE_ITEM_1>`
- `<REPLACE_IN_SCOPE_ITEM_2>`

### Out of scope
- `<REPLACE_OUT_OF_SCOPE_ITEM_1>`

---

## 4. Test Strategy

| Test Level | Responsible | Tools |
|-----------|-------------|-------|
| Unit | Dev team | Jest / JUnit |
| Integration | Dev + QA | Supertest / RestAssured |
| End-to-End | QA team | Playwright / Cypress |
| Performance | QA / DevOps | k6 |
| Security | Security / QA | OWASP ZAP |

---

## 5. Entry and Exit Criteria

### Entry Criteria
- [ ] All development tasks for the release are marked **Done**.
- [ ] Build is deployed to the test environment.
- [ ] Test data is available.

### Exit Criteria
- [ ] All **P1 / P2** defects resolved.
- [ ] Test coverage ≥ `<REPLACE_COVERAGE_TARGET>`%.
- [ ] No open blockers.

---

## 6. Test Environment

| Component | Details |
|-----------|---------|
| Environment URL | `<REPLACE_ENV_URL>` |
| Database | `<REPLACE_DB_TYPE>` version `<REPLACE_DB_VERSION>` |
| Browser(s) | `<REPLACE_BROWSERS>` |
| Mobile device(s) | `<REPLACE_DEVICES>` |

---

## 7. Test Schedule

| Activity | Start Date | End Date | Owner |
|----------|-----------|---------|-------|
| Test design | `<REPLACE>` | `<REPLACE>` | `<REPLACE>` |
| Test execution | `<REPLACE>` | `<REPLACE>` | `<REPLACE>` |
| Defect fix & retest | `<REPLACE>` | `<REPLACE>` | `<REPLACE>` |
| Sign-off | `<REPLACE>` | `<REPLACE>` | `<REPLACE>` |

---

## 8. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| `<REPLACE_RISK_1>` | High / Med / Low | High / Med / Low | `<REPLACE_MITIGATION_1>` |

---

## 9. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | `<REPLACE>` | | |
| Project Manager | `<REPLACE>` | | |
