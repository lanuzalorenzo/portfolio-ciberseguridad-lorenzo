#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Levantando Elasticsearch, Kibana y Logstash..."
docker compose up -d

echo "Esperando a Elasticsearch..."
for _ in $(seq 1 60); do
  if curl -fsS "http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=5s" >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

if ! curl -fsS "http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=5s" >/dev/null 2>&1; then
  echo "ERROR: Elasticsearch no respondió a tiempo. Revisa: docker compose logs elasticsearch" >&2
  exit 1
fi

curl -fsS "http://localhost:9200/_cluster/health?pretty"

echo "Esperando a Kibana..."
for _ in $(seq 1 90); do
  if curl -fsS "http://localhost:5601/api/status" >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

if ! curl -fsS "http://localhost:5601/api/status" >/dev/null 2>&1; then
  echo "ERROR: Kibana no respondió a tiempo. Revisa: docker compose logs kibana" >&2
  exit 1
fi

echo
echo "Servicios activos:"
docker compose ps
echo
echo "Kibana: http://localhost:5601"
echo "Elasticsearch: http://localhost:9200"
echo "Siguiente: ./scripts/verify.sh"
