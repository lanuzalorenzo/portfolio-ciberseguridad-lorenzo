# Evidencia — 11 Hacking ético de APIs / Rate limiting bajo carga

> **Identificador:** `2026-11-05-11-api-rate-limit-carga`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** Validado en local (concurrencia)
>
> **Runbook:** [03 — Rate limiting y consumo de recursos](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/runbook.md)
>
> **Práctica relacionada:** [03 — Rate limiting y mass assignment](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/README.md)

> Un aforo no se prueba contando a la primera persona que llega, sino empujando la puerta con una cola detrás. Aquí se lanzaron 10 y 50 peticiones por segundo contra un límite de 120 por minuto: el número de aceptadas no cambió, y las rechazadas no añadieron espera. La prueba fue local, con clientes concurrentes, sin datos y sin Azure.

## 1. Contexto

- **Fecha de ejecución:** 2026-11-05, tras la sesión secuencial del mismo día.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** Linux 7.0.0-38, Docker 29.1.3, k6 v2.3.0 en contenedor `grafana/k6`; `lab-api-local-azure` en `main` `2b92c85`, árbol limpio; imagen `ecommerce-api:local` (`970468f16fce`) construida desde el árbol del commit `b9176b0`, sin cambios en `EcommerceApi/Program.cs` entre ambos commits (comprobado con `git diff`).
- **Alcance:** medir el límite global de 120 peticiones por minuto y por IP con clientes concurrentes, a dos niveles de presión (10 y 50 peticiones por segundo), y comparar la latencia con una línea base de 1 petición por segundo.
- **Datos:** ninguno. Se usa `GET /health`, anónimo.
- **Autorización:** [alcance y autorización del módulo 11](../../../11-hacking-etico-api/docs/alcance-y-autorizacion.md). Laboratorio propio, local, sin coste.
- **Fuera de alcance:** endpoints autenticados, `413` del cuerpo de 16 KB, calibración contra un SLO de producto y despliegue con APIM o WAF.

## 2. Comandos ejecutados

El detalle está en [comandos.md](comandos.md). Resumen:

```bash
docker compose down && docker compose up -d          # ventana nueva
curl -s -o /dev/null -w '%{http_code}' localhost:8080/health   # abre la ventana: 1 petición
docker run --rm -i --network host -u "$(id -u):$(id -g)" -v "$PWD:/scripts" \
  -e BASE=http://localhost:8080 -e RATE=10 -e DURATION=50s -e VUS=20 \
  grafana/k6 run /scripts/rate-limit-carga.js
```

La ventana fija de un minuto obliga a alinear el arranque: se reinicia el contenedor, se hace **una** petición de salud (que abre la ventana y consume 1) y se lanza k6 durante 50 s, de modo que la carga cabe en esa misma ventana.

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Línea base, 1 petición/s durante 20 s | Todas `200` | 21 de 21 `200` | PASS |
| Saturación, 10 peticiones/s durante 50 s | 119 `200` y resto `429` | 119 `200`, 382 `429`, 501 totales | PASS |
| Saturación, 50 peticiones/s durante 50 s | 119 `200` y resto `429` | 119 `200`, 2 381 `429`, 2 500 totales | PASS |
| Estados inesperados | Ninguno | 0 en 3 523 peticiones (sin `5xx`) | PASS |
| Repetición del umbral | Mismo recuento | 119 en las tres ráfagas de saturación | PASS |
| Latencia con carga | Sin degradación apreciable | p95 de `200`: 1,58 ms a 10/s y 1,90 ms a 50/s | PASS |
| Coste del rechazo | Sin cola: el `429` no espera | p95 de `429`: 1,09 ms a 10/s y 1,07 ms a 50/s | PASS |
| Valor del umbral | 120/min es la cifra adecuada | No medible sin SLO de producto | Pendiente |

Que las 119 sean 120 menos la sonda de salud es coherente con que `curl` y k6 compartan la misma partición; la prueba directa de la clave por IP está en la [sesión secuencial](../2026-11-05-11-api-rate-limit/README.md), con `X-Forwarded-For`.

## 4. Artefactos

- [`artefactos/rate-limit-carga.js`](artefactos/rate-limit-carga.js): escenario de k6 (llegada constante, métricas separadas para `200` y `429`).
- [`artefactos/base-summary.json`](artefactos/base-summary.json) y [`artefactos/base-console.txt`](artefactos/base-console.txt): línea base.
- [`artefactos/carga-summary.json`](artefactos/carga-summary.json) y [`artefactos/carga-console-2.txt`](artefactos/carga-console-2.txt): saturación a 10/s.
- [`artefactos/carga-50-summary.json`](artefactos/carga-50-summary.json) y [`artefactos/carga-50-console.txt`](artefactos/carga-50-console.txt): saturación a 50/s.
- [`artefactos/carga-console.txt`](artefactos/carga-console.txt): primera ejecución a 10/s (sin export JSON, por permisos del montaje).
- [`artefactos/entorno.txt`](artefactos/entorno.txt): commit, imagen, versiones y usuario del contenedor.

## 5. Limpieza

- **Recursos creados:** contenedor local e imagen ya existentes.
- **Recursos eliminados:** contenedor parado con `docker compose down` al terminar.
- **Verificación:** `docker compose ps` no muestra el servicio. El volumen `api-data` se conserva.

## 6. Coste

- **Estimado:** 0 €.
- **Real:** 0 €. k6 corrió en un contenedor local; no hay servicios de pago.

## 7. Conclusiones

El umbral se sostiene bajo presión: con 10 y con 50 peticiones por segundo se aceptaron exactamente 119, y el resto recibió `429`. El número no depende de la presión, solo de la ventana y de la capacidad. La latencia de las aceptadas no se degradó de forma apreciable (p95 de 1,58 a 1,90 ms) y el rechazo es inmediato (p95 ~1 ms), coherente con `QueueLimit = 0`: no hay cola que convierta el exceso en espera.

No aparece ningún `5xx` ni error de conexión en 3 523 peticiones: 21 de línea base y tres ráfagas de saturación de 501, 501 y 2 500. La ventana fija se comportó como tal: la ráfaga cabe en una ventana y el recuento es reproducible con reinicio del proceso.

Lo que esto **no** demuestra: que 120/min sea el valor correcto. Eso exige un SLO de latencia y un coste por endpoint; sin ellos, 120 es una decisión de laboratorio documentada, no una cifra calibrada contra negocio.

## 8. Limitaciones y lo no ejecutado

- Dos niveles de presión (10/s y 50/s) durante 50 s; no hay prueba de horas ni de picos en el borde entre ventanas.
- Un solo cliente (una IP de origen). No se probaron varios clientes ni IPs distribuidas.
- La ventana fija permite hasta 240 peticiones en el borde entre dos minutos; no se midió ese caso porque el arranque se alineó a propósito.
- `GET /health` no representa el coste de un endpoint de escritura o con base de datos.
- No se probó el `413` del límite de 16 KB.
- El resultado depende del código en `b9176b0` y de la imagen construida ese día.

## 9. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas (solo `localhost`).
- [x] Sin identificadores reales ni datos personales.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
- [x] Lo no ejecutado está marcado como tal.
