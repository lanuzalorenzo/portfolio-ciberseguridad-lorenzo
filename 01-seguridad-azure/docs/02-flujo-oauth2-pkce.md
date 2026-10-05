# Informe técnico — Flujo OAuth2 PKCE en Azure AD

**Proyecto:** Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## Objetivo
Documentar la implementación técnica del flujo OAuth2 Authorization Code con PKCE frente a Microsoft Entra ID (Azure AD), detallando las configuraciones necesarias en el portal, las particularidades del proveedor y la resolución de problemas frecuentes.

## Funcionamiento del flujo con PKCE

1. **Generación del reto criptográfico:** El cliente genera un `code_verifier` (cadena aleatoria) y un `code_challenge` (hash SHA256 del verifier).
2. **Authorization Request:** El cliente redirige al usuario a la URL de autorización de Azure AD (`https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize`). La petición incluye `client_id`, `redirect_uri`, `scope`, `state`, `code_challenge` y `code_challenge_method=S256`.
3. **Autenticación y Consentimiento:** El usuario se autentica contra el tenant. Si la aplicación lo requiere, se le solicita consentimiento para los permisos solicitados.
4. **Emisión del Authorization Code:** Azure AD redirige al cliente entregando un `authorization_code` temporal.
5. **Intercambio por Tokens:** El cliente hace una petición POST al endpoint de token enviando el `authorization_code` y el `code_verifier` original.
6. **Validación y Entrega:** Azure AD aplica SHA256 al `code_verifier` y lo compara con el `code_challenge`. Si coinciden, emite el token de acceso (JWT).

## Implementación en Azure AD (App Registration)

Para que el flujo funcione correctamente, la aplicación debe estar configurada de manera precisa en Entra ID:

- **Plataforma del cliente:** Debe registrarse como aplicación de tipo *Single-page application (SPA)* o *Mobile and desktop applications* (Public Client). Esto habilita implícitamente el soporte para PKCE sin requerir un Client Secret.
- **Exposición de la API:** En la sección *Expose an API*, se configura el Application ID URI (habitualmente `api://<client-id>`) y se define un scope personalizado, típicamente `access_as_user`, para permitir la delegación de identidad.
- **Configuración de Scopes en el cliente:** Durante el *Authorization Request*, el cliente debe solicitar explícitamente este scope configurado (ej. `api://<api-client-id>/access_as_user`).

## Lecciones de Troubleshooting

Durante la integración y pruebas de laboratorio se identificaron y resolvieron los siguientes escenarios de error comunes en Entra ID:

| Código de Error Azure | Causas Comunes identificadas | Solución Aplicada |
| :--- | :--- | :--- |
| **AADSTS501481** | El `redirect_uri` no coincide, el cliente no está marcado como público, o PKCE no está bien formado. | Verificar que la URI de redirección coincide exactamente y que la plataforma en el App Registration es compatible con flujos públicos (SPA/Mobile). |
| **AADSTS90013** | Solicitud de `scope` incorrecto, falta de consentimiento del administrador, o permisos no aceptados por el usuario. | Validar que el scope solicitado tiene el formato `api://...` y que la API ha sido autorizada para delegar acceso (Admin Consent). |

## Consideraciones de Seguridad
- PKCE protege el `authorization_code` frente a ataques de interceptación durante la redirección al navegador.
- Al actuar como *Public Client*, no se almacena ningún secreto en el cliente, mitigando el riesgo de fuga de credenciales estáticas.

## Recursos de referencia
- [RFC 7636 - Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636)
- [Microsoft Entra ID - Flujo de código de autorización OAuth 2.0](https://learn.microsoft.com/azure/active-directory/develop/v2-oauth2-auth-code-flow)
