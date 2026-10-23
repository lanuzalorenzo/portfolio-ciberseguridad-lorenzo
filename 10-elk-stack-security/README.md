# 10 | ELK Stack Security

Centralizar logs sirve de poco si no se puede responder con ellos a una pregunta concreta. Este módulo monta una pila ELK en local con Docker Compose, ingiere quince eventos sintéticos de autenticación y servicio web, los normaliza y comprueba que se pueden consultar y dibujar. Todo se ejecutó en un equipo local y se apagó al terminar; no hay Azure, ni datos reales, ni alertas automatizadas.

## Qué se ejecutó

- Elasticsearch, Logstash y Kibana 8.19.23 en local, con los puertos ligados solo a `127.0.0.1`.
- Quince eventos: diez fallos de autenticación, cinco accesos correctos, cuatro errores web y una actividad con `sudo`.
- Normalización a campos tipo ECS y seis consultas en Kibana sobre la vista `Lab Security`.
- Un dashboard de cinco paneles y la exportación de siete objetos en NDJSON.
- Limpieza completa: contenedores, red y volumen eliminados.

Los eventos son sintéticos, fechados el 2026-10-20 y con usuarios e IPs de los rangos reservados para documentación; se pueden publicar sin sanearlos.

## Prácticas

- [Ingestión y normalización con Logstash](practicas/01-ingestion-logstash/README.md) — *validado en local*; runbook y evidencia.
- [Visualización, detección y análisis con Kibana](practicas/02-kibana-deteccion/README.md) — *validado en local*; seis consultas y dashboard.

## Límites

El clúster es single-node, Elasticsearch va sin TLS ni autenticación y no se han creado reglas ni alertas: el módulo demuestra ingesta, consulta y visualización, no la operación de un SIEM. Tampoco se ha probado el acceso desde otra máquina ni con datos reales. La evidencia completa está en [2026-10-19-10-elk-ingesta](../laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/README.md).
