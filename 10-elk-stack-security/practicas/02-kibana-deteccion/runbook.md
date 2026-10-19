# Runbook — Visualización, detección y análisis con Kibana

> **Estado:** Runbook preparado. No ejecutado todavía.
>
> **Última revisión:** 2026-10-19.
>
> **Objetivo de la sesión:** crear una vista de datos, validar consultas de detección y construir un dashboard con los eventos normalizados del runbook 01.

## 1. Prerrequisitos

- Pila ELK levantada con el runbook 01.
- `./scripts/verify.sh` con 15 eventos y verificación correcta.
- Kibana accesible en <http://localhost:5601>.

Comprobación rápida:

```bash
cd 10-elk-stack-security/lab
curl -fsS 'http://localhost:9200/_cat/indices/lab-security-*?v&h=index,docs.count'
```

## 2. Crear la vista de datos

1. Abre <http://localhost:5601>.
2. Ve a **Stack Management → Data Views** (Kibana 8.19) o **Index Patterns** según la versión.
3. Crea una vista con:
   - **Name:** `Lab Security`
   - **Index pattern:** `lab-security-*`
   - **Time field:** `@timestamp`
4. Guarda.

**Resultado esperado:** la vista muestra 15 documentos.

## 3. Ajustar el rango temporal

Los eventos son de `2026-10-20` entre `09:00:00Z` y `09:06:00Z`.

En Kibana:

1. Abre el selector de tiempo.
2. Elige **Absolute**.
3. Usa un rango amplio: `2026-10-19 00:00:00.000` → `2026-10-22 00:00:00.000`.
4. Aplica.

**Resultado esperado:** Discover muestra 15 hits.

## 4. Consultas de detección

En **Discover**, con la vista `Lab Security`, ejecuta estas consultas KQL y anota el número de resultados.

| Consulta KQL | Resultado esperado | Qué demuestra |
|---|---|---|
| `event.outcome.keyword: "failure"` | 10 | Fallos totales |
| `service.name.keyword: "ssh" and event.outcome.keyword: "failure"` | 6 | Fuerza bruta SSH |
| `source.ip.keyword: "203.0.113.45" and event.outcome.keyword: "failure"` | 10 | Correlación por IP |
| `http.response.status_code >= 400` | 4 | Errores web |
| `event.action.keyword: "sudo"` | 1 | Actividad privilegiada |
| `url.path.keyword: "/admin"` | 1 | Acceso a ruta protegida |

> Los campos de texto se indexan con un subcampo `.keyword`. Usa `.keyword` para coincidencias exactas y agregaciones. `http.response.status_code` es numérico y no necesita subcampo.

### Consultas equivalentes en Elasticsearch

Si quieres guardar la salida en la evidencia, valida las mismas consultas por API:

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_count' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}}}'
```

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_search?pretty&size=0' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}},"aggs":{"por_ip":{"terms":{"field":"source.ip.keyword","size":5}},"por_servicio":{"terms":{"field":"service.name.keyword","size":5}}}}'
```

## 5. Construir el dashboard

Crea un dashboard llamado `Lab Security — ELK`.

Visualizaciones mínimas:

1. **Bar chart:** conteo por `service.name`.
2. **Table:** top de `source.ip.keyword` con `event.outcome.keyword: "failure"`.
3. **Line chart:** fallos en el tiempo (`@timestamp` con intervalo de 1 minuto).
4. **Table:** eventos con `http.response.status_code >= 400`, mostrando `url.path.keyword`, `source.ip.keyword` y `http.response.status_code`.
5. **Metric:** total de fallos (`event.outcome.keyword: "failure"`).

Guarda cada visualización y añádela al dashboard.

**Resultado esperado:** el dashboard muestra el pico de 6 fallos SSH seguidos de actividad web sospechosa desde `203.0.113.45`.

## 6. Exportar los objetos de Kibana

Exporta la vista, las visualizaciones y el dashboard:

```bash
mkdir -p ../../../docs/laboratorio-final/evidencias/2026-10-20-10-elk-ingesta/artefactos
curl -fsS -X POST 'http://localhost:5601/api/saved_objects/_export' \
  -H 'kbn-xsrf: true' \
  -H 'Content-Type: application/json' \
  -d '{"type":["dashboard","visualization","search","index-pattern"],"includeReferencesDeep":true}' \
  -o ../../../docs/laboratorio-final/evidencias/2026-10-20-10-elk-ingesta/artefactos/kibana-saved-objects.ndjson
```

**Resultado esperado:** un NDJSON con el dashboard y sus referencias.

## 7. Evidencia a capturar

| Artefacto | Cómo obtenerlo | Destino |
|---|---|---|
| Vista de datos | Captura de Stack Management | `artefactos/data-view.png` |
| Resultado de consultas | Captura de Discover | `artefactos/consultas-kql.png` |
| Dashboard | Captura del dashboard | `artefactos/dashboard.png` |
| Objetos exportados | Comando de exportación | `artefactos/kibana-saved-objects.ndjson` |
| Conteos por API | `curl` de las consultas | `artefactos/consultas-elasticsearch.txt` |

Guarda también un `README.md` en la carpeta de evidencia con:

- Fecha y entorno.
- Objetivo.
- Resultado: PASS o parcial.
- Consultas y conteos.
- Limitaciones.
- Enlaces a los artefactos.

Puedes usar la [plantilla de evidencia](../../../plantillas/evidencia-template.md).

## 8. Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Vista de datos | Stack Management | 15 documentos | Pendiente de ejecución |
| Fallos totales | KQL `event.outcome.keyword: "failure"` | 10 | Pendiente de ejecución |
| Fuerza bruta SSH | KQL `service.name.keyword: "ssh"` | 6 | Pendiente de ejecución |
| Correlación por IP | KQL `source.ip.keyword: "203.0.113.45"` | 10 | Pendiente de ejecución |
| Errores web | KQL `http.response.status_code >= 400` | 4 | Pendiente de ejecución |
| Dashboard | Exportación NDJSON | Objetos presentes | Pendiente de ejecución |

## 9. Limpieza

Cuando termines la captura de evidencia:

```bash
./scripts/down.sh --yes
```

## 10. Coste y tiempo

- **Coste:** 0.
- **Tiempo estimado:** 60–90 minutos.

## 11. Limitaciones

- No hay autenticación en Kibana: es un laboratorio local.
- El dashboard se construye manualmente; la exportación NDJSON permite reproducirlo.
- Los datos son sintéticos y de bajo volumen.
- La detección es una consulta KQL, no una regla de alerta automatizada.

## 12. Referencias

- [Laboratorio ELK](../../lab/README.md).
- [Runbook 01 — Ingestión](../01-ingestion-logstash/runbook.md).
- [Plantilla de evidencia](../../../plantillas/evidencia-template.md).
