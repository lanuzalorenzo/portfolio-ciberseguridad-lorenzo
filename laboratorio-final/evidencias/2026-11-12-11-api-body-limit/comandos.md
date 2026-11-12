# Comandos — límite de cuerpo de 16 KB

Ejecutado el 2026-11-12 en local. El valor del token no se conserva; se sustituye por `$TOKEN` en los comandos reproducibles.

## 1. Cuerpos exactos

```bash
python3 - <<'PY'
from pathlib import Path
prefix = b'{"name":"body-limit","price":1,"stock":1}'
for size in (16 * 1024, 17 * 1024):
    Path(f'/tmp/body-{size}.json').write_bytes(prefix + b' ' * (size - len(prefix)))
PY
wc -c /tmp/body-16384.json /tmp/body-17408.json
```

Salida:

```text
16384 /tmp/body-16384.json
17408 /tmp/body-17408.json
```

## 2. Peticiones

```bash
for size in 16384 17408; do
  curl -sS -D "/tmp/headers-$size.txt" -o "/tmp/body-response-$size.txt" \
    -w '%{http_code}\n' \
    -X POST http://127.0.0.1:5080/api/products \
    -H "Authorization: Bearer $TOKEN" \
    -H 'Content-Type: application/json' \
    --data-binary "@/tmp/body-$size.json"
done
```

Salida observada después del cambio:

```text
201
413
```

## 3. Antes del cambio

La misma petición de 17 408 bytes, contra el árbol de `origin/main` (`8fc5767`), devolvía `500`:

```text
HTTP/1.1 500 Internal Server Error
Connection: close
Content-Type: application/problem+json; charset=utf-8
Date: Thu, 12 Nov 2026 16:41:14 GMT
Cache-Control: no-cache,no-store
Expires: -1
Pragma: no-cache
Transfer-Encoding: chunked
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'

{"type":"https://tools.ietf.org/html/rfc9110#section-15.6.1","title":"An error occurred while processing your request.","status":500,"traceId":"00-f8dde4e62cd4ee06d401c4e400a015d6-e059949f04228c3d-00"}
```

El log asociaba el `500` a `BadHttpRequestException: Request body too large. The max request body size is 16384 bytes.` La salida completa está en [`artefactos/antes-17kb.txt`](artefactos/antes-17kb.txt).

## 4. Preparación del token local

Se levantó un emisor OIDC de prueba en `https://127.0.0.1:9999`, con una clave RSA efímera y discovery/JWKS locales. La API se arrancó con `AzureAd__Authority` apuntando a ese emisor y `SSL_CERT_FILE` con el certificado autofirmado. El token se generó para `aud=api://e06`, `sub=body-limit` y una hora de vigencia. Nada de eso se versiona: es utillaje de la prueba, no una credencial del repositorio.

## 5. Limpieza

```bash
kill "$(cat /tmp/e06/app.pid)" 2>/dev/null || true
kill "$(cat /tmp/e06/oidc.pid)" 2>/dev/null || true
```
