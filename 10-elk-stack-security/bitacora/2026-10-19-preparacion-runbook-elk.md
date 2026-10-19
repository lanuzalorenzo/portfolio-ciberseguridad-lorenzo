# Bitácora — Preparación del runbook ELK

## Objetivo

Convertir el módulo 10 de diseño documental en un laboratorio local ejecutable, con pasos reproducibles y evidencia definida, sin declararlo validado hasta que se ejecute.

## Contexto y alcance

- Entorno local con Docker Compose, sin Azure.
- Elasticsearch, Logstash y Kibana 8.19.23.
- 15 eventos sintéticos de autenticación SSH, login web, `sudo` y actividad de servicio.
- Alcance limitado a ingesta, normalización y consulta; no se han creado alertas automatizadas.

## Trabajo realizado

- Definición de la pila ELK local con `docker-compose.yml`, límites de memoria y puertos ligados a `127.0.0.1`.
- Pipeline de Logstash para normalizar pares `clave=valor` a campos tipo ECS.
- Dataset sintético con 6 fallos SSH repetidos, actividad web sospechosa y actividad privilegiada.
- Scripts de preflight, arranque, verificación y limpieza.
- Runbooks de ingestión y de Kibana, con consultas KQL y criterios de evidencia.
- Actualización del estado del módulo a **Runbook preparado** y de la web a «Diseño · runbook listo».

## Resultados

- El módulo ya tiene una ruta ejecutable de principio a fin.
- La verificación automática espera 15 eventos, 10 fallos, 5 éxitos, 4 errores web y 10 fallos desde `203.0.113.45`.
- La evidencia queda definida en `docs/laboratorio-final/evidencias/2026-10-20-10-elk-ingesta/`.

## Pendientes y riesgos

- El laboratorio no se ha ejecutado: Docker no está instalado en el entorno actual.
- La configuración de Logstash y el dashboard de Kibana no se han probado contra la pila real.
- La seguridad de Elasticsearch está desactivada: es un laboratorio local, no una configuración de producción.
- Si la máquina tiene poca memoria, habrá que ajustar `ES_HEAP` y `LS_HEAP`.

## Aprendizaje

- Un runbook preparado permite distinguir entre “está documentado” y “está listo para ejecutarse”.
- La evidencia debe definirse antes de ejecutar; así se captura lo necesario y no se improvisa.
- Un dataset sintético con conteos conocidos facilita validar la ingesta de forma objetiva.

## Siguiente paso

Ejecutar la sesión del 2026-10-20, capturar la evidencia y actualizar el estado a **Parcial** o **Validado** según el resultado.
