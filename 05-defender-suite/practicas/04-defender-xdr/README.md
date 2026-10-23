# 04 | Defender XDR

> **Estado:** Diseño. El análisis de incidentes correlacionados está descrito, pero no hay registro de que se ejecutara.
>
> **Referencias:** MCSB IR-1 · IR-2 · IR-3.

Cuatro alertas en cuatro paneles distintos no cuentan un ataque; cuentan cuatro problemas. El analista que las lee por separado cierra tres como ruido y persigue la cuarta, que era la consecuencia de las otras tres.

Defender XDR no detecta nada nuevo: recoge lo que ya emitieron identidad, equipo, correo y aplicaciones y lo agrupa en un incidente con entidades y cronología. Su valor no está en la detección, está en el orden.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Incidente único | Provocar dos señales del mismo origen y comprobar que caen en un solo caso | Al menos dos productos emitiendo señales |
| Cronología legible | Revisar el orden de las entidades y los eventos del incidente | Retención suficiente en los productos de origen |
| Respuesta reversible | Aislar un equipo de laboratorio desde el incidente y deshacerlo | Permisos de respuesta y un equipo que no sea crítico |

Sin 01, 02 y 03 no hay señales que correlacionar: ninguna se ha ejecutado.

## Lecciones

- XDR no inventa señales. Si los productos de origen no están encendidos, el panel está limpio porque no mira, no porque no pase nada.
- Un incidente con cuatro alertas y dos entidades vale más que cuarenta alertas sueltas: el trabajo del analista es descartar, y agrupar es la mitad de ese trabajo.
- La respuesta se prueba con una acción reversible, como aislar un equipo. Una acción que borra o bloquea cuentas se prueba cuando ya hay un procedimiento acordado.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
