# 01 | MFA en Microsoft Entra ID

> **Estado:** **Validado** en laboratorio (evidencia documental). Tenant de prueba, sin datos reales.
>
> **Referencias:** MCSB IA-2, IA-3 · CIS 1.1 · RFC 6238.

Una cuenta protegida solo por contraseña se abre con una contraseña filtrada. MFA añade una segunda prueba —un código temporal de seis dígitos— de modo que la contraseña robada deja de ser suficiente. En esta práctica se activó Security Defaults, se habilitó MFA por usuario y se validó el flujo con un autenticador TOTP externo a Microsoft.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Inicio de sesión solo con contraseña | Login en el portal de Entra ID | Solicitud obligatoria de MFA | PASS: el portal exige el segundo factor |
| Registro de TOTP con Proton Pass | Escaneo de QR e introducción de token | Vinculación correcta | PASS: método verificado en Security Info |
| Contraseña correcta y código válido | Introducción del código de 6 dígitos | Acceso concedido | PASS: autenticación completada |

## Lecciones

- Security Defaults eleva la postura en minutos en tenants sin licencias P1/P2, a cambio de no permitir exclusiones ni condiciones.
- Bloquear la autenticación heredada elimina el *password spraying* contra protocolos sin MFA.
- Cualquier autenticador TOTP compatible con RFC 6238 sirve, no solo Microsoft Authenticator.

## Más detalle

- [Configuración paso a paso](docs/mfa-configuracion.md)
- [Bitácora del módulo](../../bitacora/2026-09-04-mfa-entra-id.md)
