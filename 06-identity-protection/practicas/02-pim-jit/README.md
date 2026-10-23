# 02 | PIM con aprobación y caducidad

> **Estado:** **Diseño**. El flujo se apoya en la elegibilidad ya probada en el módulo 02; la elevación real exige licencia P2 y no se ejecutó.
>
> **Referencias:** MCSB PA-1, PA-2, PA-3.

En el módulo 02 un rol quedó *Eligible* y el asistente pedía motivo y segundo factor, pero la elevación no llegó a completarse: sin P2 no hay activación. Este es el escalón siguiente, el que añade la licencia. No basta con que el privilegio exista solo cuando se pide; además, otra persona lo autoriza, dura un máximo y alguien comprueba cada cierto tiempo que la elegibilidad sigue teniendo sentido.

## Qué añade cada pieza

| Pieza | Qué cambia | Sin ella |
|---|---|---|
| Aprobación | Otra persona autoriza la activación | El privilegio depende de quien lo pide |
| Duración máxima | Una o dos horas, renovables con motivo | La sesión elevada dura todo el día |
| MFA en la activación | Segundo factor en el momento de elevar | Se verifica al entrar, no al elevar |
| Revisiones de acceso | Alguien confirma cada periodo que el rol sigue haciendo falta | La elegibilidad se vuelve permanente |
| Cuentas de emergencia | Dos cuentas fuera de PIM, monitorizadas | Un error de configuración deja el tenant sin administrador |

## Lo que falta

P2, una segunda persona que apruebe y otra que revise. Con un solo administrador, la aprobación es un clic y la revisión, un formulario.

## Lecciones

- Una elegibilidad que nadie revisa es una puerta abierta con mejor cerradura.
- La aprobación sin criterio se vuelve rutina en dos semanas.
- Las cuentas de emergencia se prueban; guardarlas no demuestra que funcionen.

## Más detalle

- [Módulo 06](../../README.md)
- [Elegibilidad y límites del módulo 02](../../../02-identity-security/practicas/04-pim/README.md)
