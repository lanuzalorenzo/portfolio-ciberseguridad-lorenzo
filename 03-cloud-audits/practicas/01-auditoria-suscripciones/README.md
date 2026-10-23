# 01 | Auditoría de la suscripción

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB GS-1, GS-2, PA-1, PA-3 · CIS Azure 2.0.

La suscripción es el plano de control: quien tiene permisos ahí decide sobre todo lo que hay debajo. Si los roles se reparten a mano entre personas, nadie sabe ya quién puede qué, y una baja o un cambio de puesto deja permisos vivos.

La revisión combinó Defender for Cloud para la postura (*Secure Score*), Azure Policy para el cumplimiento y Azure Resource Graph para el inventario.

## Hallazgos

| ID | Qué se comprobó | Cómo | Resultado observado | Gravedad |
|---|---|---|---|---|
| SEC-SUB-01 | Asignaciones del rol *Owner* | Inspección de IAM de la suscripción | Asignaciones directas a usuarios; se propuso pasar a grupos y a PIM | Alta |
| SEC-SUB-02 | Registro de actividad | Cumplimiento de Azure Policy | Sin directiva que obligue a enviar los diagnósticos a Log Analytics | Media |
| SEC-SUB-03 | Etiquetado de recursos | Inventario en Resource Graph | Recursos sin propietario, entorno ni criticidad | Baja |

Los tres quedaron como recomendación: no se aplicó ningún cambio en la suscripción.

## Lecciones

- Un rol asignado a una persona desaparece con la persona; asignado a un grupo, se audita y se revoca.
- Azure Policy en modo *Deny* previene la desviación; en modo *Audit* solo deja constancia de ella.
- El etiquetado no es burocracia: sin propietario no hay a quién avisar cuando un recurso aparece en un incidente.

## Más detalle

- [Informe técnico con la matriz completa](informe.md)
- [Bitácora del 14 de septiembre](../../bitacora/2026-09-14-inicio-modulo-03.md)
