# 05 | Defender for APIs

> **Estado:** Diseño. La API no está publicada en API Management y Defender for APIs no se ha activado.
>
> **Referencias:** OWASP API Security Top 10: API1, API2, API4, API5, API9.

Una API que devuelve el pedido de otro cliente cuando cambias un número no ha sido hackeada: se ha usado tal como está escrita. BOLA no necesita herramientas ni exploits, solo una sesión válida y ganas de probar identificadores.

Defender for APIs mira el tráfico que pasa por API Management y busca patrones de abuso: una cuenta que recorre cientos de recursos, peticiones que crecen sin control o llamadas que nadie usa. No corrige la autorización: la hace visible.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Inventario de operaciones | Publicar la API y revisar lo que Defender descubre y clasifica | Una instancia de API Management y el OpenAPI de la API |
| Enumeración de pedidos | Pedir identificadores consecutivos con una cuenta de prueba | Datos sintéticos y el plan de Defender for APIs |
| Límite de consumo | Superar la cuota y comprobar el `429` con su registro | Una política de cuota en API Management |
| Correlación | Buscar la alerta en Log Analytics y Sentinel | Diagnóstico y un workspace |

La API existe en local y no en API Management: ninguna se ha ejecutado.

## Lecciones

- Defender for APIs ve el tráfico de API Management; la API local, por vulnerable que sea, no entra.
- BOLA no se detecta por firma sino por patrón: muchos recursos desde la misma cuenta en poco tiempo.
- El `429` es evidencia: demuestra que el límite existe aunque Defender esté apagado.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
- [API de referencia](https://github.com/lanuzalorenzo/lab-api-local-azure)
