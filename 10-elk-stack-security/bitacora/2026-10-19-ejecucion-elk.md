# Bitácora — Ejecución del laboratorio ELK

## Objetivo

Ejecutar de principio a fin el laboratorio ELK local: levantar la pila, ingerir y normalizar los eventos sintéticos, validar consultas KQL y construir un dashboard en Kibana con evidencia reproducible.

## Contexto y alcance

- Entorno local con Ubuntu 26.04.1 LTS, Docker Engine 29.1.3 y Docker Compose 2.40.3.
- Elasticsearch, Logstash y Kibana 8.19.23, con los puertos `9200` y `5601` ligados a `127.0.0.1`.
- 15 eventos sintéticos fechados el 2026-10-20 entre las 09:00 y las 09:06 UTC.
- Alcance limitado a ingesta, normalización, consulta y visualización. Sin alertas automatizadas, sin Azure y sin datos reales.

> **Nota de fechas:** la sesión estaba prevista para el `2026-10-20`; el dataset sintético se preparó con esa fecha y la ejecución se adelantó al `2026-10-19`.

## Trabajo realizado

- Instalación de Docker nativo de Ubuntu (`docker.io` y `docker-compose-v2`) y preparación del usuario para ejecutar Docker.
- Ejecución de `preflight.sh`, `down.sh --yes`, `up.sh` y `verify.sh`.
- Verificación de 15 eventos, 10 fallos, 5 éxitos, 4 errores web y 10 fallos desde `203.0.113.45`.
- Creación de la vista de datos `Lab Security` con el patrón `lab-security-*` y el campo temporal `@timestamp`.
- Validación de 6 consultas KQL: fallos totales, fallos SSH, fallos por IP, errores web ≥400, actividad `sudo` y accesos a `/admin`.
- Creación de cinco paneles: métrica de fallos, barras por servicio, línea temporal, tabla de IPs y búsqueda guardada de errores web.
- Exportación de los objetos de Kibana en NDJSON y captura de las evidencias.
- Limpieza final con `down.sh --yes` y verificación de que el volumen `lab_esdata` desaparecía y los puertos quedaban libres.

## Resultados

- Todos los conteos esperados coinciden: 10 fallos, 6 SSH, 10 desde la IP, 4 errores web, 1 `sudo` y 1 acceso a `/admin`.
- El dashboard `Lab Security - ELK` muestra la métrica `10`, las barras `ssh=7 / web=6 / system=2`, la línea temporal con 6 fallos a las 11:00 y 2+2 a las 11:03–11:04 (UTC+2), la tabla de IPs y los 4 errores web.
- La exportación contiene 7 objetos: 1 vista de datos, 1 dashboard, 4 visualizaciones Lens y 1 búsqueda guardada.
- La limpieza no deja contenedores, red ni volumen del laboratorio.

## Pendientes o riesgos

- La seguridad de Elasticsearch está desactivada: no hay TLS ni autenticación. Es un laboratorio local, no una configuración de producción.
- El dashboard exportado no almacena el rango temporal (`timeRestore: false`). Para reproducir la vista hay que aplicar manualmente el rango `2026-10-20 10:30–11:30` en UTC+2 o `08:30–09:30` en UTC.
- El eje temporal de `Lab 03` debe fijarse en `1 minute` para que los conteos sean estables; con `Auto` el intervalo puede cambiar según el tamaño del panel.
- No se han creado reglas de detección ni alertas automatizadas.
- No se ha probado el acceso desde otra máquina ni una prueba de intrusión sobre los puertos.

## Aprendizaje

- El rango temporal es el primer punto de control cuando Kibana muestra “No results found”: los eventos sintéticos estaban fechados un día después de la fecha de ejecución.
- Las dimensiones de una tabla Lens no son columnas: si se añaden varios campos a `Rows`, Lens cruza los valores y genera filas vacías. Para mostrar eventos individuales es más directo usar Discover o un solo campo en `Rows` y el resto como métricas.
- La exportación NDJSON permite reconstruir la vista de datos, las visualizaciones y el dashboard sin depender de capturas de pantalla.

## Siguiente paso

Registrar la evidencia en el índice, actualizar los estados públicos y continuar con el tabletop forense del módulo 12 antes de pasar a Azure.
