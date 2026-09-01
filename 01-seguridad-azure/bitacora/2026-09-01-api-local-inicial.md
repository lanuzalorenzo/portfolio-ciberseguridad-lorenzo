# Bitácora del Bloque: API Local Inicial

**Fecha**: 2026-09-01  
**Proyecto**: Portfolio Ciberseguridad - Lorenzo  
**Bloque**: 01-seguridad-azure / API Local (.NET 10)  
**Estado**: ✅ COMPLETADO

---

## Objetivo del Bloque

Crear una **API REST básica en .NET 10** que funcione como base para el proyecto de ciberseguridad. La API proporcionará funcionalidades de gestión de productos y pedidos, con el objetivo de ser integrada posteriormente con **Azure Active Directory (Azure AD)** para autenticación y autorización empresarial.

---

## Acciones Realizadas

### 1. Instalación de .NET 10 SDK
- **Acción**: Descarga e instalación de .NET 10 SDK
- **Verificación**: `dotnet --version` → .NET 10.0
- **Fecha**: 2026-09-01
- **Estado**: ✅ Completado

### 2. Creación del Proyecto Base
- **Comando**: `dotnet new webapi -n EcommerceApi`
- **Ubicación**: `/01-seguridad-azure/api-local/EcommerceApi/`
- **Tecnología**: ASP.NET Core Web API
- **Framework**: .NET 10
- **Fecha**: 2026-09-01
- **Estado**: ✅ Completado

### 3. Generación de Modelos
- **Archivo**: `Models/Product.cs`
  - Propiedades: `Id`, `Name`, `Price`, `Stock`
  - Namespace: `EcommerceApi.Models`
  
- **Archivo**: `Models/Order.cs`
  - Propiedades: `Id`, `ProductIds`, `TotalAmount`, `OrderDate`
  - Namespace: `EcommerceApi.Models`

- **Estado**: ✅ Completado

### 4. Creación de Controladores
- **Archivo**: `Controllers/ProductsController.cs`
  - Endpoints:
    - `GET /api/products` - Obtener todos
    - `GET /api/products/{id}` - Obtener por ID
    - `POST /api/products` - Crear nuevo
  - Storage: Lista en memoria
  - Namespace: `EcommerceApi.Controllers`

- **Archivo**: `Controllers/OrdersController.cs`
  - Endpoints:
    - `GET /api/orders` - Obtener todos
    - `GET /api/orders/{id}` - Obtener por ID
    - `POST /api/orders` - Crear nuevo
  - Storage: Lista en memoria
  - Namespace: `EcommerceApi.Controllers`

- **Estado**: ✅ Completado

### 5. Configuración de Swagger y CORS
- **Archivo**: `Program.cs`
  - Servicios: Controllers, Swagger/OpenAPI
  - Middleware: CORS (permitir localhost)
  - Documentación automática de endpoints
  - URL Swagger: `http://localhost:5000/swagger`
  
- **Estado**: ✅ Completado

### 6. Configuración de appsettings
- **Archivo**: `appsettings.json`
  - Logging configuration
  - Configuración base de la aplicación
  
- **Archivo**: `appsettings.Development.json`
  - Logging en modo Development
  - Configuración específica del entorno
  
- **Estado**: ✅ Completado

### 7. Generación de Documentación Auxiliar

#### 7.1 README.md
- Descripción completa del proyecto
- Guía de instalación y ejecución
- Documentación de endpoints
- Estructura del proyecto
- Notas de seguridad
- Próximos pasos

#### 7.2 .gitignore
- Patrones para carpetas (`bin/`, `obj/`, `.vs/`)
- Patrones para archivos de IDE
- Archivos de configuración sensibles
- Estándar profesional para .NET

#### 7.3 tests.md
- Ejemplos con curl para productos
- Ejemplos con curl para pedidos
- Alternativas con PowerShell
- Instrucciones para Postman
- Códigos HTTP esperados

#### 7.4 azure-ad-notes.md
- Conceptos fundamentales de Azure AD
- Explicación de App Registration
- Definición de Client ID, Scopes, JWT
- Flujo de autenticación OAuth 2.0
- Cambios necesarios en Program.cs
- Implementación de middleware
- Fases de implementación

- **Fecha**: 2026-09-01
- **Estado**: ✅ Completado

### 8. Commits de Git
Se recomienda realizar los siguientes commits:

```bash
# Commit 1: Estructura base
git add .
git commit -m "feat: Crear estructura base de EcommerceApi en .NET 10"

# Commit 2: Modelos
git add Models/
git commit -m "feat: Agregar modelos Product y Order"

# Commit 3: Controladores
git add Controllers/
git commit -m "feat: Implementar controladores de Productos y Pedidos"

# Commit 4: Configuración
git add Program.cs appsettings*.json
git commit -m "feat: Configurar Swagger, CORS y logging"

# Commit 5: Documentación
git add *.md .gitignore
git commit -m "docs: Agregar documentación y guías de prueba"
```

---

## Estructura Actual del Proyecto

