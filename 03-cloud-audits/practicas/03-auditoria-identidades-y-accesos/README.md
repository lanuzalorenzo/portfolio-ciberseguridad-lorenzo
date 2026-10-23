# 03 | Auditoría de identidades y accesos

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB IA-1, PA-1, PA-6 · CIS Microsoft 365 1.2, 1.14 · NIST AC-2.

En la nube la identidad es el perímetro. Un directorio acumula con los años cuentas que ya no se usan, administradores que lo son todos los días y credenciales de aplicación que nadie recuerda haber creado; cada una es una entrada que sobrevive a su dueño.

Una cosa estaba bien: ninguna cuenta invitada tenía roles administrativos. El problema no era su privilegio sino su permanencia.

## Hallazgos

| ID | Qué se comprobó | Cómo | Resultado observado | Gravedad |
|---|---|---|---|---|
| SEC-IAM-01 | Caducidad de secretos de aplicación | Revisión de *Certificates & Secrets* | Un *client secret* configurado como *Never expire* | Crítica |
| SEC-IAM-02 | Administradores globales | Conteo de asignaciones permanentes | Varias cuentas con el rol permanente para tareas diarias | Alta |
| SEC-IAM-03 | Cuentas invitadas | Filtro por `userType == 'Guest'` | Invitados sin acceso en 90 días dentro de grupos internos | Media |
| SEC-IAM-04 | Registro de aplicaciones | Propiedades de usuario del tenant | Cualquier usuario puede registrar aplicaciones | Baja |

Ninguno se corrigió en el laboratorio: son recomendaciones. El secreto permanente debería sustituirse por una identidad administrada; los administradores globales, pasar a elegibles con PIM y quedar en dos o cuatro cuentas de emergencia.

## Lecciones

- Un secreto sin caducidad no es comodidad: es persistencia regalada a quien lo filtre.
- Lo que no se revisa no se revoca; las *Access Reviews* automatizan esa limpieza.
- Una cuenta invitada depende del directorio de un tercero: si ese directorio cae, la tuya también.

## Más detalle

- [Informe técnico con la matriz completa](informe.md)
- [Bitácora del 15 de septiembre](../../bitacora/2026-09-15-cierre-modulo-03.md)
