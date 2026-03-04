# REST API Template

A minimal, production-ready REST API starter using Node.js / Express.

## Quick Start

```bash
# 1. Copy this template into your project
cp -r accelerators/dev/templates/rest-api my-api

# 2. Replace placeholders
cd my-api
# Edit package.json, src/app.js, etc. – search for <REPLACE_*>

# 3. Install and run
npm install
npm run dev
```

## Project Structure

```
<REPLACE_PROJECT_NAME>/
├── src/
│   ├── app.js            # Express app factory
│   ├── server.js         # Entry point (starts HTTP server)
│   ├── routes/
│   │   └── health.js     # Health-check route (GET /health)
│   ├── controllers/      # Route handlers
│   ├── services/         # Business logic
│   ├── middlewares/      # Express middlewares (auth, error handling)
│   └── config/
│       └── index.js      # Centralised configuration
├── tests/
│   ├── unit/
│   └── integration/
├── .env.example
├── package.json
└── README.md
```

## Files

### `src/app.js`

```js
const express = require('express');
const healthRouter = require('./routes/health');

function createApp() {
  const app = express();
  app.use(express.json());
  app.use('/health', healthRouter);
  // <REPLACE_ADDITIONAL_ROUTES>
  return app;
}

module.exports = createApp;
```

### `src/server.js`

```js
const createApp = require('./app');

const PORT = process.env.PORT || 3000;
const app = createApp();

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### `src/routes/health.js`

```js
const { Router } = require('express');
const router = Router();

router.get('/', (_req, res) => res.json({ status: 'ok' }));

module.exports = router;
```

### `.env.example`

```
PORT=3000
NODE_ENV=development
# <REPLACE_DATABASE_URL>=
# <REPLACE_SECRET_KEY>=
```

### `package.json`

```json
{
  "name": "<REPLACE_PROJECT_NAME>",
  "version": "1.0.0",
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "test": "jest --coverage"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.5.0",
    "supertest": "^6.3.3"
  }
}
```

## Placeholders Reference

| Placeholder | Description |
|-------------|-------------|
| `<REPLACE_PROJECT_NAME>` | Name of the project (kebab-case) |
| `<REPLACE_ADDITIONAL_ROUTES>` | Register extra routers here |
| `<REPLACE_DATABASE_URL>` | Database connection string env var name |
| `<REPLACE_SECRET_KEY>` | JWT / API secret key env var name |
