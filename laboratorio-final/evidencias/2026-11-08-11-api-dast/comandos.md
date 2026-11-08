# Comandos — DAST sin autenticar sobre EcommerceApi

## 1. API en Docker

```bash
cd "$HOME/lab-api-local-azure"
docker compose up -d
sleep 3
curl -i http://localhost:8080/health
```

```text
HTTP/1.1 200 OK
Content-Type: text/plain
Server: Kestrel
Cache-Control: no-store, no-cache
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()

Healthy
```

## 2. Baseline con ZAP

La etiqueta `stable` resolvió al digest `sha256:9624669db72f54d86c4b46a7064518bd9bf79d8c61a4c31befa9923489f328af` (ZAP 2.17.0).

```bash
mkdir -p ~/zap-dast && cd ~/zap-dast
docker run --rm --network host -v "$PWD:/zap/wrk:rw" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t http://localhost:8080/health \
  -r zap-report.html -J zap-report.json -w zap-report.md
```

```text
Total of 5 URLs
FAIL-NEW: 0	FAIL-INPROG: 0	WARN-NEW: 0	WARN-INPROG: 0	INFO: 0	IGNORE: 0	PASS: 62
Automation plan warnings:
	Job spider error accessing URL http://localhost:8080/ status code returned : 404 expected 200
```

Salida: `0`. La salida completa de consola está en [`artefactos/zap-baseline.log`](artefactos/zap-baseline.log); los informes no repiten los 62 PASS.

## 3. Intento descartado: arranque en Development

Se intentó exponer la especificación OpenAPI con un contenedor en `Development`:

```bash
docker run -d --name api-dast-tmp -p 127.0.0.1:8081:8080 \
  -e ASPNETCORE_ENVIRONMENT=Development \
  -v api-dast-data:/app/data ecommerce-api:local
```

El contenedor sale con código `139` antes de escuchar:

```text
Cannot consume scoped service 'EcommerceApi.Application.Abstractions.IProcessedMessageStore'
from singleton 'EcommerceApi.Application.OrderProcessing.IProcessOrderHandler'.
```

En Producción arranca porque la validación de ámbitos está apagada. Es una dependencia
cautiva real; se deja para el caso de remediación.

## 4. Limpieza

```bash
docker rm -f api-dast-tmp
docker volume rm api-dast-data
cd "$HOME/lab-api-local-azure" && docker compose down
```
