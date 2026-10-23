# 02 | Recomendaciones y Secure Score

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB GS-1, GS-2, NS-1, DP-3 · CIS 6.2.

El panel de recomendaciones puede tener cientos de entradas. Sin criterio se convierte en una lista que nadie termina, y el valor no está en leerla entera sino en ordenarla por lo que resta al Secure Score y por lo que cuesta arreglar cada cosa.

## Cómo se priorizó

1. **Impacto:** cuántos puntos resta la recomendación.
2. **Esfuerzo:** primero lo que tiene *Quick Fix* y no obliga a rediseñar.
3. **Exclusiones explícitas:** lo que exige cambiar la arquitectura se documenta como pendiente y no se maquilla.

## Validación

| Prueba | Resultado observado |
|---|---|
| *Quick Fix* en puertos de administración | JIT activado; la recomendación pasa a *Healthy* |
| TLS 1.2 en la cuenta de almacenamiento | Propiedad actualizada y recurso conforme |
| Diagnóstico del registro de actividad | Enviado a un espacio de Log Analytics |
| Recomendaciones sin remediación rápida | Documentadas como pendientes, no como PASS |

## Lecciones

- El Secure Score mide tendencia, no seguridad: un recurso conforme al benchmark puede seguir siendo explotable.
- Un *Quick Fix* resuelve el síntoma en un recurso, no la causa en el proceso; sin política, el siguiente nace igual.
- Dejar por escrito lo que no se arregló vale más que un panel en verde.

## Más detalle

- [Recomendaciones analizadas y remediaciones](docs/informe-tecnico.md)
