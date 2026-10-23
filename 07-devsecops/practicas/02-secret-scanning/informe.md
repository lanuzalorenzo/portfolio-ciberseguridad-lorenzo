# Informe técnico — Detección de secretos y credenciales expuestas

**Módulo:** 07 — DevSecOps y gobernanza del software  
**Práctica:** 02 — Detección de secretos y credenciales expuestas

## Contexto y objetivo

Los secretos y credenciales expuestos son una de las causas más comunes de riesgo en entornos de desarrollo. Un token asociado a una cuenta de servicio, una clave de API o una contraseña embebida en un archivo de configuración puede comprometer todo el flujo de despliegue si llega a manos equivocadas.

El objetivo de esta práctica es detectar esas credenciales antes de que se fusionen con el repositorio, y también reforzar la capacidad de respuesta ante incidentes derivados de exposiciones previas.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Prevención temprana** | Detectar secretos antes del merge | Reduce exposición en producción |
| **Autocorrección** | Rotar y eliminar credenciales comprometidas | Mitiga impacto real |
| **Trazabilidad** | Registrar el hallazgo y la acción correctiva | Facilita auditoría |
| **Integración continua** | Ejecutar escaneo en cada cambio | Reforza seguridad por diseño |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **Secret scanning** | Activado en repositorio y PRs | Detecta credenciales antes del merge |
| **Pre-commit hooks** | Recomendado | Reduce problemas antes del push |
| **Rotación de secretos** | Obligatoria tras detección | Cierra la brecha de acceso |
| **Alertas** | Activas para repositorio y equipos relevantes | Permite respuesta rápida |

## Implementación técnica recomendada

1. Activar secret scanning en la plataforma del repositorio.
2. Revisar cambios y pull requests de forma automática.
3. Escanear el historial para detectar credenciales ya publicadas.
4. Rotar cualquier secreto comprometido.
5. Sustituir valores sensibles por variables seguras y referencias protegidas.
6. Consolidar la validación en CI/CD como gate obligatorio.

## Riesgos mitigados

- Exposición de tokens o claves en repositorios públicos o compartidos.
- Compromiso de identidades, servicios o entornos.
- Escalada de privilegios por credenciales erróneamente embebidas.
- Falta de trazabilidad en incidentes de seguridad.

## Conclusión

La prevención y detección de secretos no es un control opcional. Es una necesidad de seguridad en cualquier flujo de desarrollo y una base imprescindible para una estrategia DevSecOps sólida.
