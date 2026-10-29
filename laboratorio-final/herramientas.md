# Herramientas del laboratorio

> **Última revisión:** 2026-10-29.
>
> **Alcance:** qué herramienta resuelve cada necesidad del laboratorio, por qué se eligió y qué alternativa se descartó. No es un catálogo: una herramienta sin práctica o evidencia detrás no figura como usada.

## Cómo se elige

1. **Coste cero y local** siempre que el caso lo permita.
2. **Reproducible:** comando, plan o plantilla versionada.
3. **Evidencia exportable:** salida de texto, JSON o CI; una captura sola no basta.
4. **No oculta el mecanismo** cuando el objetivo es entenderlo.
5. **Encaja en el runbook o en CI** sin infraestructura adicional.

Cuando dos herramientas cumplen, se elige la que produce evidencia más fácil de verificar, no la más conocida.

## Herramientas en uso

| Necesidad | Herramienta | Por qué | Alternativa descartada | Evidencia | Estado |
|---|---|---|---|---|---|
| Ver OAuth 2.0/PKCE paso a paso | `bash`, `curl`, `openssl`, `jq`; API Node local | Deja ver cada intercambio y cada parámetro | Postman: cómodo para repetir, pero oculta el intercambio que se quería diseccionar | [Práctica 01 del módulo 01](../01-seguridad-azure/practicas/01-pkce-manual/README.md) | **Parcial**: runbook completo, evidencia pendiente |
| Validar JWT en la API | .NET 10, JwtBearer, xUnit | Misma pila que el workload y aserciones en CI | Validación manual con jwt.io: no repetible | [Módulo 01](../01-seguridad-azure/README.md) | **Validado** en CI |
| Configurar identidad y acceso | Microsoft Entra admin center y Azure portal | La política se configura donde vive y se lee el efecto | Microsoft Graph PowerShell: automatizable, pero el caso era entender la política | [Módulo 02](../02-identity-security/README.md) | **Validado** documental; PIM parcial |
| Auditar y priorizar la postura | Defender for Cloud, Azure Policy, Azure Resource Graph | Inventario, cumplimiento y recomendaciones sin desplegar | Azure CLI o scripts de Resource Graph: más repetibles, no era el objetivo | [Módulos 03](../03-cloud-audits/README.md) y [04](../04-defender-for-cloud/README.md) | **Validado** documental |
| Gates de pipeline y supply chain | GitHub Actions, Gitleaks, CodeQL, Trivy, Dependabot, `dotnet`, Docker | Gratis en repositorio público y bloquea el merge | Snyk o SonarCloud: cuenta y token adicionales | [Módulo 07](../07-devsecops/README.md) | **Validado** en CI |
| Infraestructura como código | Bicep, `bicep build`, Trivy config | Nativo de Azure, sin estado remoto | Terraform: estado y toolchain extra para el alcance del laboratorio | [Módulo 08](../08-seguridad-red-azure/README.md) | **Validado** estáticamente |
| Ingesta, búsqueda y dashboard local | Elasticsearch, Logstash y Kibana 8.19.23; Docker Compose; `curl` | Coste cero y control total del dato | Sentinel: workspace y coste, previsto para Fase 2; Wazuh: añade HIDS, fuera de alcance | [Evidencia ELK](evidencias/2026-10-19-10-elk-ingesta/README.md) | **Validado** |
| Probar autorización por objeto y función | xUnit, `WebApplicationFactory`, `curl` | Pruebas repetibles con aserciones y datos sintéticos | Burp Suite o ZAP: exploración manual y escaneo, sin aserciones para este caso | [Evidencia BOLA](evidencias/2026-10-21-11-api-bola/README.md) | **Validado**; BFLA parcial |
| Detección con KQL | Sentinel y KQL | Es la cadena que se desplegará en Fase 2 | ELK ya validado como patrón local; no sustituye a Sentinel | [Módulo 09](../09-microsoft-sentinel/README.md) | **Diseño** |
| Respuesta y forense | Tabletop y KQL revisado; sin herramienta de recolección | El caso era decidir, no recolectar | KAPE o Velociraptor: pendientes de evaluar | [Módulo 12](../12-forense-cloud-respuesta/README.md) y [acta](evidencias/2026-10-22-12-tabletop/README.md) | **Parcial** |

Azure CLI no figura porque ninguna práctica lo ejecutó: identidad y postura se revisaron en el portal. Entrará cuando un runbook tenga que repetir un despliegue.

## Pendientes de elección

| Necesidad | Candidatas | Criterio de entrada | Estado |
|---|---|---|---|
| Carga y rate limit: 120 req/min y cuerpo de 16 KB | k6, Apache JMeter, NBomber | Producir un `429` observado con latencias y limitaciones declaradas | **Pendiente** |
| Escaneo dinámico de la API | OWASP ZAP, Burp Suite Community | Añadir cobertura que las pruebas de integración no dan, sin sustituirlas | **Pendiente** |
| Recolección forense | KAPE, Velociraptor, scripts de Azure | Preservar evidencia con integridad y cadena de custodia | **Pendiente** |
| Runtime de contenedores en AKS (Fase 2) | Falco, frente a Defender for Containers | Detectar comportamiento anómalo con reglas y medir el ruido antes de compararlo con el producto de Azure | **Pendiente** |

JMeter es una opción válida y, si ya se conoce, reutilizarlo tiene sentido: el plan `.jmx` se versiona y se ejecuta sin interfaz con `jmeter -n -t plan.jmx -l resultados.jtl -e -o informe/`. Frente a k6 o NBomber pesa más —JVM y XML— y encaja peor en una revisión por diff. La elección se hace al escribir el runbook, no antes.

Falco no se evalúa hasta que exista el clúster de Fase 2. Su papel será contrastar el control de Azure, no montar un stack paralelo.

## Qué no prueba cada herramienta

- `trivy config` revisa la plantilla, no que el NSG bloquee tráfico real.
- Un `429` generado desde un portátil no demuestra el comportamiento con IPs distribuidas ni detrás de APIM.
- CodeQL y Gitleaks reducen riesgo; no certifican ausencia de fallos.
- Defender for Cloud mide configuración y recomendaciones, no tráfico.
- Las pruebas con `X-Test-User` no validan Entra ID real.
- El tabletop demuestra criterio de decisión, no recolección técnica.

## Mantenimiento

Una fila cambia cuando cambia la práctica que la usa, no cuando cambia una preferencia. Si una herramienta no tiene runbook ni evidencia, permanece en pendientes y no se presenta como adoptada.
