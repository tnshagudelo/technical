# Multi-stage Dockerfile
# Usage: docker build --build-arg APP_PORT=3000 -t <REPLACE_IMAGE_NAME> .

# ── Stage 1: Install dependencies ─────────────────────────────────────────────
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

# ── Stage 2: Build (only needed for TypeScript / compiled projects) ────────────
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
# Remove or adjust if there is no build step
RUN npm run build --if-present

# ── Stage 3: Production image ──────────────────────────────────────────────────
FROM node:20-alpine AS production
WORKDIR /app

ARG APP_PORT=3000
ENV PORT=${APP_PORT} \
    NODE_ENV=production

# Add non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
# If there is no build step, replace the line above with:
# COPY --from=deps /app/node_modules ./node_modules
# COPY . .

USER appuser
EXPOSE ${APP_PORT}

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost:${APP_PORT}/health || exit 1

CMD ["node", "dist/server.js"]
# If there is no build step, replace with:
# CMD ["node", "src/server.js"]
