# Comandos ejecutados — 2026-11-05

Todos los comandos se ejecutaron en el equipo local, en la sesión del 2026-11-05, desde el clon de `lab-api-local-azure` en `~/lab-api-local-azure` y con la imagen reconstruida en esa misma sesión.

## 1. Estado del repositorio y construcción

```bash
git rev-parse --short HEAD
git status --short
docker compose build
docker compose up -d
```

**Salida observada:**

```text
b9176b0
(sin modificaciones)
#21 naming to docker.io/library/ecommerce-api:local done
 Container lab-api-local-azure-api-1  Started
```

## 2. Salud del contenedor

```bash
curl -s -o /dev/null -w 'health=%{http_code}\n' http://localhost:8080/health
```

**Salida observada:**

```text
health=200
```

## 3. Ráfaga de 130 peticiones

```bash
sleep 65
for i in $(seq 1 130); do
  read -r code t < <(curl -s -o /dev/null -w '%{http_code} %{time_total}' http://localhost:8080/health)
  printf '%3d  %s  %ss\n' "$i" "$code" "$t"
done
```

**Salida observada (recorte de las inmediaciones del corte):**

```text
118  200  0.001134s
119  200  0.000841s
120  200  0.001176s
121  429  0.002017s
122  429  0.001082s
...
130  429  0.001184s
```

Recuento: `200=120 429=10 total=130`; primera `429` en la petición 121. La salida completa está en [`artefactos/rate-limit.txt`](artefactos/rate-limit.txt).

## 4. Control tras reiniciar la ventana

```bash
sleep 62
for i in $(seq 1 3); do
  curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8080/health
done
```

**Salida observada:**

```text
200
200
200
```

## 5. Cabeceras de la respuesta 429

```bash
for i in $(seq 1 130); do
  code=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/health)
  [ "$code" = "429" ] && break
done
curl -s -D - -o /dev/null http://localhost:8080/health
```

**Salida observada:** ver [`artefactos/429-headers.txt`](artefactos/429-headers.txt). Resumen:

```text
HTTP/1.1 429 Too Many Requests
Content-Length: 0
Server: Kestrel
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

No aparece `Retry-After`.

## 6. Prueba negativa con cabecera de reenvío

```bash
for xff in 192.0.2.10 203.0.113.50 198.51.100.7; do
  curl -s -o /dev/null -w "X-Forwarded-For: $xff -> %{http_code}\n" \
    -H "X-Forwarded-For: $xff" http://localhost:8080/health
done
```

**Salida observada:**

```text
X-Forwarded-For: 192.0.2.10 -> 429
X-Forwarded-For: 203.0.113.50 -> 429
X-Forwarded-For: 198.51.100.7 -> 429
```

Las direcciones son inventadas y pertenecen a rangos reservados para documentación (RFC 5737); no identifican equipos reales.

## 7. Entorno

```bash
uname -srm
docker --version
docker compose version --short
dotnet --version
docker compose images
docker compose exec -T api id
```

La salida está en [`artefactos/entorno.txt`](artefactos/entorno.txt).

## 8. Limpieza

```bash
docker compose down
```

El volumen `api-data` se conserva de forma deliberada; la prueba no escribe en la base.
