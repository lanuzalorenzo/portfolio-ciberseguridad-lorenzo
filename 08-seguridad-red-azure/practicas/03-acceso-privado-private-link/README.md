# 03 | Acceso privado a servicios con Private Link

## Descripción del escenario y objetivo de seguridad

**Escenario:** Un servicio PaaS seleccionado para el laboratorio debe ser accesible desde una red virtual mediante conectividad privada. El escenario es una propuesta y no describe un despliegue realizado.<br>
**Objetivo de seguridad:** Limitar la exposición del servicio y comprobar la resolución DNS y conectividad desde la red autorizada.<br>
**Alcance:** Private Endpoint, zona DNS privada correspondiente al servicio y evaluación de la configuración de acceso público.

> [!NOTE]
> Práctica propuesta para un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| Servicio PaaS | Recurso de destino del laboratorio | Seleccionar el servicio y revisar sus opciones de red antes de configurarlo. |
| Private Endpoint | Conecta el servicio a una interfaz de red privada | Ubicarlo en la VNet y subred definidas para el escenario. |
| DNS privado | Resuelve el nombre del servicio hacia el acceso privado | Confirmar la zona DNS requerida por el servicio seleccionado antes de crearla. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Conectividad privada | Asociar el servicio a un Private Endpoint en la red de laboratorio | Configuración de Private Link | Diseño de conectividad privada |
| Resolución DNS privada | Configurar la integración DNS necesaria para el servicio elegido | Zona DNS privada y enlace a la red, si aplica | Requisitos DNS del servicio |
| Reducción de acceso público | Evaluar la restricción del endpoint público después de probar el acceso privado | Configuración de red del servicio | Decisión pendiente según el escenario |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Resolución desde la red autorizada | Consultar el nombre del servicio desde el entorno de prueba | Se resuelve según el diseño privado | Pendiente: práctica no ejecutada. |
| Acceso desde la red autorizada | Probar la conectividad al servicio | El acceso funciona por la ruta privada | Pendiente: práctica no ejecutada. |
| Acceso público | Evaluar el acceso público tras validar dependencias | Se comporta conforme a la decisión documentada | Pendiente: práctica no ejecutada. |

> [!WARNING]
> No restringir el acceso público hasta comprobar dependencias y validar el acceso privado. No declarar una prueba superada si no se ejecutó.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| Pendiente de verificar contra la versión vigente | Relacionar el control aplicable con la exposición y conectividad comprobadas | Completar después de confirmar la referencia y ejecutar el laboratorio. |

- Registrar la zona DNS y las dependencias reales del servicio seleccionado.
- Documentar si se restringió el acceso público y qué prueba justificó esa decisión.