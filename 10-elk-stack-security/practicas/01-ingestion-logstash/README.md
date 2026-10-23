# 01 | Ingestión y normalización con Logstash

Quince líneas de log no son una detección, pero sí permiten comprobar si una tubería conserva lo que importa: quién entró, desde dónde, qué servicio respondió y con qué resultado. La práctica ejecutó esa tubería en local y verificó los conteos antes de pasar a Kibana.

**Referencias:** MCSB LT-1 · NIST SP 800-92

| Qué se hizo | Resultado observado |
|---|---|
| Levantar Elasticsearch, Logstash y Kibana con Docker Compose | Tres contenedores `healthy`; puertos solo en `127.0.0.1` |
| Ingerir 15 eventos sintéticos | 15 documentos: 10 fallos, 5 accesos correctos, 4 errores web y 1 `sudo` |
| Normalizar campos | `host.name`, `service.name`, `source.ip`, `event.outcome` y `http.response.status_code` presentes |
| Correlacionar por IP | 10 fallos desde `203.0.113.45` |
| Limpiar | Contenedores, red y volumen eliminados; puertos libres |

La normalización fue lo que hizo útil el resto: sin campos comunes, la consulta por IP o por resultado no se puede escribir. El volumen era pequeño a propósito; el objetivo era verificar la tubería, no medir rendimiento. El dataset usa usuarios e IPs de los rangos reservados para documentación, así que se puede publicar sin sanearlo.

El [runbook](runbook.md) recoge los pasos y la [evidencia](../../../laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/README.md) los artefactos. El log de ejemplo y los scripts viven en `lab/`.

El esquema importa más que el número de eventos; un campo mal tipado arrastra el análisis; y comprobar los conteos justo después de ingerir evita descubrir el fallo en el dashboard.
