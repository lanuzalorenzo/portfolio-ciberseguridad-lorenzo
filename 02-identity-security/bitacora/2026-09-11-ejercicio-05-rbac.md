# Bitácora — 2026-09-11: RBAC y Control de Acceso en Azure

**Módulo:** 02 — Identity Security  
**Práctica:** 05 — Role-Based Access Control

Hoy me he centrado en el diseño y validación del modelo RBAC para el entorno de laboratorio, buscando aterrizar el principio de mínimo privilegio en Azure Resource Manager.

El objetivo fue evitar la práctica habitual de asignar roles genéricos como *Contributor* a nivel de suscripción. Diseñé una matriz separando perfiles de SecOps (*Security Admin*), operaciones (*Virtual Machine Contributor*) y auditoría (*Security Reader*), delimitando el ámbito exclusivamente al Resource Group del laboratorio.

Para validar el aislamiento, probé a ejecutar cambios de red (modificación de NSG) con el usuario operador y verifiqué que la API de Azure bloquea la petición con error 403 AuthorizationFailed por falta de permisos específicos sobre `Microsoft.Network`. Comprobé además que los roles de plano de control asignados no heredan acceso al plano de datos sin un rol explícito.

Con esto queda establecida la base de gobernanza de identidades para los siguientes ejercicios del módulo.
