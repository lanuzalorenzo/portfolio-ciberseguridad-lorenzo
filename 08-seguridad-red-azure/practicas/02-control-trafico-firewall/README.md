# 02 | Control centralizado de tráfico con Azure Firewall

## Descripción del escenario y objetivo de seguridad

**Escenario:** Diseño de salida controlada desde una red de laboratorio mediante un punto central de inspección. El escenario es una propuesta y no describe un despliegue realizado.<br>
**Objetivo de seguridad:** Hacer explícitas las rutas y políticas que determinan qué tráfico puede salir de las subredes incluidas en el laboratorio.<br>
**Alcance:** Azure Firewall, rutas definidas por el usuario y pruebas de conectividad; sujeto a disponibilidad regional, permisos y presupuesto.

> [!NOTE]
> Práctica propuesta para un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| Azure Firewall | Punto central de aplicación de reglas de tráfico | Desplegar solo tras comprobar coste y disponibilidad para el laboratorio. |
| Route table | Dirige los flujos seleccionados hacia el punto de inspección | Rutas definidas de acuerdo con la topología final. |
| Subredes de carga de trabajo | Origen de los flujos sujetos a control | Incluir únicamente las subredes previstas en el escenario. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Egreso controlado | Definir políticas explícitas para los destinos requeridos y las rutas asociadas | Reglas de Firewall y rutas definidas por el usuario | Política de tráfico del laboratorio |
| Reducción de exposición | Evitar excepciones amplias que no estén justificadas por el escenario | Revisión manual de reglas y rutas | Matriz de tráfico |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Destino aprobado | Probar el destino controlado que se seleccione para el laboratorio | El flujo permitido alcanza el destino | Pendiente: práctica no ejecutada. |
| Destino no aprobado | Probar un destino de control definido para el laboratorio | El flujo queda bloqueado y el resultado puede atribuirse a la política | Pendiente: práctica no ejecutada. |
| Ruta de salida | Revisar el camino efectivo desde una subred incluida | El tráfico sigue el diseño previsto | Pendiente: práctica no ejecutada. |

> [!WARNING]
> No desplegar el firewall sin revisar costes, disponibilidad y procedimiento de limpieza. No declarar una prueba superada si no se ejecutó.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| Pendiente de verificar contra la versión vigente | Relacionar el control aplicable con las políticas y rutas validadas | Completar después de confirmar la referencia y ejecutar el laboratorio. |

- Registrar las reglas, excepciones y rutas que se hayan probado realmente.
- Documentar costes y límites del laboratorio antes de extraer conclusiones sobre su viabilidad.