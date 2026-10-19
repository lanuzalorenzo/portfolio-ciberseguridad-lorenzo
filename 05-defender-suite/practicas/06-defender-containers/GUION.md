# Guion — Práctica 06: Defender for Containers

## Objetivo

Validar el ciclo de vida de seguridad de la imagen de `EcommerceApi`: build no-root, escaneo en registro y detección en runtime.

## Preparación

1. Crear un Azure Container Registry.
2. Crear un clúster AKS de laboratorio con Azure Policy.
3. Habilitar Defender for Containers.
4. Construir y subir la imagen `ecommerce-api`.
5. Configurar el despliegue con un `securityContext` no-root y sin privilegios.

## Ejecución

1. Confirmar el escaneo de la imagen en ACR.
2. Revisar recomendaciones de hardening del clúster.
3. Validar que el pod no ejecuta como root.
4. Intentar desplegar una imagen sin firma o con `privileged: true`.
5. Ejecutar un proceso de prueba y revisar alertas de runtime.
6. Exportar evidencia y documentar hallazgos.

## Validaciones

| Prueba | Resultado esperado |
|---|---|
| Escaneo de imagen | Hallazgos priorizados |
| Pod no-root | `runAsNonRoot: true` efectivo |
| Admisión | Bloqueo de configuración insegura |
| Runtime | Alerta ante proceso anómalo |

## Cierre

Registrar qué se ejecutó y qué quedó pendiente. Si no hay AKS/ACR, no presentar la práctica como validada.
