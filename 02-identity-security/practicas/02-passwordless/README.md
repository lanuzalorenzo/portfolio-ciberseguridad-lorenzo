# 02 | Autenticación Passwordless en Microsoft Entra ID

> **Estado:** validado en laboratorio (PASS). Tenant de prueba, sin datos reales.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Identidades dependientes de contraseñas complejas, vulnerables a phishing, fatiga de contraseñas y fuerza bruta.  
**Objetivo de seguridad:** Desplegar una estrategia sin contraseñas basada en Microsoft Authenticator, Passkeys (FIDO2) y Windows Hello for Business.  
**Alcance:** Políticas de métodos de autenticación del tenant y usuario nativo (*Member*).

## Enfoque técnico

- Microsoft Authenticator en modo Passwordless.
- Passkey / FIDO2.
- Windows Hello for Business.
- Validación del inicio de sesión sin contraseña.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluye identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Authenticator** | Notificación push con coincidencia de números | Passwordless habilitado; number matching activo. |
| **Passkey (FIDO2)** | Autenticación resistente al phishing | Habilitado autoservicio; sin atestación estricta en pruebas. |
| **Windows Hello for Business** | Autenticación biométrica/PIN ligada al hardware | Habilitado en la directiva de métodos. |
| **Usuario nativo (Member)** | Sujeto de autenticación | Cuenta `@dominio.onmicrosoft.com`; las cuentas Guest no admiten Passwordless nativo. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Autenticación resistente a phishing | Passkey / FIDO2 | MCSB IA-2 / FIDO Alliance |
| Coincidencia de números | Número en pantalla que se teclea en la app | NIST SP 800-63B |
| Eliminación del secreto estático | Inicio de sesión sin contraseña | MCSB IA-1 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Habilitación de métodos | Portal Entra ID → Authentication methods | Métodos activos para usuarios del laboratorio | PASS: Authenticator, FIDO2 y WHfB habilitados |
| Registro en cuenta Guest | Intento de registro en cuenta EXT | Guest no habilita Passwordless nativo | PASS: se creó un usuario Member para el laboratorio |
| Login Passwordless con Authenticator | UPN + coincidencia de número | Acceso sin contraseña | PASS: autenticación completada |

## Lecciones aprendidas

- Las cuentas invitadas dependen de su tenant de origen y no admiten Passwordless nativo gestionado en el destino.
- La coincidencia de números mitiga ataques de fatiga de MFA.
- Passkeys reduce el riesgo de phishing inverso y *man-in-the-middle*.

## Artefactos relacionados

- [Configuración de métodos Passwordless](docs/passwordless-configuracion.md)
- [Bitácora del módulo](../../bitacora/2026-09-08-identity-security.md)
