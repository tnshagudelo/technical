#!/usr/bin/env bash
# smoke-test.sh – Basic smoke test for a REST API
#
# Usage:
#   chmod +x smoke-test.sh
#   BASE_URL=https://api.example.com ./smoke-test.sh
#
# Exit codes:
#   0 – all checks passed
#   1 – one or more checks failed

set -euo pipefail

BASE_URL="${BASE_URL:-<REPLACE_BASE_URL>}"
PASS=0
FAIL=0

# ── Colour helpers ─────────────────────────────────────────────────────────────
GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"

pass() { echo -e "${GREEN}[PASS]${RESET} $1"; ((PASS++)); }
fail() { echo -e "${RED}[FAIL]${RESET} $1"; ((FAIL++)); }

# ── HTTP helper ────────────────────────────────────────────────────────────────
# check_status <description> <expected_status> <actual_status>
check_status() {
  local desc="$1" expected="$2" actual="$3"
  if [[ "$actual" == "$expected" ]]; then
    pass "$desc – HTTP $actual"
  else
    fail "$desc – expected HTTP $expected, got $actual"
  fi
}

# ── Tests ──────────────────────────────────────────────────────────────────────
echo "=== Smoke Test: ${BASE_URL} ==="

# 1. Health check
status=$(curl -s -o /dev/null -w "%{http_code}" "${BASE_URL}/health")
check_status "GET /health" "200" "$status"

# 2. Unauthenticated access returns 401
status=$(curl -s -o /dev/null -w "%{http_code}" "${BASE_URL}/<REPLACE_PROTECTED_RESOURCE>")
check_status "GET /<REPLACE_PROTECTED_RESOURCE> without token" "401" "$status"

# 3. Login returns 200 and a token
response=$(curl -s -w "\n%{http_code}" -X POST "${BASE_URL}/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"${TEST_EMAIL:-<REPLACE_TEST_EMAIL>}\",\"password\":\"${TEST_PASSWORD:-<REPLACE_TEST_PASSWORD>}\"}")
body=$(echo "$response" | head -n 1)
status=$(echo "$response" | tail -n 1)
check_status "POST /auth/login" "200" "$status"

token=$(echo "$body" | grep -o '"accessToken":"[^"]*"' | cut -d'"' -f4 || true)
if [[ -n "$token" ]]; then
  pass "Login returns accessToken"
else
  fail "Login response missing accessToken"
fi

# 4. Authenticated access to protected resource
if [[ -n "$token" ]]; then
  status=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer $token" \
    "${BASE_URL}/<REPLACE_PROTECTED_RESOURCE>")
  check_status "GET /<REPLACE_PROTECTED_RESOURCE> with token" "200" "$status"
fi

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "Results: ${PASS} passed, ${FAIL} failed"

if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi
