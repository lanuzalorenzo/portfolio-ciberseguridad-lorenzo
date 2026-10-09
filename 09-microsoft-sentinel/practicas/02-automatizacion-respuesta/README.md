# 02 | Automatización de respuesta y contención

## Descripción del escenario y objetivo de seguridad

**Escenario:** Un entorno donde una alerta de seguridad necesita una respuesta rápida para limitar daños, iniciar triage o pedir validación humana. El diseño del laboratorio se mantiene orientativo y no representa producción.
**Objetivo de seguridad:** Reducir el tiempo de respuesta mediante automatización basada en incidentes, alertas y playbooks.
**Alcance:** Microsoft Sentinel, analíticas, playbooks y acciones de contención sobre entornos de laboratorio controlados.

> [!NOTE]
> Práctica propuesta para un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| Microsoft Sentinel | Orquestación y gestión de incidentes | Reglas, alertas y triage. |
| Playbook de automatización | Acción de respuesta iniciada por alerta | Ejecutar tareas controladas y documentadas. |
| Entornos conectados | Recursos que pueden ser objeto de contención | Azure, Entra ID o servicios con permisos limitados. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Respuesta inicial | Playbook que inicia revisión y/o contención | Automatización basada en alerta | Sentinel automation |
| Contención | Acciones limitadas y documentadas | Playbooks con permisos mínimos | Seguridad operativa |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Disparador de playbook | Ejecutar una alerta de prueba | Se inicia la automatización esperada | Pendiente: no ejecutado en laboratorio. |
| Contención controlada | Validar que la acción es mínima y reversible | Se evita impacto innecesario | Pendiente: no ejecutado en laboratorio. |

> [!WARNING]
> No declarar una prueba superada si no se ejecutó. Redactar datos sensibles.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| Pendiente de verificar contra la versión vigente | Automatización y respuesta ante incidentes | La automatización debe ser simple, reversible y claramente documentada. |

- Asegurar que los playbooks no ejecuten acciones sin una firma humana o validación documental.
- Limitar el alcance de la automatización al caso de uso definido.
