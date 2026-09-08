# Ejercicio 02 – Passwordless Authentication en Microsoft Entra ID

## Objetivo
Configurar y validar métodos de autenticación passwordless en Microsoft Entra ID:
- Microsoft Authenticator (passwordless)
- Passkey / FIDO2
- Windows Hello for Business
- Usuario nativo del tenant para pruebas

## Configuración aplicada
### Microsoft Authenticator
- Enable: On
- Target: All users
- Passwordless: Enabled

### Passkey (FIDO2)
- Enable: On
- Include: All users
- Allow self-service: Yes
- Enforce attestation: No

### Windows Hello for Business
- Enable: On
- Include: All users

## Usuario de prueba
Se crea un usuario nativo del tenant:
- UPN: test@lanuzalorenzooutlook.onmicrosoft.com
- Tipo: Member
- Contraseña temporal

## Registro de métodos
El usuario accede a https://mysignins.microsoft.com/security-info y registra:
- MFA (Microsoft Authenticator)
- Passwordless en Authenticator
- Windows Hello (opcional)
- Llave FIDO2 (opcional)

## Validación
El usuario puede iniciar sesión sin contraseña usando:
- Authenticator passwordless
- Windows Hello
- FIDO2 (si aplica)

## Resultado
Ejercicio completado con éxito. Passwordless funcional en usuario nativo del tenant.
