# Informe técnico — Configuración y validación de MFA en Microsoft Entra ID

**Módulo:** 02 — Identity Security
**Práctica:** 01 — Multi-Factor Authentication (MFA)
**Entorno:** tenant de laboratorio, sin datos reales.

## Contexto y alcance

En entornos corporativos y de laboratorio, la autenticación basada únicamente en credenciales estáticas está expuesta a *password spraying*, filtraciones y fuerza bruta. Esta práctica aplica una línea base de seguridad, habilita MFA para un usuario de laboratorio y valida un método TOTP externo compatible con OATH.

## Objetivo

Aplicar Security Defaults, habilitar MFA por usuario y verificar el flujo completo con una aplicación de autenticación TOTP externa (Proton Pass).

## Configuración y decisiones

### 1. Activación de Security Defaults

- **Ruta:** *Microsoft Entra admin center* → *Overview* → *Properties* → *Manage security defaults*.
- **Configuración aplicada:** `Security defaults = Enabled`.
- **Impacto:**
  - MFA obligatoria para roles con privilegios administrativos.
  - Bloqueo global de protocolos de autenticación heredada (POP3, IMAP, SMTP y PowerShell básico).
  - Exigencia de registro de MFA a los usuarios en situaciones de riesgo o según directiva.

### 2. Localización del panel clásico de MFA

Durante la práctica se comprobó que la interfaz moderna integra el panel tradicional de MFA de forma embebida:

- **Ruta identificada:** *Identidad* → *Usuarios* → pestaña *Métodos de autenticación* → tarjeta *Autenticación multifactor por usuario*.
- **Observación:** la opción clásica *Enforce* ya no aparece; solo *Enable*. La obligatoriedad se delega en el siguiente inicio de sesión o en directivas de acceso modernas.

### 3. Habilitación de MFA por usuario

- Selección del usuario en el panel clásico.
- Acción: **Enable MFA**.
- Resultado: el usuario debe registrar MFA en el siguiente inicio de sesión.

### 4. Registro de un método TOTP externo (Proton Pass)

Para validar la interoperabilidad del estándar RFC 6238 sin depender solo de Microsoft Authenticator:

1. El usuario inicia sesión y el portal solicita configurar el segundo factor.
2. Se selecciona la opción *«Deseo usar otra aplicación de autenticación»*.
3. Se escanea el código QR con Proton Pass.
4. Se introduce el código temporal de 6 dígitos para confirmar la sincronización.
5. El método queda registrado y validado en el perfil de seguridad del usuario.

## Validaciones y pruebas

| Control / prueba | Método | Comportamiento esperado | Resultado observado |
|---|---|---|---|
| Acceso solo con contraseña | Autenticación en el portal de Entra ID | El sistema exige el segundo factor | PASS: acceso detenido hasta verificar MFA |
| Validación de código TOTP | Código de 6 dígitos desde Proton Pass | Validación criptográfica del hash temporal | PASS: autenticación exitosa |
| Cliente con autenticación básica | Intento sin soporte MFA | Rechazo por Security Defaults | PASS: protocolos heredados deshabilitados |

Resumen: Security Defaults activo, usuario en estado **Enabled**, método TOTP registrado y flujo validado de extremo a extremo.

## Problemas encontrados

- El panel clásico de MFA está oculto dentro de la UI moderna.
- La documentación oficial sigue referenciando opciones que ya no existen, como *Enforce*.

## Soluciones aplicadas

- Documentar la ruta real al panel clásico.
- Ajustar el procedimiento a la interfaz moderna.
- Validar Security Defaults como reemplazo de *Enforce*.

## Implicaciones de seguridad

Security Defaults es adecuado para laboratorios y entornos pequeños, pero no permite exclusiones granulares ni condiciones contextuales.

## Lecciones

- **Estados clásicos vs modernos:** saber que *Enforce* ya no se usa evita discrepancias al seguir documentación histórica.
- **Interoperabilidad OATH:** admitir autenticadores RFC 6238 da flexibilidad a quien gestiona sus credenciales en un gestor de contraseñas.
- **Límite de Security Defaults:** en entornos maduros debe sustituirse por **Conditional Access** (requiere Entra ID P1/P2).
