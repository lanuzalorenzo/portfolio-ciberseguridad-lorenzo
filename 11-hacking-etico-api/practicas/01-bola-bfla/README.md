# 01 | BOLA/BFLA: aislamiento de pedidos

> **Estado:** validado localmente con pruebas de integración. No se ha ejecutado contra un despliegue real con tokens de Entra ID.
>
> **Runbook:** [runbook.md](runbook.md).
>
> **Evidencia:** [2026-10-21-11-api-bola](../../../docs/laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md).

## Descripción del escenario y objetivo de seguridad

**Escenario:** Una API autenticada devuelve pedidos por identificador. Si no comprueba la propiedad del recurso, un usuario puede leer pedidos de otro cambiando el `{id}` (BOLA/IDOR). Si no separa funciones, puede acceder a operaciones administrativas (BFLA).  
**Objetivo de seguridad:** Garantizar que cada usuario solo accede a sus propios pedidos y que las funciones administrativas no están expuestas a usuarios estándar.  
**Alcance:** `GET /api/orders`, `GET /api/orders/{id}`, `POST /api/orders` y endpoints de productos.

## Hipótesis

1. Un usuario B puede leer un pedido creado por A si conoce el ID.
2. Un usuario B puede listar pedidos de A.
3. Un usuario estándar puede invocar funciones administrativas inexistentes o no protegidas.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **JwtBearer** | Identidad del llamante | Claims `NameIdentifier`/`oid`/`sub`. |
| **OrdersController** | Autorización de objeto | Filtra por `UserId`; devuelve `404` para recursos ajenos. |
| **InMemoryStore** | Repositorio | Pedidos con `UserId` no serializado. |
| **xUnit + WebApplicationFactory** | Pruebas | Esquema de test `X-Test-User` para dos identidades. |

## Pruebas ejecutadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Lectura de pedido ajeno | A crea pedido; B solicita el mismo ID | `404` | PASS: `UserCannotReadAnotherUsersOrder` |
| Listado de pedidos ajenos | B lista `/api/orders` | Solo pedidos de B | PASS: `CreateOrder_ReturnsOnlyOwnOrders` |
| Lectura del pedido propio | A solicita su pedido | `200` | PASS |
| Pedido inexistente | A solicita ID inexistente | `404` | No ejecutado: no existe una prueba específica |
| BFLA | Revisión de endpoints | Sin funciones admin expuestas | PASS: no existen endpoints admin; no hay políticas de rol |

Comando:

```bash
dotnet test tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj --filter "FullyQualifiedName~OrdersEndpointsTests"
```

## Remediación aplicada

- `Order.UserId` se asigna desde el claim de identidad y se marca `[JsonIgnore]`.
- `GetAllOrders` filtra por `UserId`.
- `GetOrderById` devuelve `404` si el pedido no pertenece al usuario.
- Se eliminó la lista de pedidos compartida sin control de propiedad.

## Limitaciones

- Las pruebas usan un esquema de autenticación de test, no tokens reales de Entra ID.
- BFLA se limita a confirmar que no hay endpoints administrativos; no hay una matriz de roles que probar.
- No se ha probado contra APIM, WAF ni un entorno con dos usuarios delegados.

## Recomendaciones

- Añadir políticas por scopes/roles y una prueba negativa para cada rol.
- Añadir auditoría de accesos denegados.
- Repetir la prueba contra el entorno desplegado antes de cerrar el hallazgo.

## Artefactos relacionados

- [Pruebas de pedidos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/tests/EcommerceApi.Tests/OrdersEndpointsTests.cs)
- [Controlador de pedidos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Controllers/OrdersController.cs)
- [Threat model de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/threat-model-appsec.md)
- [Evidencia de ejecución](../../../docs/laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md)
