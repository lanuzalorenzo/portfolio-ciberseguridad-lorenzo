#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 - <<'PY'
import json
import sys
import time
import urllib.error
import urllib.request

ES_URL = "http://localhost:9200"
INDEX = "lab-security-*"


def request(path, method="GET", body=None):
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(ES_URL + path, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


# Espera a que Logstash haya indexado al menos un evento.
total = 0
for _ in range(60):
    try:
        total = request(f"/{INDEX}/_count")["count"]
        if total > 0:
            break
    except (urllib.error.URLError, KeyError, json.JSONDecodeError):
        pass
    time.sleep(2)

if total == 0:
    print("ERROR: no hay eventos en el índice. Revisa: docker compose logs logstash", file=sys.stderr)
    sys.exit(1)

search = request(
    f"/{INDEX}/_search",
    method="POST",
    body={
        "size": 0,
        "query": {"match_all": {}},
        "aggs": {
            "outcomes": {"terms": {"field": "event.outcome.keyword"}},
            "services": {"terms": {"field": "service.name.keyword"}},
            "failures_by_source": {
                "filter": {"term": {"event.outcome.keyword": "failure"}},
                "aggs": {"sources": {"terms": {"field": "source.ip.keyword"}}},
            },
            "web_4xx": {"filter": {"range": {"http.response.status_code": {"gte": 400}}}},
            "sudo": {"filter": {"term": {"event.action.keyword": "sudo"}}},
        },
    },
)

aggregations = search["aggregations"]
outcomes = {bucket["key"]: bucket["doc_count"] for bucket in aggregations["outcomes"]["buckets"]}
services = {bucket["key"]: bucket["doc_count"] for bucket in aggregations["services"]["buckets"]}
sources = {
    bucket["key"]: bucket["doc_count"]
    for bucket in aggregations["failures_by_source"]["sources"]["buckets"]
}
web_4xx = aggregations["web_4xx"]["doc_count"]
sudo = aggregations["sudo"]["doc_count"]

print(f"Eventos totales: {total}")
print(f"Fallos: {outcomes.get('failure', 0)}")
print(f"Éxitos: {outcomes.get('success', 0)}")
print(f"Web 4xx/5xx: {web_4xx}")
print(f"Eventos sudo: {sudo}")
print("Servicios: " + ", ".join(f"{key}={value}" for key, value in sorted(services.items())))
print("IPs con más fallos: " + ", ".join(f"{key}={value}" for key, value in sources.items()))

checks = {
    "eventos totales": (total, 15),
    "fallos": (outcomes.get("failure", 0), 10),
    "éxitos": (outcomes.get("success", 0), 5),
    "web 4xx/5xx": (web_4xx, 4),
    "sudo": (sudo, 1),
    "IP 203.0.113.45": (sources.get("203.0.113.45", 0), 10),
}

failed = False
for name, (observed, expected) in checks.items():
    if observed != expected:
        print(f"WARN: {name}: observado={observed}, esperado={expected}", file=sys.stderr)
        failed = True

if failed:
    print("Si el volumen tenía datos previos, ejecuta ./scripts/down.sh --yes y repite.", file=sys.stderr)
    sys.exit(1)

print("OK: los valores coinciden con el dataset sintético.")
PY
