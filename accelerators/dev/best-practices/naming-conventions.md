# Naming Conventions

Consistent naming reduces cognitive load and speeds up code navigation.

---

## General Rules

- Be descriptive: names should reveal intent.
- Avoid abbreviations unless they are universally understood (`id`, `url`, `http`).
- Avoid generic names: `data`, `info`, `temp`, `foo`, `bar`.

---

## Files and Directories

| Context | Convention | Example |
|---------|-----------|---------|
| JavaScript / TypeScript source | `kebab-case` | `user-service.ts` |
| React components | `PascalCase` | `UserCard.tsx` |
| Test files | Same as source + `.test` / `.spec` | `user-service.test.ts` |
| Configuration files | `kebab-case` | `jest.config.js` |
| Directories | `kebab-case` | `src/user-management/` |

---

## Variables and Functions

| Type | Convention | Example |
|------|-----------|---------|
| Local variable | `camelCase` | `const userList = []` |
| Constant (module-level) | `SCREAMING_SNAKE_CASE` | `const MAX_RETRIES = 3` |
| Function / method | `camelCase`, verb-first | `getUserById()`, `sendEmail()` |
| Boolean variable | Prefix with `is`, `has`, `can` | `isActive`, `hasPermission` |
| Event handler | Prefix with `on` or `handle` | `onSubmit`, `handleClick` |

---

## Classes and Interfaces

| Type | Convention | Example |
|------|-----------|---------|
| Class | `PascalCase` | `UserRepository` |
| Interface (TypeScript) | `PascalCase`, no `I` prefix | `UserService` |
| Type alias | `PascalCase` | `PaginationOptions` |
| Enum | `PascalCase` (members: `SCREAMING_SNAKE_CASE`) | `enum Status { ACTIVE, INACTIVE }` |

---

## REST API Resources

| Element | Convention | Example |
|---------|-----------|---------|
| Resource path | `kebab-case`, plural nouns | `/api/v1/user-accounts` |
| Query param | `camelCase` or `snake_case` (pick one, be consistent) | `?pageSize=10` |
| JSON response field | `camelCase` | `{ "createdAt": "..." }` |

---

## Database

| Element | Convention | Example |
|---------|-----------|---------|
| Table name | `snake_case`, plural | `user_accounts` |
| Column name | `snake_case` | `created_at` |
| Index name | `idx_<table>_<column(s)>` | `idx_users_email` |
| Foreign key | `fk_<table>_<referenced_table>` | `fk_orders_users` |

---

## Environment Variables

| Convention | Example |
|-----------|---------|
| `SCREAMING_SNAKE_CASE` | `DATABASE_URL`, `JWT_SECRET` |
| Prefix by service for shared environments | `AUTH_SERVICE_PORT` |
