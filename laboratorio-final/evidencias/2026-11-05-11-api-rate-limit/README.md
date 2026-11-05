# Evidencia — 11 Hacking ético de APIs / Rate limiting y consumo

> **Identificador:** `2026-11-05-11-api-rate-limit`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** Validado en local
>
> **Runbook:** [03 — Rate limiting y consumo de recursos](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/runbook.md)
>
> **Práctica relacionada:** [03 — Rate limiting y mass assignment](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/README.md)

> Un límite de peticiones es como el aforo de una sala: deja pasar a 120 por minuto y cierra la puerta al siguiente. Se comprobó que la API corta la petición 121 con `429` y vuelve a atender al minuto siguiente; la prueba fue una ráfaga de un solo cliente contra el contenedor local, sin datos y sin Azure.

## 1. Contexto

- **Fecha de ejecución:** 2026-11-05.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** equipo local con Linux 7.0.0-38, Docker 29.1.3 y Compose 2.40.3, .NET SDK 10.0.114 en el host; `lab-api-local-azure` en el commit `b9176b0`, árbol limpio, imagen `ecommerce-api:local` (`970468f16fce`) reconstruida en la sesión.
- **Alcance:** medir el límite global de 120 peticiones por minuto y por IP en `GET /health`, comprobar la recuperación tras reiniciar la ventana y probar que `X-Forwarded-For` no abre una cuota nueva.
- **Datos:** ninguno. `/health` no consulta la base ni devuelve información de negocio.
- **Autorización:** [alcance y autorización del módulo 11](../../../11-hacking-etico-api/docs/alcance-y-autorizacion.md). Laboratorio propio, local, sin recursos cloud y sin coste.
- **Fuera de alcance:** carga concurrente, calibración del umbral, endpoints autenticados, límite de cuerpo de 16 KB, APIM y WAF.

## 2. Comandos ejecutados

El detalle está en [comandos.md](comandos.md). Resumen:

```bash
git -C ~/lab-api-local-azure rev-parse --short HEAD
docker compose build && docker compose up -d
sleep 65
for i in $(seq 1 130); do
  curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8080/health
done
sleep 62
for i in $(seq 1 3); do curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8080/health; done
```

**Salida observada (resumen):**

```text
b9176b0
health=200
200=120 429=10 total=130   # primera 429 en la petición 121
200
200
200                        # control tras reiniciar la ventana
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Cuota de la ventana | 120 peticiones con `200` | 120 `200` | PASS |
| Corte del límite | `429` desde la petición 121 | `429` en 121–130 | PASS |
| Recuperación | `200` al minuto siguiente | 3 de 3 `200` | PASS |
| Cuerpo y cabeceras del `429` | Sin cuerpo | `Content-Length: 0`; sin `Retry-After` | PASS, con limitación declarada |
| Clave de la cuota | Cabecera de reenvío no cambia la partición | 3 de 3 `429` con IP inventada | PASS |
| Carga concurrente | Varios clientes simultáneos | No ejecutado | Pendiente |
| Límite de cuerpo 16 KB | `413` con cuerpo grande | No ejecutado | Pendiente |

Los tiempos de respuesta durante la ráfaga fueron de 0,7 a 4,9 ms por petición; el `429` no introduce latencia adicional apreciable porque no llega al endpoint.

## 4. Artefactos

- [`artefactos/rate-limit.txt`](artefactos/rate-limit.txt): las 130 peticiones con código y tiempo, el recuento y la prueba de control.
- [`artefactos/429-headers.txt`](artefactos/429-headers.txt): cabeceras completas de una respuesta `429`.
- [`artefactos/clave-por-ip.txt`](artefactos/clave-por-ip.txt): reintentos con `X-Forwarded-For` inventada.
- [`artefactos/entorno.txt`](artefactos/entorno.txt): commit, imagen, versiones, usuario del contenedor y estado del servicio.
- [`artefactos/build.txt`](artefactos/build.txt): registro de la reconstrucción de la imagen.

No se incluyen tokens, cabeceras de autorización, direcciones internas ni capturas.

## 5. Limpieza

- **Recursos creados:** un contenedor local y una imagen ya existente, reconstruida en la sesión.
- **Recursos eliminados:** contenedor parado con `docker compose down` al terminar.
- **Verificación:** `docker compose ps` no muestra el servicio tras la limpieza. El volumen `api-data` se conserva porque la prueba no escribe en la base.

## 6. Coste

- **Estimado:** 0 €.
- **Real:** 0 €.
- **Notas:** ejecución local; la reconstrucción de la imagen usa la caché de NuGet del equipo.

## 7. Conclusiones

El límite es exacto: 120 respuestas `200` y `429` desde la petición 121, con el recuento del artefacto (`200=120 429=10`). La cuota se reinicia al minuto, no bloquea de forma permanente, y la clave es la IP de conexión: tres `X-Forwarded-For` distintas siguen recibiendo `429`, lo que confirma que el despliegue no aplica `UseForwardedHeaders`.

La respuesta `429` sale vacía y **no** lleva `Retry-After`, así que el cliente no recibe indicación de cuándo reintentar. Es una brecha de interoperabilidad, no de protección: el límite protege igual.

Lo que la evidencia **no** demuestra: que 120/min sea un umbral adecuado, que el límite aguante carga concurrente, ni que proteja endpoints autenticados o de escritura. Sigue siendo un control de laboratorio por IP.

## 8. Limitaciones y lo no ejecutado

- Ráfaga secuencial de un solo cliente: no hay concurrencia ni medición de latencia bajo saturación.
- Sin calibración: 120/min es una intención de laboratorio, no un valor derivado del coste de cada endpoint.
- La ventana fija permite ráfagas en el borde (hasta 120 al final de un minuto y 120 al principio del siguiente); no se midió.
- Detrás de NAT los clientes comparten cuota; con IP rotativa el límite se esquiva.
- No se probó el `413` del límite de 16 KB ni ningún endpoint autenticado.
- El resultado depende del commit `b9176b0` y de la imagen construida en la sesión; cambios posteriores exigen repetir el runbook.

## 9. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas (solo `localhost`).
- [x] Sin identificadores reales ni datos personales.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
- [x] Lo no ejecutado está marcado como tal.
