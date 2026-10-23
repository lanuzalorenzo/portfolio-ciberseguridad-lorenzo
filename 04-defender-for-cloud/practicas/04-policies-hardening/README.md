# 04 | Políticas y hardening

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB GS-2, DP-3, DP-4, LT-1 · CIS Azure 3.7.

Una recomendación se resuelve una vez; el siguiente recurso nace mal otra vez. Azure Policy cambia eso: la regla se aplica sola a todo lo que se despliegue, en modo *Audit* para ver la desviación o en modo *Deny* para impedirla.

## Qué se aplicó

| Control | Directiva y efecto | Qué consigue |
|---|---|---|
| Línea base de cumplimiento | Iniciativa MCSB, en auditoría | Porcentaje de cumplimiento común para toda la suscripción |
| Acceso público a blobs | *Deny* sobre `allowBlobPublicAccess` | El despliegue falla antes de crear el recurso |
| TLS 1.2 en almacenamiento | *AuditIfNotExists* sobre `minimumTlsVersion` | Marca los recursos antiguos para remediar |
| Diagnóstico de actividad | *AuditIfNotExists* sobre *Diagnostic Settings* | Detecta recursos que no envían registros |

## Validación

| Prueba | Resultado observado |
|---|---|
| Iniciativa visible en *Security policy* | Activa y evaluando la suscripción |
| Despliegue de una cuenta con acceso público | Bloqueado por la política antes de aprovisionar |
| Recursos sin TLS 1.2 | Marcados como *Non-compliant* |

## Lecciones

- *Audit* informa; *Deny* protege. Sin *Deny*, una política es un aviso, no un control.
- Empezar en *Audit* y pasar a *Deny* cuando se confirma que no rompe nada evita incidentes de adopción.
- Una directiva bien puesta ahorra más trabajo que cien remediaciones a mano.

## Más detalle

- [Módulo 04](../../README.md)
