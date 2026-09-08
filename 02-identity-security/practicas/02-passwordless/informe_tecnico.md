# Informe Técnico – Ejercicio 02: Passwordless Authentication

## Resumen
Se habilitan los tres métodos passwordless en Microsoft Entra ID y se valida su funcionamiento mediante un usuario nativo del tenant.

## Configuración aplicada
- Microsoft Authenticator: Enabled + Passwordless
- FIDO2 Passkey: Enabled + All users
- Windows Hello for Business: Enabled + All users

## Problema detectado
El usuario original era EXT:
lanuzalorenzo_outlook.com#EXT#@lanuzalorenzooutlook.onmicrosoft.com

Las cuentas EXT no soportan passwordless → se crea usuario nativo.

## Usuario de prueba
- test@lanuzalorenzooutlook.onmicrosoft.com
- Member
- Compatible con MFA, SSPR, Passwordless, Hello, FIDO2

## Validación
El usuario accede a My Sign-Ins y aparece el flujo de registro:
- MFA
- Authenticator
- Passwordless
- Windows Hello
- FIDO2

Esto confirma que la configuración es correcta.

## Conclusión
Passwordless queda habilitado y funcional en el tenant.
