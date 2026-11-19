# 06 | Gobierno de dependencias y versiones de plataforma

> **Estado:** Validado (2026-11-19). La comprobación y el bloqueo están probados: `check-platform` corre dentro del job que exige el ruleset de cuatro repositorios y los cuatro están en verde el mismo día: [lab-api](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/44550540902), [shared-dotnet](https://github.com/lanuzalorenzo/shared-dotnet/actions/runs/44549614615), [plantillas](https://github.com/lanuzalorenzo/plantillas-dotnet/actions/runs/44550651106) y [comicteca](https://github.com/lanuzalorenzo/comicteca/actions/runs/44549263514). La migración a .NET 12 queda en **Diseño**: escrita y sin ejecutar.
>
> **Referencias:** NIST SSDF PW.4 · CIS 16.

Un escáner dice si un paquete arrastra un CVE (la ficha pública de una vulnerabilidad); no dice qué versión de plataforma usa el proyecto ni qué hacer cuando aparece una mayor. Como los neumáticos y el coche: lo primero se revisa a diario, lo segundo no se improvisa un viernes. Sin esa decisión, una actualización automática deja el servicio sin arrancar.

**In English.** A scanner tells whether a package carries a CVE; it does not say which platform version the project uses or what to do when a major appears. Like tyres and the car: the first is checked daily, the second is not improvised on a Friday. Without that decision, an automatic update leaves the service unable to start.

## Qué se aplicó

| Control | Cómo |
|---|---|
| Versión única | El `TargetFramework` declara la plataforma; `global.json`, versiones, imágenes y CI la siguen |
| Familia atada | ASP.NET Core, Extensions, EF Core, SQLite y `Pkcs`, en el mayor del destino; `check-platform` lo comprueba |
| Mayores | Dependabot los bloquea; parche y menor van con auto-merge (fusión automática) y siete días de enfriamiento |
| Transitivas | Pin en el centro con motivo y fecha; directa solo si el código usa el tipo |

## Validación

| Prueba | Resultado observado |
|---|---|
| Plataforma mezclada | Código 1 con paquete, imagen, `global.json` y `dotnet-version` señalados |
| Cuatro consumidores | Job exigido por el ruleset y en verde el 19/11; en `shared-dotnet` el check es un job propio, en los otros tres un paso del job requerido |
| Mayores que no entran | Cuatro PRs de .NET 11 sobre `net10.0` y una de Swashbuckle 11, cerradas con motivo; Swashbuckle rompe el restore con `NU1107` |

## Lecciones

- El mayor de un paquete de plataforma no es una actualización: es una migración.
- La puerta va en el CI: once pull requests en una semana no se revisan, se cierran.
- Un rechazo con motivo también es gobierno.

## Más detalle

- [Módulo 07](../../README.md)
- [ADR-0001](https://github.com/lanuzalorenzo/core/blob/main/docs/adr/0001-plataforma-y-dependencias.md) y [procedimiento](https://github.com/lanuzalorenzo/core/blob/main/docs/versiones-y-dependencias.md)
- [Acción `check-platform` en `v1.8`](https://github.com/lanuzalorenzo/core/blob/v1.8/actions/check-platform/action.yml)
- [Primer consumidor](https://github.com/lanuzalorenzo/lab-api-local-azure/pull/80) y [la aplicación principal](https://github.com/lanuzalorenzo/comicteca/pull/34)
