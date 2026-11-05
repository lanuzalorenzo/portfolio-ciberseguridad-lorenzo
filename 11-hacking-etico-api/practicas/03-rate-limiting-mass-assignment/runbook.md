# Runbook — Rate limiting y consumo de recursos

> **Estado:** Validado en local. Ejecutado el 2026-11-05 contra la imagen del commit `b9176b0`.
>
> **Última revisión:** 2026-11-05.
>
> **Objetivo de la sesión:** comprobar que la API corta con `429` al superar las 120 peticiones por minuto y por IP, que vuelve a atender al reiniciarse la ventana y que la cuota no se esquiva cambiando cabeceras del cliente.

Un límite de peticiones es como el aforo de una sala: no impide que alguien entre, pero fija cuántos caben a la vez y deja fuera al que insiste. Aquí el aforo son 120 visitas por minuto y por dirección de origen; el runbook comprueba que la puerta se cierra en la petición 121 y que se vuelve a abrir sola al minuto siguiente. Se ejecuta en local, contra un contenedor, sin Azure y sin datos reales.

## 1. Objetivo

Validar el control de consumo de recursos (OWASP API4) en su forma más básica: un límite global de peticiones. Se considera éxito que:

- Las 120 primeras peticiones de una ventana devuelvan `200`.
- La petición 121 y las siguientes devuelvan `429`, sin cuerpo.
- Tras reiniciarse la ventana, la API vuelva a responder `200`.
- Cambiar `X-Forwarded-For` no abra una cuota nueva: la clave es la IP de conexión.

El límite de cuerpo de 16 KB y el límite por usuario **no** forman parte de esta sesión.

## 2. Alcance

- **Incluido:** `GET /health` (anónimo) en el contenedor local de `EcommerceApi`, middleware global de rate limiting.
- **Excluido:** endpoints autenticados, carga concurrente, calibración del umbral, límite de cuerpo, APIM (pasarela de APIs), WAF (cortafuegos de aplicación), Azure y tokens de Entra ID.
- **Entorno:** local, Docker en el equipo de trabajo; sin recursos cloud.
- **Datos:** ninguno. La prueba solo lee un endpoint de salud que no consulta la base.

La autorización y los criterios de parada están en [`docs/alcance-y-autorizacion.md`](../../docs/alcance-y-autorizacion.md).

## 3. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| Docker | 29.x con Compose 2.x | `docker --version` |
| Repositorio | `lab-api-local-azure` clonado y limpio | `git -C "$API_REPO" status --short` |
| `curl` | Cualquier versión reciente | `curl --version` |
| Puerto | `8080` libre en el host | `curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/health` |
| Permisos | Usuario local del grupo `docker`; sin roles de Azure | `docker ps` |
| Presupuesto | No aplica | — |
| Red | Solo para construir la imagen (restauración NuGet) | — |

## 4. Variables

| Variable | Valor de ejemplo | Descripción |
|---|---|---|
| `API_REPO` | `~/lab-api-local-azure` | Ruta local del clon del workload |
| `BASE` | `http://localhost:8080` | URL publicada por el contenedor |
| `OUT` | `laboratorio-final/evidencias/2026-11-05-11-api-rate-limit` | Carpeta de artefactos |
| `RATE` | `120` | Peticiones permitidas por ventana |

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

## 7. Validación

| Prueba | Método | Resultado esperado | Resultado observado (2026-11-05) |
|---|---|---|---|
| Cuota exacta | 130 peticiones en una ventana | 120 × `200` | 120 × `200` |
| Corte | Petición 121 | `429` | `429`, y las 9 siguientes |
| Recuperación | 3 peticiones tras 62 s | `200` | 3 × `200` |
| Cuerpo del `429` | Cabeceras de respuesta | Sin cuerpo, sin `Retry-After` | `Content-Length: 0`; sin `Retry-After` |
| Clave de cuota | `X-Forwarded-For` inventada | `429` | 3 × `429` |
| Carga concurrente | Varios clientes en paralelo | No ejecutado | Pendiente |
| Límite de cuerpo 16 KB | `POST` con cuerpo grande | No ejecutado | Pendiente |

## 8. Evidencia

- [x] Salida de comandos redactada.
- [x] Recuento de códigos por petición y cabeceras del `429`.
- [x] Fecha, entorno, commit e imagen.
- [x] Resultado y limitaciones.
- [x] Enlace a la entrada del índice: [`2026-11-05-11-api-rate-limit`](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md).

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
- **Tiempo estimado:** 10 minutos, incluidas dos esperas de un minuto.
- **Tiempo real:** unos 12 minutos con reconstrucción de la imagen.

## 11. Limitaciones

- La ráfaga es **secuencial** y sale de un solo cliente: mide el umbral, no el comportamiento bajo carga concurrente ni la latencia en saturación.
- 120/min no está calibrado contra el coste real de cada endpoint; es una cifra elegida para el laboratorio.
- La ventana fija permite hasta 120 al final de un minuto y 120 al principio del siguiente. Es una propiedad de `FixedWindowRateLimiter` y no se midió en esta sesión.
- El límite es por IP: los usuarios detrás de NAT comparten cuota y una IP por petición lo esquiva.
- Sin `Retry-After`, el cliente no sabe cuándo reintentar; lo deduce del minuto de reloj.
- Solo se ejercita `GET /health`. Los endpoints autenticados y de escritura no se han probado bajo este límite.
- El límite no se aplica a nivel de recurso: no distingue lecturas, escrituras ni usuarios.
- Sustituir esto por APIM o un WAF sigue fuera de alcance; el contenedor es un despliegue local, no producción.

## 12. Referencias

- [Práctica 03 — Rate limiting y mass assignment](README.md)
- [Módulo 11 — Hacking ético de APIs](../../README.md)
- [Evidencia de ejecución](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md)
- [`docs/api.md` — límites operativos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/api.md)
- OWASP API Security Top 10 (2023), API4: Unrestricted Resource Consumption
