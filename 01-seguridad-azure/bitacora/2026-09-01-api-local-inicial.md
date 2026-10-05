# Bitácora — 2026-09-01: Setup de API Local (Migrado)

> [!NOTE]
> El código desarrollado durante esta jornada se encuentra ahora en el repositorio `lab-api-local-azure`. Mantengo esta entrada como registro histórico del proceso.

**Objetivo del día:** Levantar una API REST básica en .NET que sirva como campo de pruebas para las integraciones de identidad con Azure.

Hoy he comenzado preparando el entorno local. Lo primero fue verificar el SDK de .NET y levantar la plantilla base de una Web API. Mi intención es no complicarme con la lógica de negocio, así que he creado dos modelos muy sencillos: `Product` y `Order`.

A continuación, implementé un par de controladores (`ProductsController` y `OrdersController`) con métodos GET básicos. Por ahora, los endpoints responden en abierto. Comprobé con Swagger que las rutas levantan bien y devuelven el JSON esperado.

Mañana el objetivo será cerrar el acceso a estos endpoints exigiendo un token de Entra ID.
