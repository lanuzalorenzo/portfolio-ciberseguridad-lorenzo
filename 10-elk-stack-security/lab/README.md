# Laboratorio ELK local

> **Estado:** Validado en local. Ejecutado el 2026-10-19 con 15 eventos sintéticos, consultas KQL y dashboard de Kibana.
>
> **Evidencia:** [2026-10-19-10-elk-ingesta](../../laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/README.md).
>
> Laboratorio local para practicar ingesta, normalización y detección con Elasticsearch, Logstash y Kibana sobre logs sintéticos.

## Arquitectura

```text
sample-logs/security.log
          │
          ▼
     Logstash :5044 (solo red interna)
          │  normalización y campos ECS
          ▼
 Elasticsearch :9200 (127.0.0.1)
          │
          ▼
      Kibana :5601 (127.0.0.1)
```

## Componentes

| Servicio | Imagen | Puerto local | Función |
|---|---|---|---|
| Elasticsearch | `docker.elastic.co/elasticsearch/elasticsearch:8.19.23` | `127.0.0.1:9200` | Almacenamiento y búsqueda |
| Logstash | `docker.elastic.co/logstash/logstash:8.19.23` | No expuesto | Ingesta y normalización |
| Kibana | `docker.elastic.co/kibana/kibana:8.19.23` | `127.0.0.1:5601` | Visualización y análisis |

La versión se puede cambiar con `ELK_VERSION` en `.env`. Los límites de memoria son Elasticsearch 2 GB, Kibana 1 GB y Logstash 512 MB; los heaps se ajustan con `ES_HEAP` y `LS_HEAP`.

## Datos sintéticos

`sample-logs/security.log` contiene 15 eventos de laboratorio:

- 6 fallos de autenticación SSH desde `203.0.113.45`.
- 2 fallos de login web desde la misma IP.
- 1 acceso a `/admin` con `403`.
- 1 intento de path traversal con `400`.
- 1 login SSH correcto, 1 login web correcto y 1 consulta de pedido correcta.
- 1 uso de `sudo`.
- 1 parada del servicio SSH.

Todos los nombres, IPs y usuarios son ficticios y usan rangos reservados para documentación.

## Puesta en marcha

```bash
cd 10-elk-stack-security/lab
cp .env.example .env
./scripts/preflight.sh
./scripts/up.sh
./scripts/verify.sh
```

Kibana queda disponible en <http://localhost:5601>.

## Verificación esperada

```text
Eventos totales: 15
Fallos: 10
Éxitos: 5
IP con más fallos: 203.0.113.45 (10)
```

Los valores exactos se comprueban con `./scripts/verify.sh`. Si el volumen ya contenía datos de una ejecución anterior, el total puede ser mayor; para una ejecución limpia usa `./scripts/down.sh --yes` antes de volver a subir.

## Limpieza

```bash
./scripts/down.sh --yes
```

El script elimina contenedores y el volumen `esdata`. Los logs sintéticos del repositorio permanecen como parte del código, pero no quedan datos de Elasticsearch en el host.

## Seguridad y límites

- La pila está pensada para **uso local**, no para producción.
- Se recomiendan 6 GB de memoria libre (4 GB mínimo) y 10 GB de disco.
- Elasticsearch y Kibana se publican solo en `127.0.0.1`.
- La seguridad de Elasticsearch está desactivada para simplificar el laboratorio. No hay TLS ni autenticación.
- No se usan datos reales ni secretos.
- No se debe exponer el puerto `9200` ni `5601` a Internet.
- Para una variante productiva habría que habilitar TLS, autenticación, RBAC, API keys y una política de retención.

## Ficheros

- `docker-compose.yml`: definición de la pila.
- `logstash/pipeline/security.conf`: pipeline de normalización.
- `sample-logs/security.log`: eventos sintéticos.
- `scripts/preflight.sh`: comprobaciones previas.
- `scripts/up.sh`: arranque y espera de servicios.
- `scripts/verify.sh`: verificación de ingesta y consultas.
- `scripts/down.sh`: parada y borrado del volumen.

## Runbooks

- [Ingestión y normalización](../practicas/01-ingestion-logstash/runbook.md).
- [Visualización y detección en Kibana](../practicas/02-kibana-deteccion/runbook.md).
