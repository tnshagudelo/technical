# Microservice Template

A minimal starter for a standalone microservice with messaging support.

## Quick Start

```bash
cp -r accelerators/dev/templates/microservice my-service
cd my-service
# Replace all <REPLACE_*> placeholders
npm install
npm run dev
```

## Project Structure

```
<REPLACE_SERVICE_NAME>/
├── src/
│   ├── index.js          # Entry point
│   ├── consumer.js       # Message-queue consumer (e.g. RabbitMQ / Kafka)
│   ├── producer.js       # Message-queue producer
│   ├── handlers/         # Business logic handlers
│   └── config/
│       └── index.js      # Centralised config (reads env vars)
├── tests/
├── Dockerfile
├── .env.example
└── package.json
```

## Key Files

### `src/index.js`

```js
const { startConsumer } = require('./consumer');
const config = require('./config');

(async () => {
  console.log(`Starting <REPLACE_SERVICE_NAME> on ${config.env}`);
  await startConsumer();
})();
```

### `src/config/index.js`

```js
module.exports = {
  env: process.env.NODE_ENV || 'development',
  brokerUrl: process.env.BROKER_URL || 'amqp://localhost',
  queueName: process.env.QUEUE_NAME || '<REPLACE_QUEUE_NAME>',
};
```

### `.env.example`

```
NODE_ENV=development
BROKER_URL=amqp://localhost
QUEUE_NAME=<REPLACE_QUEUE_NAME>
```

## Placeholders Reference

| Placeholder | Description |
|-------------|-------------|
| `<REPLACE_SERVICE_NAME>` | Name of the microservice (kebab-case) |
| `<REPLACE_QUEUE_NAME>` | Message-queue topic / queue name |
