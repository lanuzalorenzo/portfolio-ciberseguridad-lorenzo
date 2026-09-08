# 🔐 Informe técnico — Configuración de SSPR en Microsoft Entra ID

🧾 **Contexto**  
Laboratorio de identidad en Microsoft Entra ID.  
Se requiere habilitar Self-Service Password Reset (SSPR) y validar el flujo completo de recuperación de contraseña para un usuario de pruebas.

🎯 **Objetivo**  
Configurar SSPR, habilitar métodos de recuperación y verificar que un usuario puede restablecer su contraseña sin intervención del administrador.

🛠 **Trabajo realizado**

1. **Habilitación de SSPR en el tenant**  
   Ruta: Identidad → Métodos de autenticación → Self-Service Password Reset  
   - Enabled: Selected  
   - Target: All users (laboratorio)

2. **Configuración de métodos de recuperación**  
   Métodos habilitados:  
   - Email alternativo  
   - Teléfono móvil  
   - Microsoft Authenticator (si ya está registrado)

3. **Asignación del usuario de pruebas**  
   Usuario: `test@lanuzalorenzooutlook.onmicrosoft.com`  
   Motivo: usuario nativo compatible con MFA, SSPR y Passwordless.

4. **Validación del flujo SSPR**  
   Ruta: https://aka.ms/sspr  
   Flujo seguido:  
   - Introducción del UPN  
   - Selección del método de verificación  
   - Recepción del código  
   - Restablecimiento de contraseña  
   Resultado: contraseña restablecida correctamente.

🔍 **Validaciones realizadas**  
- SSPR habilitado en el tenant  
- Usuario con métodos de recuperación configurados  
- Flujo de restablecimiento funcional  
- Contraseña actualizada y autenticación posterior validada

⚠️ **Problemas encontrados**  
- Algunos métodos no aparecen si el usuario no los registró previamente  
- La UI moderna oculta rutas antiguas documentadas en guías previas

🛠 **Soluciones aplicadas**  
- Registro previo de métodos en My Sign-Ins  
- Documentación de rutas reales en la interfaz moderna  
- Validación del flujo completo con usuario nativo

🔐 **Implicaciones de seguridad**  
SSPR reduce la carga del administrador y mejora la resiliencia del tenant.  
Permite recuperación segura sin intervención manual y evita bloqueos operativos.
