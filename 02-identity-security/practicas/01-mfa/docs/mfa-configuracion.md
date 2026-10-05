# Informe técnico — Configuración de MFA en Microsoft Entra ID
# Informe técnico — Configuración y Validación de MFA en Microsoft Entra ID

## Contexto
Tenant de laboratorio en Microsoft Entra ID.  
Se requiere habilitar MFA, registrar un método TOTP externo y validar el flujo completo de autenticación.
**Módulo:** 02 — Identity Security  
**Práctica:** 01 — Multi-Factor Authentication (MFA)

---
## Contexto y Alcance
En entornos corporativos y de laboratorio, la autenticación basada únicamente en credenciales estáticas (usuario y contraseña) es vulnerable a ataques de *password spraying*, filtraciones y fuerza bruta.

## Objetivo
Aplicar una configuración mínima de seguridad basada en Security Defaults, habilitar MFA para un usuario de laboratorio y verificar el funcionamiento de un método TOTP externo (Proton Pass).
Esta práctica documenta la aplicación de una directiva base de seguridad mediante **Security Defaults**, la configuración de MFA por usuario y la verificación del flujo completo utilizando una aplicación de autenticación TOTP externa compatible con el estándar OATH (Proton Pass).

---
## Procedimiento Técnico y Decisiones de Configuración

## Trabajo realizado

### 1. Activación de Security Defaults
- Acceso al portal: https://entra.microsoft.com  
- Ruta: Identidad → Overview → Properties  
- Acción: activar **Security Defaults**.  
- Efectos:
  - MFA obligatorio para administradores.  
  - Bloqueo de autenticación heredada.  
  - Baseline mínima sin granularidad avanzada.
Se habilitó la línea base de seguridad en el tenant:
- **Ruta de configuración:** *Microsoft Entra admin center* → *Overview* → *Properties* → *Manage security defaults*.
- **Configuración aplicada:** `Security defaults = Enabled`.
- **Impacto directo:** 
  - Obligatoriedad de MFA para roles con privilegios administrativos.
  - Bloqueo global de protocolos de autenticación heredada (*Legacy Authentication* como POP3, IMAP, SMTP y PowerShell básico).
  - Exigencia de registro de MFA a todos los usuarios en situaciones de riesgo o según directiva.

### 2. Localización del panel clásico de MFA
- Ruta real en la UI moderna:
  - Identidad → Usuarios  
  - Métodos de autenticación  
  - Tarjeta: **Autenticación multifactor por usuario**  
- Observación: la opción clásica **Enforce** ya no aparece; solo **Enable**.
### 2. Navegación en Interfaz y Localización del Panel Clásico
Durante la práctica se identificó que la interfaz moderna de Entra integra el panel tradicional de MFA de forma embebida:
- **Ruta identificada:** *Identidad* → *Usuarios* → pestaña *Métodos de autenticación* → tarjeta *Autenticación multifactor por usuario*.
- **Observación técnica:** La opción clásica de estado *Enforce* ha quedado obsoleta en la consola moderna; el estado operativo es *Enabled*, delegando la obligatoriedad en el siguiente inicio de sesión o mediante directivas de acceso moderno.

### 3. Habilitación de MFA por usuario
- Selección del usuario en el panel clásico.  
- Acción: **Enable MFA**.  
- Resultado: el usuario debe registrar MFA en el siguiente inicio de sesión.
### 3. Registro de Método OATH-TOTP Externo (Proton Pass)
En lugar de depender exclusivamente de la aplicación propietaria Microsoft Authenticator, se validó la interoperabilidad del estándar RFC 6238:
1. El usuario inicia sesión y el portal solicita la configuración del segundo factor.
2. Se selecciona la opción *"Deseo usar otra aplicación de autenticación"*.
3. Se escanea el código QR generado con Proton Pass.
4. Se introduce el código temporal de 6 dígitos para confirmar la sincronización temporal.
5. El método queda registrado y validado en el perfil de seguridad del usuario.

### 4. Registro del método TOTP externo (Proton Pass)
- Flujo seguido:
  - Inicio de sesión del usuario.  
  - Selección de “Aplicación de autenticación”.  
  - Escaneo del QR con Proton Pass.  
  - Introducción del código TOTP.  
- Resultado: método registrado y verificado correctamente.
## Validaciones y Pruebas Realizadas

### 5. Validación del flujo MFA
- Inicio de sesión con MFA habilitado.  
- Introducción del código TOTP desde Proton Pass.  
- Resultado: autenticación completada y MFA aplicado.
| Control / Prueba | Método | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Bloqueo de acceso directo solo con contraseña | Autenticación en portal web de Azure/Entra | El sistema exige registro/desafío de segundo factor | PASS: Acceso detenido hasta verificar MFA |
| Validación de código TOTP | Introducción del código de 6 dígitos desde Proton Pass | Validación criptográfica del hash temporal | PASS: Autenticación exitosa y acceso concedido |
| Bloqueo de cliente con autenticación básica | Intento de autenticación vía cliente sin soporte MFA | Rechazo de la conexión por Security Defaults | PASS: Protocolos heredados deshabilitados |

---

## Validaciones realizadas
- Security Defaults activo.  
- Usuario marcado como **Enabled** para MFA.  
- Método TOTP registrado y funcional.  
- Flujo de autenticación validado de extremo a extremo.

---

## Problemas encontrados
- El panel clásico de MFA está oculto dentro de la UI moderna.  
- Documentación oficial aún referencia opciones que ya no existen (como **Enforce**).

---

## Soluciones aplicadas
- Documentación de la ruta real hacia el panel clásico.  
- Ajuste del procedimiento para la interfaz moderna.  
- Validación del comportamiento de Security Defaults como reemplazo de Enforce.

---

## Implicaciones de seguridad
- Security Defaults es adecuado para laboratorios y entornos pequeños
## Lecciones de Troubleshooting y Seguridad
- **Diferencia de estados clásicos vs modernos:** Comprender que *Enforce* ya no se utiliza en implementaciones modernas evita discrepancias al seguir guías o documentación histórica.
- **Interoperabilidad OATH:** Permitir autenticadores compatibles con RFC 6238 ofrece flexibilidad para usuarios que gestionan sus credenciales en gestores de contraseñas de terceros.
- **Limitación de Security Defaults:** Aunque es gratuito y protege eficazmente entornos pequeños o de laboratorio, no permite exclusiones granulares ni condiciones contextuales (ubicación, riesgo de IP); en entornos empresariales maduros debe sustituirse por directivas de **Conditional Access** (requiere Entra ID P1/P2).
