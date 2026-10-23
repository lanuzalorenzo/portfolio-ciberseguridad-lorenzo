# 07 | Defender for Storage

> **Estado:** Diseño. No hay cuenta de almacenamiento con Defender for Storage habilitado.
>
> **Referencias:** MCSB DP-2 · DP-3 · IR-2 · NS-2.

El almacenamiento es donde un dato se queda. Un archivo malicioso subido a un contenedor de blobs espera ahí a que alguien lo descargue, y un blob público sigue respondiendo aunque nadie lo recuerde.

Defender for Storage vigila el plano de datos: analiza lo que se sube, detecta accesos anómalos y busca información sensible en lo que se guarda. Es de los pocos controles del módulo que se puede probar con un fichero y una cuenta.

## Qué lo validaría

| Prueba | Cómo se haría | Qué hace falta |
|---|---|---|
| Malware en carga | Subir EICAR a una cuenta aislada y comprobar la cuarentena | Una cuenta de almacenamiento con el plan activo |
| Acceso anónimo | Intentar leer un blob sin credenciales y confirmar el bloqueo | Acceso público deshabilitado en la cuenta |
| Acceso anómalo | Descargar en volumen desde otra ubicación | Diagnóstico activo y el plan de Defender for Storage |
| Datos sensibles | Revisar qué contenedores aparecen con información detectada | El análisis de datos sensibles habilitado |

Falta la cuenta con el plan, así que ninguna se ha ejecutado.

## Lecciones

- El análisis de malware necesita una cuenta real. Un fichero en el portátil no se escanea.
- El acceso anónimo se cierra con configuración, no con detección. Defender solo lo señala si está mirando.
- Un contenedor público con datos antiguos es la fuga más silenciosa del laboratorio: nadie la busca porque nadie cree que esté ahí.

## Más detalle

- [Matriz de requisitos del módulo](../../docs/requisitos.md)
