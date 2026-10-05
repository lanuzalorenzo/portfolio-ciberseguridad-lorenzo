# Informe técnico — Configuración de SSPR en Microsoft Entra ID
# Informe técnico — Configuración y Validación de SSPR en Microsoft Entra ID

## Arquitectura del caso práctico
Para validar SSPR en un entorno realista dentro del laboratorio de identidad, se define el siguiente escenario:
**Módulo:** 02 — Identity Security  
**Práctica:** 03 — Self-Service Password Reset (SSPR)

- **Identidad:** cuenta nativa del tenant de laboratorio (identificador omitido)
- **Tipo de usuario:** nativo del tenant (ideal para MFA, SSPR y Passwordless)
- **Métodos de recuperación configurados:**
  - Email alternativo
  - Teléfono móvil
  - Microsoft Authenticator (si está registrado)
- **Alcance de SSPR:** habilitado para todos los usuarios del laboratorio
- **Objetivo del caso práctico:** demostrar que el usuario puede recuperar su contraseña sin intervención del administrador y validar el flujo completo de restablecimiento.
## Contexto y Alcance
El restablecimiento manual de contraseñas por parte del equipo de soporte (Help Desk) no solo genera una carga operativa elevada, sino que constituye uno de los vectores principales de ingeniería social (ataques de suplantación de identidad telefónica para forzar cambios de credenciales).

---
Esta práctica documenta la implementación de **Self-Service Password Reset (SSPR)** en Microsoft Entra ID, evaluando los requisitos previos de registro de métodos, las políticas de seguridad aplicadas y la verificación del flujo de recuperación de autoservicio.

## Contexto
Laboratorio de identidad en Microsoft Entra ID.  
Se requiere habilitar Self-Service Password Reset (SSPR) y validar el flujo completo de recuperación de contraseña para un usuario de pruebas.
## Configuración y Decisiones de Arquitectura

---
### 1. Habilitación de la Directiva de SSPR
- **Ruta de configuración:** *Microsoft Entra admin center* → *Protección* → *Restablecimiento de contraseña*.
- **Alcance (*Properties*):** Habilitado para el grupo de usuarios de prueba del laboratorio (`Enabled = Selected`).
- **Número de métodos requeridos para restablecer:** Se configuró en **1 método** para pruebas de laboratorio (en producción corporativa la recomendación MCSB es exigir 2 métodos independientes).

## Objetivo
Configurar SSPR, habilitar métodos de recuperación y verificar que un usuario puede restablecer su contraseña sin intervención del administrador.
### 2. Métodos de Autenticación Habilitados para Recuperación
Se seleccionaron métodos que garanticen un canal fuera de banda (*out-of-band*):
- Correo electrónico alternativo (no corporativo).
- Teléfono móvil (código SMS o llamada).
- Notificación de la aplicación móvil (Microsoft Authenticator).

---
### 3. Registro Previo de Información de Seguridad
Uno de los puntos críticos de control identificados es que SSPR depende de la **experiencia de registro combinado**:
- Si el usuario no ha registrado previamente sus métodos de contacto en `https://mysignins.microsoft.com/security-info`, el portal de autoservicio (`aka.ms/sspr`) bloquea la recuperación y remite al usuario a su administrador.
- Se verificó el alta previa de los datos de contacto con el usuario nativo de prueba antes de simular el incidente de pérdida de clave.

## Trabajo realizado
## Validaciones y Pruebas Realizadas

### Habilitación de SSPR en el tenant
**Ruta:** Identidad → Métodos de autenticación → Self-Service Password Reset  
**Enabled:** Selected  
**Target:** All users (laboratorio)
| Escenario Evaluado | Método de Comprobación | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Recuperación sin datos registrados | Acceso a `aka.ms/sspr` con usuario sin métodos | Mensaje de bloqueo: *"Póngase en contacto con el administrador"* | PASS: Bloqueo de seguridad preventivo |
| Desafío de identidad en `aka.ms/sspr` | Introducción de UPN y resolución de Captcha | Envío de código de un solo uso (OTP) al método registrado | PASS: Código recibido en el canal alternativo |
| Restablecimiento y actualización de contraseña | Introducción del código OTP y nueva clave segura | Actualización inmediata en Entra ID y cierre de sesiones previas | PASS: Contraseña cambiada y validada en siguiente login |

### Configuración de métodos de recuperación
Métodos habilitados:
- Email alternativo  
- Teléfono móvil  
- Microsoft Authenticator (si ya está registrado)

### Asignación del usuario de pruebas
- **Identidad:** cuenta nativa del tenant de laboratorio (identificador omitido)
- **Motivo:** usuario nativo compatible con MFA, SSPR y Passwordless.

---

## Validación del flujo SSPR
**Ruta:** https://aka.ms/sspr

**Flujo seguido:**
1. Introducción del UPN  
2. Selección del método de verificación  
3. Recepción del código  
4. Restablecimiento de contraseña  

**Resultado:** contraseña restablecida correctamente.

---

## 🧪 Caso práctico final — Validación completa de SSPR

### 1. Inicio del flujo
El usuario accede a la ruta oficial de recuperación de contraseña:  
https://aka.ms/sspr

Introduce su UPN y selecciona “No recuerdo mi contraseña”.

### 2. Selección del método de verificación
El sistema muestra los métodos previamente registrados:
- Email alternativo  
- Teléfono móvil  
- Microsoft Authenticator  

El usuario selecciona uno de ellos y recibe el código de verificación.

### 3. Restablecimiento de contraseña
Tras validar el código, el usuario introduce una nueva contraseña cumpliendo los requisitos del tenant.

**Resultado:**
- Contraseña actualizada correctamente  
- El usuario puede iniciar sesión con la nueva credencial  
- El flujo completo funciona sin intervención del administrador

### 4. Conclusión
El ejercicio demuestra que SSPR está correctamente habilitado, configurado y funcional en el entorno del laboratorio.  
La recuperación de contraseña es segura, autónoma y reduce la carga operativa del administrador.

---

## Problemas encontrados
- Algunos métodos no aparecen si el usuario no los registró previamente.  
- La UI moderna oculta rutas antiguas documentadas en guías previas.

---

## Soluciones aplicadas
- Registro previo de métodos en My Sign-Ins.  
- Documentación de rutas reales en la interfaz moderna.  
- Validación del flujo completo con usuario nativo.

---

## Implicaciones de seguridad
SSPR reduce la carga del administrador y mejora la resiliencia del tenant.  
Permite recuperación segura sin intervención manual y evita bloqueos operativos.
## Lecciones de Troubleshooting y Seguridad
- **Password Writeback en entornos híbridos:** En arquitecturas sincronizadas con Active Directory local (mediante Microsoft Entra Connect), el reseteo en la nube solo impactará en el Directorio Activo on-premises si se cuenta con licencia P1/P2 y se activa explícitamente *Password Writeback*.
- **Mitigación de ingeniería social:** Automatizar el proceso mediante SSPR elimina la necesidad de que los operadores de Help Desk restablezcan contraseñas "a ciegas" ante llamadas telefónicas no verificadas.
