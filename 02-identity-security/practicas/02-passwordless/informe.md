# Informe técnico — Configuración y validación de Passwordless en Microsoft Entra ID

**Módulo:** 02 — Identity Security
**Práctica:** 02 — Passwordless Authentication
**Entorno:** tenant de laboratorio, sin datos reales.

## Contexto y alcance

Las contraseñas siguen siendo el eslabón más débil de la cadena de identidad: son vulnerables a phishing inverso, ataques de intermediario (AitM), fatiga de alertas y reutilización entre plataformas. Esta práctica habilita y valida mecanismos sin contraseña en un tenant de laboratorio con un usuario nativo.

## Objetivo

Configurar Microsoft Authenticator en modo passwordless, Passkey (FIDO2) y Windows Hello for Business, crear un usuario nativo y verificar el flujo completo sin contraseña.

## Configuración y decisiones

### 1. Microsoft Authenticator

- **Ruta:** *Identidad* → *Métodos de autenticación* → *Microsoft Authenticator*.
- **Estado:** habilitado para todos los usuarios de prueba.
- **Modo:** *Cualquiera* (notificaciones push y flujo sin contraseña).
- **Ajustes:** coincidencia de números (*Number Matching*) y contexto de aplicación/ubicación para neutralizar ataques de fatiga de MFA.

### 2. Passkey / llave de seguridad FIDO2

- **Estado:** habilitado.
- **Autoservicio:** permitido para el registro autónomo de usuarios.
- **Atestación:** deshabilitada en el laboratorio para permitir pruebas con llaves y emuladores sin restricciones de proveedor.

### 3. Windows Hello for Business

- **Estado:** habilitado a nivel de directiva como método biométrico y PIN respaldado por TPM.

### 4. Usuario nativo del tenant

Se identificó una limitación de diseño de Entra ID:

- Las cuentas de tipo invitado (*Guest / #EXT#*) delegan la emisión de credenciales en su IdP de origen y **no admiten el registro de credenciales passwordless nativas** en el tenant hospedador.
- **Acción:** se aprovisionó un usuario de prueba nativo (*Member*) del dominio `onmicrosoft.com` para poder registrar métodos en *My Sign-Ins*.

### 5. Registro de métodos

Flujo seguido en `https://mysignins.microsoft.com/security-info`:

1. Registro de MFA.
2. Activación de passwordless en Authenticator.
3. Registro opcional de Windows Hello.
4. Registro opcional de llave FIDO2 mediante reto WebAuthn.

## Validaciones y pruebas

| Escenario evaluado | Método | Comportamiento esperado | Resultado observado |
|---|---|---|---|
| Registro con cuenta EXT | Acceso de un usuario Guest a *Security Info* | La opción sin contraseña no está disponible | PASS: bloqueo esperado por diseño |
| Login con Authenticator passwordless | Introducción del UPN en el portal | No se solicita contraseña; se muestra un número de 2 dígitos | PASS: coincidencia completada y acceso autorizado |
| Resistencia al phishing (Passkey / FIDO2) | Reto criptográfico WebAuthn | La autenticación se enlaza al dominio del portal | PASS: no interceptable con proxies AitM |

## Problemas encontrados

- El usuario inicial era *EXT* y no soporta passwordless.
- La documentación oficial sigue mostrando rutas antiguas.

## Soluciones aplicadas

- Crear un usuario *Member* nativo.
- Documentar las rutas reales de la interfaz moderna.
- Validar el flujo completo con los métodos passwordless.

## Implicaciones de seguridad

Passwordless reduce la exposición a fuerza bruta y phishing. FIDO2 y Windows Hello eliminan la dependencia de contraseñas y mejoran la postura del tenant.

## Lecciones

- **Identidad nativa:** toda estrategia passwordless debe planificarse para cuentas sincronizadas o nativas (*Member*); las identidades B2B requieren acuerdos de confianza entre tenants.
- **Sin secreto en reposo:** al basarse en criptografía de clave pública/privada, con la clave privada protegida en el dispositivo o llave de hardware, no existe un hash estático en los servidores que pueda filtrarse.
