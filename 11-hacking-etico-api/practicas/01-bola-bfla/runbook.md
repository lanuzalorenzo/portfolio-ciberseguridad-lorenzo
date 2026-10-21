# Runbook — BOLA/BFLA: aislamiento de pedidos

> **Estado:** Validado en local. Ejecutado el 2026-10-21 con la suite de integración de `lab-api-local-azure`.
>
> **Última revisión:** 2026-10-21.
>
> **Objetivo de la sesión:** comprobar que la API no devuelve pedidos de otro usuario y que un usuario estándar no alcanza funciones administrativas.

## 1. Objetivo

Validar el control de autorización a nivel de objeto (BOLA/IDOR) y de función (BFLA) en los endpoints de pedidos. Se considera éxito que:

- Un usuario B reciba `404` al solicitar un pedido de A.
- El listado de B no incluya pedidos de A.
- El propietario siga recibiendo `200` para su propio pedido.
- No existan endpoints administrativos accesibles sin política de rol.

## 2. Alcance

- **Incluido:** `GET /api/orders`, `GET /api/orders/{id}`, `POST /api/orders` y los endpoints de productos, ejecutados con `WebApplicationFactory`.
- **Excluido:** despliegue en Azure, APIM, WAF, contenedor, tokens reales de Entra ID y pruebas de carga.
- **Entorno:** local, sin recursos cloud.
- **Datos:** sintéticos, creados por cada prueba en el almacén en memoria y destruidos al terminar el proceso.

La autorización y los criterios de parada están en [`docs/alcance-y-autorizacion.md`](../../docs/alcance-y-autorizacion.md).

## 3. Prerrequisitos

| Requisito | Detalle | Verificación |
|---|---|---|
| .NET SDK | 10.0 o superior | `dotnet --version` |
| Repositorio | `lab-api-local-azure` clonado | `git -C lab-api-local-azure status --short` |
| Dependencias | Restauración de NuGet disponible | `dotnet restore tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj` |
| Red | No requiere conectividad saliente más allá de NuGet | — |
| Permisos | Usuario local; sin roles de Azure | — |
| Presupuesto | No aplica | — |

## 4. Variables

| Variable | Valor de ejemplo | Descripción |
|---|---|---|
| `API_REPO` | `~/Repositorios/lab-api-local-azure` | Ruta local del workload |
| `TEST_PROJECT` | `tests/EcommerceApi.Tests/EcommerceApi.Tests.csproj` | Proyecto de pruebas de integración |
| `TEST_USER_HEADER` | `X-Test-User` | Cabecera del esquema de autenticación de test |

Los valores son locales; no se usan identidades reales ni tokens.

## 5. Arquitectura del escenario

```text
Cliente de prueba A ──X-Test-User: owner-*──┐
                                           ├──> WebApplicationFactory ──> OrdersController ──> InMemoryStore
Cliente de prueba B ──X-Test-User: other-*──┘                                   │
                                                                                └── filtra por UserId del claim
```

- `TestAuthHandler` sustituye a Entra ID y emite los claims de identidad.
- `OrdersController` resuelve el propietario desde el claim y devuelve `404` cuando el pedido no pertenece al usuario.
- `Order.UserId` no se serializa (`[JsonIgnore]`), por lo que el cliente no puede fijar el propietario.

## 6. Ejecución

### Paso 1 — Restaurar dependencias

```bash
cd "$API_REPO"
dotnet restore "$TEST_PROJECT"
```

**Resultado esperado:** restauración correcta de `EcommerceApi` y `EcommerceApi.Tests`.

**Si falla:** comprobar la versión del SDK y el acceso a NuGet.

### Paso 2 — Ejecutar las pruebas de pedidos

```bash
dotnet test "$TEST_PROJECT" --nologo \
  --filter "FullyQualifiedName~OrdersEndpointsTests" \
  --logger "console;verbosity=normal"
```

**Resultado esperado:** 4 pruebas superadas, 0 con error.

### Paso 3 — Ejecutar la suite completa como regresión

```bash
dotnet test "$TEST_PROJECT" --nologo --logger "console;verbosity=normal"
```

**Resultado esperado:** 10 pruebas superadas, 0 con error.

### Paso 4 — Revisar la superficie administrativa

```bash
grep -rn "Authorize\|Roles\|Admin" EcommerceApi/Controllers/
```

**Resultado esperado:** los controladores exigen autenticación y no exponen endpoints administrativos ni políticas de rol que probar.

## 7. Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Lectura de pedido ajeno | A crea un pedido; B solicita el mismo `id` | `404` | PASS — `UserCannotReadAnotherUsersOrder` |
| Listado de pedidos ajenos | B lista `/api/orders` | Solo pedidos de B | PASS — `CreateOrder_ReturnsOnlyOwnOrders` |
| Lectura del pedido propio | A solicita su pedido | `200` | PASS — misma prueba, aserción `OK` |
| Pedido inexistente | A solicita un `id` no creado | `404` | No ejecutado: no hay prueba específica |
| BFLA | Revisión de controladores | Sin endpoints admin expuestos | PASS — no existen endpoints ni políticas de rol |
| Control de autenticación | `GET /api/products` sin token | `401` | PASS — `GetProducts_WithoutToken_ReturnsUnauthorized` |

## 8. Evidencia

- [x] Salida de comandos redactada.
- [x] Listado de pruebas con nombre y resultado.
- [x] Fecha y entorno.
- [x] Resultado y limitaciones.
- [x] Enlace a la entrada del índice.

Evidencia registrada: [`2026-10-21-11-api-bola`](../../../docs/laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md).

## 9. Limpieza

Las pruebas no crean ficheros, cuentas ni recursos: los pedidos y productos viven en el almacén en memoria y desaparecen al terminar el proceso. No hay contenedores ni recursos cloud que retirar.

**Verificación:** `git -C "$API_REPO" status --short` no muestra artefactos nuevos; `docker ps` no lista contenedores del laboratorio.

## 10. Coste y tiempo

- **Coste estimado:** 0 €.
- **Coste real:** 0 €.
- **Tiempo estimado:** 10 minutos.
- **Tiempo real:** menos de 1 minuto de ejecución; la sesión completa, unos 15 minutos.

## 11. Limitaciones

- El esquema `X-Test-User` sustituye a Entra ID; no se validan firma, emisor, audiencia ni vida útil del token.
- BFLA se limita a confirmar que no existen endpoints administrativos; no hay una matriz de roles que probar.
- No se ha ejecutado contra APIM, WAF ni un entorno con dos usuarios delegados.
- La prueba no cubre rate limiting ni consumo de recursos.

## 12. Referencias

- [README de la práctica](README.md)
- [Alcance y autorización del laboratorio](../../docs/alcance-y-autorizacion.md)
- [OWASP API Security Top 10 (2023) — API1 BOLA y API5 BFLA](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)
