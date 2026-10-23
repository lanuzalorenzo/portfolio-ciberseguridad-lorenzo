# 02 | Recomendaciones y Secure Score

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB GS-1, GS-2, NS-1, DP-3 · CIS 6.2.

El panel de recomendaciones puede tener cientos de entradas. Sin criterio se convierte en una lista que nadie termina, y el valor no está en leerla entera sino en ordenarla por lo que resta al Secure Score y por lo que cuesta arreglar cada cosa.

## Qué se priorizó y qué se hizo

| Control | Recomendación | Impacto | Acción | Resultado |
|---|---|---|---|---|
| Puertos de administración | Cerrarlos o protegerlos con acceso JIT | Alto | JIT activado desde el panel | Recomendación en *Healthy* |
| Cifrado en tránsito | Exigir TLS 1.2 en la cuenta de almacenamiento | Medio | `minimumTlsVersion = TLS1_2` | Recurso conforme |
| Diagnóstico del registro de actividad | Enviarlo a Log Analytics | Medio | *Diagnostic Settings* sobre la suscripción | Log centralizado |
| MFA para administradores | Exigir segundo factor a los roles privilegiados | Alto | Pendiente: requiere Conditional Access o *Security Defaults* | Documentada, no aplicada |
| Red privada | Migrar a Private Endpoints | Alto | Excluida: obliga a rediseñar la red | Pendiente por arquitectura |

El criterio fue impacto en la puntuación, esfuerzo de la corrección y exclusiones explícitas. Lo que no se arregló se quedó escrito como pendiente, no se maquilló como aprobado.

## Lecciones

- El Secure Score mide tendencia, no seguridad: un recurso conforme al benchmark puede seguir siendo explotable.
- Un *Quick Fix* resuelve el síntoma en un recurso, no la causa en el proceso; sin política, el siguiente nace igual.
- Dejar por escrito lo que no se arregló vale más que un panel en verde.

## Más detalle

- [Módulo 04](../../README.md)
