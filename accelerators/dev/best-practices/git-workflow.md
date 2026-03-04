# Git Workflow Best Practices

## Branch Strategy (Trunk-Based Development with Short-Lived Feature Branches)

```
main
 └── feature/<ticket-id>-short-description   (max lifetime: 2 days)
 └── fix/<ticket-id>-short-description
 └── chore/<ticket-id>-short-description
 └── hotfix/<ticket-id>-short-description    (merged directly to main + tag)
```

### Rules

| Rule | Detail |
|------|--------|
| Branch from | `main` always |
| Merge back to | `main` via Pull Request |
| Max branch age | 2 working days |
| Branch naming | `type/<ticket-id>-kebab-description` (lowercase, hyphens only) |
| Delete after merge | Yes |

### Branch Type Prefixes

| Prefix | When to Use |
|--------|-------------|
| `feature/` | New functionality |
| `fix/` | Bug fix in a non-production branch |
| `hotfix/` | Urgent fix for a production issue |
| `chore/` | Tooling, dependency updates, config changes |
| `docs/` | Documentation-only changes |

---

## Commit Message Convention (Conventional Commits)

```
<type>(<scope>): <short summary>

[optional body]

[optional footer: BREAKING CHANGE, closes #issue]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or fixing tests |
| `chore` | Maintenance tasks |
| `ci` | CI/CD configuration |
| `perf` | Performance improvement |
| `revert` | Reverts a previous commit |

### Examples

```bash
feat(auth): add JWT refresh token support

fix(users): prevent duplicate email registration
closes #42

chore(deps): bump express from 4.18.1 to 4.18.2
```

### Rules

- Use the imperative mood in the summary: "add" not "added" / "adds".
- Keep the summary under 72 characters.
- Reference tickets in the footer: `closes #123` or `refs #123`.

---

## Pull Request Guidelines

1. **Size**: Keep PRs small – aim for < 400 lines changed.
2. **Title**: Follow the same Conventional Commit format.
3. **Description**: Fill in the PR template (what, why, how to test).
4. **Checks**: All CI checks must pass before merging.
5. **Reviewers**: Assign at least one reviewer before requesting review.
6. **Squash merge**: Preferred to keep `main` history clean.
