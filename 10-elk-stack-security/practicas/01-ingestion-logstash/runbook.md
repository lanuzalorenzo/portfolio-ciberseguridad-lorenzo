# Runbook — Ingestión y normalización con Logstash

> **Estado:** Validado en local. Ejecutado el 2026-10-19 con 15 eventos sintéticos.
>
> **Última revisión:** 2026-10-19.
>
> **Objetivo de la sesión:** levantar la pila ELK local, ingerir 15 eventos sintéticos y verificar que Logstash normaliza los campos de seguridad.

> Este documento explica cómo arrancar tres programas en local, darles registros de ejemplo y comprobar que salen ordenados. Al terminar se apaga todo. Nada de esto toca Azure ni datos reales.

## 1. Alcance

- Entorno local con Docker Compose.
- Elasticsearch 8.19.23, Logstash 8.19.23 y Kibana 8.19.23.
- Datos sintéticos de autenticación SSH, login web, `sudo` y actividad de servicio.
- Sin Azure, sin datos reales y sin secretos.

## 2. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| Docker Engine | Versión 24 o superior | `docker --version` |
| Docker Compose | Plugin v2 | `docker compose version` |
| Memoria | 6 GB libres recomendados (4 GB mínimo) | `free -h` |
| Disco | 10 GB libres recomendados | `df -h` |
| Puertos | 9200 y 5601 libres | `ss -ltn` |
| Permisos | Usuario en el grupo `docker` | `docker info` |

### Anexo: instalar Docker en Ubuntu

Si `docker` no está instalado:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker "$USER"
```

Cierra la sesión y vuelve a entrar para aplicar el grupo `docker`, o ejecuta `newgrp docker`.

Verifica:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

### Ajuste del kernel para Elasticsearch

```bash
sudo sysctl -w vm.max_map_count=262144
```

Para hacerlo persistente:

```bash
echo 'vm.max_map_count=262144' | sudo tee /etc/sysctl.d/99-elasticsearch.conf
sudo sysctl --system
```

## 3. Variables

| Variable | Valor por defecto | Uso |
|---|---|---|
| `ELK_VERSION` | `8.19.23` | Versión de las imágenes |
| `ES_HEAP` | `512m` | Heap de Elasticsearch |
| `LS_HEAP` | `256m` | Heap de Logstash |

Copia el archivo de ejemplo:

```bash
cd 10-elk-stack-security/lab
cp .env.example .env
```

## 4. Ejecución

### Paso 1 — Preflight

```bash
./scripts/preflight.sh
```

**Resultado esperado:** todos los `[OK]`, o avisos `[WARN]` asumibles. No debe haber `[FAIL]`.

### Paso 2 — Arranque

```bash
./scripts/up.sh
```

**Resultado esperado:**

- Elasticsearch responde con `status: yellow` o `green`.
- Kibana responde en `http://localhost:5601`.
- `docker compose ps` muestra los tres servicios en ejecución.

Si falla, revisa:

```bash
docker compose logs --tail=100 elasticsearch
docker compose logs --tail=100 kibana
docker compose logs --tail=100 logstash
```

### Paso 3 — Ingesta y normalización

Logstash lee `sample-logs/security.log` y escribe en el índice `lab-security-*`.

```bash
./scripts/verify.sh
```

**Resultado esperado:**

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

### Paso 4 — Comprobación manual en Elasticsearch

```bash
curl -fsS 'http://localhost:9200/_cat/indices/lab-security-*?v&h=index,docs.count,store.size'
```

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_search?pretty&size=3' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}},"sort":[{"@timestamp":"asc"}]}'
```

**Resultado esperado:** se ven documentos con campos `host.name`, `service.name`, `source.ip`, `event.outcome`, `event.action` y `http.response.status_code`.

### Paso 5 — Confirmar que la pila no está expuesta

```bash
docker compose port elasticsearch 9200
docker compose port kibana 5601
ss -ltn | grep -E ':(9200|5601)'
```

**Resultado esperado:** los puertos aparecen asociados a `127.0.0.1`, no a `0.0.0.0`.

## 5. Evidencia a capturar

Crea la carpeta de evidencia:

```bash
mkdir -p ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos
```

Captura y guarda:

```bash
./scripts/preflight.sh | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/preflight.txt
./scripts/up.sh 2>&1 | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/up.txt
docker compose ps | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/compose-ps.txt
curl -fsS 'http://localhost:9200/_cluster/health?pretty' | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/cluster-health.json
./scripts/verify.sh 2>&1 | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/verify.txt
curl -fsS 'http://localhost:9200/_cat/indices/lab-security-*?v&h=index,docs.count,store.size' | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/indices.txt
docker compose logs --tail=80 logstash | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/logstash.log
docker compose port elasticsearch 9200 | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/puerto-elasticsearch.txt
docker compose port kibana 5601 | tee ../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/puerto-kibana.txt
```

No incluyas rutas personales, tokens ni datos reales. Los logs del laboratorio son sintéticos, pero revisa igualmente antes de publicar.

## 6. Validación

| Prueba | Método | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|---|
| Ingesta | `./scripts/verify.sh` | 15 eventos | 15 eventos | Validado en local |
| Normalización | Consulta a Elasticsearch | Campos ECS visibles | `host.name`, `service.name`, `source.ip`, `event.outcome` y `http.*` presentes | Validado en local |
| Detección de fallos | Agregación `event.outcome` | 10 fallos | 10 fallos | Validado en local |
| Correlación por IP | Agregación `source.ip` | 10 fallos desde `203.0.113.45` | 10 fallos desde `203.0.113.45` | Validado en local |
| Exposición local | `docker compose port` | Solo `127.0.0.1` | `127.0.0.1:9200` y `127.0.0.1:5601` | Validado en local |

## 7. Limpieza

Después de capturar la evidencia de Kibana (runbook 02):

```bash
./scripts/down.sh --yes
```

**Verificación:**

```bash
docker volume ls | grep esdata || echo 'Volumen eliminado'
```

## 8. Coste y tiempo

- **Coste:** 0. Todo local.
- **Tiempo estimado:** 60–90 minutos, incluyendo la instalación de Docker si falta.

## 9. Limitaciones

- La seguridad de Elasticsearch está desactivada para el laboratorio.
- No hay TLS ni autenticación.
- Los datos son sintéticos y no representan tráfico real.
- La pila está pensada para local, no para producción.

## 10. Referencias

- [Laboratorio ELK](../../lab/README.md).
- [Runbook 02 — Kibana](../02-kibana-deteccion/runbook.md).
- [Plantilla de evidencia](../../../plantillas/evidencia-template.md).
