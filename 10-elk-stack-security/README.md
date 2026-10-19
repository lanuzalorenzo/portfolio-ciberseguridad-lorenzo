# 10 | ELK Stack Security

> **Estado:** Validado en local. La pila ELK se ha ejecutado con Docker Compose, la ingesta y la normalización se han verificado, y se ha construido y exportado un dashboard de Kibana. No se ha desplegado en Azure ni se ha probado con datos reales.

Este módulo amplía el portfolio hacia la observabilidad y la analítica de seguridad. El enfoque es documentar cómo una pila ELK puede recibir eventos, normalizarlos, correlacionarlos y convertirlos en indicadores útiles para detección y respuesta.

## Laboratorio

- [Laboratorio ELK local](lab/README.md): Docker Compose, Logstash, logs sintéticos y scripts.
- [Runbook de ingestión](practicas/01-ingestion-logstash/runbook.md): levantar la pila, ingerir y verificar.
- [Runbook de Kibana](practicas/02-kibana-deteccion/runbook.md): vista de datos, consultas y dashboard.
- [Evidencia de ejecución](../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/README.md): ingesta, consultas KQL, dashboard y exportación.

## Prácticas

- [Ingestión y normalización con Logstash](practicas/01-ingestion-logstash/README.md)
- [Visualización, detección y análisis con Kibana](practicas/02-kibana-deteccion/README.md)

## Registro del trabajo

La [bitácora del módulo](bitacora/) refleja el planteamiento del caso de uso, el diseño de la arquitectura y el estado de validación.

## Alcance

El módulo se plantea como un laboratorio orientativo de seguridad operativa. No representa una implantación de producción ni una configuración real con datos sensibles. El objetivo es comprender cómo ELK puede apoyar la investigación de eventos, la detección y la visualización de riesgo.
