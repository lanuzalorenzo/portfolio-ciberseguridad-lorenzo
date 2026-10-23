# Evidencia — 11 Hacking ético de APIs / BOLA, BFLA y mass assignment

> **Identificador:** `2026-10-21-11-api-bola`
>
> **Resultado:** Validado en local
>
> **Runbook:** [01 — BOLA/BFLA: aislamiento de pedidos](../../../11-hacking-etico-api/practicas/01-bola-bfla/runbook.md)
>
> **Práctica relacionada:** [03 — Rate limiting y mass assignment](../../../11-hacking-etico-api/practicas/03-rate-limiting-mass-assignment/README.md)

> Se comprobó que un usuario no puede abrir el pedido de otro cambiando el número de la dirección. Lo hicieron las pruebas automáticas, con dos usuarios falsos y ningún dato real, en el propio portátil.

## 1. Contexto

- **Fecha de ejecución:** 2026-10-21.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** equipo local con Ubuntu 26.04.1 LTS, kernel 7.0.0-38 y .NET SDK 10.0.113; `lab-api-local-azure` en el commit `b66028a`.
- **Alcance:** ejecutar la suite de integración de `EcommerceApi` contra `WebApplicationFactory`, con dos identidades de test, y verificar aislamiento de pedidos, control de funciones y validación de entrada.
- **Datos:** sintéticos, generados por las propias pruebas en un almacén en memoria.
- **Autorización:** [alcance y autorización del módulo 11](../../../11-hacking-etico-api/docs/alcance-y-autorizacion.md). Laboratorio propio, sin recursos cloud, sin coste y sin datos reales.
- **Identidades:** `X-Test-User` con valores aleatorios por prueba (`owner-*`, `other-*`, `list-owner-*`). No se usan cuentas ni tokens de Entra ID.

## 2. Comandos ejecutados

El detalle está en [comandos.md](comandos.md). Resumen:

```bash
cd ~/Repositorios/lab-api-local-azure
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --nologo
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --no-build --nologo \
  --logger "console;verbosity=normal"
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --no-build --nologo \
  --filter "FullyQualifiedName~OrdersEndpointsTests" \
  --logger "console;verbosity=normal"
grep -rn "Authorize\|Roles\|Admin" EcommerceApi/Controllers/
```

**Salida observada (resumen):**

```text
Correctas! - Con error: 0, Superado: 10, Omitido: 0, Total: 10, Duración: 782 ms
Pruebas totales: 10
Pruebas totales: 4   # filtro OrdersEndpointsTests
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Suite completa | 10 superadas, 0 con error | 10 superadas, 0 con error | PASS |
| Lectura de pedido ajeno (BOLA) | B recibe `404` sobre el pedido de A | `UserCannotReadAnotherUsersOrder` superada | PASS |
| Listado de pedidos ajenos | B solo ve sus pedidos | `CreateOrder_ReturnsOnlyOwnOrders`: A ve 1, B ve 0 | PASS |
| Lectura del pedido propio | A recibe `200` | Aserción `OK` en la misma prueba | PASS |
| BFLA | Sin endpoints administrativos ni políticas de rol | Solo `[Authorize]`; `POST /api/products` sin rol (H-03) | Parcial |
| Control de autenticación | Productos sin token devuelve `401` | `GetProducts_WithoutToken_ReturnsUnauthorized` superada | PASS |
| Mass assignment | El `id` enviado por el cliente se ignora | `CreateProduct_IgnoresClientSuppliedId` superada | PASS |
| Validación de entrada | Lista vacía, producto inexistente, precio negativo y nombre vacío devuelven `400` | Las cuatro pruebas superadas | PASS |

### Pruebas ejecutadas

| Prueba | Clase | Resultado |
|---|---|---|
| `Health_IsAnonymous_ReturnsHealthy` | `HealthEndpointTests` | PASS |
| `GetProducts_WithoutToken_ReturnsUnauthorized` | `ProductsEndpointsTests` | PASS |
| `GetProducts_WithAuthenticatedUser_ReturnsOk` | `ProductsEndpointsTests` | PASS |
| `CreateProduct_IgnoresClientSuppliedId` | `ProductsEndpointsTests` | PASS |
| `CreateProduct_WithEmptyName_ReturnsBadRequest` | `ProductsEndpointsTests` | PASS |
| `CreateProduct_WithNegativePrice_ReturnsBadRequest` | `ProductsEndpointsTests` | PASS |
| `UserCannotReadAnotherUsersOrder` | `OrdersEndpointsTests` | PASS |
| `CreateOrder_ReturnsOnlyOwnOrders` | `OrdersEndpointsTests` | PASS |
| `CreateOrder_WithEmptyProductList_ReturnsBadRequest` | `OrdersEndpointsTests` | PASS |
| `CreateOrder_WithUnknownProduct_ReturnsBadRequest` | `OrdersEndpointsTests` | PASS |

## 4. Artefactos

- [`artefactos/dotnet-test.txt`](artefactos/dotnet-test.txt): ejecución completa de la suite con el resumen final.
- [`artefactos/dotnet-test-detalle.txt`](artefactos/dotnet-test-detalle.txt): listado prueba a prueba y trazas del host de test.
- [`artefactos/dotnet-test-orders.txt`](artefactos/dotnet-test-orders.txt): ejecución filtrada a `OrdersEndpointsTests` (4 pruebas).
- [`artefactos/entorno.txt`](artefactos/entorno.txt): versión del SDK, sistema operativo, kernel y commit del workload.

No se incluyen tokens, cabeceras de autorización, identificadores reales ni capturas.

## 5. Limpieza

- **Recursos creados:** ninguno. Los pedidos y productos viven en el almacén en memoria del proceso de test.
- **Recursos eliminados:** no aplica; el proceso termina y libera el almacén.
- **Verificación:** las pruebas no escriben ficheros ni crean cuentas; no hay contenedores ni recursos cloud.

## 6. Coste

- **Estimado:** 0 €.
- **Real:** 0 €.
- **Notas:** ejecución local, sin Azure ni servicios de pago.

## 7. Conclusiones

La API aplica autorización a nivel de objeto: el propietario lee su pedido (`200`) y otro usuario recibe `404`, sin filtrar la existencia del recurso. El listado se filtra por el `UserId` del claim y el `id` enviado por el cliente no se acepta en la creación de productos. No existen endpoints administrativos, pero `POST /api/products` tampoco exige rol: BFLA se declara **parcial**, no mitigado (H-03).

La suite completa (10 pruebas) pasa también en el mismo commit, por lo que los cambios de autorización y validación no rompen salud, productos ni autenticación.

## 8. Limitaciones

- El esquema `X-Test-User` sustituye a Entra ID: no se validan firma, emisor, audiencia ni expiración del token.
- No se ha probado contra APIM, WAF ni un despliegue con dos usuarios delegados reales.
- BFLA se limita a la ausencia de endpoints administrativos; no hay matriz de roles.
- `POST /api/products` solo exige autenticación: cualquier usuario válido puede alterar el catálogo. Se declara en H-03.
- Rate limiting y consumo de recursos siguen pendientes de prueba manual.
- El resultado depende del commit `b66028a`; cambios posteriores requieren repetir el runbook.

## 9. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas.
- [x] Sin identificadores reales ni datos personales (rutas sustituidas por `~`).
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
