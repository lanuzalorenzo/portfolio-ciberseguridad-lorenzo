# 06 | Acceso privilegiado bajo licencia

> **Estado:** **Diseño**. Los tres controles descritos aquí no se pueden configurar en el tenant de laboratorio por falta de licencia P1 o P2. No hay ejecución ni evidencia, y la página no los presenta como si la hubiera.

El módulo 02 hace lo que un tenant gratuito permite: segundo factor con Security Defaults, contraseña fuera de la ecuación, recuperación autónoma, roles elegibles y un modelo de mínimo privilegio. Seis de esos siete controles están ejecutados y validados; el séptimo, la elegibilidad en PIM, quedó en **Parcial** porque la elevación efectiva exige licencia P2. Lo que queda detrás del muro de pago es otra cosa: políticas que deciden según el contexto, elevación con aprobación y caducidad, y riesgo de identidad calculado por Microsoft. Sin licencia P1 o P2 no se pueden ni configurar.

Este módulo existe para separar las dos capas. Mezclar lo probado con lo que no se puede probar es la forma más rápida de que un lector deje de saber qué creer.

## Los tres controles

| Control | Qué añade sobre el módulo 02 | Qué exige |
|---|---|---|
| Conditional Access | Condición y decisión por política —quién, desde dónde, con qué equipo, con qué riesgo— en lugar de un segundo factor para todos | P1, usuarios de prueba y una cuenta de emergencia excluida |
| PIM con aprobación y caducidad | Otra persona autoriza la elevación, dura una o dos horas y se revisa cada periodo | P2, una segunda persona que apruebe y otra que revise |
| Identity Protection y revisiones | Riesgo puntuado por señal —credenciales filtradas, IP anónima, viaje imposible— y retirada de lo que ya no se necesita | P2 e historial de inicio de sesión suficiente |

Cada control tenía su página con la configuración detallada. Se retiraron: sin ejecución no hay nada que comprobar en ellas, y lo que el módulo sostiene cabe en esta página.

## Por qué no se ejecutó

El tenant de laboratorio no tiene licencia P1 ni P2. Probar Conditional Access exige además usuarios de prueba y una cuenta de emergencia excluida de todas las políticas, porque un administrador que se bloquea a sí mismo se queda fuera del tenant. Medir riesgo de identidad requiere un historial que un tenant vacío no genera. Se podría hacer con una prueba de P2 de treinta días y un tenant desechable; no se hizo, y el estado lo dice.

## Lo que ya está probado

El segundo factor, la elegibilidad en PIM y el modelo de roles se ejecutaron en el módulo 02, con sus tablas de resultados y sus límites escritos: [MFA](../02-identity-security/practicas/01-mfa/README.md), [PIM](../02-identity-security/practicas/04-pim/README.md) y [RBAC](../02-identity-security/practicas/05-rbac/README.md). Aquí no se repiten.

Este módulo no tiene bitácora. La entrada que había contaba la decisión de crearlo, y eso cabe en las dos primeras frases de esta página.
