# Laboratorio final

> **Estado:** Fase 0 cerrada. Tres evidencias de ejecución (ELK, módulo 10; BOLA/BFLA, módulo 11; tabletop forense, módulo 12) y cuatro documentales o verificables (02, 03, 04 y 07). No hay recursos Azure desplegados.

El laboratorio conecta los doce módulos sobre una sola carga de trabajo: [**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure). No es una colección de prácticas aisladas, sino el recorrido que las pone en orden: cada capa se activa, se valida y se retira, y no se abre la siguiente hasta que la anterior tiene prueba.

Se practica cerradura a cerradura: primero en local y sin coste; después, Azure con autorización y presupuesto.

## Cómo se lee

- [Arquitectura de referencia](arquitectura.md): capas, flujos, límites de confianza y orden de activación.
- [Plan de ejecución](plan-ejecucion.md): fases, gates, costes y limpieza.
- [Herramientas](herramientas.md): qué se usa en cada caso, por qué y qué alternativas se descartaron.
- [Índice de evidencias](evidencias/README.md): qué se ejecutó, cuándo y dónde está la prueba.
- [Plantilla de runbook](../plantillas/runbook-template.md) y [de evidencia](../plantillas/evidencia-template.md).

## Las capas

| Capa | Qué incluye | Estado |
|---|---|---|
| Workload | API .NET, DTOs, autorización por propietario, tests | **Validado en CI**; integración Azure no desplegada |
| Identidad | Entra ID, OAuth 2.0/PKCE, JWT/JWKS, RBAC, Managed Identities | Ver módulos [01](../01-seguridad-azure/README.md), [02](../02-identity-security/README.md) y [06](../06-identity-protection/README.md) |
| Red | VNet, subredes, NSG, Private Endpoints, DNS privado | **Diseño + IaC validada estáticamente** en el [módulo 08](../08-seguridad-red-azure/README.md) |
| Datos y secretos | Key Vault, Storage, acceso privado | **Diseño** |
| Observabilidad | Log Analytics, Application Insights, diagnóstico | **Diseño** |
| Detección y respuesta | Defender for Cloud, Sentinel, KQL, playbooks | **Diseño**; ver módulos [04](../04-defender-for-cloud/README.md), [05](../05-defender-suite/README.md) y [09](../09-microsoft-sentinel/README.md) |
| Validación ofensiva | OWASP API Top 10, BOLA/BFLA, mass assignment | **Validado en local**; BFLA parcial. Ver [módulo 11](../11-hacking-etico-api/README.md) y su [evidencia](evidencias/2026-10-21-11-api-bola/README.md) |
| Forense | Recolección, integridad, timeline, cadena de custodia | **Parcial**: tabletop de decisión; recolección pendiente. Ver [módulo 12](../12-forense-cloud-respuesta/README.md) |
| Laboratorio local | ELK, logs sintéticos, dashboards | **Validado en local**; ver [módulo 10](../10-elk-stack-security/README.md) y su [evidencia](evidencias/2026-10-19-10-elk-ingesta/README.md) |

## Reparto de repositorios

| Repositorio | Responsabilidad |
|---|---|
| `portfolio-ciberseguridad-lorenzo` | Arquitectura, runbooks, plantillas, evidencias y narrativa. |
| `lab-api-local-azure` | Código, tests, Dockerfile, CI e IaC del workload. |
| `lab-ia-aprendizaje` | Laboratorio de IA independiente; no forma parte del laboratorio de seguridad. |

## Reglas

- Nada se despliega sin autorización explícita, suscripción de laboratorio, presupuesto, resource group temporal, datos sintéticos y plan de limpieza.
- No se ejecuta en producción ni con datos reales.
- Lo no ejecutado se marca como **no ejecutado**; un runbook preparado no es una validación.
- Cada evidencia elimina secretos, IPs internas, identificadores reales y datos personales.
- Los estados coinciden con el README del módulo, la web y el perfil.

## Próximo paso

La Fase 0 está cerrada con las tres evidencias locales. La Fase 1 (Azure mínimo) no se inicia hasta que haya autorización, suscripción y presupuesto. En local quedan la reejecución de PKCE con tenant y la recolección técnica del módulo 12.
