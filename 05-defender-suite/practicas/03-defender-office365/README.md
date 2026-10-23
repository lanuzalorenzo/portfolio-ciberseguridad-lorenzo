# 03 | Defender for Office 365

> **Estado:** Diseño. La configuración de políticas y su validación están descritas, pero no hay registro de que se ejecutaran.
>
> **Referencias:** MCSB AM-1 · AM-2 · IR-2.

El correo sigue siendo la entrada más barata: no hace falta una vulnerabilidad, basta con que alguien abra un archivo o pulse un enlace. Y el usuario que lo abre no está haciendo nada malo; está haciendo su trabajo.

Defender for Office 365 añade dos filtros que hacen cosas distintas. Safe Links reescribe la dirección y la comprueba en el momento del clic, cuando ya se sabe si el dominio cambió de dueño. Safe Attachments abre el archivo en una máquina aislada y observa qué intenta hacer antes de entregarlo.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Enlace bloqueado | Enviar una URL de prueba entre dos buzones del laboratorio y seguir el clic | Un tenant con dos buzones y la política aplicada |
| Adjunto detonado | Enviar un archivo de prueba y revisar la detonación y su alerta | La política de adjuntos en modo bloqueo |
| Alerta correlacionada | Comprobar que el evento aparece en el explorador de amenazas | Retención y permisos de lectura sobre el tenant |

No hay tenant de correo, así que ninguna se ha ejecutado.

## Lecciones

- Los dos filtros no son intercambiables. Uno actúa sobre el enlace, el otro sobre el archivo, y un ataque puede usar solo uno.
- El modo auditoría sirve para medir, no para proteger. Se queda en pruebas y se documenta la fecha en que se cambió.
- El correo es el vector más barato del laboratorio: no requiere exploits, requiere una víctima y una excusa.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
