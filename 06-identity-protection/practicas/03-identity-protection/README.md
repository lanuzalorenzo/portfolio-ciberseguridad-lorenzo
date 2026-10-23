# 03 | Identity Protection y revisiones de acceso

> **Estado:** **Diseño**. Señales y políticas descritas; no configuradas ni observadas: exigen licencia P2 y una actividad que el tenant de pruebas no genera.
>
> **Referencias:** MCSB IA-1, IR-2, GS-2.

El riesgo de una cuenta no es una etiqueta fija: cambia con cada inicio de sesión. Identity Protection lo puntúa —credenciales filtradas, IP anónima, viaje imposible, dispositivo desconocido— y deja que la política decida si pide un segundo factor, obliga a cambiar la contraseña o bloquea. Las revisiones de acceso cubren el otro extremo: comprobar cada cierto tiempo que quien conserva un rol o una pertenencia lo sigue necesitando.

## Qué se diseñó

| Señal o revisión | Qué mide | Respuesta |
|---|---|---|
| Riesgo de usuario | Credenciales filtradas | Cambio de contraseña y MFA |
| Riesgo de sesión | IP anónima, viaje imposible | MFA o bloqueo |
| Revisión de roles | Necesidad del privilegio | Retirar si no se confirma |
| Revisión de invitados | Cuentas externas activas | Caducidad si nadie las valida |

## Lo que falta

P2, historial de inicio de sesión suficiente y alguien que revise. Un tenant vacío no genera riesgo: las señales necesitan cuentas que se comporten como lo harían las reales, y un laboratorio sin usuarios no produce eso.

## Lecciones

- El riesgo se calcula con señales; sin actividad, no hay nada que calcular.
- Una revisión de acceso sin retirada efectiva es teatro.
- Las cuentas de invitado caducan mejor de lo que se revisan.

## Más detalle

- [Módulo 06](../../README.md)
- [PIM en el módulo 02](../../../02-identity-security/practicas/04-pim/README.md)
