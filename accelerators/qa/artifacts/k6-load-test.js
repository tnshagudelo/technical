/**
 * k6 Load Test Template
 *
 * Usage:
 *   k6 run k6-load-test.js
 *   k6 run --env BASE_URL=https://api.example.com k6-load-test.js
 *
 * Install k6: https://k6.io/docs/get-started/installation/
 */

import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// ── Custom metrics ─────────────────────────────────────────────────────────────
const errorRate = new Rate('error_rate');
const responseTime = new Trend('response_time', true);

// ── Test configuration ─────────────────────────────────────────────────────────
export const options = {
  stages: [
    { duration: '1m', target: 10 },   // Ramp up to 10 virtual users
    { duration: '3m', target: 10 },   // Hold at 10 VUs
    { duration: '1m', target: 50 },   // Ramp up to 50 VUs (stress)
    { duration: '3m', target: 50 },   // Hold at 50 VUs
    { duration: '1m', target: 0 },    // Ramp down
  ],
  thresholds: {
    // <REPLACE_THRESHOLDS> – adjust to your SLOs
    http_req_duration: ['p(95)<500'],  // 95th percentile < 500 ms
    http_req_failed: ['rate<0.01'],    // Error rate < 1 %
    error_rate: ['rate<0.01'],
  },
};

const BASE_URL = __ENV.BASE_URL || '<REPLACE_BASE_URL>';

// ── Helpers ────────────────────────────────────────────────────────────────────
function getAuthToken() {
  const res = http.post(
    `${BASE_URL}/auth/login`,
    JSON.stringify({
      email: __ENV.TEST_EMAIL || '<REPLACE_TEST_EMAIL>',
      password: __ENV.TEST_PASSWORD || '<REPLACE_TEST_PASSWORD>',
    }),
    { headers: { 'Content-Type': 'application/json' } },
  );
  check(res, { 'login 200': (r) => r.status === 200 });
  return res.json('accessToken');
}

// ── Setup (runs once before the test) ─────────────────────────────────────────
export function setup() {
  const token = getAuthToken();
  return { token };
}

// ── Default function (runs for each VU on each iteration) ─────────────────────
export default function ({ token }) {
  const headers = {
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json',
  };

  // Scenario 1: Health check
  const healthRes = http.get(`${BASE_URL}/health`, { headers });
  check(healthRes, { 'health 200': (r) => r.status === 200 });
  errorRate.add(healthRes.status !== 200);
  responseTime.add(healthRes.timings.duration);

  sleep(1);

  // Scenario 2: <REPLACE_SCENARIO_NAME>
  const res = http.get(`${BASE_URL}/<REPLACE_RESOURCE>`, { headers });
  check(res, {
    '<REPLACE_SCENARIO_NAME> 200': (r) => r.status === 200,
    'response is array': (r) => Array.isArray(r.json()),
  });
  errorRate.add(res.status !== 200);
  responseTime.add(res.timings.duration);

  sleep(1);
}
