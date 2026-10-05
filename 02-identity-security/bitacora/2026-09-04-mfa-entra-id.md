# Bitácora — 2026-09-04: Habilitación de MFA y Verificación con Proton Pass

**Módulo:** 02 — Identity Security  
**Práctica:** 01 — MFA en Microsoft Entra ID

Hoy inicié las prácticas del bloque de seguridad de identidades centrándome en la línea base de autenticación multifactor en Entra ID.

Comencé activando **Security Defaults** desde las propiedades del tenant para forzar la protección en cuentas administrativas y bloquear de raíz protocolos de autenticación básica heredada (*legacy auth*). 

Al intentar configurar la directiva granular por usuario, me encontré con la primera dificultad práctica en el portal: la consola moderna de Entra ID ha absorbido el panel clásico de MFA de una forma poco intuitiva (oculto en una tarjeta dentro de la pestaña de métodos de autenticación del usuario). Además, confirmé que la opción histórica *Enforce* ya no se utiliza en la interfaz moderna; ahora el estado funcional es *Enabled*, y el portal fuerza el registro en el siguiente inicio de sesión.

Para validar el flujo, utilicé una cuenta de prueba del laboratorio y decidí probar un método alternativo a la app de Microsoft: vinculé **Proton Pass** mediante el estándar OATH-TOTP escaneando el código QR. La verificación temporal de 6 dígitos se sincronizó al primer intento. Cerré la sesión, probé el login y verifiqué que el acceso queda completamente detenido hasta introducir el código del gestor TOTP.

Práctica inicial completada con éxito.
