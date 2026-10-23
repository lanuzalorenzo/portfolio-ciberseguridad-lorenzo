# Comandos ejecutados — 11 API / BOLA y mass assignment

> Evidencia: `2026-10-21-11-api-bola`
>
> Fecha: 2026-10-21.
>
> Rutas locales sustituidas por `~`. Sin tokens, cabeceras de autorización ni identificadores reales.

## 1. Entorno

```bash
dotnet --version          # 10.0.113
. /etc/os-release && echo "$PRETTY_NAME"   # Ubuntu 26.04.1 LTS
uname -r                  # 7.0.0-38-generic
git -C ~/Repositorios/lab-api-local-azure rev-parse --short HEAD   # b66028a
```

## 2. Suite completa (restauración implícita)

```bash
cd ~/Repositorios/lab-api-local-azure
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --nologo
```

Salida (resumen; completa en [`artefactos/dotnet-test.txt`](artefactos/dotnet-test.txt)):

```text
Correctas! - Con error:     0, Superado:    10, Omitido:     0, Total:    10, Duración: 782 ms - EcommerceApi.Tests.dll (net10.0)
```

## 3. Detalle prueba a prueba

```bash
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --no-build --nologo \
  --logger "console;verbosity=normal"
```

Salida (completa en [`artefactos/dotnet-test-detalle.txt`](artefactos/dotnet-test-detalle.txt)):

```text
Correctas EcommerceApi.Tests.HealthEndpointTests.Health_IsAnonymous_ReturnsHealthy [292 ms]
Correctas EcommerceApi.Tests.ProductsEndpointsTests.GetProducts_WithoutToken_ReturnsUnauthorized [292 ms]
Correctas EcommerceApi.Tests.ProductsEndpointsTests.CreateProduct_IgnoresClientSuppliedId [47 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_ReturnsOnlyOwnOrders [363 ms]
Correctas EcommerceApi.Tests.ProductsEndpointsTests.CreateProduct_WithEmptyName_ReturnsBadRequest [19 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_WithEmptyProductList_ReturnsBadRequest [7 ms]
Correctas EcommerceApi.Tests.ProductsEndpointsTests.CreateProduct_WithNegativePrice_ReturnsBadRequest [3 ms]
Correctas EcommerceApi.Tests.ProductsEndpointsTests.GetProducts_WithAuthenticatedUser_ReturnsOk [4 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.UserCannotReadAnotherUsersOrder [8 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_WithUnknownProduct_ReturnsBadRequest [8 ms]
Pruebas totales: 10
```

## 4. Filtro de la práctica BOLA/BFLA

```bash
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --no-build --nologo \
  --filter "FullyQualifiedName~OrdersEndpointsTests" \
  --logger "console;verbosity=normal"
```

Salida (completa en [`artefactos/dotnet-test-orders.txt`](artefactos/dotnet-test-orders.txt)):

```text
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_ReturnsOnlyOwnOrders [356 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_WithEmptyProductList_ReturnsBadRequest [20 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.UserCannotReadAnotherUsersOrder [9 ms]
Correctas EcommerceApi.Tests.OrdersEndpointsTests.CreateOrder_WithUnknownProduct_ReturnsBadRequest [5 ms]
Pruebas totales: 4
```

## 5. Revisión de superficie administrativa

```bash
grep -rn "Authorize\|Roles\|Admin" EcommerceApi/Controllers/
```

Salida:

```text
EcommerceApi/Controllers/OrdersController.cs:12:[Authorize]
EcommerceApi/Controllers/ProductsController.cs:10:[Authorize]
```

No hay atributos de rol ni controladores administrativos.

## 6. Observación del host de test

La ejecución emite el aviso esperado de configuración de Entra ID:

```text
warn: EcommerceApi[0]
      AzureAd is using placeholder values. Configure a real tenant before validating tokens. See docs/azure-ad-config.md.
```

Es coherente con el alcance: la autenticación se sustituye por `TestAuthHandler` y no se validan tokens reales. No se registra ningún valor de configuración.
