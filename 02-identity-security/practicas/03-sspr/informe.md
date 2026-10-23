# Informe técnico — Configuración y validación de SSPR en Microsoft Entra ID

**Módulo:** 02 — Identity Security
**Práctica:** 03 — Self-Service Password Reset (SSPR)
**Entorno:** tenant de laboratorio, sin datos reales.

## Contexto y alcance

El restablecimiento manual de contraseñas por parte del Help Desk genera carga operativa y es un vector habitual de ingeniería social (suplantación telefónica para forzar un cambio de credenciales). Esta práctica implanta SSPR con un usuario nativo del tenant y valida el flujo completo sin intervención del administrador.

- **Identidad:** cuenta nativa del tenant (identificador omitido).
- **Métodos configurados:** email alternativo, teléfono móvil y Microsoft Authenticator.
- **Alcance:** habilitado para los usuarios de laboratorio.

## Objetivo

Configurar SSPR, habilitar métodos de recuperación y verificar que un usuario puede restablecer su contraseña de forma autónoma.

## Configuración y decisiones

### 1. Directiva de SSPR

- **Ruta:** *Microsoft Entra admin center* → *Protección* → *Restablecimiento de contraseña*.
- **Alcance (*Properties*):** `Enabled = Selected` para el grupo de usuarios de prueba.
- **Métodos requeridos:** **1** para el laboratorio. En producción, MCSB recomienda exigir 2 métodos independientes.

### 2. Métodos de recuperación

Se seleccionaron canales fuera de banda (*out-of-band*):

- Correo electrónico alternativo, no corporativo.
- Teléfono móvil (SMS o llamada).
- Notificación de Microsoft Authenticator.

### 3. Registro previo de información de seguridad

SSPR depende de la experiencia de registro combinado: si el usuario no ha registrado sus métodos en `https://mysignins.microsoft.com/security-info`, el portal de autoservicio bloquea la recuperación y remite al administrador. Se verificó el alta previa con el usuario nativo antes de simular la pérdida de contraseña.

### 4. Asignación del usuario de pruebas

- **Identidad:** cuenta nativa del tenant (identificador omitido).
- **Motivo:** es compatible con MFA, SSPR y Passwordless.

## Validaciones y pruebas

| Escenario evaluado | Método | Comportamiento esperado | Resultado observado |
|---|---|---|---|
| Recuperación sin datos registrados | Acceso a `aka.ms/sspr` con un usuario sin métodos | Bloqueo con aviso de contacto con el administrador | PASS: bloqueo preventivo |
| Desafío de identidad | UPN y captcha en `aka.ms/sspr` | Envío de OTP al método registrado | PASS: código recibido en el canal alternativo |
| Restablecimiento de contraseña | OTP y nueva clave segura | Actualización inmediata y cierre de sesiones previas | PASS: contraseña cambiada y validada en el siguiente login |

Flujo seguido: introducción del UPN → selección del método → recepción del código → nueva contraseña. Resultado: contraseña restablecida y acceso correcto sin intervención del administrador.

## Problemas encontrados

- Algunos métodos no aparecen si el usuario no los registró previamente.
- La interfaz moderna oculta rutas antiguas documentadas en guías previas.

## Soluciones aplicadas

- Registro previo de métodos en *My Sign-Ins*.
- Documentación de las rutas reales de la interfaz moderna.
- Validación del flujo completo con un usuario nativo.

## Implicaciones de seguridad

SSPR reduce la carga del administrador y mejora la resiliencia del tenant, pero exige registro previo y métodos fuera de banda para no convertirse en un vector de secuestro de cuenta.

## Lecciones

- **Password Writeback en entornos híbridos:** con Microsoft Entra Connect, el reseteo en la nube solo impacta en Active Directory local si hay licencia P1/P2 y *Password Writeback* activo.
- **Ingeniería social:** automatizar el proceso elimina la necesidad de que el Help Desk restablezca contraseñas «a ciegas» ante llamadas no verificadas.
