# Laboratorio final

> **Estado:** Parcial (2026-11-28). Fase 0 cerrada. La red y la API se desplegaron en la capa gratuita el 2026-11-26 y se retiraron el 2026-11-28; la capa de pago —Key Vault, Private Endpoints, DNS privado, App Service y observabilidad— sigue en Diseño. Evidencias de ejecución y documentales, con fecha y resultado, en el [índice](evidencias/README.md).

El laboratorio tiene una aplicación principal, [**Comicteca**](https://github.com/lanuzalorenzo/comicteca), que recibe lo que ya está probado en un banco de pruebas, [**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure). Conecta los doce módulos sobre esas dos cargas. No es una colección de prácticas aisladas, sino el recorrido que las pone en orden: cada capa se activa, se valida y se retira, y no se abre la siguiente hasta que la anterior tiene prueba.

Se practica cerradura a cerradura: primero en local y sin coste; después, Azure con autorización y presupuesto.

## Cómo se lee

- [Arquitectura de referencia](arquitectura.md): capas, flujos, límites de confianza y orden de activación.
- [Plan de ejecución](plan-ejecucion.md): fases, gates, costes y limpieza.
- [Herramientas](herramientas.md): qué se usa en cada caso, por qué y qué alternativas se descartaron.
- [VM de pruebas](vm-de-pruebas.md): importar Kali, cifrar el disco del perfil y dejar un snapshot base.
- [Índice de evidencias](evidencias/README.md): qué se ejecutó, cuándo y dónde está la prueba.
- [Plantilla de runbook](../plantillas/runbook-template.md) y [de evidencia](../plantillas/evidencia-template.md).

## Las capas

| Capa | Qué incluye | Estado |
|---|---|---|
| Cargas | Comicteca (aplicación principal) y EcommerceApi (banco de pruebas): API .NET, DTOs, autorización por propietario, tests | **Validado en CI** en el banco de pruebas y **en local y CI** en la aplicación principal; caso de caída intermitente del CLR por `libunwind` en una solución .NET distinta de EcommerceApi, con resultado **Validado en local** ([evidencia](evidencias/2026-11-09-dotnet-clr-libunwind/README.md)); **API desplegada en Container Apps** el 2026-11-26 y retirada el 2026-11-28 ([evidencia](evidencias/2026-11-26-08-red-y-api/README.md)) |
| Identidad | Entra ID, OAuth 2.0/PKCE, JWT/JWKS, RBAC, Managed Identities | Ver módulos [01](../01-seguridad-azure/README.md), [02](../02-identity-security/README.md) y [06](../06-identity-protection/README.md) |
| Red | VNet, subredes, NSG, Private Endpoints, DNS privado | **Validado en la capa gratuita**: VNet, NSG y subredes desplegadas el 2026-11-26 y retiradas el 2026-11-28; Private Endpoints y DNS privado en **Diseño**. Ver el [módulo 08](../08-seguridad-red-azure/README.md) |
| Datos y secretos | Key Vault, Storage, acceso privado | **Diseño** |
| Observabilidad | Log Analytics, Application Insights, diagnóstico | **Diseño** |
| Detección y respuesta | Defender for Cloud, Sentinel, KQL, playbooks | **Diseño**; ver módulos [04](../04-defender-for-cloud/README.md), [05](../05-defender-suite/README.md) y [09](../09-microsoft-sentinel/README.md) |
| Validación ofensiva | OWASP API Top 10, BOLA/BFLA, mass assignment, rate limit, límite de cuerpo, DAST | **Validado en local** en BOLA, rate limit y límite de cuerpo; BFLA y DAST parciales. Ver [módulo 11](../11-hacking-etico-api/README.md) y sus evidencias [BOLA](evidencias/2026-10-21-11-api-bola/README.md), [rate limit](evidencias/2026-11-05-11-api-rate-limit/README.md), [carga](evidencias/2026-11-05-11-api-rate-limit-carga/README.md), [límite de cuerpo](evidencias/2026-11-12-11-api-body-limit/README.md), [DAST](evidencias/2026-11-08-11-api-dast/README.md) y [agente autónomo](evidencias/2026-11-22-11-api-agente/README.md) |
| Forense | Recolección, integridad, timeline, cadena de custodia | **Parcial**: tabletop de decisión; recolección pendiente. Ver [módulo 12](../12-forense-cloud-respuesta/README.md) |
| Laboratorio local | ELK, logs sintéticos, dashboards | **Validado en local**; ver [módulo 10](../10-elk-stack-security/README.md) y su [evidencia](evidencias/2026-10-19-10-elk-ingesta/README.md) |

## Reparto de repositorios

| Repositorio | Responsabilidad |
|---|---|
| `portfolio-ciberseguridad-lorenzo` | Arquitectura, runbooks, plantillas, evidencias y narrativa. |
| `comicteca` | Aplicación principal: web, API y cliente Android en .NET MAUI, este último en **Diseño** y sin APK probado en un móvil; código, tests, Docker y CI donde se aplican los controles probados. |
| `lab-api-local-azure` | Banco de pruebas: código, tests, Dockerfile, CI e IaC donde se estrena cada control. |
| `lab-ia-aprendizaje` | Laboratorio de IA independiente; no forma parte del laboratorio de seguridad. |

## Reglas

- Nada se despliega sin autorización explícita, suscripción de laboratorio, presupuesto, resource group temporal, datos sintéticos y plan de limpieza.
- No se ejecuta en producción ni con datos reales.
- Lo no ejecutado se marca como **no ejecutado**; un runbook preparado no es una validación.
- Cada evidencia elimina secretos, IPs internas, identificadores reales y datos personales.
- Los estados coinciden con el README del módulo, la web y el perfil.

## Próximo paso

La Fase 0 se cerró el 2026-10-22 con tres evidencias locales; después llegaron la inclusión de ficheros del módulo 11 (2026-11-02), el rate limit secuencial y de carga (2026-11-05), el baseline DAST (2026-11-08), el caso de caída intermitente del CLR por `libunwind` (2026-11-09), con la mitigación local validada, y el PKCE con tenant (2026-11-26). La capa gratuita de la Fase 1 se ejecutó el 2026-11-26 (red y API) y su grupo se eliminó el 2026-11-28; la capa de pago no se inicia hasta que haya autorización y presupuesto. En local quedan la recolección técnica del módulo 12 y confirmar el arreglo de `libunwind` en Ubuntu.
