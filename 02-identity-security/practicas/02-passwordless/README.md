# 02 | Autenticación Passwordless en Microsoft Entra ID

> **Estado:** **Validado** en laboratorio (evidencia documental). Tenant de prueba, sin datos reales.
>
> **Referencias:** MCSB IA-1, IA-2 · NIST SP 800-63B · FIDO Alliance.

MFA encarece el ataque, pero la contraseña sigue existiendo. Passwordless la elimina: el usuario demuestra quién es con un dispositivo, una passkey o la cara, y no hay secreto que robar, adivinar ni reutilizar en otro servicio.

En esta práctica se habilitaron Microsoft Authenticator en modo sin contraseña, passkeys FIDO2 y Windows Hello for Business, y se validó el inicio de sesión sin contraseña con coincidencia de números.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Habilitación de métodos | Portal de Entra ID, métodos de autenticación | Métodos activos para el laboratorio | PASS: Authenticator, FIDO2 y Windows Hello habilitados |
| Registro en una cuenta Guest | Intento de alta en cuenta externa | Passwordless no disponible para Guest | PASS: se creó un usuario Member para la práctica |
| Inicio de sesión sin contraseña | UPN y coincidencia de número | Acceso sin contraseña | PASS: autenticación completada |

## Lecciones

- Una cuenta invitada depende de su tenant de origen: no admite Passwordless nativo en el destino.
- La coincidencia de números corta la fatiga de MFA, porque el usuario no aprueba a ciegas.
- Las passkeys resisten el phishing inverso y el ataque de intermediario mucho mejor que un código.

## Más detalle

- [Configuración de métodos](informe.md)
- [Bitácora del módulo](../../bitacora/2026-09-08-identity-security.md)
