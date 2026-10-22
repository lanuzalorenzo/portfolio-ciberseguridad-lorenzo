# Comandos ejecutados — ELK 10 / Ingestión

> Evidencia: `2026-10-19-10-elk-ingesta`
>
> Fecha: 2026-10-19.

Comandos en el orden del runbook. Cada paso enlaza la salida redactada correspondiente.

## 1. Preflight

```bash
cd 10-elk-stack-security/lab
./scripts/preflight.sh
```

Salida completa: [`artefactos/preflight.txt`](artefactos/preflight.txt).

Resultado: 9 comprobaciones `[OK]`, sin `[FAIL]`.

## 2. Limpieza previa

```bash
./scripts/down.sh --yes
docker volume ls --format '{{.Name}}' | grep lab_esdata
```

Salida completa: [`artefactos/down.txt`](artefactos/down.txt) y [`artefactos/limpieza.txt`](artefactos/limpieza.txt).

Resultado: contenedores y red eliminados; volumen `lab_esdata` eliminado y verificado.

## 3. Arranque

```bash
./scripts/up.sh
```

Salida completa: [`artefactos/up.txt`](artefactos/up.txt).

Resultado:

- Elasticsearch `green` al arrancar y `yellow` estable en single-node.
- Kibana y Logstash levantados.
- Kibana disponible en `http://localhost:5601`.

## 4. Estado de los servicios

```bash
docker compose ps
curl -fsS 'http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=30s&pretty'
curl -fsS 'http://localhost:5601/api/status'
```

Salidas: [`artefactos/compose-ps.txt`](artefactos/compose-ps.txt), [`artefactos/cluster-health.json`](artefactos/cluster-health.json) y [`artefactos/kibana-status.json`](artefactos/kibana-status.json).

Resultado:

- Elasticsearch, Kibana y Logstash en estado `healthy`.
- Kibana `available`.
- Clúster `yellow` por ser single-node, sin shards primarios sin asignar.

## 5. Ingesta y normalización

```bash
./scripts/verify.sh
```

Salida completa: [`artefactos/verify.txt`](artefactos/verify.txt).

Resultado observado:

```text
Eventos totales: 15
Fallos: 10
Éxitos: 5
Web 4xx/5xx: 4
Eventos sudo: 1
Servicios: ssh=7, system=2, web=6
IPs con más fallos: 203.0.113.45=10
OK: los valores coinciden con el dataset sintético.
```

## 6. Índice y mapping

```bash
curl -fsS 'http://localhost:9200/_cat/indices/lab-security-*?v&h=index,docs.count,store.size'
curl -fsS 'http://localhost:9200/lab-security-*/_mapping?pretty'
```

Salidas: [`artefactos/indices.txt`](artefactos/indices.txt) y [`artefactos/mapping.json`](artefactos/mapping.json).

Resultado:

- Índice `lab-security-2026.10.20` con 15 documentos.
- Campos `@timestamp` como `date`, `http.response.status_code` como `long` y el resto como `text` con subcampo `.keyword`.

## 7. Log de Logstash

```bash
docker compose logs --tail=80 logstash
```

Salida: [`artefactos/logstash.log`](artefactos/logstash.log).

Resultado: eventos normalizados con `host.name`, `service.name`, `source.ip`, `user.name`, `event.outcome`, `event.action`, `event.reason`, `event.severity`, `http.*`, `url.path` y `process.command_line`.

## 8. Consultas de control

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_count' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}}}'

curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_search?pretty&size=0' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}},"aggs":{"por_ip":{"terms":{"field":"source.ip.keyword","size":5}},"por_servicio":{"terms":{"field":"service.name.keyword","size":5}}}}'
```

Salida: [`artefactos/consultas-elasticsearch.txt`](artefactos/consultas-elasticsearch.txt).

Resultado:

- 10 fallos.
- 10 fallos desde `203.0.113.45`.
- 6 fallos en `ssh` y 4 en `web`.

## 9. Kibana: vista de datos, consultas y dashboard

La vista de datos se creó desde la interfaz:

- Nombre: `Lab Security`.
- Patrón: `lab-security-*`.
- Campo temporal: `@timestamp`.

Evidencia: [`artefactos/data-view.png`](artefactos/data-view.png) y [`artefactos/consultas-elasticsearch.txt`](artefactos/consultas-elasticsearch.txt).

Las 6 consultas KQL se validaron con estos conteos:

```text
1. Fallos totales: 10
2. Fallos SSH: 6
3. Fallos desde 203.0.113.45: 10
4. Errores web >= 400: 4
5. Eventos sudo: 1
6. Accesos a /admin: 1
```

Evidencia: [`artefactos/consultas-elasticsearch.txt`](artefactos/consultas-elasticsearch.txt) y [`artefactos/consultas-kql.png`](artefactos/consultas-kql.png).

El dashboard `Lab Security - ELK` se construyó con cinco paneles:

- `Lab 01 - Eventos por servicio`.
- `Lab 02 - Fallos por IP`.
- `Lab 03 - Fallos en el tiempo`.
- `Lab 04 - Errores web` (búsqueda guardada).
- `Lab 05 - Total de fallos`.

Evidencia: [`artefactos/dashboard.png`](artefactos/dashboard.png).

Exportación de los objetos de Kibana:

```bash
curl -s -X POST 'http://localhost:5601/api/saved_objects/_export' \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{"objects":[{"type":"index-pattern","id":"53df8705-4770-45d4-b9dd-bd181698a4ad"},{"type":"dashboard","id":"d2a30262-82c5-4ce4-b9cb-2746dbfef110"},{"type":"lens","id":"3a27fe79-5be4-4437-bdfd-03e939122bbb"},{"type":"lens","id":"a5ea1c38-2f79-4a8c-af9b-f6a72d58cea9"},{"type":"lens","id":"8445c92b-3cb8-4645-a570-775d21cd4142"},{"type":"lens","id":"95767c3f-4340-44cb-b1cc-f901eefd3197"},{"type":"search","id":"98f7a09e-61d2-4f28-b83e-e590d06912e0"}],"includeReferencesDeep":true}' \
  -o ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/kibana-saved-objects.ndjson
```

Resultado: 7 objetos exportados (1 vista de datos, 1 dashboard, 4 visualizaciones Lens y 1 búsqueda guardada).

## 10. Exposición de puertos

```bash
docker compose port elasticsearch 9200
docker compose port kibana 5601
```

Salidas: [`artefactos/puerto-elasticsearch.txt`](artefactos/puerto-elasticsearch.txt) y [`artefactos/puerto-kibana.txt`](artefactos/puerto-kibana.txt).

Resultado: `127.0.0.1:9200` y `127.0.0.1:5601`.

## 11. Limpieza final

Ejecutado al terminar el runbook 02:

```bash
./scripts/down.sh --yes
docker volume ls --format '{{.Name}}' | grep -x 'lab_esdata' || echo 'lab_esdata no existe'
docker compose ps
ss -ltn | grep -E ':(9200|5601)' || echo 'puertos 9200 y 5601 libres'
```

Salida: [`artefactos/limpieza-final.txt`](artefactos/limpieza-final.txt).

Resultado: contenedores y red eliminados, volumen `lab_esdata` eliminado y puertos `9200`/`5601` libres.
