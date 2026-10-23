# 08 | Defender EASM

> **Estado:** Diseño. No hay un dominio público propio que verificar, así que EASM no tiene superficie que descubrir.
>
> **Referencias:** MCSB GS-1 · PV-1 · RM-1.

Un subdominio que alguien levantó para una demo en 2023 y nadie apagó sigue publicado, con un servidor sin parchear y un certificado válido. No está en el inventario porque el inventario lo mantiene alguien a mano.

Defender EASM mira desde fuera y descubre lo que ya es visible: dominios, subdominios, direcciones, servicios y tecnologías. No escanea la red ni ataca nada; recopila lo que Microsoft ya conoce y lo ordena por exposición.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Verificación del dominio | Demostrar la propiedad del dominio ante el servicio | Un dominio propio y acceso a su DNS |
| Descubrimiento de activos | Revisar dominios, subdominios y servicios encontrados | La licencia de EASM asociada al dominio |
| Exposición confirmada | Comprobar un servicio antiguo o un puerto abierto detectado | Un activo real que se pueda revisar sin tocarlo |
| Seguimiento | Marcar un activo y ver si vuelve a aparecer tras retirarlo | Tiempo entre dos descubrimientos |

No hay dominio público propio, así que ninguna se ha ejecutado.

## Lecciones

- EASM descubre lo que ya está publicado. Lo que nunca salió a Internet no aparece, y eso incluye lo que crees que tienes apagado.
- La verificación del dominio es el límite del producto: sin ella ves lo que Microsoft ya conoce, no lo que es tuyo.
- Un subdominio olvidado vale más para un atacante que un fallo en el dominio principal: nadie lo vigila y todos confían en él.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
