# 02 | Automatización de respuesta y contención

Cuando la alerta ya existe, la pregunta es qué se hace en los primeros minutos. Un playbook de Sentinel puede abrir una revisión, pedir aprobación o aplicar una contención limitada; lo que no puede es sustituir el criterio de quien decide. El diseño está escrito; no hay automatización probada.

**Referencias:** MCSB IR-2 · NIST SP 800-61

| Paso | Qué haría | Estado |
|---|---|---|
| Disparador | Incidente creado por la regla de la práctica 01 | Pendiente: sin regla |
| Aprobación | Revisión humana antes de tocar una identidad o un recurso | Diseño |
| Contención | Acción mínima y reversible, con permisos acotados | Diseño |
| Registro | Traza de qué se ejecutó y con qué resultado | Diseño |
| Prueba | Incidente simulado de principio a fin | Pendiente |

La lógica es deliberadamente corta: el playbook no decide, ejecuta lo que una persona aprueba. Esa decisión reduce el riesgo de que un falso positivo bloquee a un usuario legítimo, pero también limita la velocidad; el equilibrio depende del caso.

El [playbook del módulo 12](../../../12-forense-cloud-respuesta/practicas/03-playbook-respuesta/README.md) se recorrió a mano en un tabletop, sin automatización. Automatizarlo exige el workspace, la regla y permisos de la identidad del playbook, y ninguno está desplegado.

Tampoco conviene que el playbook crezca antes de tener un caso probado: cada acción añade permisos y una forma nueva de equivocarse.

Automatizar sin aprobación multiplica errores; una acción irreversible no debería ser la primera; y un playbook sin registro no se puede auditar.
