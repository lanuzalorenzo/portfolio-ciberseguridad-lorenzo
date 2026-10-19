# 01 | MFA en Microsoft Entra ID

> **Estado:** validado en laboratorio (PASS). Tenant de prueba, sin datos reales.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Tenant de Microsoft Entra ID con identidades administrativas y estándar expuestas al riesgo de autenticación basada únicamente en contraseña.  
**Objetivo de seguridad:** Eliminar el riesgo de compromiso de cuentas mediante autenticación multifactor (MFA), combinando Security Defaults y el registro de un método TOTP externo.  
**Alcance:** Tenant de laboratorio, usuarios de prueba nativos y aplicación de autenticación TOTP (Proton Pass).

## Enfoque técnico

- Activación de Security Defaults.
- Revisión de la configuración de MFA por usuario en el portal.
- Registro de un autenticador TOTP externo.
- Validación del desafío MFA en el inicio de sesión.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluye identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra ID** | Proveedor de identidad | Tenant cloud-native; gestión centralizada de usuarios. |
| **Security Defaults** | Directiva base de protección | Activado; impone MFA y bloquea autenticación heredada. |
| **Panel MFA por usuario** | Gestión granular | Usuario de prueba en estado *Enabled*. |
| **Proton Pass (TOTP)** | Autenticador externo OATH-TOTP | Registro por QR y validación de código de 6 dígitos. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| MFA obligatoria | Security Defaults activado en el tenant | MCSB IA-2 / CIS 1.1 |
| Bloqueo de autenticación heredada | Forzado por Security Defaults | MCSB IA-3 |
| Registro de método OATH-TOTP | Alta y comprobación en *My Sign-Ins* | RFC 6238 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Inicio de sesión solo con contraseña | Login en el portal de Entra ID | Solicitud obligatoria de MFA | PASS: el portal exige el segundo factor |
| Registro de TOTP con Proton Pass | Escaneo de QR e introducción de token | Vinculación exitosa | PASS: método verificado en *Security Info* |
| Desafío MFA en login | Introducción de código de 6 dígitos | Acceso concedido | PASS: autenticación completada |

## Lecciones aprendidas

- Security Defaults es la forma más rápida de elevar la postura en tenants sin licencias P1/P2.
- El bloqueo de autenticación heredada elimina ataques de *password spraying* contra protocolos sin MFA.
- La opción clásica *Enforce* pierde relevancia frente a Security Defaults o Acceso Condicional moderno.
- Los autenticadores TOTP de terceros son interoperables mediante RFC 6238.

## Artefactos relacionados

- [Informe técnico de configuración](docs/mfa-configuracion.md)
- [Bitácora del módulo](../../bitacora/2026-09-04-mfa-entra-id.md)
