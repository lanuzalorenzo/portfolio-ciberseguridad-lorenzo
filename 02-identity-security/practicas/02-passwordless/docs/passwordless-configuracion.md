# Informe técnico — Configuración de Passwordless en Microsoft Entra ID
# Informe técnico — Configuración y Validación de Passwordless en Microsoft Entra ID

**Contexto**
Laboratorio de identidad en Microsoft Entra ID.
Se requiere habilitar métodos passwordless y validar su funcionamiento con un usuario nativo del tenant.
**Módulo:** 02 — Identity Security  
**Práctica:** 02 — Passwordless Authentication

**Objetivo**
Configurar Microsoft Authenticator passwordless, Passkey (FIDO2) y Windows Hello for Business.
Crear un usuario nativo del tenant y verificar el flujo completo de autenticación sin contraseña.
## Contexto y Alcance
Las contraseñas tradicionales representan el eslabón más débil de la cadena de identidad: son susceptibles a ataques de phishing inverso, intermediarios (Adversary-in-the-Middle o AitM), fatiga de alertas y reutilización entre plataformas.

**Trabajo realizado**
Esta práctica aborda la habilitación y validación de mecanismos de autenticación sin contraseña (*Passwordless*) en Microsoft Entra ID, evaluando tres tecnologías complementarias: Microsoft Authenticator en modo sin contraseña, llaves de seguridad FIDO2 (Passkeys) y Windows Hello for Business.

1. **Habilitación de Microsoft Authenticator (passwordless)**
   Ruta: Identidad → Métodos de autenticación → Microsoft Authenticator
   - Enabled: On
   - Passwordless: Enabled
   - Target: All users
## Decisiones Técnicas y Procedimiento de Configuración

2. **Habilitación de Passkey (FIDO2)**
   Ruta: Identidad → Métodos de autenticación → Passkey (FIDO2)
   - Enabled: On
   - Allow self-service: Yes
   - Enforce attestation: No
### 1. Habilitación de Directivas de Métodos de Autenticación
Desde *Microsoft Entra admin center* (*Protección* → *Métodos de autenticación* → *Directivas*), se configuraron los siguientes métodos:

3. **Habilitación de Windows Hello for Business**
   Ruta: Identidad → Métodos de autenticación → Windows Hello for Business
   - Enabled: On
   - Target: All users
1. **Microsoft Authenticator:**
   - **Estado:** Habilitado para todos los usuarios de prueba.
   - **Modo:** *Cualquiera* (permite tanto notificaciones push estándar como flujo sin contraseña).
   - **Ajustes avanzados:** Se impuso la coincidencia de números (*Number Matching*) y contexto de aplicación/ubicación para neutralizar ataques de fatiga de MFA.
2. **Passkey / Llave de seguridad FIDO2:**
   - **Estado:** Habilitado.
   - **Autoservicio:** Permitido para registro autónomo de los usuarios.
   - **Atestación:** Deshabilitada en el laboratorio para permitir pruebas con llaves y emuladores sin restricciones de proveedor específico.
3. **Windows Hello for Business:**
   - **Estado:** Habilitado a nivel de directiva como método de factor biométrico y PIN respaldado por chip TPM.

4. **Creación del usuario nativo del tenant**
   Identidad: cuenta de laboratorio (identificador omitido)
   Tipo: Member
   Motivo: las cuentas EXT no soportan passwordless.
### 2. Gestión de Identidades: Cuentas Externas (Guest) vs. Cuentas Nativas (Member)
Durante el laboratorio se identificó una limitación fundamental de diseño en Entra ID:
- Las cuentas de tipo invitado (*Guest / #EXT#*) delegan la emisión de credenciales en su IdP de origen, por lo que **no soportan el registro de credenciales Passwordless nativas** en el tenant hospedador.
- **Acción técnica:** Se aprovisionó un usuario de prueba nativo (*Member*) perteneciente al dominio `onmicrosoft.com`, habilitando sin fricción el registro en el portal *My Sign-Ins*.

5. **Registro de métodos passwordless**
   Flujo seguido en https://mysignins.microsoft.com/security-info
   - Registro de MFA
   - Activación de passwordless en Authenticator
   - Registro opcional de Windows Hello
   - Registro opcional de llave FIDO2
### 3. Registro y Flujo de Verificación
1. El usuario accede a `https://mysignins.microsoft.com/security-info`.
2. Se completa la configuración de Microsoft Authenticator activando el inicio de sesión telefónico sin contraseña.
3. Se vincula la llave de seguridad FIDO2 / Passkey mediante reto WebAuthn.

**Validaciones realizadas**
- Usuario nativo detectado correctamente por Entra ID
- Passwordless disponible en el flujo de inicio de sesión
- Authenticator funcionando en modo passwordless
- Windows Hello y FIDO2 disponibles para registro
## Validaciones y Pruebas Realizadas

**Problemas encontrados**
- El usuario original era EXT → no soporta passwordless
- La documentación oficial sigue mostrando rutas antiguas
| Escenario Evaluado | Método de Comprobación | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Intento de registro passwordless con cuenta EXT | Acceso con usuario Guest a *Security Info* | Opción de inicio de sesión sin contraseña no disponible | PASS: Bloqueo esperado por diseño arquitectónico |
| Login con Microsoft Authenticator Passwordless | Introducción de UPN en portal de login | El portal no solicita contraseña; muestra un número de 2 dígitos | PASS: Coincidencia de número completada y login autorizado |
| Resistencia frente a phishing (Passkey / FIDO2) | Reto criptográfico mediante WebAuthn | La autenticación se enlaza criptográficamente al dominio del portal | PASS: Imposible de interceptar mediante proxys inversos AitM |

**Soluciones aplicadas**
- Creación de usuario Member nativo
- Documentación de rutas reales en la UI moderna
- Validación del flujo completo con métodos passwordless

**Implicaciones de seguridad**
Passwordless reduce exposición a ataques de fuerza bruta y phishing.
FIDO2 y Hello eliminan dependencia de contraseñas y mejoran postura de seguridad del tenant.
## Lecciones de Troubleshooting y Buenas Prácticas
- **Requisito de identidad nativa:** Toda estrategia de despliegue Passwordless en Entra ID debe planificarse exclusivamente para cuentas sincronizadas o nativas (*Member*), requiriendo acuerdos de confianza entre tenants para identidades B2B.
- **Eliminación del secreto en reposo:** Al basarse en criptografía de clave pública/privada (con la clave privada protegida en el enclave seguro del dispositivo o llave de hardware), no existe ningún hash ni secreto estático en los servidores susceptible de ser filtrado.
