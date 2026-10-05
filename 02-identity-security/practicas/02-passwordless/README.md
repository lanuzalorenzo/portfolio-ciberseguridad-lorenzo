# Autenticación Passwordless
# 02 | Autenticación Passwordless en Microsoft Entra ID

La práctica documenta la habilitación y comprobación de métodos de inicio de sesión sin contraseña en Microsoft Entra ID.
## Descripción del escenario y objetivo de seguridad

## Enfoque técnico
**Escenario:** Identidades de usuario dependientes de contraseñas complejas, vulnerables a ataques de phishing de credenciales, fatiga de contraseñas y fuerza bruta.  
**Objetivo de seguridad:** Desplegar una estrategia de autenticación sin contraseñas (Passwordless) robusta basada en Microsoft Authenticator, Passkeys (FIDO2) y Windows Hello for Business.  
**Alcance:** Políticas de métodos de autenticación del tenant de Entra ID y usuario nativo (*Member*).

- Microsoft Authenticator en modo Passwordless.
- Passkey / FIDO2.
- Windows Hello for Business.
> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Validación
## Arquitectura y componentes de Azure utilizados

El escenario registra el inicio de sesión con los métodos configurados y la comprobación de sus controles de autenticación.
| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Authenticator** | Notificación push con coincidencia de números | Passwordless habilitado; coincidencia de números activa para evitar fatiga de MFA. |
| **Passkey (FIDO2)** | Autenticación resistente al phishing | Habilitado autoservicio; sin requisito de atestación estricta para pruebas. |
| **Windows Hello for Business** | Autenticación biométrica / PIN local ligada a hardware | Habilitado a nivel de directiva de métodos de autenticación. |
| **Usuario Nativo (Member)** | Sujeto de autenticación | Cuenta nativa en `@dominio.onmicrosoft.com` (las cuentas Guest/EXT no soportan passwordless nativo). |

## Documentación técnica
## Implementación de controles DevSecOps / Seguridad

[Configuración de métodos Passwordless](docs/passwordless-configuracion.md)
| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Autenticación resistente a phishing | Métodos Passkey / FIDO2 | Directiva de métodos en portal Entra ID | MCSB IA-2 / FIDO Alliance |
| Notificación de número coincidente | Número mostrado en pantalla que debe teclearse en app | Política de Microsoft Authenticator | NIST SP 800-63B |
| Eliminación de secreto estático (contraseña) | Flujo completo de inicio sin solicitar contraseña | Autenticación basada en criptografía asimétrica | MCSB IA-1 |

**Artefactos relacionados:** [Configuración de métodos Passwordless](docs/passwordless-configuracion.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Habilitación de métodos en directiva | Portal Entra ID → Authentication methods | Métodos activados y dirigidos a usuarios del laboratorio | PASS: Habilitados Authenticator, FIDO2 y WHfB |
| Registro de usuario invitado (EXT) vs nativo | Intento de registro en cuenta Guest | Cuentas tipo Guest no habilitan flujo passwordless | PASS: Confirmado; se creó usuario Member nativo para el laboratorio |
| Inicio de sesión Passwordless con Authenticator | Login introduciendo solo UPN y emparejando número | Acceso concedido sin teclear contraseña | PASS: Autenticación completada con éxito |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **IA-1: Identidades de confianza y credenciales seguras** | Adopción de Passwordless | Elimina el vector de ataque número uno en identidad corporativa: el robo y reutilización de credenciales. |
| **IA-2: Autenticación fuerte y moderna** | Despliegue de Passkeys / FIDO2 | Ofrece la mayor protección contra ataques Man-in-the-Middle (AitM) y phishing inverso. |

- Las cuentas invitadas o externas (B2B/Guest) tienen un ciclo de autenticación dependiente de su tenant de origen y no admiten Passwordless nativo gestionado en el tenant de destino.
- La coincidencia de números (*Number Matching*) es esencial para anular los ataques de saturación o fatiga de MFA (*MFA fatigue*).
