# Lorenzo Lanuza | Portfolio de Ciberseguridad & DevSecOps

Este portfolio documenta la aplicación de **Security by Design, DevSecOps y Cloud Security en Microsoft Azure** sobre una carga de trabajo empresarial real. Articula la seguridad no como una colección de configuraciones aisladas, sino como un modelo de **Defensa en Profundidad (*Defense-in-Depth*)** construido alrededor de una API moderna diseñada en .NET.

> [!NOTE]
> El contenido describe laboratorios y documentación técnica verificable; no representa despliegues de producción comercial. Toda la información sensible y credenciales han sido redactadas. El estado de validación de cada práctica se indica de forma explícita en su respectiva documentación.

---

## 🏛️ Arquitectura del Portfolio: Protección de una Carga de Trabajo Real

El portfolio toma como activo digital de referencia la aplicación [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure), una Web API empresarial desarrollada en .NET con arquitectura desacoplada y autenticación federada.

Alrededor de este activo central se despliegan **5 capas concéntricas de seguridad**:

```
                       [ TRÁFICO EXTERNO / CLIENTES ]
                                      │
                                      ▼
      ┌───────────────────────────────────────────────────────────────┐
      │  CAPA 5: DETECCIÓN, SOC Y ANALÍTICA (Módulos 09 y 10)         │
      │  Monitorización KQL en Microsoft Sentinel y visualización ELK │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 4: SEGURIDAD DE RED Y POSTURA CLOUD (03, 04, 05 y 08)   │
      │  Segmentación VNet/NSG, Private Link y Defender for Cloud     │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 3: IDENTIDAD Y GOBERNANZA ZERO TRUST (01, 02 y 06)      │
      │  Microsoft Entra ID, OAuth 2.0 / PKCE, JWT/JWKS, PIM y RBAC   │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 2: SEGURIDAD DEL DESARROLLO / DEVSECOPS (Módulo 07)     │
      │  Pipelines CI/CD, SAST, SCA, Secret Scanning, OIDC y Docker   │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 1: ARQUITECTURA DE SOFTWARE & APPSEC (lab-api-local)    │
      │  EcommerceApi: Código .NET, DTOs, validación y OWASP API Top  │
      └───────────────────────────────────────────────────────────────┘
```

---

## 🧭 Recorridos Técnicos por Capa de Seguridad

<details open>
<summary><strong>1. Carga de Trabajo Core & AppSec</strong> — Arquitectura de software y seguridad en código</summary>

- [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure): Repositorio del código fuente de `EcommerceApi` en .NET.
- [01 | Seguridad Azure](01-seguridad-azure/README.md): Autenticación moderna para APIs.
  - [Flujo OAuth 2.0 con PKCE](01-seguridad-azure/docs/02-flujo-oauth2-pkce.md).
  - [Validación estricta de JWT y claves JWKS en la API](01-seguridad-azure/docs/03-validacion-jwt-jwks.md).

</details>

<details open>
<summary><strong>2. DevSecOps & Supply Chain</strong> — Seguridad en el flujo de entrega e integración continua</summary>

- [07 | DevSecOps y gobernanza del software](07-devsecops/README.md): Controles automatizados para repositorios y pipelines.
  - [Protección de la rama principal y revisión obligatoria](07-devsecops/branch-protection.md).
  - [Escaneo de secretos y credenciales expuestas](07-devsecops/practicas/02-secret-scanning/README.md).
  - [Análisis estático (SAST), dependencias (SCA) e IaC scanning](07-devsecops/practicas/03-sast-sca-iac/README.md).
  - [Pipeline segura y validación de entregas](07-devsecops/practicas/04-pipeline-security/README.md).

</details>

<details>
<summary><strong>3. Identidad, Acceso y Gobierno Zero Trust</strong> — Autenticación robusta y mínimos privilegios</summary>

- [02 | Identity Security](02-identity-security/README.md): MFA, Passwordless, SSPR, PIM, RBAC, Managed Identities y Azure Key Vault.
  - [Práctica: Autenticación multifactor (MFA)](02-identity-security/practicas/01-mfa/README.md).
  - [Práctica: Gestión de secretos con Azure Key Vault](02-identity-security/practicas/06-key-vault/README.md).
  - [Práctica: Identidades administradas (Managed Identities)](02-identity-security/practicas/07-managed-identities/README.md).
