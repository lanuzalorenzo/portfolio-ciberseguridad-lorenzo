# Lorenzo Lanuza | Portfolio de Ciberseguridad, DevSecOps y Arquitectura

Este portfolio documenta la aplicación de **Security by Design, DevSecOps, Cloud Security y respuesta a incidentes** sobre una carga de trabajo empresarial: una API .NET protegida con Microsoft Entra ID. El hilo conductor no es una colección de herramientas, sino un modelo de **Defensa en Profundidad** con evidencia y estado de validación explícito.

> [!NOTE]
> El contenido describe laboratorios, código y documentación técnica. No representa despliegues de producción ni certificaciones. Cada práctica indica si está validada, es parcial, tiene un runbook preparado, es un diseño o está pendiente. No se incluyen secretos, identificadores reales ni datos personales.

---

## 🌐 Ecosistema

| Repositorio | Rol | Enlace |
|---|---|---|
| **Portfolio** | Documentación, prácticas y narrativa técnica | [portfolio-ciberseguridad-lorenzo](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo) |
| **API de referencia** | Código .NET, tests, CI y Bicep | [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure) |
| **Laboratorio de IA local** | Modelos locales, agentes y seguridad de prompts | [ai-agent-local-lab](https://github.com/lanuzalorenzo/ai-agent-local-lab) |
| **Perfil profesional** | Trayectoria, stack y proyectos | [lanuzalorenzo](https://github.com/lanuzalorenzo) |
| **Web personal** | Portfolio visual y contacto | [lanuzalorenzo.github.io](https://lanuzalorenzo.github.io) |

---

## 🏛️ Arquitectura del portfolio

La carga de trabajo de referencia es [**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure), una Web API en .NET 10 con autenticación federada, autorización por usuario, DTOs, pruebas de integración y pipeline DevSecOps.

```
                       [ TRÁFICO EXTERNO / CLIENTES ]
                                      │
                                      ▼
      ┌───────────────────────────────────────────────────────────────┐
      │  CAPA 5: DETECCIÓN, SOC Y ANALÍTICA (09 y 10)                 │
      │  KQL en Sentinel, visualización ELK y respuesta (12)          │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 4: RED Y POSTURA CLOUD (03, 04, 05 y 08)                │
      │  Segmentación VNet/NSG, Private Endpoints y Defender          │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 3: IDENTIDAD Y GOBERNANZA ZERO TRUST (01, 02 y 06)      │
      │  Entra ID, OAuth 2.0/PKCE, JWT/JWKS, PIM, RBAC y MFA          │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 2: DESARROLLO SEGURO / DEVSECOPS (07)                   │
      │  SAST, SCA, secretos, contenedor, IaC y dependencias          │
      └──────────────────────────────┬────────────────────────────────┘
                                     │
      ┌──────────────────────────────▼────────────────────────────────┐
      │  CAPA 1: ARQUITECTURA Y APPSEC (API + 11)                     │
      │  .NET, DTOs, BOLA/BFLA, mass assignment y pruebas             │
      └───────────────────────────────────────────────────────────────┘

      Capa transversal: validación ofensiva (11), forense y respuesta (12),
      matriz de cumplimiento (cumplimiento-normativo/).
```

### 🧪 Laboratorio final

El [laboratorio final](docs/laboratorio-final/README.md) define cómo se conectan las capas sobre una sola carga de trabajo, con [arquitectura de referencia](docs/laboratorio-final/arquitectura.md), [plan de ejecución](docs/laboratorio-final/plan-ejecucion.md) y un [índice de evidencias](docs/laboratorio-final/evidencias/README.md). Las prácticas ejecutables usan un [runbook](plantillas/runbook-template.md), registran su prueba con una [plantilla de evidencia](plantillas/evidencia-template.md) y documentan el caso con una [plantilla de README de práctica](plantillas/README-practica-template.md).

> El laboratorio tiene una primera evidencia local (ELK). Las fases Azure siguen pendientes de autorización, presupuesto y resource group temporal; no hay recursos Azure desplegados.

---

## 🧭 Recorridos técnicos

### 1. Arquitectura y AppSec

- [01 | OAuth 2.0, PKCE y validación JWT](01-seguridad-azure/README.md) — *validado en laboratorio*; incluye la práctica de [PKCE manual](01-seguridad-azure/practicas/01-pkce-manual/README.md), con evidencia pendiente de reejecución.
- [11 | Hacking ético de APIs](11-hacking-etico-api/README.md) — *validación local de BOLA y mass assignment; pentest desplegado pendiente*.
- [API de referencia](https://github.com/lanuzalorenzo/lab-api-local-azure) — código, tests, CI y Bicep.

### 2. DevSecOps y supply chain

- [07 | DevSecOps y gobernanza del software](07-devsecops/README.md) — *validado en CI: build, pruebas, Gitleaks, CodeQL, Trivy y contenedor no-root*.
  - [Protección de ramas](07-devsecops/branch-protection.md).
  - [Detección de secretos](07-devsecops/practicas/02-secret-scanning/README.md).
  - [SAST, SCA e IaC](07-devsecops/practicas/03-sast-sca-iac/README.md).
  - [Pipeline segura](07-devsecops/practicas/04-pipeline-security/README.md).

### 3. Identidad, acceso y gobierno Zero Trust

- [02 | Identity Security](02-identity-security/README.md) — *validado en laboratorio*: MFA, Passwordless, SSPR, PIM, RBAC, Key Vault y Managed Identities.
- [06 | Identity Protection](06-identity-protection/README.md) — *validado en laboratorio*: Conditional Access, PIM/JIT, RBAC e Identity Protection.

### 4. Cloud, postura y redes

- [03 | Cloud Audits](03-cloud-audits/README.md) — *validado en laboratorio*.
- [04 | Defender for Cloud](04-defender-for-cloud/README.md) — *validado en laboratorio*.
- [05 | Microsoft Defender Suite](05-defender-suite/README.md) — *parcial*: identidad, endpoint, XDR y CSPM; APIs, contenedores y storage en diseño.
- [08 | Seguridad de red en Azure](08-seguridad-red-azure/README.md) — *diseño + IaC*: VNet, NSG y Private Endpoints; no desplegado.

### 5. Operaciones de seguridad, forense y respuesta

- [09 | Microsoft Sentinel](09-microsoft-sentinel/README.md) — *diseño en curso*: KQL y automatización.
- [10 | ELK Stack Security](10-elk-stack-security/README.md) — *validado en local*: pila ELK con Docker Compose, 15 eventos sintéticos, 6 consultas KQL y dashboard exportado; sin Azure ni datos reales.
- [12 | Forense cloud y respuesta](12-forense-cloud-respuesta/README.md) — *diseño y KQL*: evidencia, timeline y playbook.

### 6. Cumplimiento y arquitectura de control

- [Matriz de cumplimiento](cumplimiento-normativo/README.md) — mapeo a MCSB, NIS2, ENS, CIS, ISO 27001 y OWASP API Top 10, con brechas declaradas.

### 7. IA local y desarrollo asistido

- [ai-agent-local-lab](https://github.com/lanuzalorenzo/ai-agent-local-lab) — laboratorio local-first con Ollama, OpenCode y modelos abiertos.
- [Caso de estudio de migración a OpenCode](https://github.com/lanuzalorenzo/ai-agent-local-lab/blob/main/CASE_STUDY_OPENCODE_MIGRATION.md) — decisiones, configuración y límites.

---

## 📊 Estado de validación

| Estado | Significado |
|---|---|
| **Validado** | Ejecutado en laboratorio y con evidencia documentada. |
| **Parcial** | Implementado en código o configuración, pero sin ejecución completa o con brechas. |
| **Runbook preparado** | Pasos y comandos escritos, todavía no ejecutados. Se muestra como «Diseño · runbook listo». |
| **Diseño** | Arquitectura, procedimiento o IaC documentados; no desplegados. |
| **Pendiente** | Identificado y no iniciado. |

La tabla de cada módulo y la [matriz de cumplimiento](cumplimiento-normativo/README.md) usan este criterio. No se presenta un diseño como una validación.

---

## 🧪 Caso de estudio end-to-end

**De la API al SOC:** un recorrido que conecta arquitectura, identidad, red, entrega, detección y respuesta.

1. **Arquitectura:** API .NET con DTOs, validación y separación de responsabilidades.
2. **Identidad:** Entra ID, OAuth 2.0/PKCE, validación JWT y MFA.
3. **Red:** VNet, NSG, Private Endpoints y Key Vault sin acceso público (IaC).
4. **Entrega:** pipeline con tests, Gitleaks, CodeQL, Trivy SCA, contenedor no-root e IaC.
5. **Detección:** diagnóstico a Log Analytics y consultas KQL en Sentinel.
6. **Validación ofensiva:** BOLA, mass assignment y revisión de JWT sobre la API local.
7. **Respuesta:** preservación de evidencia, timeline y playbook NIST.

Enlaces: [API](https://github.com/lanuzalorenzo/lab-api-local-azure) · [módulo 07](07-devsecops/README.md) · [módulo 11](11-hacking-etico-api/README.md) · [módulo 12](12-forense-cloud-respuesta/README.md).

---

## 🛠️ Organización

Cada módulo incluye:

- `README.md` con alcance, objetivos, prácticas y estado.
- `bitacora/` con el registro cronológico.
- `practicas/` con procedimientos y limitaciones; cuando la práctica es ejecutable, incluye `runbook.md` y `evidencias/`.
- `lab/` con los artefactos locales de ejecución (por ejemplo, `docker-compose.yml`, pipeline y scripts).
- `docs/` con informes técnicos y plantillas.
- `docs/laboratorio-final/` con la arquitectura, el plan de ejecución y el índice de evidencias del laboratorio integrado.

El código de la carga de trabajo se versiona en [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure).

---

## 📫 Contacto

- **Autor:** Lorenzo Lanuza Arellano — *Software Architect | .NET, DevSecOps & Cloud Security*
- **LinkedIn:** [linkedin.com/in/lanuzalorenzo](https://www.linkedin.com/in/lanuzalorenzo)
- **GitHub:** [github.com/lanuzalorenzo](https://github.com/lanuzalorenzo)
- **Email:** [lanuzalorenzo@gmail.com](mailto:lanuzalorenzo@gmail.com)

---

## ⚖️ Licencia y responsabilidad

Material técnico y formativo. No acredita configuraciones de producción ni certificaciones. No incluye secretos, identificadores reales ni datos personales. Distribuido bajo licencia [MIT](LICENSE).
