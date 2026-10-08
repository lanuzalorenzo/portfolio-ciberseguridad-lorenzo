# Lorenzo Lanuza | Portfolio de ciberseguridad

Este portfolio reúne trabajo documentado sobre seguridad cloud, identidad, protección de entornos Azure y DevSecOps. Puedes explorarlo por objetivo: abre un recorrido y salta directamente a sus módulos y prácticas destacadas.

> [!NOTE]
> El contenido describe laboratorios y documentación técnica; no representa despliegues de producción. El estado de cada práctica se indica en su documentación.

## Explora por objetivo

<details>
<summary><strong>Identidad y acceso</strong> — autenticación, gobierno y protección de identidades</summary>

- [01 | Seguridad Azure](01-seguridad-azure/README.md): [flujo OAuth 2.0 con PKCE y validación JWT/JWKS](01-seguridad-azure/docs/03-validacion-jwt-jwks.md).
- [02 | Identity Security](02-identity-security/README.md): MFA, Passwordless, SSPR, PIM, RBAC, Key Vault y Managed Identities. [Ver práctica de MFA](02-identity-security/practicas/01-mfa/README.md).
- [06 | Identity Protection](06-identity-protection/README.md): Conditional Access, PIM/JIT, minimización de privilegios e Identity Protection. [Ver práctica de PIM/JIT](06-identity-protection/practicas/02-pim-jit/README.md).

</details>

<details>
<summary><strong>Seguridad cloud y redes</strong> — auditoría, postura, defensa y conectividad</summary>

- [03 | Cloud Audits](03-cloud-audits/README.md): revisión de suscripciones, recursos críticos e identidades. [Ver auditoría de recursos críticos](03-cloud-audits/practicas/02-auditoria-recursos-criticos/README.md).
- [04 | Defender for Cloud](04-defender-for-cloud/README.md): planes, recomendaciones, workloads y hardening. [Ver práctica de policies y hardening](04-defender-for-cloud/practicas/04-policies-hardening/README.md).
- [05 | Microsoft Defender](05-defender-suite/README.md): protección de identidad, endpoints, correo y respuesta con XDR. [Ver análisis con Defender XDR](05-defender-suite/practicas/04-defender-xdr/README.md).
- [08 | Seguridad de red en Azure](08-seguridad-red-azure/README.md): segmentación, control de tráfico y Private Link. [Ver diseño de segmentación VNet/NSG](08-seguridad-red-azure/practicas/01-segmentacion-vnet-nsg/README.md). **Validación del laboratorio pendiente.**

</details>

<details>
<summary><strong>Seguridad del desarrollo</strong> — controles para repositorios y pipelines</summary>

- [07 | DevSecOps](07-devsecops/README.md): protección de ramas, secretos, análisis de código y seguridad de pipelines.
- [Protección de la rama principal](07-devsecops/branch-protection.md).
- [SAST, SCA e IaC scanning](07-devsecops/practicas/03-sast-sca-iac/README.md).

</details>

## Cómo está organizado

Cada módulo ofrece contexto y enlaces a sus prácticas. Los informes técnicos detallan procedimientos y validaciones; las bitácoras registran la evolución del trabajo. Los resultados se documentan según lo realmente ejecutado.

## Contacto

- [LinkedIn](https://linkedin.com/in/lanuzalorenzo)
- Email: [lanuzalorenzo@gmail.com](mailto:lanuzalorenzo@gmail.com)

## Aviso y licencia

El contenido tiene fines educativos y no acredita configuraciones de producción. No incluye información confidencial. El repositorio se distribuye bajo licencia [MIT](LICENSE).
