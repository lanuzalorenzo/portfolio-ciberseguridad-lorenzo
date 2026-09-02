# EcommerceApi (.NET 10)

## Descripción del proyecto

**EcommerceApi** es una API REST desarrollada en **.NET 10** para demostrar un caso real de integración de autenticación empresarial con **Microsoft Entra ID / Azure AD**. La API gestiona productos y pedidos en memoria y está protegida con **JWT Bearer** para validar tokens emitidos por Azure AD.

El objetivo del proyecto dentro del portfolio es evidenciar una implementación práctica de:
- autenticación con Azure AD,
- validación de tokens JWT,
- protección de endpoints con `Authorize`,
- seguridad aplicada en APIs modernas.

## Requisitos

- **.NET 10 SDK** instalado
  - Descarga desde: https://dotnet.microsoft.com/download
- acceso a un tenant Azure AD / Microsoft Entra ID configurado para pruebas

## Cómo ejecutar la API

1. Navega a la carpeta del proyecto:
   ```bash
   cd 01-seguridad-azure/api-local/EcommerceApi
   ```

2. Restaura dependencias:
   ```bash
   dotnet restore
   ```

3. Ejecuta la API:
   ```bash
   dotnet run
   ```

4. La API estará disponible en:
   - **Swagger UI**: `http://localhost:5177/swagger`
   - **URL base**: `http://localhost:5177`

## Endpoints disponibles

### Productos

- **GET** `/api/products` - Obtener todos los productos
- **GET** `/api/products/{id}` - Obtener un producto por ID
- **POST** `/api/products` - Crear un nuevo producto
  - Body: `{ "name": "string", "price": number, "stock": number }`

### Pedidos

- **GET** `/api/orders` - Obtener todos los pedidos
- **GET** `/api/orders/{id}` - Obtener un pedido por ID
- **POST** `/api/orders` - Crear un nuevo pedido
  - Body: `{ "productIds": [number, ...] }`

> Los endpoints están protegidos con autenticación y requieren un token JWT válido emitido por Azure AD.

## Estructura del proyecto

```
EcommerceApi/
├── Models/
│   ├── Product.cs
│   └── Order.cs
├── Controllers/
│   ├── ProductsController.cs
│   └── OrdersController.cs
├── Program.cs
├── appsettings.json
├── EcommerceApi.csproj
├── README.md
├── azure-ad-config.md
├── azure-ad-register.md
├── azure-ad-tests.md
├── AZURE-AD-TESTS.md
├── azure-ad-notes.md
├── tests.md
└── .gitignore
```

## Estado actual de seguridad

✅ **La API ya está protegida con Azure AD mediante JWT Bearer**.

Esto incluye:
- autenticación con `AddAuthentication("Bearer")`,
- validación del issuer y del audience,
- uso de `UseAuthentication()` y `UseAuthorization()`,
- protección de controladores con `[Authorize]`.

## Documentación asociada

- [azure-ad-register.md](./azure-ad-register.md) - registro de la aplicación en Azure AD
- [azure-ad-config.md](./azure-ad-config.md) - configuración del tenant y audiencia
- [AZURE-AD-TESTS.md](./AZURE-AD-TESTS.md) - pruebas con tokens y llamadas a la API
- [azure-ad-notes.md](./azure-ad-notes.md) - notas técnicas del flujo de autenticación
- [tests.md](./tests.md) - ejemplos de pruebas con curl

## Siguientes pasos

1. **Autorización granular**: scopes y roles por endpoint
2. **Persistencia**: sustituir almacenamiento en memoria por base de datos
3. **Observabilidad**: logging centralizado y trazabilidad
4. **Seguridad adicional**: validación más estricta y hardening del entorno

## Para desarrolladores y reclutadores

El proyecto demuestra una API moderna con identidad empresarial integrada, un diseño orientado a seguridad y documentación técnica clara, útil tanto para revisión técnica como para presentación profesional en un portfolio público.

---

**Última actualización**: 2026-09-02
