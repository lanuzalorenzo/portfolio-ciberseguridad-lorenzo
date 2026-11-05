import http from 'k6/http';
import { check } from 'k6';
import { Counter, Trend } from 'k6/metrics';

// Carga concurrente contra GET /health para medir el rate limit global.
// No usa datos ni autenticación: solo cuenta estados y latencia.

const BASE = __ENV.BASE || 'http://localhost:8080';

const okCount = new Counter('ok_count');
const limitedCount = new Counter('limited_count');
const otherCount = new Counter('other_count');
const okLatency = new Trend('ok_latency', true);
const limitedLatency = new Trend('limited_latency', true);

export const options = {
  scenarios: {
    carga: {
      executor: 'constant-arrival-rate',
      rate: Number(__ENV.RATE || 10),
      timeUnit: '1s',
      duration: __ENV.DURATION || '50s',
      preAllocatedVUs: Number(__ENV.VUS || 20),
      maxVUs: Number(__ENV.MAXVUS || 60),
    },
  },
  summaryTrendStats: ['avg', 'min', 'med', 'p(90)', 'p(95)', 'p(99)', 'max'],
  discardResponseBodies: true,
};

export default function () {
  const res = http.get(`${BASE}/health`, { tags: { name: 'health' } });

  if (res.status === 200) {
    okCount.add(1);
    okLatency.add(res.timings.duration);
  } else if (res.status === 429) {
    limitedCount.add(1);
    limitedLatency.add(res.timings.duration);
  } else {
    otherCount.add(1);
  }

  check(res, { 'estado 200 o 429': (r) => r.status === 200 || r.status === 429 });
}
