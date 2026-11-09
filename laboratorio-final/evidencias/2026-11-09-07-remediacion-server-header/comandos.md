# Comandos — remediación de la cabecera `Server`

Ejecutados el 2026-11-09 desde el clon local. La salida se reproduce redactada; no hay credenciales ni datos personales en ella.

## 1. Rojo, antes del cambio

```bash
docker compose up --build -d
curl -s -i http://localhost:8080/health | sed -n '1,12p'
scripts/check-server-header.sh http://localhost:8080/health; echo "salida=$?"
```

```text
HTTP/1.1 200 OK
Content-Type: text/plain
Server: Kestrel
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()

La respuesta publica la cabecera Server:
Server: Kestrel
salida=1
```

También en `401` y `404`:

```bash
for u in /api/products /nope; do curl -s -o /dev/null -w '%{http_code}\n' "http://localhost:8080$u"; done
```

```text
401
404
```

## 2. Rojo de la prueba de integración

Con la línea de `Program.cs` comentada:

```bash
dotnet test tests/EcommerceApi.Tests -c Release --filter ServerHeaderTests
```

```text
Con error! - Con error: 1, Superado: 0, Omitido: 0, Total: 1
```

## 3. Verde, después del cambio

```bash
docker compose build
docker run -d --name probe -p 8081:8080 ecommerce-api:local
scripts/check-server-header.sh http://localhost:8081/health; echo "salida=$?"
```

```text
Sin cabecera Server en http://localhost:8081/health
salida=0
```

Cabeceras de la misma respuesta: `200 OK`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer` y `Permissions-Policy`; sin `Server`.

## 4. Verificación del repositorio

```bash
dotnet build EcommerceApi.sln -c Release
dotnet test EcommerceApi.sln -c Release --no-build
dotnet format EcommerceApi.sln --verify-no-changes
gitleaks detect --source . --redact --exit-code 2
```

```text
Errores: 0
45 + 7 + 10 + 26 pruebas, 0 fallos
formato sin cambios
no leaks found
```

## 5. CI

```bash
gh pr checks 52 --watch
gh run view 42685834576 --log | grep -i "cabecera Server"
```

```text
Hardening y escaneo de contenedor  Verificar que la API no publica la cabecera Server  Sin cabecera Server en http://localhost:8080/health
```
