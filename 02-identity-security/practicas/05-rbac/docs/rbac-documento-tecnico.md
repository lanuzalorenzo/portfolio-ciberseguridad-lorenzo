# Informe técnico — RBAC y Separación de Funciones

**Módulo:** 02 — Identity Security  
**Práctica:** 05 — Role-Based Access Control (RBAC)

## Contexto y Alcance
En entornos cloud, asignar permisos directos a usuarios o usar credenciales con privilegios excesivos (como *Owner* o *Contributor* a nivel de suscripción) representa un vector de riesgo crítico de escalada de privilegios y movimiento lateral. 

Esta práctica aborda el diseño y validación de una matriz RBAC siguiendo el principio de mínimo privilegio en Azure Resource Manager (ARM), delimitando claramente los ámbitos (*Management Group*, *Subscription*, *Resource Group*) y la separación de funciones entre perfiles operativos y de auditoría.

## Arquitectura del Modelo RBAC Diseñado

Se implementó un modelo basado en tres perfiles funcionales, asignando roles integrados (*built-in roles*) de Azure y restringiendo el ámbito estricto al Resource Group del proyecto:

| Perfil / Rol Funcional | Rol Integrado de Azure | Ámbito (*Scope*) | Acciones Clave Permitidas | Justificación de Seguridad |
| :--- | :--- | :--- | :--- | :--- |
| **Administrador / SecOps** | *Security Admin* | Resource Group | Lectura de configuraciones de seguridad, gestión de alertas y directivas. | Control operativo de seguridad sin acceso directo a datos de negocio. |
| **Operador de Infraestructura** | *Virtual Machine Contributor* | Resource Group | Reiniciar, detener e iniciar máquinas virtuales; no puede modificar la red ni asignar roles. | Impide la modificación de NSGs o asignaciones de permisos a terceros. |
| **Auditor de Cumplimiento** | *Reader* / *Security Reader* | Subscription / RG | Inspección de configuraciones, logs y estado de cumplimiento en Microsoft Defender for Cloud. | Capacidad de visibilidad total sin riesgo de alteración o borrado accidental. |

## Puntos Críticos y Mitigaciones Implementadas

1. **Evitar la asignación directa de permisos a identidades individuales:**  
   Se diseñó la asignación de roles a través de grupos de seguridad de Microsoft Entra ID (`sg-secops`, `sg-operations`, `sg-audit`) en lugar de usuarios sueltos, garantizando gobernanza centralizada y ciclo de vida de identidades automatizable.
2. **Restricción de permisos sobre el plano de control:**  
   Se eliminó la tentación de otorgar *Contributor* genérico al operador, restringiéndolo a *Virtual Machine Contributor* para mitigar riesgos de modificación en redes virtuales asociadas.
3. **Separación entre Plano de Control y Plano de Datos:**  
   Se verificó que los roles de ARM asignados a nivel de Resource Group no otorguen automáticamente acceso al plano de datos (por ejemplo, leer secretos de un Key Vault o blobs de una cuenta de Storage) sin roles de datos específicos.

## Comprobaciones y Validaciones de Acceso

| Prueba Realizada | Método de Validación | Resultado Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Operador intenta modificar NSG | Azure Portal / CLI con usuario operador | Acceso denegado (403 AuthorizationFailed) | PASS: Denegado por falta de `Microsoft.Network/networkSecurityGroups/write` |
| Auditor intenta reiniciar servicio | Azure Portal con usuario auditor | Botón de reinicio deshabilitado / 403 | PASS: Solo dispone de acciones `*/read` |
| Asignación de roles no autorizada | Intento de conceder rol con cuenta operador | Bloqueado | PASS: Falta acción `Microsoft.Authorization/roleAssignments/write` |

## Lecciones Aprendidas
- Otorgar roles en el ámbito más granular posible (Resource Group) minimiza el radio de impacto (*blast radius*) ante una identidad comprometida.
- La distinción entre roles de plano de control y roles de plano de datos en Azure es un control fundamental para evitar accesos indebidos a datos sensibles.
