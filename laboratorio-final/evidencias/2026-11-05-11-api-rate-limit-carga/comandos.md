# Comandos ejecutados — 2026-11-05 (carga)

Sesión de carga concurrente contra `GET /health` del contenedor local, después de la sesión secuencial del mismo día. Todos los comandos se ejecutaron desde el clon de `lab-api-local-azure`; las rutas locales se sustituyen por `~` en este documento.

```bash
OUT_LOAD=laboratorio-final/evidencias/2026-11-05-11-api-rate-limit-carga
```

## 1. Preparación

```bash
docker pull grafana/k6
docker run --rm grafana/k6 version
```

**Salida observada:**

```text
k6 v2.3.0 (commit/e088784614, go1.27.1, linux/amd64)
```

El escenario está en [`artefactos/rate-limit-carga.js`](artefactos/rate-limit-carga.js): llegada constante, métricas separadas para `200` y `429`, sin cuerpos de respuesta.

## 2. Ventana limpia y alineada

La ventana fija de un minuto empieza con la primera petición del proceso. Para que la carga quepa en una sola ventana:

```bash
docker compose down
docker compose up -d
sleep 4
curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/health   # 1 petición: abre la ventana
```

**Salida observada:** `200`. Se hace una sola petición de salud para que el recuento esperado sea 119 y no 120.

## 3. Línea base — 1 petición/s durante 20 s

```bash
cd "$OUT_LOAD/artefactos"
sleep 65
docker run --rm -i --network host -u "$(id -u):$(id -g)" -v "$PWD:/scripts" \
  -e BASE=http://localhost:8080 -e RATE=1 -e DURATION=20s -e VUS=2 -e MAXVUS=5 \
  grafana/k6 run /scripts/rate-limit-carga.js \
  --summary-export=/scripts/base-summary.json
```

**Salida observada:**

```text
ok_count: 21
http_req_failed: 0.00%  0 out of 21
ok_latency: p(95)=1.28ms  p(99)=1.48ms  max=1.53ms
```

## 4. Saturación — 10 peticiones/s durante 50 s

```bash
docker compose down && docker compose up -d && sleep 4
curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/health
cd "$OUT_LOAD/artefactos"
docker run --rm -i --network host -u "$(id -u):$(id -g)" -v "$PWD:/scripts" \
  -e BASE=http://localhost:8080 -e RATE=10 -e DURATION=50s -e VUS=20 -e MAXVUS=60 \
  grafana/k6 run /scripts/rate-limit-carga.js \
  --summary-export=/scripts/carga-summary.json
```

**Salida observada:**

```text
http_reqs: 501       10.02/s
ok_count: 119
limited_count: 382
ok_latency: p(95)=1.58ms  p(99)=4.56ms  max=14.80ms
limited_latency: p(95)=1.09ms  max=1.58ms
estado 200 o 429: 100.00%  501 out of 501
```

## 5. Saturación — 50 peticiones/s durante 50 s

Mismo procedimiento con `RATE=50 -e VUS=50 -e MAXVUS=100` y salida a `carga-50-summary.json`.

**Salida observada:**

```text
http_reqs: 2500      50.00/s
ok_count: 119
limited_count: 2381
ok_latency: p(95)=1.90ms  p(99)=11.82ms  max=13.99ms
limited_latency: p(95)=1.07ms  max=9.50ms
estado 200 o 429: 100.00%  2500 out of 2500
```

## 6. Incidencia del montaje

La primera ejecución a 10/s usó el contenedor de k6 con su usuario por defecto y `--summary-export` falló:

```text
failed to handle the end-of-test summary: could not open
'/scripts/carga-summary.json': permission denied
```

Los datos de consola se conservan en [`artefactos/carga-console.txt`](artefactos/carga-console.txt) y coinciden con la repetición (119/382). Las ejecuciones posteriores añaden `-u "$(id -u):$(id -g)"` y escriben el JSON del resumen.

## 7. Entorno

```bash
uname -srm
docker --version
docker run --rm grafana/k6 version
git -C ~/lab-api-local-azure rev-parse --short HEAD
docker compose images
```

La salida está en [`artefactos/entorno.txt`](artefactos/entorno.txt).

## 8. Limpieza

```bash
cd ~/lab-api-local-azure
docker compose down
```

El volumen `api-data` se conserva; la prueba no escribe en la base.
