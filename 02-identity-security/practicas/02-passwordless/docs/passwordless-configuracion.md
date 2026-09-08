# 🔐 Informe técnico — Configuración de Passwordless en Microsoft Entra ID

🧾 **Contexto**  
Laboratorio de identidad en Microsoft Entra ID.  
Se requiere habilitar métodos passwordless y validar su funcionamiento con un usuario nativo del tenant.

🎯 **Objetivo**  
Configurar Microsoft Authenticator passwordless, Passkey (FIDO2) y Windows Hello for Business.  
Crear un usuario nativo del tenant y verificar el flujo completo de autenticación sin contraseña.

🛠 **Trabajo realizado**

1. **Habilitación de Microsoft Authenticator (passwordless)**  
   Ruta: Identidad → Métodos de autenticación → Microsoft Authenticator  
   - Enabled: On  
   - Passwordless: Enabled  
   - Target: All users  

2. **Habilitación de Passkey (FIDO2)**  
   Ruta: Identidad → Métodos de autenticación → Passkey (FIDO2)  
   - Enabled: On  
   - Allow self-service: Yes  
   - Enforce attestation: No  

3. **Habilitación de Windows Hello for Business**  
   Ruta: Identidad → Métodos de autenticación → Windows Hello for Business  
   - Enabled: On  
   - Target: All users  

4. **Creación del usuario nativo del tenant**  
   UPN: `test@lanuzalorenzooutlook.onmicrosoft.com`  
   Tipo: Member  
   Motivo: las cuentas EXT no soportan passwordless.

5. **Registro de métodos passwordless**  
   Flujo seguido en https://mysignins.microsoft.com/security-info  
   - Registro de MFA  
   - Activación de passwordless en Authenticator  
   - Registro opcional de Windows Hello  
   - Registro opcional de llave FIDO2  

🔍 **Validaciones realizadas**  
- Usuario nativo detectado correctamente por Entra ID  
- Passwordless disponible en el flujo de inicio de sesión  
- Authenticator funcionando en modo passwordless  
- Windows Hello y FIDO2 disponibles para registro  

⚠️ **Problemas encontrados**  
- El usuario original era EXT → no soporta passwordless  
- La documentación oficial sigue mostrando rutas antiguas  

🛠 **Soluciones aplicadas**  
- Creación de usuario Member nativo  
- Documentación de rutas reales en la UI moderna  
- Validación del flujo completo con métodos passwordless  

🔐 **Implicaciones de seguridad**  
Passwordless reduce exposición a ataques de fuerza bruta y phishing.  
FIDO2 y Hello eliminan dependencia de contraseñas y mejoran postura de seguridad del tenant.
