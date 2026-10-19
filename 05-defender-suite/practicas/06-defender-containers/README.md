# 06 | Defender for Containers

> **Estado:** diseño documentado. No ejecutado: no hay clúster de Kubernetes ni registro de contenedores desplegado.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Imagen de contenedor de la API construida con Docker, sin análisis continuo de vulnerabilidades, control de admisión ni detección de runtime en un clúster.  
**Objetivo de seguridad:** Extender la seguridad del contenedor desde el build hasta el runtime con Defender for Containers: escaneo de imágenes, recomendaciones de hardening y detección de comportamientos anómalos.  
**Alcance:** Imagen `ecommerce-api`, Azure Container Registry y un clúster AKS de laboratorio.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Container Registry** | Registro de imágenes | Escaneo de imágenes al push. |
| **AKS** | Runtime de contenedores | Defender for Containers habilitado. |
| **Defender for Containers** | Postura y detección | Agente y sensores de runtime. |
| **Dockerfile** | Build seguro | Multi-stage, usuario no-root. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Imagen mínima y no-root | Multi-stage + `USER $APP_UID` | CIS Docker Benchmark |
| Escaneo de imagen | Defender for Containers / Trivy | MCSB PV-3 |
| Control de admisión | Azure Policy para AKS | MCSB DS-1 |
| Detección de runtime | Defender for Containers | MCSB IR-2 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escaneo al push | Subir imagen a ACR | Hallazgos visibles | Pendiente: requiere ACR |
| Usuario no-root | `docker run --entrypoint id` | UID distinto de 0 | Definido en CI; no ejecutado localmente |
| Control de admisión | Desplegar imagen no firmada | Bloqueo o alerta | Pendiente |
| Detección de runtime | Ejecutar proceso sospechoso | Alerta | Pendiente |

## Limitaciones

- Defender for Containers requiere un clúster y un registro; no se ha desplegado.
- El Dockerfile se valida en CI, pero el escaneo de imagen depende de Docker en el runner.
- La firma de imágenes y la verificación de procedencia son trabajo futuro (Sigstore/Notation).

## Artefactos relacionados

- [Dockerfile de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/Dockerfile)
- [Workflow de contenedor](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Guion de la práctica](GUION.md)
