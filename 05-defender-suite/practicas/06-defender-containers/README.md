# 06 | Defender for Containers

> **Estado:** Diseño. No hay clúster de Kubernetes ni registro de imágenes en el laboratorio, así que no hay nada que proteger todavía.
>
> **Referencias:** MCSB DS-1 · IR-2 · PV-3 · CIS Kubernetes Benchmark.

Una imagen con una librería vulnerable no es un incidente hasta que se ejecuta con red y credenciales. Para entonces el fallo ya está en producción y el Dockerfile que lo introdujo lleva semanas sin tocarse.

Defender for Containers cubre tres momentos que se confunden con facilidad: la imagen antes de desplegarse, el clúster antes de admitirla y el contenedor mientras corre. Son controles distintos y se compran juntos.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Escaneo de imagen | Subir la imagen de la API y revisar sus recomendaciones | Un registro de imágenes y el plan de contenedores |
| Control de admisión | Intentar desplegar una imagen con vulnerabilidades críticas | Un clúster con la política de admisión activa |
| Detección en runtime | Ejecutar un proceso anómalo dentro de un pod de laboratorio | El agente desplegado en el clúster |
| Auditoría del API server | Revisar los eventos de Kubernetes | Registro de auditoría habilitado |

No hay clúster ni registro, así que ninguna se ha ejecutado.

## Lecciones

- Escaneo y runtime son dos planes de la misma pieza. Uno mira lo que la imagen contiene; el otro, lo que hace cuando corre.
- Un Dockerfile no es un clúster. Sin registro ni orquestador no hay superficie que Defender pueda vigilar.
- El control de admisión es lo único que impide que una imagen vulnerable llegue a ejecutarse. El escaneo avisa; la admisión decide.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
