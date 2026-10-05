# MFA en Microsoft Entra ID
# 01 | Habilitación de MFA en Microsoft Entra ID

La práctica documenta la habilitación de MFA en un tenant de laboratorio, el registro de un método TOTP y la comprobación del inicio de sesión.
## Descripción del escenario y objetivo de seguridad

## Enfoque técnico
**Escenario:** Entorno de laboratorio en Microsoft Entra ID con identidades administrativas y estándar expuestas a riesgos de autenticación basada únicamente en contraseña.  
**Objetivo de seguridad:** Eliminar el riesgo de compromiso de cuentas mediante el despliegue de autenticación multifactor (MFA), combinando Security Defaults y registro de un método TOTP externo.  
**Alcance:** Tenant de laboratorio en Microsoft Entra ID, usuarios de prueba nativos y aplicación de autenticación TOTP (Proton Pass).

- Activación de Security Defaults.
- Revisión de la configuración de MFA por usuario en el portal.
- Registro de un autenticador TOTP externo.
> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Validación
## Arquitectura y componentes de Azure utilizados

El informe técnico registra la activación de MFA y la validación del flujo de inicio de sesión con el método TOTP.
| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra ID** | Proveedor de Identidad (IdP) | Tenant en modo nube nativo; gestión centralizada de usuarios. |
| **Security Defaults** | Directiva base de protección | Activado en propiedades del tenant; impone MFA y bloquea legacy auth. |
| **Panel MFA por Usuario** | Gestión granular de autenticación multifactor | Usuario de prueba en estado *Enabled*. |
| **Proton Pass (TOTP)** | Autenticador externo compatible OATH-TOTP | Registro mediante código QR y validación de código temporal de 6 dígitos. |

## Documentación
## Implementación de controles DevSecOps / Seguridad

[Informe técnico de configuración](docs/mfa-configuracion.md)
| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Autenticación multifactor obligatoria | Security Defaults activado en Entra ID | Directiva global de tenant | MCSB IA-2 / CIS 1.1 |
| Bloqueo de autenticación heredada | Forzado automáticamente por Security Defaults | Política de acceso básico | MCSB IA-3 |
| Registro de método OATH-TOTP | Registro y comprobación en portal *My Sign-Ins* | Flujo autoservicio de usuario | RFC 6238 |

**Artefactos relacionados:** [Informe técnico de configuración](docs/mfa-configuracion.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Inicio de sesión solo con contraseña | Login en portal Entra ID | Solicitud obligatoria de configuración/desafío MFA | PASS: El portal detiene el acceso y exige el segundo factor |
| Registro de método TOTP con Proton Pass | Escaneo de código QR e introducción de token | Vinculación exitosa del generador de códigos | PASS: Token verificado y método guardado en *Security Info* |
| Validación de desafío MFA en login | Inicio de sesión introduciendo código de 6 dígitos | Acceso concedido al portal | PASS: Autenticación completada satisfactoriamente |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **IA-2: Despliegue de MFA** | Aplicación de MFA en todas las identidades | Security Defaults es la forma más rápida y efectiva de elevar la postura en tenants sin licencias premium P1/P2. |
| **IA-3: Bloqueo de legacy authentication** | Mitigación de protocolos POP3/IMAP/SMTP básicos | Elimina de raíz ataques de *password spraying* dirigidos a protocolos sin soporte MFA. |

- La opción clásica *Enforce* de MFA ya no es relevante con Security Defaults o Acceso Condicional moderno; *Enabled* dispara el registro en el siguiente login.
- Aplicaciones TOTP de terceros (Proton Pass, Bitwarden, etc.) son perfectamente interoperables con Entra ID vía estándar RFC 6238.
