# Registro de la API en Azure AD

## ¿Qué es Azure AD y App Registration?

**Azure Active Directory (Azure AD)** es el servicio de identidad en la nube de Microsoft que proporciona:
- Autenticación centralizada
- Gestión de identidades
- Control de acceso basado en roles (RBAC)

**App Registration** es el proceso de registrar tu aplicación en Azure AD para que pueda:
- Autenticar usuarios
- Autorizar aplicaciones cliente
- Emitir y validar tokens JWT

## Pasos para Registrar la API en Azure AD

### 1. Acceder al Portal de Azure
1. Ir a [portal.azure.com](https://portal.azure.com)
2. Iniciar sesión con tu cuenta de Azure
3. En el menú de búsqueda superior, escribir "Azure Active Directory" o "App registrations"

### 2. Crear un Nuevo Registro
1. Hacer clic en **"App registrations"** en el menú lateral
2. Hacer clic en **"New registration"**
3. Completar el formulario:
   - **Name**: `EcommerceApi` (nombre descriptivo de tu API)
   - **Supported account types**: Seleccionar según tu caso:
     - "Accounts in this organizational directory only" (recomendado para producción)
     - "Accounts in any organizational directory" (multi-tenant)
   - **Redirect URI**: Dejar vacío por ahora (las APIs no necesitan redirección)
4. Hacer clic en **"Register"**

### 3. Obtener Tenant ID, Client ID y Application ID URI

Después del registro, verás la página de **Overview** con:

#### **Tenant ID (Directory ID)**
- Se encuentra en el campo "Directory (tenant) ID"
- Ejemplo: `00000000-0000-0000-0000-000000000000`
- Uso: En la URL de autoridad de Azure AD

#### **Client ID (Application ID)**
- Se encuentra en el campo "Application (client) ID"
- Ejemplo: `11111111-1111-1111-1111-111111111111`
- Uso: Identificador único de tu aplicación

#### **Application ID URI**
1. En la página de registro, hacer clic en **"Expose an API"** en el menú lateral
2. En la sección "Application ID URI", hacer clic en **"Set"**
3. Azure sugiere un URI predeterminado: `api://[CLIENT-ID]`
4. Puedes personalizarlo a algo como: `api://ecommerce-api`
5. Hacer clic en **"Save"**

## Crear un Scope (API Permission)

### ¿Qué es un Scope?

Un **scope** define permisos específicos que las aplicaciones cliente pueden solicitar. Ejemplo:
- `api://ecommerce-api/order.read` - Leer órdenes
- `api://ecommerce-api/order.write` - Crear órdenes
- `api://ecommerce-api/admin` - Acceso administrativo

### Crear Scopes

1. En la página de registro, ir a **"Expose an API"**
2. En la sección "Scopes defined by this API", hacer clic en **"Add a scope"**
3. Completar el formulario:

**Para lectura de órdenes:**
- **Scope name**: `order.read`
- **Admin consent display name**: `Read orders`
- **Admin consent description**: `Allows reading orders from the API`
- **User consent display name**: `Read orders`
- **User consent description**: `Allows you to read orders`
- **State**: `Enabled`

**Para escritura de órdenes:**
- **Scope name**: `order.write`
- **Admin consent display name**: `Manage orders`
- **Admin consent description**: `Allows creating and updating orders`
- **User consent display name**: `Manage orders`
- **User consent description**: `Allows you to create and update orders`
- **State**: `Enabled`

4. Hacer clic en **"Add scope"**

Los scopes quedarán disponibles como:
- `api://ecommerce-api/order.read`
- `api://ecommerce-api/order.write`

## Asignar Roles o Permisos a Aplicaciones Cliente

### Para Aplicaciones Cliente (Confidential Clients)

Si tienes una aplicación cliente que necesita acceder a la API:

#### 1. Registrar la Aplicación Cliente
- Ir a **App registrations** > **New registration**
- Nombrarla: `EcommerceClient` (o similar)
- Registrar

#### 2. Asignar Permisos desde la Cliente
1. En el registro de la aplicación **cliente**, ir a **API permissions**
2. Hacer clic en **"Add a permission"**
3. En **"My APIs"**, seleccionar **"EcommerceApi"**
4. Seleccionar los scopes que necesita (ej: `order.read`, `order.write`)
5. Hacer clic en **"Add permissions"**

#### 3. Conceder Consentimiento (Admin Consent)
1. Si es necesario, hacer clic en **"Grant admin consent for [Tenant]"**
2. Confirmar la acción

#### 4. Crear un Client Secret
1. En el registro cliente, ir a **Certificates & secrets**
2. En **Client secrets**, hacer clic en **"New client secret"**
3. Agregar descripción y expiration (recomendado: 6 meses o 1 año)
4. Hacer clic en **"Add"**
5. **IMPORTANTE**: Copiar el valor del secret inmediatamente (solo se muestra una vez)
6. Guardar de forma segura (nunca en código, usar Key Vault o variables de entorno)

### Para Aplicaciones Frontend (Public Clients)

Si tienes una aplicación web o desktop:

1. En el registro del cliente, ir a **API permissions**
2. Agregar el permiso a la API de tu proyecto como se describió arriba
3. Asegurarse de que la aplicación cliente tenga **Redirect URIs** configuradas correctamente

## Notas de Seguridad

### ✅ Mejores Prácticas

1. **Rotación de Secrets**
   - Cambiar regularmente los client secrets (cada 6-12 meses)
   - No usar secrets con expiración "Never"

2. **Usar Managed Identity en Azure**
   - Si ejecutas en Azure (App Service, Container, VM), usar Managed Identity en lugar de secrets
   - Elimina la necesidad de almacenar credenciales

3. **Almacenar Credenciales Seguramente**
   - Nunca guardar Client ID o Secrets en código
   - Usar Azure Key Vault para producción
   - Usar variables de entorno para desarrollo

4. **Limitar Permisos**
   - Asignar solo los scopes necesarios a cada cliente
   - Seguir el principio de menor privilegio

5. **Monitoreo y Auditoría**
   - Revisar los logs de Azure AD regularmente
   - Monitorear intentos fallidos de autenticación
   - Habilitar alertas para cambios en permisos

6. **Validación de Tokens**
   - Validar la firma del token (clave pública de Azure AD)
   - Validar el issuer (debe ser Azure AD de tu tenant)
   - Validar la audiencia (debe ser tu Application ID URI)
   - Validar la expiración

7. **HTTPS Obligatorio**
   - La API siempre debe usar HTTPS en producción
   - Los tokens se transmiten en el header Authorization

8. **Tokens de Acceso vs Refresh**
   - Los tokens de acceso son de corta duración (1 hora típicamente)
   - Los refresh tokens permiten obtener nuevos tokens sin re-autenticar
   - Almacenar refresh tokens de forma segura

### ⚠️ Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `invalid_client` | Client ID incorrecto | Verificar Application ID en Azure Portal |
| `invalid_scope` | Scope no registrado | Asegurar que el scope existe en "Expose an API" |
| `unauthorized_client` | Client no tiene permiso | Agregar API permission desde cliente a API |
| `AADSTS50001` | Tenant no encontrado | Verificar el Tenant ID es correcto |
| `AADSTS70001` | Application no encontrada | Verificar Application ID URI está configurado |

### 🔒 Checklist de Seguridad

- [ ] Application ID URI configurado
- [ ] Scopes creados según necesidades
- [ ] Aplicación cliente registrada (si aplica)
- [ ] Permisos asignados a cliente
- [ ] Admin consent concedido (si aplica)
- [ ] Client Secret almacenado en lugar seguro
- [ ] HTTPS habilitado en todos los endpoints
- [ ] Tokens JWT validados completamente en la API
- [ ] Logs de autenticación monitoreados
- [ ] Plan de rotación de secrets establecido

