# Fase 1 — red y API en la capa gratuita

> **Estado:** Validado (2026-11-26) para la red y para la ejecución de la API; Diseño para la capa de pago, que no se despliega. El grupo de recursos se eliminó el 2026-11-28 (§Limpieza). Evidencia: [comandos ejecutados](comandos.md).

La red del laboratorio y la API corrieron en la capa gratuita: una VNet con dos subredes y la imagen de la API en Container Apps con escala a cero. `/health` respondió 200 y `/api/products` 401; la capa de pago sigue en Diseño. El grupo se eliminó el 2026-11-28, así que nada de esto está en marcha.

**In English.** The lab network and the API ran on the free tier: a VNet with two subnets and the API image on Container Apps with scale to zero. `/health` returned 200 and `/api/products` returned 401; the paid layer stays in Design. The resource group was deleted on 2026-11-28, so none of it is running.

Runbook utilizado: `docs/despliegue-y-rollback.md` del repositorio `lab-api-local-azure`.

## Qué se probó

Se desplegó la parte de la plantilla que no tiene medidor de precio y se ejecutó la API sobre ella:

- **Red:** VNet `10.20.0.0/16`, subred de aplicación `10.20.1.0/24` delegada a `Microsoft.Web/serverFarms` y con el NSG, y subred de Private Endpoint `10.20.2.0/24` con las políticas de endpoint privado desactivadas.
- **Cómputo:** la imagen `ghcr.io/lanuzalorenzo/ecommerceapi@sha256:6702…` en Container Apps, con mínimo cero réplicas, máximo una y sin espacio de Log Analytics (`--logs-destination none`).
- **API:** `/health` anónimo y `/api/products` protegido.

No se desplegó Key Vault, ni Private Endpoints, ni DNS privado, ni App Service P1v3, ni Log Analytics. El parámetro `desplegarServiciosDePago` quedó en `false`, y el `what-if` lo confirmó: solo se crean el NSG y la VNet.

## Resultado

| Prueba | Esperado | Observado | Resultado |
|---|---|---|---|
| `what-if` con `desplegarServiciosDePago=false` | Solo NSG y VNet | Dos recursos, ninguno con medidor | PASS |
| Despliegue de la red | `Succeeded` | `Succeeded`; VNet, dos subredes y NSG | PASS |
| Subred de aplicación | Delegada a `Microsoft.Web/serverFarms`, con NSG | Delegación y NSG presentes; prefijo `10.20.1.0/24` | PASS |
| Subred de Private Endpoint | Políticas de endpoint privado desactivadas | `Disabled`; prefijo `10.20.2.0/24` | PASS |
| `GET /health` | 200 y `Healthy` | HTTP/2 200, cuerpo `Healthy` | PASS |
| Cabecera `Server` | Ausente | No aparece en la respuesta | PASS |
| `GET /api/products` sin token | 401 | HTTP/2 401, `WWW-Authenticate: Bearer` | PASS |
| Cuerpo del 401 | Un cuerpo de error legible | 0 bytes, sin `content-type` | **Hallazgo** |

## Hallazgo

El 401 del *challenge* sin token devuelve el cuerpo vacío del framework. El contrato de error del repositorio (`problemdetails`) cubre `400`, `404` y `500`; el 401 no está en él, así que no hay una afirmación incumplida, pero tampoco un cuerpo legible para el cliente. La prueba negativa del gate se cumple (401). Unificar el 401 con `application/problem+json` queda como mejora abierta, no como validada.

## Vuelta atrás (T5)

La aplicación estaba en modo de revisión única. Se pasó a múltiples, se fijó el 100 % a la revisión `v1thzxk`, se creó `t5` con un cambio de entorno inocuo y se probó antes de darle tráfico:

| Paso | Observado | Resultado |
|---|---|---|
| `t5` al 0 %, por su FQDN de revisión | `health` 200, `products` 401 | PASS |
| `t5` al 100 %, por el FQDN de la aplicación | `health` 200, `products` 401 | PASS |
| Vuelta a `v1thzxk` al 100 % | `health` 200, `products` 401; tráfico `v1thzxk=100`, `t5=0` | PASS |

El modo de revisión múltiple y las dos revisiones se conservaron hasta la limpieza. El comando de vuelta atrás es un cambio de pesos, no un redespliegue.

## Límites

- La API corrió en Container Apps, no en App Service: el diseño P1v3 con integración VNet y slots sigue en **Diseño**.
- La base es SQLite en el sistema de ficheros efímero del contenedor; no hay persistencia ni copia.
- No hay Log Analytics ni Application Insights: no se recogen trazas ni logs del servicio.
- No se prueban Private Endpoint, DNS privado, Key Vault ni firewall. La conectividad privada no está validada.
- El endpoint público no tenía SLA y escalaba a cero; la primera petición podía tardar.

## Limpieza

El grupo `rg-ecomlab-f1` llevaba `expires=2026-12-03` y se eliminó el 2026-11-28, cinco días antes, con `az group delete --name rg-ecomlab-f1 --yes`. `az group exists --name rg-ecomlab-f1` devuelve `false` y no queda ningún grupo con el prefijo `rg-ecomlab-`. Los comandos y su salida están en [comandos ejecutados](comandos.md#7-limpieza-2026-11-28).

## Redacción

Los identificadores de suscripción, tenant, aplicación, propietario y el nombre DNS del entorno se sustituyen por marcadores. El rango `10.20.0.0/16` es el del diseño público en `infra/main.bicep`, no una dirección interna real. El digest de la imagen es público y se conserva para poder reproducir la prueba.
