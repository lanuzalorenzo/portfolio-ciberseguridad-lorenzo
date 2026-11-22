# Agente autónomo contra la API

El 22/11 monté el banco para medir qué encuentra un agente con un modelo local cuando la API es vulnerable, no para descubrir los fallos: BOLA, escritura de producto sin rol y precio elegido por el cliente ya estaban documentados desde octubre. Fijé el commit anterior al arreglo de autorización, puse una red interna sin salida y ejecuté tres tandas con el mismo prompt ciego.

Salió desigual. Las tres leyeron el pedido de `user-b` en la segunda petición, entre 5 y 14 segundos. Solo una probó a crear un producto, y la API aceptó el precio que eligió. La tercera tanda se quedó repitiendo `GET /api/products/5` dieciocho veces después de inventarse un `403` que en realidad fue `200`; la segunda afirmó haber borrado un pedido que la API rechazó con `405`.

La lección no es que el modelo sea bueno o malo: es que su resumen no sirve como prueba. Lo que cuenta es la respuesta HTTP y la línea del log. El detalle está en la [evidencia](../../laboratorio-final/evidencias/2026-11-22-11-api-agente/README.md); la medición es local, con autenticación sustituida y un objetivo histórico, así que no describe el estado actual de `main`.
