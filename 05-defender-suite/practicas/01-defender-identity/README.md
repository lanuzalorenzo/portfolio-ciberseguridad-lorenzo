# 01 | Defender for Identity

> **Estado:** Diseño. La instalación del sensor y la validación de alertas están descritas, pero no hay registro de que se ejecutaran.
>
> **Referencias:** MCSB IA-1 · IA-2 · IR-2.

Una cuenta con privilegios que empieza a enumerar el dominio no dispara ninguna alarma: el inicio de sesión es correcto. El ataque ocurre dentro de la sesión legítima, y los eventos que lo delatarían llevan años sin que nadie los lea.

Defender for Identity pone un sensor en el controlador de dominio que lee esos eventos. Un Kerberoasting suelto no dice nada; el reconocimiento que lo precede, sí.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Sensor operativo | Instalar el paquete y revisar estado del servicio y última conexión | Un controlador de dominio de laboratorio y la clave de acceso del tenant |
| Telemetría real | Comprobar en el portal el volumen de eventos procesados | Auditoría de AD habilitada en el dominio |
| Detección de técnica conocida | Kerberoasting controlado con una cuenta de servicio del laboratorio | Sensor sano y una licencia que cubra identidad |

No hay dominio en el laboratorio, así que ninguna se ha ejecutado.

## Lecciones

- El sensor no ve el dominio, ve el tráfico que el dominio ya genera. Si la auditoría avanzada está apagada, la mitad de la señal no existe aunque el sensor esté sano.
- Lo que se detecta es la secuencia. Una alerta aislada de identidad se puede explicar; tres en el mismo orden y sobre la misma cuenta, no.
- La licencia va antes que la configuración: sin Defender for Identity no hay nada que instalar, y es la razón por la que esta práctica sigue en diseño.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
