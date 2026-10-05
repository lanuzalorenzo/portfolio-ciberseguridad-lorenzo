# Informe técnico — Validación JWT y JWKS en Entra ID

**Proyecto:** Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## Objetivo
Documentar el mecanismo por el cual una API valida un token JWT de acceso emitido por Azure AD (v2.0). Se centra en la verificación criptográfica mediante JWKS y la inspección crítica de *claims* específicos de Microsoft Entra ID.

## Estructura y Validación del Token

Un JWT consta de tres partes:
- **Header**: Especifica el algoritmo (`RS256`) y el identificador de la clave (`kid`) utilizada por Azure AD para firmar el token.
- **Payload**: Contiene los *claims* de identidad y autorización.
- **Signature**: La firma asimétrica generada por Azure AD usando su clave privada.

## Proceso de Verificación Criptográfica (JWKS)

Para evitar la validación con claves estáticas, la API consulta el endpoint oficial Discovery de Azure AD:
`https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys`

1. **Obtención de claves públicas:** La API descarga el JSON Web Key Set (JWKS).
2. **Selección de la clave:** Se localiza la clave pública que coincide con el claim `kid` del header del JWT.
3. **Verificación:** Se comprueba que la firma RS256 es válida y que el token no ha sido alterado.

## Validación de Claims Específicos de Azure AD v2.0

La verificación de la firma es solo el primer paso. Para garantizar la seguridad del endpoint, la API debe validar obligatoriamente los siguientes claims:

| Claim | Propósito | Validación Requerida en Azure AD |
| :--- | :--- | :--- |
| **`iss`** (Issuer) | Identifica al emisor del token. | Debe coincidir exactamente con el tenant: `https://login.microsoftonline.com/<tenant-id>/v2.0`. |
| **`aud`** (Audience) | Identifica el destinatario esperado. | Debe ser el Client ID de la API (o su Application ID URI). Rechaza tokens de otras APIs (ej. Microsoft Graph). |
| **`exp` / `nbf`** | Control de tiempos. | El token no debe haber caducado y su tiempo de "not before" debe ser válido. |
| **`scp`** (Scopes) | Permisos delegados (cuando hay un usuario). | Verificar que contiene los scopes necesarios (ej. `access_as_user`). |
| **`roles`** (App Roles) | Permisos de aplicación (daemon/M2M). | En flujos de *Client Credentials*, se validan los roles asignados en lugar de scopes. |

## Gestión del Ciclo de Vida de Claves
Microsoft Entra ID rota sus claves de firma de forma periódica y automática por seguridad. La API implementa una estrategia de caché para las respuestas JWKS, pero fuerza una recarga contra el endpoint `/keys` si recibe un token firmado con un `kid` desconocido, garantizando cero interrupciones durante la rotación.

## Recursos de referencia
- [Microsoft Entra ID - Tokens de acceso de la plataforma de identidad](https://learn.microsoft.com/azure/active-directory/develop/access-tokens)
- [RFC 7517 - JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517)
