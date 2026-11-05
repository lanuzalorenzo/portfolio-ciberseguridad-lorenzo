# Runbook — Rate limiting y consumo de recursos

> **Estado:** Validado en local. Ejecutado el 2026-11-05 contra la imagen del commit `b9176b0`.
>
> **Última revisión:** 2026-11-05.
>
> **Objetivo de la sesión:** comprobar que la API corta con `429` al superar las 120 peticiones por minuto y por IP, que vuelve a atender al reiniciarse la ventana, que la cuota no se esquiva cambiando cabeceras del cliente y que el umbral se sostiene con clientes concurrentes sin cola ni error.

Un límite de peticiones es como el aforo de una sala: no impide que alguien entre, pero fija cuántos caben a la vez y deja fuera al que insiste. Aquí el aforo son 120 visitas por minuto y por dirección de origen; el runbook comprueba que la puerta se cierra en la petición 121 y que se vuelve a abrir sola al minuto siguiente. Se ejecuta en local, contra un contenedor, sin Azure y sin datos reales.

## 1. Objetivo

Validar el control de consumo de recursos (OWASP API4) en su forma más básica: un límite global de peticiones. Se considera éxito que:

- Las 120 primeras peticiones de una ventana devuelvan `200`.
- La petición 121 y las siguientes devuelvan `429`, sin cuerpo.
- Tras reiniciarse la ventana, la API vuelva a responder `200`.
- Cambiar `X-Forwarded-For` no abra una cuota nueva: la clave es la IP de conexión.
- Con clientes concurrentes, el número de aceptadas no cambie y el rechazo no añada espera.

El límite de cuerpo de 16 KB y el límite por usuario **no** forman parte de esta sesión.

## 2. Alcance

- **Incluido:** `GET /health` (anónimo) en el contenedor local de `EcommerceApi`, middleware global de rate limiting, con carga secuencial y concurrente.
- **Excluido:** endpoints autenticados, calibración del umbral contra un SLO, límite de cuerpo, APIM (pasarela de APIs), WAF (cortafuegos de aplicación), Azure y tokens de Entra ID.
- **Entorno:** local, Docker en el equipo de trabajo; sin recursos cloud.
- **Datos:** ninguno. La prueba solo lee un endpoint de salud que no consulta la base.

La autorización y los criterios de parada están en [`docs/alcance-y-autorizacion.md`](../../docs/alcance-y-autorizacion.md).

## 3. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| Docker | 29.x con Compose 2.x | `docker --version` |
| Repositorio | `lab-api-local-azure` clonado y limpio | `git -C "$API_REPO" status --short` |
| `curl` | Cualquier versión reciente | `curl --version` |
| k6 | v2.3.0 o compatible, en contenedor `grafana/k6` | `docker run --rm grafana/k6 version` |
| Puerto | `8080` libre en el host | `curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/health` |
| Permisos | Usuario local del grupo `docker`; sin roles de Azure | `docker ps` |
| Presupuesto | No aplica | — |
| Red | Solo para construir la imagen (restauración NuGet) | — |

## 4. Variables

| Variable | Valor de ejemplo | Descripción |
|---|---|---|
| `API_REPO` | `~/lab-api-local-azure` | Ruta local del clon del workload |
| `BASE` | `http://localhost:8080` | URL publicada por el contenedor |
| `OUT` | `laboratorio-final/evidencias/2026-11-05-11-api-rate-limit` | Carpeta de artefactos de la sesión secuencial |
| `OUT_LOAD` | `laboratorio-final/evidencias/2026-11-05-11-api-rate-limit-carga` | Carpeta de artefactos de la sesión de carga |
| `RATE_K6` | `10` | Peticiones por segundo que lanza k6; el umbral de 120 está en el código |
| `DURATION` | `50s` | Duración de cada escenario de carga |

En los pasos de carga, `-e RATE=<n>` es la tasa de llegada de k6, no la cuota de la API.

No se usan identidades, tokens ni valores de producción.

## 5. Arquitectura del escenario

```text
curl (host) ──> 0.0.0.0:8080 ──> [ UseRateLimiter ] ──> MapHealthChecks("/health")
                                      │                          └── 200
                                      └── cuota agotada ──────────── 429
```

El middleware de rate limiting se registra en `EcommerceApi/Program.cs` antes de autenticación y autorización, así que cuenta también las peticiones anónimas. La partición es `context.Connection.RemoteIpAddress`; no se configura `UseForwardedHeaders`, por lo que las cabeceras del cliente no cambian la clave.

## 6. Ejecución

### Paso 1 — Construir y levantar el contenedor

```bash
cd "$API_REPO"
docker compose build
docker compose up -d
```

**Resultado esperado:** imagen `ecommerce-api:local` construida y contenedor `Up` con `8080` publicado.

**Si falla:** revisar el acceso a NuGet durante la construcción; si el puerto está ocupado, parar el proceso que lo usa. No se sobrescribe nada de la imagen: el compose no define `environment` ni `build.args`.

