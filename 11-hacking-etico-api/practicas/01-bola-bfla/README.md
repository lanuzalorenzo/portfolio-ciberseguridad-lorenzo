# 01 | BOLA/BFLA: aislamiento de pedidos

Una API autenticada que devuelve pedidos por identificador puede estar diciendo «tienes sesión» sin decir «este pedido es tuyo». La prueba consiste en crear un pedido con un usuario y pedirlo con otro. Si responde `200`, hay BOLA; si responde `404`, el control de propiedad funciona.

**Referencias:** OWASP API1 · MCSB PA-7

| Prueba | Resultado observado |
|---|---|
| A crea un pedido; B pide el mismo ID | PASS: `UserCannotReadAnotherUsersOrder` (`404`) |
| B lista sus pedidos | PASS: solo ve los suyos (`CreateOrder_ReturnsOnlyOwnOrders`) |
| A pide su propio pedido | PASS: `200` |
| ID inexistente | No ejecutado: sin prueba específica |
| BFLA | Parcial: no hay endpoints admin, pero `POST /api/products` no exige rol (H-03) |

La remediación fue asignar `Order.UserId` desde el claim, marcarlo `[JsonIgnore]`, filtrar el listado y devolver `404` cuando el pedido no pertenece al usuario.

Las pruebas usan el esquema `X-Test-User` y dos identidades falsas, no tokens de Entra ID; tampoco se han ejecutado contra APIM o WAF. El [runbook](runbook.md) y la [evidencia](../../../laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md) recogen los pasos y la salida.

Si B recibiera el pedido de A, el fallo estaría en la consulta y no en el token: la identidad se validó y aun así el recurso se entregó. Esa distinción importa al buscar la causa.

Un `403` ya revela que el recurso existe; el `404` evita esa fuga. Y el listado también necesita el filtro: proteger solo el detalle deja abierto el índice de pedidos.
