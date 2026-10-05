# Lorenzo Lanuza | Portfolio de ciberseguridad

Este repositorio documenta laboratorios y proyectos de seguridad cloud centrados en identidad, control de acceso, auditoría y protección de entornos Azure y Microsoft. El hilo conductor es técnico: partir de una configuración o riesgo, explicar las decisiones tomadas y dejar constancia de cómo se validó el resultado.

El portfolio evoluciona junto con el trabajo. El contenido publicado describe prácticas de laboratorio y documentación técnica; no representa despliegues de producción.

## Proyectos destacados

- [Autenticación con OAuth 2.0 y PKCE](01-seguridad-azure/README.md): flujo de autorización y validación de tokens JWT mediante JWKS.
- [Seguridad de identidades en Entra ID](02-identity-security/README.md): MFA, Passwordless, SSPR, PIM, RBAC, Key Vault y Managed Identities.
- [Auditoría de entornos cloud](03-cloud-audits/README.md): revisión de suscripciones, recursos críticos e identidades.
- [Postura de seguridad con Defender for Cloud](04-defender-for-cloud/README.md): planes, recomendaciones, workloads y hardening con políticas.
- [Operación de Microsoft Defender](05-defender-suite/README.md): prácticas sobre identidad, endpoints, correo, XDR y otros componentes de la suite.
- [Controles DevSecOps para repositorios](07-devsecops/README.md): protección de ramas y revisión de cambios.

## Recorrido técnico

Algunos documentos de entrada:

- [Validación de JWT y JWKS](01-seguridad-azure/docs/03-validacion-jwt-jwks.md)
- [Práctica de PIM](02-identity-security/practicas/04-pim/README.md)
- [Auditoría de recursos críticos](03-cloud-audits/practicas/02-auditoria-recursos-criticos/README.md)
- [Policies y hardening en Defender for Cloud](04-defender-for-cloud/practicas/04-policies-hardening/README.md)
- [Análisis de incidentes en Defender XDR](05-defender-suite/practicas/04-defender-xdr/README.md)
- [Protección de la rama principal](07-devsecops/branch-protection.md)

## Cómo leer los proyectos

Los README de entrada ofrecen contexto y enlazan al trabajo disponible. Los informes técnicos describen procedimientos y validaciones; las bitácoras, cuando existen, registran la evolución cronológica. La documentación se amplía a medida que avanzan los laboratorios.

## Contacto

- Email: [lanuzalorenzo@gmail.com](mailto:lanuzalorenzo@gmail.com)
- [LinkedIn](https://linkedin.com/in/lanuzalorenzo)

## Aviso y licencia

El contenido tiene fines educativos y describe entornos de laboratorio. No incluye información confidencial ni acredita configuraciones de producción. El repositorio se distribuye bajo licencia [MIT](LICENSE).
