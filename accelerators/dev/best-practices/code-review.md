# Code Review Best Practices

## Goals

- Catch bugs and logic errors before they reach production.
- Share knowledge across the team.
- Maintain consistent code quality and style.
- Validate that acceptance criteria are met.

---

## For the Author

- [ ] Self-review your diff before requesting a review.
- [ ] Keep the PR small and focused (ideally < 400 changed lines).
- [ ] Write a clear description: **what** changed, **why**, and **how to test**.
- [ ] Link the related ticket/issue.
- [ ] Ensure all CI checks pass (lint, tests, build).
- [ ] Respond to every comment, even if only with 👍 or a brief explanation.
- [ ] Mark resolved comments as resolved after addressing them.

---

## For the Reviewer

### Process

1. Understand the context (read the ticket and PR description first).
2. Review in passes: architecture → logic → style.
3. Distinguish between **must-fix** and **nice-to-have** comments using prefixes:
   - `[must]` – blocks merge; correctness or security issue.
   - `[nit]` – minor style or readability improvement (non-blocking).
   - `[question]` – asking for clarification, not requesting a change.
   - `[suggestion]` – optional improvement idea.

### Checklist

#### Functionality
- [ ] Does the code do what the ticket describes?
- [ ] Are edge cases handled (null, empty, large input)?
- [ ] Are errors handled and surfaced properly?

#### Design
- [ ] Is the solution as simple as it could be?
- [ ] Does it follow existing patterns in the codebase?
- [ ] Are abstractions at the right level?

#### Security
- [ ] Is user input validated and sanitised?
- [ ] Are secrets/credentials handled via environment variables, not hardcoded?
- [ ] Are dependencies updated and free of known vulnerabilities?

#### Performance
- [ ] Are there obvious N+1 queries or unnecessary loops?
- [ ] Are expensive operations cached where appropriate?

#### Tests
- [ ] Are there unit tests for new logic?
- [ ] Do tests cover happy path **and** failure cases?
- [ ] Are tests readable and maintainable?

#### Documentation
- [ ] Are public APIs / exported functions documented?
- [ ] Is the README updated if the setup or usage changed?

---

## SLAs

| PR Size | First Review SLA |
|---------|-----------------|
| < 100 lines | 4 working hours |
| 100–400 lines | 1 working day |
| > 400 lines | Break it up or agree separately |
