# 02 | Defender for Endpoint

> **Estado:** Diseño. El onboarding y la validación de telemetría están descritos, pero no hay registro de que se ejecutaran.
>
> **Referencias:** MCSB EP-1 · EP-2 · IR-2.

Un equipo sin agente es una caja opaca: se sabe que está encendido, no qué ejecutó, qué abrió ni con quién habló. Cuando llega una alerta de ransomware, la pregunta ya no es cómo entrar, es qué hizo durante las seis horas anteriores.

Defender for Endpoint recoge procesos, conexiones y archivos, y los guarda el tiempo suficiente para reconstruir una sesión. Sirve para dos cosas distintas: detectar mientras ocurre y explicar después lo que ocurrió.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Dispositivo incorporado | Aplicar el paquete de onboarding y comprobar que aparece en el portal | Un equipo Windows o Linux y una licencia P2 |
| Telemetría en el tiempo | Revisar el historial de procesos del equipo y su retención | El dispositivo activo durante varios días |
| Detección de una muestra | Ejecutar EICAR en un equipo aislado y seguir la alerta | El paquete vigente y una política que no la excluya |

Falta la licencia, así que ninguna se ha ejecutado.

## Lecciones

- El onboarding es un paquete, no una instalación manual. Si el paquete caduca, el equipo sigue funcionando y deja de enviar, y eso no se nota hasta que hace falta el dato.
- La retención es parte del control. Un EDR que guarda treinta días no sirve para investigar un incidente que se descubrió al mes.
- EICAR demuestra que el archivo llega y se registra; la detección de comportamiento se prueba con técnicas, no con muestras.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
