# Informe técnico — Privileged Identity Management (PIM) en Microsoft Entra ID

**Módulo:** 02 — Identity Security  
**Práctica:** 04 — Privileged Identity Management (PIM)

## Contexto y Alcance
El modelo tradicional de administración basado en privilegios permanentes (*Standing Access*) implica que un atacante que comprometa las credenciales de un administrador obtiene control inmediato y sostenido sobre el tenant o los recursos cloud.

Esta práctica documenta la aplicación del principio de privilegios permanentes cero (*Zero Standing Privileges* o ZSP) mediante **Microsoft Entra Privileged Identity Management (PIM)**, implementando elevaciones temporales *Just-in-Time* (JIT), requerimiento de factores de autenticación adicionales, justificación operativa y auditoría de eventos.

## Configuración y Decisiones de Arquitectura

### 1. Modelo de Asignaciones en PIM
En *Identity Governance* → *Privileged Identity Management* → *Microsoft Entra roles*, se diferencian dos tipos de asignación:
- **Active (Activa):** Permiso asignado de manera continua. Su uso debe limitarse estrictamente a cuentas de emergencia (*Break-Glass*).
- **Eligible (Elegible):** El usuario no dispone de los privilegios en su estado base, pero tiene derecho a solicitarlos temporalmente cuando exista una necesidad técnica justificada.

Para este laboratorio se configuró al usuario de prueba con asignación **Eligible** sobre el rol **Global Reader**.

### 2. Políticas del Rol (*Role Settings*)
Se revisaron y aplicaron las directivas que gobiernan la activación del rol:
- **Duración máxima de activación:** Limitada a 2 horas (reduciendo la ventana de exposición a lo estrictamente necesario).
- **Requisito de MFA:** Obligatorio validar un segundo factor de autenticación antes de autorizar la elevación.
- **Justificación de negocio:** Campo de texto obligatorio donde el operador debe indicar el motivo o ticket de soporte asociado.
- **Aprobación:** Deshabilitada en el laboratorio para autoservicio, pero evaluada para escenarios de producción que requieran autorización explícita de un responsable.

### 3. Procedimiento de Elevación JIT
1. El usuario accede a *PIM* → *My roles*.
2. El rol figura en estado *Eligible*. Se pulsa en **Activate**.
3. El sistema solicita verificación MFA previa.
4. Se introduce la justificación técnica y se define el periodo de tiempo.
5. El rol pasa a estado **Active** de forma inmediata.

## Validaciones y Pruebas Realizadas

| Control / Prueba | Método | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Comprobación de permisos antes de activación | Navegación en portal como usuario base | Sin visibilidad ni capacidades administrativas | PASS: Sin privilegios concedidos en reposo |
| Activación sin justificación o sin MFA | Intento de elevación omitiendo datos requeridos | Bloqueo del asistente de activación | PASS: Campos obligatorios impuestos por directiva |
| Verificación de elevación temporal | Inspección de estado en *Active assignments* | El rol permanece activo durante la ventana definida | PASS: Permisos operativos concedidos temporalmente |
| Trazabilidad y auditoría de elevación | Consulta de *Resource audit* en PIM | Registro completo con timestamp, identidad y justificación | PASS: Trazabilidad inmutable comprobada |

## Lecciones de Troubleshooting y Seguridad
- **Cuentas de emergencia (Break-Glass):** Un error grave al implementar PIM es aplicarlo al 100% de los administradores. Siempre deben mantenerse al menos 2 cuentas de acceso de emergencia excluidas de PIM y de directivas de Conditional Access, con contraseñas complejas almacenadas en caja fuerte física y monitorizadas mediante alertas de Sentinel o Defender.
- **Requisito de licenciamiento:** En Azure, PIM sobre roles de Entra ID y recursos de Azure requiere licencia Microsoft Entra ID P2 o Microsoft Entra ID Governance para cada usuario elegible.
