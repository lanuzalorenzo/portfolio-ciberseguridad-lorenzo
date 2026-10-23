# Informe técnico — Auditoría de Identidades, Roles y Accesos en Microsoft Entra ID

**Módulo:** 03 — Auditorías Cloud  
**Práctica:** 03 — Auditoría de Identidades y Accesos

## Contexto y Alcance
En los entornos cloud modernos, la identidad constituye el perímetro principal de seguridad. Con el paso del tiempo, los tenants de Microsoft Entra ID acumulan cuentas obsoletas, asignaciones de roles administrativos innecesarias y credenciales de aplicaciones desatendidas que amplían significativamente la superficie de ataque.

Esta práctica documenta la auditoría exhaustiva sobre el directorio Microsoft Entra ID y las asignaciones de acceso en Azure, evaluando la higiene de cuentas, la gestión de privilegios elevados y el ciclo de vida de los Service Principals conforme a las directrices de CIS Microsoft 365 y Microsoft Cloud Security Benchmark.

## Áreas Auditadas
1. **Higiene de Cuentas de Usuario:** Detección de cuentas inactivas (>90 días sin inicio de sesión) y cuentas de invitados (B2B/Guest) residuales.
2. **Gobernanza de Roles Privilegiados:** Conteo y análisis de asignaciones permanentes en roles críticos (*Global Administrator*, *Privileged Role Administrator*, *Security Admin*).
3. **Credenciales de Aplicaciones (Service Principals):** Revisión de vigencia de secretos (*Client Secrets*), certificados asociados y permisos delegados excesivos en *App Registrations*.

## Matriz de Hallazgos de Seguridad

| ID Hallazgo | Severidad | Área Auditada | Descripción del Hallazgo | Riesgo Asociado | Recomendación de Remediación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SEC-IAM-01** | **Crítica** | App Registrations | Registro de aplicación con un *Client Secret* configurado sin fecha de caducidad (*Never expire*). | Persistencia a largo plazo si el secreto se filtra en repositorios o logs; ausencia de ciclo de vida forzado. | Eliminar el secreto permanente, crear un secreto con vigencia máxima de 6 a 12 meses, o migrar preferentemente a una **Managed Identity** sin secretos. |
| **SEC-IAM-02** | **Alta** | Roles de Entra ID | Múltiples cuentas de usuario asignadas de forma permanente como *Global Administrator* para tareas operativas rutinarias. | Compromiso total del tenant ante el robo de credenciales de una sola cuenta de usuario. | Reducir el número de administradores permanentes a un máximo de 2-4 (incluyendo cuentas de emergencia Break-Glass) y configurar el resto como elegibles bajo demanda mediante Privileged Identity Management (PIM). |
| **SEC-IAM-03** | **Media** | Cuentas B2B / Guest | Cuentas de invitados externos sin actividad de inicio de sesión registrada en los últimos 90 días con pertenencia a grupos internos. | Identidades huérfanas que pueden ser explotadas si el directorio de origen del tercero es comprometido. | Habilitar revisiones periódicas de acceso (*Access Reviews*) en Entra ID Governance para revocar automáticamente cuentas de invitados inactivas. |
| **SEC-IAM-04** | **Baja** | Políticas de Acceso | Usuarios estándar del tenant con permisos por defecto para registrar aplicaciones (*Users can register applications = Yes*). | Creación descontrolada de Service Principals y posibles aplicaciones maliciosas con consentimiento implícito. | Restringir el registro de aplicaciones a administradores o roles específicos de desarrollador en las propiedades de usuario de Entra ID. |

## Conclusiones Técnicas y Plan de Acción
- **Prioridad Inmediata:** La remediación de secretos de aplicaciones de duración infinita y la supresión de roles permanentes deben abordarse de forma prioritaria, ya que representan vectores directos de persistencia.
- **Automatización de Gobernanza:** Depender exclusivamente de revisiones manuales no es escalable. La implementación de revisiones de acceso automatizadas (*Access Reviews*) y políticas de ciclo de vida de identidades en Entra ID Governance es indispensable para mantener la higiene del directorio a largo plazo.