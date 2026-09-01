# EcommerceApi (.NET 10)

## Descripción del Proyecto

**EcommerceApi** es una API REST desarrollada en **.NET 10** que proporciona funcionalidades básicas de un sistema de comercio electrónico. La API gestiona productos y pedidos, almacenando datos en memoria (sin base de datos externa).

Este proyecto es parte del portfolio de ciberseguridad y está diseñado para ser integrado con **Azure Active Directory (Azure AD)** para autenticación y autorización empresarial.

## Requisitos

- **.NET 10 SDK** instalado
  - Descarga desde: https://dotnet.microsoft.com/download

## Cómo Ejecutar la API

1. Navega a la carpeta del proyecto:
   ```bash
   cd EcommerceApi
   ```

2. Restaura las dependencias (si las hay):
   ```bash
   dotnet restore
   ```

3. Ejecuta la API:
   ```bash
   dotnet run
   ```

4. La API estará disponible en:
   - **URL base**: `http://localhost:5000` o `https://localhost:5001`
   - **Swagger UI**: `http://localhost:5000/swagger`

## Endpoints Disponibles

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

## Estructura del Proyecto

```
EcommerceApi/
├── Models/
│   ├── Product.cs         # Modelo de Producto
│   └── Order.cs           # Modelo de Pedido
├── Controllers/
│   ├── ProductsController.cs  # Controlador de Productos
│   └── OrdersController.cs    # Controlador de Pedidos
├── Program.cs             # Configuración de la aplicación
├── appsettings.json       # Configuración
├── EcommerceApi.csproj    # Archivo del proyecto
├── .gitignore            # Archivos a ignorar en Git
├── README.md             # Este archivo
└── tests.md              # Ejemplos de pruebas con curl
```

## Notas sobre Seguridad

⚠️ **Estado Actual**: Esta API está en desarrollo sin autenticación implementada.

🔒 **Próximos Pasos**:
- Integración con **Azure Active Directory (Azure AD)**
- Validación de **JWT tokens**
- Control de acceso basado en roles (**RBAC**)
- Cifrado de datos sensibles
- HTTPS obligatorio

Consulta [azure-ad-notes.md](./azure-ad-notes.md) para más detalles sobre la integración con Azure AD.

## Próximos Pasos

1. **Autenticación Azure AD**: Integrar con Microsoft Entra ID (Azure AD)
2. **Base de datos**: Migrar de almacenamiento en memoria a una base de datos persistente
3. **Logging**: Implementar logging centralizado
4. **Validación**: Añadir validaciones más robustas en modelos
5. **Testing**: Crear unit tests y integration tests

## Para Desarrolladores

Para más información sobre las pruebas de los endpoints, consulta [tests.md](./tests.md).

Para detalles sobre la preparación para Azure AD, consulta [azure-ad-notes.md](./azure-ad-notes.md).

---

**Última actualización**: 2024