```
EcommerceApi/
├── Models/
│   ├── Product.cs                    # Modelo de Producto
│   └── Order.cs                      # Modelo de Pedido
├── Controllers/
│   ├── ProductsController.cs         # Controlador de Productos
│   └── OrdersController.cs           # Controlador de Pedidos
├── Properties/
│   └── launchSettings.json           # Configuración de ejecución
├── bin/                              # Compilados (excluido en .gitignore)
├── obj/                              # Objetos (excluido en .gitignore)
├── Program.cs                        # Punto de entrada y configuración
├── EcommerceApi.csproj              # Archivo del proyecto
├── EcommerceApi.http                # Archivo de pruebas HTTP
├── appsettings.json                 # Configuración (Producción)
├── appsettings.Development.json     # Configuración (Desarrollo)
├── .gitignore                        # Archivo Git ignore
├── README.md                         # Documentación principal
├── tests.md                          # Guía de pruebas
└── azure-ad-notes.md                 # Notas sobre Azure AD
```

---

## Estado Actual de la API

### ✅ Implementado
- [x] Estructura de proyecto .NET 10
- [x] Modelos de datos (Product, Order)
- [x] Controladores REST (CRUD básico)
- [x] Endpoints funcionales
- [x] Swagger/OpenAPI integrado
- [x] CORS configurado
- [x] Almacenamiento en memoria
- [x] Logging configurado
- [x] Documentación completa
- [x] .gitignore profesional

### ⏳ Pendiente (Próximas Fases)
- [ ] Autenticación con Azure AD
- [ ] Validación de JWT tokens
- [ ] Control de acceso basado en roles (RBAC)
- [ ] Base de datos persistente
- [ ] Validación avanzada de datos
- [ ] Implementación de logs centralizados
- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentación de seguridad
- [ ] Deployment a Azure App Service

---

## Próximos Pasos

### Fase 2: Autenticación con Azure AD (Próxima)
1. Crear App Registration en Azure Portal
2. Obtener Client ID y Tenant ID
3. Instalar NuGet package: `Microsoft.Identity.Web`
4. Configurar `appsettings.json` con credenciales de Azure AD
5. Modificar `Program.cs` para validar tokens JWT
6. Decorar controladores con `[Authorize]`
7. Implementar control de roles

### Fase 3: Persistencia de Datos
1. Crear contexto de base de datos (Entity Framework Core)
2. Configurar conexión a SQL Server o PostgreSQL
3. Crear migraciones
4. Implementar repositorios
5. Reemplazar almacenamiento en memoria

### Fase 4: Testing y Documentación
1. Escribir unit tests
2. Crear integration tests
3. Documentar API completa
4. Crear guías de desarrollo
5. Implementar CI/CD

### Fase 5: Seguridad y Deployment
1. Implementar HTTPS obligatorio
2. Configurar rate limiting
3. Agregar logging de seguridad
4. Implementar refresh tokens
5. Usar Azure Key Vault para secretos
6. Desplegar a Azure App Service

---

## Cómo Usar Este Bloque

### Para Desarrolladores
1. Clonar/descargar el proyecto
2. Asegurarse de tener .NET 10 instalado
3. Ejecutar: `dotnet run`
4. Acceder a Swagger: `http://localhost:5000/swagger`
5. Consultar [tests.md](./tests.md) para ejemplos de prueba

### Para Revisión de Código
1. Revisar namespaces correctos en Models y Controllers
2. Verificar que no hay dependencias externas innecesarias
3. Comprobar que el almacenamiento es en memoria
4. Validar que la API responde en `http://localhost:5000`

### Para Siguiente Fase
1. Leer [azure-ad-notes.md](./azure-ad-notes.md) para entender Azure AD
2. Crear App Registration en Azure Portal
3. Comenzar con la configuración de autenticación

---

## Checklist de Finalización

- [x] Estructura de proyecto creada
- [x] Modelos implementados
- [x] Controladores implementados
- [x] Endpoints funcionales
- [x] Swagger configurado
- [x] CORS habilitado
- [x] Logging configurado
- [x] README.md completado
- [x] .gitignore profesional
- [x] tests.md con ejemplos
- [x] azure-ad-notes.md preparada
- [x] Documentación en bitácora
- [x] Código limpio y sin dependencias externas
- [x] Compatible con .NET 10
- [x] Namespaces correctos

---

## Notas Importantes

### Seguridad Actual
⚠️ **La API actualmente NO tiene autenticación**. Es apta solo para desarrollo local.

### Para Producción
- Implementar Azure AD es **OBLIGATORIO**
- Usar HTTPS en todas las comunicaciones
- Implementar validación de entrada
- Usar base de datos segura
- Implementar rate limiting

### Almacenamiento
Actualmente usa listas en memoria que se pierden al reiniciar. Esto es intencional para esta fase.

---

## Recursos Útiles

- [Documentación de .NET 10](https://learn.microsoft.com/en-us/dotnet/)
- [ASP.NET Core Web API](https://learn.microsoft.com/en-us/aspnet/core/web-api/)
- [Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/)
- [JWT.io](https://jwt.io/) - Decodificar tokens
- [Swagger/OpenAPI](https://swagger.io/)

---

## Cambios Recientes

| Fecha | Cambio | Estado |
|-------|--------|--------|
| 2026-09-01 | Creación de estructura base | ✅ |
| 2026-09-01 | Implementación de modelos | ✅ |
| 2026-09-01 | Implementación de controladores | ✅ |
| 2026-09-01 | Configuración de Swagger | ✅ |
| 2026-09-01 | Documentación completa | ✅ |

---

## Responsables

- **Desarrollador**: Lorenzo
- **Proyecto**: Portfolio Ciberseguridad
- **Organización**: Personal

---

**Bloque API Local: CERRADO** ✅

Próxima fase: Integración con Azure AD (2026-09-02)
