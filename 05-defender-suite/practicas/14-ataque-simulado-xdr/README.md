# 14 | Simulación controlada y correlación en XDR

> **Estado:** Diseño. No se ha lanzado ninguna simulación; además depende de los productos 01–04, que tampoco están desplegados.
>
> **Referencias:** MCSB IR-1 · IR-2 · IR-3.

Lanzar un ataque contra el laboratorio sin alcance escrito no es una prueba: es un incidente con el nombre cambiado. La simulación necesita permiso, límites y una forma de pararla, y eso se escribe antes de empezar.

Con esas condiciones, la prueba es la más útil del módulo: un escenario simple que recorra identidad, equipo y correo, y comprobar si la suite lo cuenta como una historia o como cuatro alertas sueltas.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Escenario simple | Contraseña débil o adjunto de prueba, sin exploits | Un tenant de laboratorio y datos sintéticos |
| Detección por producto | Confirmar que cada pieza emite su alerta | 01, 02 y 03 activos |
| Incidente único | Revisar que XDR las agrupa con entidades y cronología | XDR con las señales conectadas |
| Respuesta y cierre | Aislar un equipo, documentar y deshacer | Permisos de respuesta y un equipo no crítico |

No hay resultados que presentar: ninguna se ha ejecutado.

## Lecciones

- Una simulación sin permiso y sin alcance escrito no es una prueba. El documento que la autoriza es parte del control.
- El valor está en el incidente único: si cada producto abre su propio caso, XDR no está correlacionando y el problema no es el ataque.
- Se empieza por la técnica más simple. El escenario complejo esconde los fallos de detección detrás del ruido que genera.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
