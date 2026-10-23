# 11 | Defender for DevOps

> **Estado:** Parcial. El repositorio existe y el conector es gratuito, pero los hallazgos requieren Defender CSPM, que no está activo.
>
> **Referencias:** MCSB DS-1 · IM-1 · PV-2.

El mismo fallo cuesta un commit en el repositorio y un incidente en el portal. La diferencia no es la gravedad: es el momento en que se descubre, y ese momento lo decide dónde está el control.

Defender for DevOps conecta repositorios y pipelines para revisar plantillas de infraestructura, secretos y dependencias antes de que lleguen a producción. Ve los repositorios que se le dan; el resto sigue invisible.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Repositorio conectado | Autorizar el conector sobre un repositorio de laboratorio | Defender CSPM activo y permisos sobre el repositorio |
| Fallo de IaC | Introducir una plantilla Bicep con un puerto abierto | El análisis de IaC habilitado |
| Secreto expuesto | Añadir una credencial falsa y comprobar que se marca | El escaneo de secretos y el historial del repo |
| Trazabilidad | Abrir el hallazgo y ver el commit que lo introdujo | El conector con acceso al historial |

Solo existe el repositorio: el conector no se ha probado y, sin CSPM, los hallazgos no aparecen.

## Lecciones

- El escaneo de IaC demuestra la diferencia de tiempo: el mismo puerto abierto es un comentario en el pull request o un incidente en producción.
- Un secreto en el historial sigue siendo un secreto filtrado aunque se borre la línea. Rotarlo es la única corrección real.
- El conector ve los repositorios que le das. La sensación de cobertura total es el error más común al activarlo.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
