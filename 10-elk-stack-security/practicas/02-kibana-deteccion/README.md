# 02 | Visualización, detección y análisis con Kibana

Con los eventos ya en Elasticsearch, la pregunta cambia: se puede ver un patrón sin escribir una consulta a mano cada vez. La práctica creó una vista de datos, validó seis consultas y montó un dashboard con cinco paneles; no creó alertas.

**Referencias:** MCSB LT-1 · NIST SP 800-92

| Qué se hizo | Resultado observado |
|---|---|
| Vista de datos `Lab Security` | Índice `lab-security-*`, campo de tiempo `@timestamp` |
| Seis consultas KQL | Fallos 10; SSH 6; IP 10; web ≥400 4; `sudo` 1; `/admin` 1 |
| Dashboard de cinco paneles | Métrica 10, barras 7/6/2, línea temporal 6/2/2, tabla de IPs 10 y búsqueda con 4 errores |
| Exportación de objetos | 7 objetos en NDJSON |
| Alertas | Ninguna: fuera del alcance de la práctica |

El dashboard no guarda el rango temporal: para reproducirlo hay que aplicar `2026-10-20 10:30–11:30` en UTC+2. Es una limitación del export, no del análisis.

Las seis consultas cubren fallos de autenticación, accesos correctos, errores web y uso de privilegios. La correlación por IP y ventana temporal es lo que convierte cuatro señales sueltas en una hipótesis. Se validaron por sus conteos, no por la forma del panel: si un número no cuadra, el problema está antes de la visualización.

Una visualización sin consulta detrás es decoración; el rango temporal hay que fijarlo o el panel cambia de significado; y exportar los objetos permite repetir el análisis sin rehacerlo a mano.