### Paso 2 — Comprobar salud y esperar una ventana limpia

```bash
curl -s -o /dev/null -w 'health=%{http_code}\n' "$BASE/health"
sleep 65
```

**Resultado esperado:** `health=200`. La espera deja la ventana de un minuto sin consumo previo.

**Si falla:** `docker compose logs api` y comprobar que la base se inicializa en `/app/data`.

### Paso 3 — Ráfaga de 130 peticiones secuenciales

```bash
for i in $(seq 1 130); do
  curl -s -o /dev/null -w "%{http_code}\n" "$BASE/health"
done | sort | uniq -c
```

**Resultado esperado:** `120` respuestas `200` y `10` respuestas `429`.

Para saber en qué petición cae la primera `429`:

```bash
for i in $(seq 1 130); do
  code=$(curl -s -o /dev/null -w '%{http_code}' "$BASE/health")
  printf '%3d  %s\n' "$i" "$code"
done
```

**Resultado esperado:** `429` desde la petición 121.

**Si falla:** si aparece un `429` antes de la 121, la ventana no estaba limpia; repetir el paso 2. Si no aparece ninguno, comprobar que el `Program.cs` del commit probado mantiene `PermitLimit = 120` y que el middleware sigue registrado.

### Paso 4 — Control: reinicio de la ventana

```bash
sleep 62
for i in $(seq 1 3); do
  curl -s -o /dev/null -w '%{http_code}\n' "$BASE/health"
done
```

**Resultado esperado:** tres `200`. Demuestra que el límite es temporal y no un bloqueo permanente.

**Si falla:** si sigue devolviendo `429`, la ventana no se reinicia como se espera; revisar `Window` y el reloj del contenedor.

### Paso 5 — Cabeceras de la respuesta `429`

```bash
for i in $(seq 1 130); do
  code=$(curl -s -o /dev/null -w '%{http_code}' "$BASE/health")
  [ "$code" = "429" ] && break
done
curl -s -D - -o /dev/null "$BASE/health"
```

**Resultado esperado:** `HTTP/1.1 429 Too Many Requests`, `Content-Length: 0` y las cabeceras de seguridad habituales. **No** incluye `Retry-After`.

**Si falla:** anotar qué cabeceras aparecen; si se añade `Retry-After`, actualizar la tabla de validación y la práctica.

### Paso 6 — Prueba negativa: clave de la cuota

Con la cuota agotada, repetir con direcciones inventadas:

```bash
for xff in 192.0.2.10 203.0.113.50 198.51.100.7; do
  curl -s -o /dev/null -w "X-Forwarded-For: $xff -> %{http_code}\n" \
    -H "X-Forwarded-For: $xff" "$BASE/health"
done
```

**Resultado esperado:** los tres intentos devuelven `429`. La cuota se aplica a la IP de conexión, no a la cabecera.

**Si falla:** si alguno devuelve `200`, el despliegue tiene un proxy que reescribe la IP o `UseForwardedHeaders` activo; en ese caso la práctica cambia y el límite deja de ser fiable por IP.

### Paso 7 — Línea base con carga baja

Sirve de referencia para saber si la latencia bajo presión se degrada o no.

```bash
cd "$OUT_LOAD/artefactos"
sleep 65
docker run --rm -i --network host -u "$(id -u):$(id -g)" -v "$PWD:/scripts" \
  -e BASE="$BASE" -e RATE=1 -e DURATION=20s -e VUS=2 -e MAXVUS=5 \
  grafana/k6 run /scripts/rate-limit-carga.js \
  --summary-export=/scripts/base-summary.json
```

**Resultado esperado:** 21 respuestas `200`, ninguna `429`, p95 en torno a 1 ms.

**Si falla:** revisar que el contenedor esté arriba y que `BASE` apunte al puerto publicado. `--network host` es necesario en Linux para llegar a `localhost`.

### Paso 8 — Saturación alineada a una ventana

La ventana fija de un minuto empieza con la primera petición del proceso. Para que la carga quepa en una sola ventana se reinicia el contenedor, se hace **una** petición de salud y se lanza k6 durante 50 s.

```bash
cd "$API_REPO"
docker compose down && docker compose up -d && sleep 4
curl -s -o /dev/null -w '%{http_code}\n' "$BASE/health"

cd "$OUT_LOAD/artefactos"
docker run --rm -i --network host -u "$(id -u):$(id -g)" -v "$PWD:/scripts" \
  -e BASE="$BASE" -e RATE=10 -e DURATION=50s -e VUS=20 -e MAXVUS=60 \
  grafana/k6 run /scripts/rate-limit-carga.js \
  --summary-export=/scripts/carga-summary.json
```

**Resultado esperado:** 501 peticiones, 119 `200` (120 menos la petición de salud) y 382 `429`, sin otros estados. p95 de `200` en torno a 1,6 ms y de `429` en torno a 1,1 ms.

