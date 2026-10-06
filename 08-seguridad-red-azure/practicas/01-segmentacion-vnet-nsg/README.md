# 01 | Segmentación con VNet y Network Security Groups

## Descripción del escenario y objetivo de seguridad

**Escenario:** Diseño de una red virtual de laboratorio con capas de carga de trabajo que requieren flujos explícitos entre subredes. El escenario es una propuesta y no describe un despliegue realizado.<br>
**Objetivo de seguridad:** Reducir la comunicación no necesaria entre componentes mediante segmentación y reglas de red justificadas.<br>
**Alcance:** Diseño de subredes, matriz de flujos y reglas de Network Security Groups (NSG); no incluye recursos de producción.

> [!NOTE]
> Práctica propuesta para un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| Virtual Network | Límite de conectividad privada del laboratorio | Espacio de direcciones y subredes por definir según el escenario. |
| Subredes | Separación lógica de capas | Crear solo las capas necesarias para demostrar los flujos. |
| Network Security Group | Filtrado de tráfico de red | Reglas explícitas basadas en origen, destino, protocolo, puerto y dirección. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Segmentación de red | Separar componentes por función y documentar sus comunicaciones necesarias | Diseño y configuración de NSG en el laboratorio | Matriz de flujos de la práctica |
| Mínimo privilegio de red | Permitir solo flujos justificados y revisar reglas efectivas | Revisión manual y validación de conectividad | Reglas NSG |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Flujo autorizado | Probar una comunicación incluida en la matriz | El flujo requerido funciona | Pendiente: práctica no ejecutada. |
| Flujo no autorizado | Probar una comunicación excluida de la matriz | El flujo queda bloqueado por el control previsto | Pendiente: práctica no ejecutada. |

> [!WARNING]
> No declarar una prueba superada si no se ejecutó. Redactar datos sensibles.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| Pendiente de verificar contra la versión vigente | Relacionar el control aplicable con la segmentación y las reglas validadas | Completar después de confirmar la referencia y ejecutar el laboratorio. |

- Registrar la matriz de flujos y justificar cada regla después de completar la práctica.
- Documentar limitaciones y excepciones observadas durante la validación.