# 03 | Playbook de respuesta y tabletop

Un acceso anómalo a Key Vault desde una identidad de aplicación obliga a preservar la prueba, contener sin destruir la traza y devolver el servicio. El playbook sigue las fases de NIST SP 800-61 y se recorrió en un tabletop sobre documentación el 2026-10-22.

**Referencias:** NIST SP 800-61 · MCSB IR-2

| Fase | Qué se hace |
|---|---|
| Preparación | Contactos, accesos de emergencia, retención y runbook |
| Detección | Alertas, KQL y alcance temporal |
| Contención | Revocar sesiones, deshabilitar identidad, restringir red |
| Erradicación | Rotar secretos, corregir configuración, revisar persistencia |
| Recuperación | Restaurar servicio y vigilar reingreso |
| Lecciones | Causa raíz, acciones y responsable |

El orden importa: exportar y hashear antes de contener; contener antes de rotar; rotar antes de restaurar. El [runbook](runbook.md) detalla cada paso y las [consultas](../02-timeline-kql/README.md) alimentan la línea temporal.

El tabletop recorrió el runbook con un caso ficticio; falta la variante con reparto de roles y entorno real, y los tiempos de contención no están medidos.

| Táctica | Técnica | Evidencia a buscar |
|---|---|---|
| Credential Access | T1528 Steal Application Access Token | Token usado fuera de su ventana, IP o user agent habitual |
| Credential Access | T1078.004 Cloud Accounts | Identidad válida desde una ubicación o dispositivo anómalo |
| Persistence | T1098 Account Manipulation | Cambios de roles, aplicaciones o credenciales |
| Defense Evasion | T1562.007 Disable or Modify Cloud Firewall | Cambios de NSG, reglas o diagnósticos |
| Collection | T1530 Data from Cloud Storage | Lectura masiva de blobs; no aplica a secretos de Key Vault |

Sin preservación previa, contener destruye la evidencia; una identidad de aplicación comprometida exige rotar el secreto; y un playbook sin recorrer es una lista de deseos.