**Si falla:** si las aceptadas no son 119, la carga cruzó el borde de la ventana o había cuota consumida; repetir desde `docker compose down`. Si aparece un `5xx`, el problema no es el límite y hay que revisar los logs.

### Paso 9 — Presión mayor

Repetir el paso 8 con `RATE=50`, `VUS=50` y `MAXVUS=100`, guardando en `carga-50-summary.json`.

**Resultado esperado:** 2 500 peticiones, las mismas 119 aceptadas y 2 381 `429`. El umbral no cambia con la presión; solo cambia el número de rechazos.

**Si falla:** si las aceptadas suben con la presión, el limitador no está aplicando la partición o el `PermitLimit` cambió.

## 7. Validación

| Prueba | Método | Resultado esperado | Resultado observado (2026-11-05) |
|---|---|---|---|
| Cuota exacta | 130 peticiones en una ventana | 120 × `200` | 120 × `200` |
| Corte | Petición 121 | `429` | `429`, y las 9 siguientes |
| Recuperación | 3 peticiones tras 62 s | `200` | 3 × `200` |
| Cuerpo del `429` | Cabeceras de respuesta | Sin cuerpo, sin `Retry-After` | `Content-Length: 0`; sin `Retry-After` |
| Clave de cuota | `X-Forwarded-For` inventada | `429` | 3 × `429` |
| Línea base | 1 petición/s durante 20 s | Todo `200` | 21 × `200` |
| Saturación 10/s | 50 s con k6 | 119 × `200` y resto `429` | 119 `200`, 382 `429` |
| Saturación 50/s | 50 s con k6 | 119 × `200` y resto `429` | 119 `200`, 2 381 `429` |
| Estados inesperados | Recuento de no `200`/`429` | 0 | 0 de 3 523 |
| Latencia con carga | p95 de `200` | Sin degradación apreciable | 1,58 ms a 10/s; 1,90 ms a 50/s |
| Coste del rechazo | p95 de `429` | Inmediato, sin cola | 1,09 ms a 10/s; 1,07 ms a 50/s |
| Límite de cuerpo 16 KB | `POST` con cuerpo grande | No ejecutado | Pendiente |

## 8. Evidencia

- [x] Salida de comandos redactada.
- [x] Recuento de códigos por petición y cabeceras del `429`.
- [x] Fecha, entorno, commit e imagen.
- [x] Resultado y limitaciones.
- [x] Enlace a la entrada del índice: [`2026-11-05-11-api-rate-limit`](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md) y [`2026-11-05-11-api-rate-limit-carga`](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit-carga/README.md).

## 9. Limpieza

```bash
cd "$API_REPO"
docker compose down
```

**Verificación:** `docker compose ps` no muestra el servicio y `docker ps` no lista `lab-api-local-azure-api-1`.

El volumen `api-data` se conserva para no destruir la base de pruebas. Si la sesión debe dejar el equipo como estaba, añadir `-v` a `docker compose down` para borrarlo.

## 10. Coste y tiempo

- **Coste estimado:** 0 €.
- **Coste real:** 0 €.
- **Tiempo estimado:** 25 minutos, incluidas las esperas de un minuto y las tres ejecuciones de k6.
- **Tiempo real:** unos 30 minutos entre las dos sesiones, con reconstrucción de la imagen.

## 11. Limitaciones

- La ráfaga secuencial mide el umbral; la concurrencia se midió a 10 y 50 peticiones por segundo durante 50 s, no durante horas ni en el borde entre ventanas.
- 120/min no está calibrado contra un SLO de latencia ni el coste real de cada endpoint; es una cifra elegida para el laboratorio.
- La ventana fija permite hasta 120 al final de un minuto y 120 al principio del siguiente. Es una propiedad de `FixedWindowRateLimiter` y no se midió en esta sesión.
- Un solo cliente y una IP de origen: no se probaron varios clientes ni IPs distribuidas.
- El límite es por IP: los usuarios detrás de NAT comparten cuota y una IP por petición lo esquiva.
- Sin `Retry-After`, el cliente no sabe cuándo reintentar; lo deduce del minuto de reloj.
- Solo se ejercita `GET /health`. Los endpoints autenticados y de escritura no se han probado bajo este límite.
- El límite no se aplica a nivel de recurso: no distingue lecturas, escrituras ni usuarios.
- Sustituir esto por APIM o un WAF sigue fuera de alcance; el contenedor es un despliegue local, no producción.

## 12. Referencias

- [Práctica 03 — Rate limiting y mass assignment](README.md)
- [Módulo 11 — Hacking ético de APIs](../../README.md)
- [Evidencia de ejecución, sesión secuencial](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md)
- [Evidencia de ejecución, sesión de carga](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit-carga/README.md)
- [`docs/api.md` — límites operativos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/api.md)
- [k6 — documentación de escenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- OWASP API Security Top 10 (2023), API4: Unrestricted Resource Consumption
