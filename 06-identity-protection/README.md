# 06 | Acceso privilegiado bajo licencia

> **Estado:** **Diseño**. Las tres prácticas describen controles que el tenant de laboratorio no puede configurar por falta de licencia P1 o P2. No hay ejecución ni evidencia, y el módulo no las presenta como si la hubiera.

El módulo 02 hace lo que un tenant gratuito permite: segundo factor con Security Defaults, contraseña fuera de la ecuación, recuperación autónoma, roles elegibles y un modelo de mínimo privilegio. Ese trabajo está ejecutado y validado. Lo que queda detrás del muro de pago es otra cosa: políticas que deciden según el contexto, elevación con aprobación y caducidad, y riesgo de identidad calculado por Microsoft. Sin licencia P1 o P2 no se pueden ni configurar.

Este módulo existe para separar las dos capas. Mezclar lo probado con lo que no se puede probar es la forma más rápida de que un lector deje de saber qué creer.

## Las tres prácticas

| # | Práctica | Qué añade | Estado |
|---|---|---|---|
| 01 | [Conditional Access](practicas/01-conditional-access/README.md) | Políticas por contexto, no un segundo factor para todos | **Diseño** |
| 02 | [PIM con aprobación y caducidad](practicas/02-pim-jit/README.md) | Elevación autorizada por otra persona y con límite de tiempo | **Diseño** |
| 03 | [Identity Protection y revisiones](practicas/03-identity-protection/README.md) | Riesgo calculado y permisos que se revisan | **Diseño** |

## Lo que ya está probado

El segundo factor, la elegibilidad en PIM y el modelo de roles se ejecutaron en el módulo 02, con sus tablas de resultados y sus límites escritos: [MFA](../02-identity-security/practicas/01-mfa/README.md), [PIM](../02-identity-security/practicas/04-pim/README.md) y [RBAC](../02-identity-security/practicas/05-rbac/README.md). Aquí no se repiten.

## Por qué no se ejecutó

El tenant de laboratorio no tiene licencia P1 ni P2. Probar Conditional Access exige además usuarios de prueba y una cuenta de emergencia excluida de todas las políticas, y medir riesgo de identidad requiere un historial que un tenant vacío no genera. Se podría hacer con una prueba de P2 de treinta días y un tenant desechable; no se hizo, y el estado lo dice.

Este módulo no tiene bitácora. La entrada que había contaba la decisión de crearlo, y eso cabe en las dos primeras frases de esta página.
