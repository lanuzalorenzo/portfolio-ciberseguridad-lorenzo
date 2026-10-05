# Informe técnico — Conceptos del Módulo 01

**Proyecto:** Módulo 01 — Seguridad en Azure (Autenticación, Autorización y Protección de APIs).

## Objetivo del documento
Definir y explicar los conceptos fundamentales necesarios para comprender el flujo de autenticación y autorización implementado en el módulo, incluyendo OAuth2, PKCE, JWT y Azure AD como proveedor de identidad.

## Conceptos fundamentales

1. **Autenticación y Autorización**: Bases teóricas del control de acceso.
2. **OAuth2**: Estándar de autorización utilizado para delegar acceso mediante tokens.
3. **PKCE (Proof Key for Code Exchange)**: Extensión de OAuth2 esencial en clientes públicos para proteger el intercambio del código de autorización.
4. **JWT (JSON Web Token)**: Formato de token utilizado para transmitir claims estructurados.
5. **JWKS (JSON Web Key Set) y RS256**: Conjunto de claves públicas y algoritmo asimétrico empleados para verificar la firma de los tokens emitidos.
6. **Azure AD (Microsoft Entra ID)**: Actúa como proveedor de identidad (IdP) encargado de autenticar usuarios y emitir tokens.

## Conclusiones teóricas clave
- PKCE es imprescindible para proteger el `authorization_code` en escenarios donde el cliente no puede custodiar un secreto (clientes públicos).
- La seguridad de la API depende enteramente de la correcta validación de los JWT emitidos por Azure AD, lo que incluye comprobar las firmas mediante JWKS para el algoritmo RS256.
- Es necesario validar sistemáticamente en cada petición el issuer (emisor), la audiencia (destinatario) y la fecha de expiración del token.

## Recursos de referencia
- [Microsoft Entra ID / Azure AD Documentation](https://learn.microsoft.com/azure/active-directory)
- [RFC 7636 - Proof Key for Code Exchange by OAuth Public Clients](https://datatracker.ietf.org/doc/html/rfc7636)
- [JWT.io - JSON Web Tokens](https://jwt.io)
