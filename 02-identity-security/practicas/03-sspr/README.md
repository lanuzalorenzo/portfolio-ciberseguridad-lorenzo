# 03 | Self-Service Password Reset (SSPR) en Microsoft Entra ID

> **Estado:** validado en laboratorio (PASS). Tenant de prueba, sin datos reales.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Usuarios con bloqueos de cuenta o contraseñas olvidadas generan carga en el Help Desk y abren vectores de ingeniería social telefónica.  
**Objetivo de seguridad:** Habilitar la recuperación autónoma de contraseñas exigiendo factores previamente registrados.  
**Alcance:** Tenant de laboratorio, directiva SSPR y usuario nativo con métodos de contacto registrados.

## Enfoque técnico

- Alcance de SSPR y métodos de verificación.
- Registro previo de métodos de recuperación.
- Validación del restablecimiento y del login posterior.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluye identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Directiva SSPR** | Motor de autoservicio | Habilitada para usuarios de prueba; exige métodos registrados. |
| **Portal My Sign-Ins** | Registro unificado de métodos | Email alternativo, móvil y Microsoft Authenticator. |
| **Endpoint `aka.ms/sspr`** | Interfaz de recuperación | Captcha, UPN y retos de verificación. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Verificación multifactor en el reset | Métodos pre-registrados | MCSB IA-1 |
| Notificación al usuario | Alerta automática al cambiar la contraseña | NIST SP 800-63B |
| Mitigación de ingeniería social | Flujo autoservicio sin Help Desk | CIS Microsoft 365 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso sin métodos registrados | Usuario no preparado | El flujo se bloquea | PASS: no permite continuar |
| Registro de métodos | Alta de email y móvil | Métodos validados por OTP | PASS: estado confirmado |
| Recuperación autónoma | Flujo completo en `aka.ms/sspr` | Código, cambio de clave y login | PASS: contraseña restablecida sin TI |

## Lecciones aprendidas

- El registro combinado de MFA y SSPR en una sola sesión mejora la experiencia y la cobertura.
- En entornos híbridos, *Password Writeback* es necesario para reflejar el cambio en Active Directory.
- Los métodos deben revisarse periódicamente para evitar factores obsoletos.

## Artefactos relacionados

- [Configuración y validación de SSPR](docs/sspr-configuracion.md)
- [Bitácora del módulo](../../bitacora/2026-09-08-identity-security.md)
