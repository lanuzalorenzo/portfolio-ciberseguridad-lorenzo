# 10 | Defender App Governance

> **Estado:** Diseño. No hay licencia de App Governance ni aplicaciones OAuth de laboratorio que revisar.
>
> **Referencias:** MCSB AM-2 · IA-3 · IR-2.

Una aplicación de terceros con permiso para leer todo el correo de la organización no es un usuario: es una llave maestra que nadie revisa. Se concedió en dos clics, funciona sin contraseña y sobrevive al empleado que la aprobó.

App Governance mira las aplicaciones conectadas a Microsoft 365: qué permisos tienen, quién los concedió y cómo se comportan. El riesgo no suele estar en la aplicación, está en el permiso que arrastra.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Inventario de aplicaciones | Revisar las apps con permisos de Graph y quién las consintió | Defender for Cloud Apps con el complemento |
| Permiso excesivo | Buscar una app con acceso de lectura a todo el correo | Una app registrada y un consentimiento de administrador |
| Comportamiento anómalo | Generar actividad fuera de su patrón habitual | La app en uso y unos días de línea base |
| Respuesta | Revocar el permiso desde el panel y comprobar el efecto | Permisos de administrador y una app no crítica |

Falta la licencia y no hay apps que auditar: ninguna se ha ejecutado.

## Lecciones

- El riesgo no es la aplicación, es el permiso. Una app útil con `Mail.Read` en toda la organización es un buzón compartido con todos.
- La gobernanza empieza por el inventario. Sin la lista de aplicaciones consentidas no hay política que aplicar.
- Un consentimiento de administrador concedido para una demo no caduca solo. Se revisa o se revoca, y casi nunca se hace lo segundo.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
