# Evidencia — límite de cuerpo de 16 KB en EcommerceApi

> **Identificador:** `2026-11-12-11-api-body-limit`
>
> **Tipo:** ejecución (local)
>
> **Resultado:** **Validado en local**
>
> **Runbook:** [03 — Rate limiting y mass assignment](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/runbook.md)

Un límite de cuerpo es como el marco de una puerta: el paquete que cabe pasa y el que no cabe se queda fuera, sin romper la puerta. Esta evidencia comprueba el marco de 16 KB de EcommerceApi con dos cuerpos exactos, uno de 16 384 bytes y otro de 17 408, y demuestra que el segundo se rechaza con `413`.

**In English.** A body limit is like a door frame: a package that fits goes through and one that does not is stopped without breaking the door. This evidence checks the 16 KB frame in EcommerceApi with two exact bodies, 16,384 and 17,408 bytes, and proves that the second is rejected with `413`.

## 1. Contexto

- **Fecha:** 2026-11-12.
- **Entorno:** Ubuntu 26.04.1 LTS, .NET SDK 10.0.115, ejecución local desde el árbol de trabajo.
- **Objetivo:** `lab-api-local-azure`, `POST /api/products`, con `[RequestSizeLimit(16 * 1024)]`.
- **Alcance:** un cuerpo exacto de 16 KB, un cuerpo de 17 KB y el contrato de error del rechazo.
- **Fuera de alcance:** carga concurrente, otros endpoints, contenedor y despliegue.
- **Datos:** ninguno real; el producto creado en la prueba se queda en la base SQLite local.

## 2. Hallazgo

Antes del cambio, el cuerpo de 17 KB no devolvía `413`: Kestrel lanzaba `BadHttpRequestException` al leer el cuerpo y el manejador de excepciones lo convertía en un `500` genérico. El límite existía, pero el cliente no recibía el estado que el contrato de `docs/api.md` declara.

La salida anterior está en [`artefactos/antes-17kb.txt`](artefactos/antes-17kb.txt), capturada contra el árbol de `origin/main` (`8fc5767`) con las cabeceras de seguridad completas.

## 3. Cambio

Se añadió `BadHttpRequestExceptionHandler`, registrado junto a `DomainExceptionHandler`. Conserva el `StatusCode` que asigna Kestrel cuando la excepción es de petición inválida y lo escribe como ProblemDetails. El límite de 16 KB sigue en los controladores; no se movió ni se relajó. El cambio está en el [PR #65 de lab-api](https://github.com/lanuzalorenzo/lab-api-local-azure/pull/65), commit `59a7cec`.

## 4. Ejecución

| Cuerpo | Tamaño | Resultado | Artefacto |
|---|---:|---|---|
| Producto válido con relleno | 16 384 bytes | `201 Created`; el cuerpo se procesa | [`16kb-headers.txt`](artefactos/16kb-headers.txt) · [`16kb-body.json`](artefactos/16kb-body.json) |
| Mismo producto con 1 KB más | 17 408 bytes | `413 Payload Too Large`; ProblemDetails sin detalles internos | [`17kb-headers.txt`](artefactos/17kb-headers.txt) · [`17kb-body.json`](artefactos/17kb-body.json) |

La prueba se hizo contra la API arrancada en `http://127.0.0.1:5080`, con un emisor OIDC local y un token de prueba de una hora. El token no se guarda en el repositorio; los comandos y la preparación están en [`comandos.md`](comandos.md).

## 5. Límites

- La prueba es local y contra el proceso, no contra la imagen publicada. El límite lo aplica Kestrel en ambos casos, pero la imagen no se volvió a construir en esta sesión.
- El token de prueba sustituye a Entra ID: valida el camino de autorización de la API, no la configuración de un tenant real.
- El cuerpo válido se completa con espacios hasta el byte exacto; el límite se mide sobre el cuerpo HTTP, no sobre el JSON normalizado.
- No se probó el mismo límite en `POST /api/orders`; comparte el atributo, pero no se midió uno a uno.

## 6. Enlaces

- Práctica: [`03 — Rate limiting y mass assignment`](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/README.md)
- Cambio: [PR #65 de lab-api](https://github.com/lanuzalorenzo/lab-api-local-azure/pull/65), commit `59a7cec`.
- Contrato y capacidades: [`docs/api.md` en el commit 59a7cec](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/59a7cec/docs/api.md) y [`docs/capacidades.md` en el commit 768c440](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/768c440/docs/capacidades.md).
