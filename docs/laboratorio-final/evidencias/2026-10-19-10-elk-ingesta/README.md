# Evidencia — 10 ELK Stack Security / Ingestión, normalización y dashboard

> **Identificador:** `2026-10-19-10-elk-ingesta`
>
> **Resultado:** Validado en local
>
> **Runbooks:** [01 — Ingestión y normalización](../../../../10-elk-stack-security/practicas/01-ingestion-logstash/runbook.md) · [02 — Visualización y detección](../../../../10-elk-stack-security/practicas/02-kibana-deteccion/runbook.md)

## 1. Contexto

- **Fecha de ejecución:** 2026-10-19.
- **Datos sintéticos:** fechados el 2026-10-20 entre las 09:00 y las 09:06 UTC.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** equipo local XPS con Ubuntu 26.04.1 LTS, Docker Engine 29.1.3, Docker Compose 2.40.3 y pila ELK 8.19.23.
- **Alcance:** levantar Elasticsearch, Logstash y Kibana en local, ingerir 15 eventos sintéticos, normalizarlos, crear la vista de datos `Lab Security`, validar 6 consultas KQL, construir un dashboard de 5 paneles y exportar los objetos de Kibana.
- **Datos:** sintéticos, con usuarios e IPs de los rangos reservados para documentación.
- **Autorización:** laboratorio local sin recursos cloud, sin coste y sin datos reales.

## 2. Comandos ejecutados

El detalle está en [comandos.md](comandos.md). Resumen:

```bash
./scripts/preflight.sh
./scripts/down.sh --yes
./scripts/up.sh
./scripts/verify.sh
# Kibana: vista de datos, 6 consultas KQL, 5 visualizaciones y dashboard
# Exportación de objetos y limpieza final
./scripts/down.sh --yes
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Preflight | Sin `[FAIL]` | 9 comprobaciones `[OK]` | PASS |
| Limpieza de volumen | `lab_esdata` eliminado | Volumen eliminado y verificado | PASS |
| Servicios | Elasticsearch, Kibana y Logstash activos | Los tres `healthy` | PASS |
| Elasticsearch | Clúster disponible en single-node | `status: yellow`, 0 shards sin asignar de tipo primario | PASS |
| Ingesta | 15 eventos | 15 eventos | PASS |
| Fallos | 10 | 10 | PASS |
| Éxitos | 5 | 5 | PASS |
| Errores web | 4 | 4 | PASS |
| Actividad `sudo` | 1 | 1 | PASS |
| Correlación por IP | 10 fallos desde `203.0.113.45` | 10 | PASS |
| Normalización | Campos tipo ECS | `host.name`, `service.name`, `source.ip`, `event.outcome`, `http.response.status_code` presentes | PASS |
| Exposición de puertos | Solo `127.0.0.1` | `127.0.0.1:9200` y `127.0.0.1:5601` | PASS |
| Vista de datos Kibana | `Lab Security` con `lab-security-*` y `@timestamp` | Creada y verificada | PASS |
| Consultas KQL | 6 consultas con los conteos esperados | Fallos 10; SSH 6; IP 10; web ≥400 4; `sudo` 1; `/admin` 1 | PASS |
| Dashboard | 5 paneles con los datos esperados | Métrica 10, barras 7/6/2, línea temporal 6/2/2, tabla de IPs 10 y búsqueda con 4 errores | PASS |
| Exportación de objetos | NDJSON con la vista, el dashboard, las 4 visualizaciones y la búsqueda | 7 objetos exportados | PASS |
| Limpieza final | Contenedores, red y volumen eliminados | `lab_esdata no existe`; puertos 9200 y 5601 libres | PASS |

## 4. Artefactos

- [`artefactos/preflight.txt`](artefactos/preflight.txt): comprobaciones previas con la pila parada.
- [`artefactos/down.txt`](artefactos/down.txt): limpieza previa de la pila.
- [`artefactos/limpieza.txt`](artefactos/limpieza.txt): verificación de que el volumen desaparece en la limpieza previa.
- [`artefactos/up.txt`](artefactos/up.txt): arranque y espera de servicios.
- [`artefactos/compose-ps.txt`](artefactos/compose-ps.txt): estado de los tres contenedores.
- [`artefactos/cluster-health.json`](artefactos/cluster-health.json): estado del clúster.
- [`artefactos/verify.txt`](artefactos/verify.txt): verificación de conteos.
- [`artefactos/indices.txt`](artefactos/indices.txt): índice creado y número de documentos.
- [`artefactos/mapping.json`](artefactos/mapping.json): mapping dinámico de los campos.
- [`artefactos/logstash.log`](artefactos/logstash.log): eventos normalizados por Logstash.
- [`artefactos/consultas-elasticsearch.txt`](artefactos/consultas-elasticsearch.txt): conteo de fallos, agregaciones por IP/servicio, vista de datos y conteos de las 6 consultas.
- [`artefactos/kibana-status.json`](artefactos/kibana-status.json): estado de Kibana.
- [`artefactos/puerto-elasticsearch.txt`](artefactos/puerto-elasticsearch.txt) y [`artefactos/puerto-kibana.txt`](artefactos/puerto-kibana.txt): puertos ligados solo a localhost.
- [`artefactos/data-view.png`](artefactos/data-view.png): creación de la vista `Lab Security` con `lab-security-*` y `@timestamp`.
- [`artefactos/consultas-kql.png`](artefactos/consultas-kql.png): búsqueda de errores web con `http.response.status_code >= 400` y 4 hits.
- [`artefactos/dashboard.png`](artefactos/dashboard.png): dashboard `Lab Security - ELK` con los cinco paneles.
- [`artefactos/kibana-saved-objects.ndjson`](artefactos/kibana-saved-objects.ndjson): exportación de la vista, el dashboard, las cuatro visualizaciones y la búsqueda guardada.
- [`artefactos/limpieza-final.txt`](artefactos/limpieza-final.txt): parada final, eliminación del volumen y verificación de puertos libres.

## 5. Limpieza

- **Recursos creados:** red `lab_default`, volumen `lab_esdata` y tres contenedores.
- **Recursos eliminados:** se ejecutó `./scripts/down.sh --yes` al terminar y se verificó que el volumen `lab_esdata` desaparecía.
- **Estado actual:** pila parada y sin recursos del laboratorio en ejecución.
- **Verificación:** [`artefactos/limpieza-final.txt`](artefactos/limpieza-final.txt) y [`artefactos/limpieza.txt`](artefactos/limpieza.txt).

## 6. Coste

- **Estimado:** 0.
- **Real:** 0. Todo se ejecuta en local.

## 7. Conclusiones

La evidencia demuestra que la pila ELK local arranca, que Logstash normaliza eventos sintéticos a campos tipo ECS, que Elasticsearch responde con los conteos esperados y que Kibana permite construir una vista de datos, validar consultas KQL y montar un dashboard operativo con cinco paneles.

También demuestra que los objetos de Kibana se pueden exportar en NDJSON y que el ciclo de limpieza elimina contenedores, red y volumen, dejando los puertos locales libres.

## 8. Limitaciones

- La seguridad de Elasticsearch está desactivada: no hay TLS ni autenticación.
- Es un laboratorio local con datos sintéticos y de bajo volumen.
- El clúster es single-node; `yellow` es el estado esperado.
- No se ha probado el acceso desde otra máquina ni una prueba de intrusión sobre los puertos.
- No se han creado alertas automatizadas ni reglas de detección; el trabajo se limita a ingesta, consulta y visualización.
- El dashboard se ha validado en local; no se ha probado con datos reales ni en un entorno de producción.
- El dashboard exportado no almacena el rango temporal (`timeRestore: false`). Para reproducir la vista hay que aplicar manualmente `2026-10-20 10:30–11:30` en UTC+2 o `08:30–09:30` en UTC.

## 9. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas reales; solo rangos reservados y nombres ficticios.
- [x] Sin identificadores reales ni datos personales.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