- [06 | Identity Protection](06-identity-protection/README.md): Gobierno avanzado de identidades y elevación controlada.
  - [Práctica: Políticas de Conditional Access](06-identity-protection/practicas/01-conditional-access/README.md).
  - [Práctica: Privileged Identity Management (PIM / JIT)](06-identity-protection/practicas/02-pim-jit/README.md).

</details>

<details>
<summary><strong>4. Seguridad Cloud, Postura y Redes</strong> — Auditoría, hardening y aislamiento en Azure</summary>

- [03 | Cloud Audits](03-cloud-audits/README.md): Auditoría de suscripciones, identidades y recursos críticos.
  - [Auditoría de recursos críticos en Azure](03-cloud-audits/practicas/02-auditoria-recursos-criticos/README.md).
- [04 | Defender for Cloud](04-defender-for-cloud/README.md): Gestión de postura de seguridad (CSPM) y hardening.
  - [Policies y hardening bajo MCSB](04-defender-for-cloud/practicas/04-policies-hardening/README.md).
- [05 | Microsoft Defender Suite](05-defender-suite/README.md): Capacidades de protección integral XDR, endpoint e identidades.
  - [Análisis y respuesta con Defender XDR](05-defender-suite/practicas/04-defender-xdr/README.md).
- [08 | Seguridad de red en Azure](08-seguridad-red-azure/README.md): Segmentación, control de tráfico y acceso privado.
  - [Segmentación VNet y reglas NSG](08-seguridad-red-azure/practicas/01-segmentacion-vnet-nsg/README.md). *(Validación de laboratorio pendiente)*.
  - [Acceso privado con Private Link](08-seguridad-red-azure/practicas/03-acceso-privado-private-link/README.md). *(Validación de laboratorio pendiente)*.

</details>

<details>
<summary><strong>5. Operaciones de Seguridad y Detección (SOC)</strong> — Telemetría, analítica y respuesta</summary>

- [09 | Microsoft Sentinel](09-microsoft-sentinel/README.md): Detección basada en KQL y automatización en seguridad cloud.
  - [Detección de amenazas con KQL](09-microsoft-sentinel/practicas/01-deteccion-kql/README.md). *(Diseño de laboratorio en curso)*.
- [10 | ELK Stack Security](10-elk-stack-security/README.md): Ingesta, normalización y análisis de eventos de seguridad.
  - [Ingesta y filtrado con Logstash](10-elk-stack-security/practicas/01-ingestion-logstash/README.md). *(Diseño de laboratorio en curso)*.

</details>

---

## 🛠️ Cómo está organizado el Portfolio

Cada módulo cuenta con un `README.md` que define su alcance y componentes, un directorio `bitacora/` con el registro cronológico del aprendizaje y decisiones técnicas, y carpetas `practicas/` o `docs/` donde se detallan los procedimientos, configuraciones y evidencias verificables.

El código fuente de la carga de trabajo de referencia y sus pruebas de integración se versiona de forma independiente en [**lanuzalorenzo/lab-api-local-azure**](https://github.com/lanuzalorenzo/lab-api-local-azure).

---

## 📫 Contacto y Perfil Profesional

- **Autor:** Lorenzo Lanuza Arellano — *Software Architect | .NET & DevSecOps*
- **LinkedIn:** [linkedin.com/in/lanuzalorenzo](https://www.linkedin.com/in/lanuzalorenzo)
- **Perfil GitHub:** [github.com/lanuzalorenzo](https://github.com/lanuzalorenzo)
- **Email:** [lanuzalorenzo@gmail.com](mailto:lanuzalorenzo@gmail.com)

---

## ⚖️ Licencia y Responsabilidad

El material de este repositorio tiene fines exclusivamente técnicos y formativos. No acredita configuraciones de entornos de producción comerciales ni incluye secretos ni datos personales. Distribuido bajo licencia [MIT](LICENSE).

