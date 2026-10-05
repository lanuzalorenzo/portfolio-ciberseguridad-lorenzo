# Self-Service Password Reset
# 03 | Self-Service Password Reset (SSPR) en Microsoft Entra ID

La práctica recorre la configuración de recuperación autónoma de contraseñas en Microsoft Entra ID y la comprobación del flujo con una cuenta de laboratorio.
## Descripción del escenario y objetivo de seguridad

## Enfoque técnico
**Escenario:** Usuarios que sufren bloqueos de cuenta o contraseñas olvidadas, generando sobrecarga en el centro de soporte (Help Desk) y abriendo vectores de ingeniería social telefónica para reseteo indebido de claves.  
**Objetivo de seguridad:** Habilitar la recuperación de contraseñas de forma autónoma y segura mediante Self-Service Password Reset (SSPR), exigiendo factores de autenticación previos comprobados.  
**Alcance:** Tenant de laboratorio en Entra ID, directiva de SSPR y usuario nativo con métodos de contacto registrados.

- Alcance de SSPR y métodos de verificación disponibles.
- Registro previo de métodos de recuperación.
- Validación del restablecimiento y del inicio de sesión posterior.
> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Validación
## Arquitectura y componentes de Azure utilizados

El informe técnico describe el flujo utilizado y las condiciones que afectan a la disponibilidad de cada método.
| Componente | Función | Configuración relevante |
|---|---|---|
| **Directiva de SSPR** | Motor de restablecimiento de autoservicio | Habilitado para usuarios de prueba; exige 1 o 2 métodos de verificación. |
| **Portal My Sign-Ins** | Registro unificado de métodos de seguridad | Registro previo de correo alternativo, teléfono móvil y Microsoft Authenticator. |
| **Endpoint de autoservicio (`aka.ms/sspr`)** | Interfaz pública de recuperación de credenciales | Validación de captcha, solicitud de UPN y envío de retos de verificación. |

## Documentación técnica
## Implementación de controles DevSecOps / Seguridad

[Configuración y validación de SSPR](docs/sspr-configuracion.md)
| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Verificación multifactor en restablecimiento | Exigir métodos pre-registrados antes de permitir cambio | Directiva SSPR en Entra ID | MCSB IA-1 |
| Notificación de seguridad al usuario | Envío de alerta automática al cambiar la contraseña | Ajustes de directiva SSPR | NIST SP 800-63B |
| Mitigación de ingeniería social a Helpdesk | Automatización del proceso sin intervención humana | Flujo autoservicio validado | CIS Microsoft 365 Benchmark |

**Artefactos relacionados:** [Configuración y validación de SSPR](docs/sspr-configuracion.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso a `aka.ms/sspr` sin métodos registrados | Inicio de flujo con usuario no preparado | El sistema bloquea el reseteo y remite al administrador | PASS: Sin métodos de contacto previos, el flujo no permite continuar |
| Registro de métodos en `mysignins.microsoft.com` | Alta de email alternativo y móvil | Métodos validados con código OTP | PASS: Métodos registrados en estado confirmado |
| Recuperación autónoma de contraseña | Ejecución completa del flujo en `aka.ms/sspr` | Recepción de código, cambio de clave y login exitoso | PASS: Contraseña restablecida sin intervención de TI |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **IA-1: Gestión segura de credenciales** | Implementación de SSPR con métodos robustos | Evita que Help Desk sea engañado mediante suplantación de identidad para forzar cambios de contraseña. |

- La experiencia de registro combinado (*Combined Security Information Registration*) debe fomentarse activamente para que el usuario registre MFA y SSPR en una única sesión.
- En entornos híbridos con Active Directory on-premises, es indispensable habilitar *Password Writeback* en Microsoft Entra Connect si se desea que el reseteo en la nube impacte en el directorio local.
