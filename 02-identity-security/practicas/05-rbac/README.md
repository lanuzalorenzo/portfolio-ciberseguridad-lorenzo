# 05 | Control de acceso basado en roles (RBAC)

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB PA-1, PA-7 · NIST SP 800-53 AC-6.

Un operador con permisos de propietario sobre toda la suscripción puede cambiar reglas de red sin necesitarlo. RBAC reparte el acceso por funciones y limita cada rol al ámbito donde trabaja, de modo que una cuenta comprometida no arrastra el resto del entorno.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Cambiar un NSG con rol *VM Contributor* | Intento de modificar reglas de red | Denegado por falta de permisos en `Microsoft.Network` | PASS: 403 |
| Reiniciar un servicio con rol *Security Reader* | Petición de parada o reinicio | Denegado, solo lectura | PASS: acción no autorizada |
| Delegar permisos desde la cuenta de operador | Asignación de roles | Bloqueado sin `roleAssignments/write` | PASS: elevación impedida |

## Lecciones

- Asignar en el grupo de recursos, no en la suscripción, reduce el radio de daño.
- Quien despliega no debería auditar sus propias configuraciones: separar funciones evita el conflicto de interés.
- Asignar a grupos y no a personas evita permisos residuales cuando alguien cambia de puesto o se va.

## Más detalle

- [Diseño y validación del modelo](docs/rbac-documento-tecnico.md)
- [Bitácora del módulo](../../bitacora/2026-09-11-ejercicio-05-rbac.md)
