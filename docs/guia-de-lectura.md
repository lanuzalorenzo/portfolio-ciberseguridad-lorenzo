# Guía de lectura — cómo entender este portfolio

> **Para quién es:** para quien abre el repositorio por primera vez y no sabe por dónde empezar. No hace falta ser experto en ciberseguridad, pero ayuda entender qué es una API y qué es un token.
>
> **Qué vas a encontrar:** el orden recomendado, un glosario mínimo y un mapa de los doce módulos. La guía no sustituye a la documentación de cada módulo: la ordena.
>
> **Última revisión:** 2026-10-21. Ver [mantenimiento](#10-mantenimiento).

## 1. La idea en cinco líneas

Este portfolio no es una colección de herramientas. Es un **modelo de defensa en profundidad** aplicado a una sola carga de trabajo: una API .NET llamada **EcommerceApi**.

- La API tiene identidad, código, red, entrega, detección y respuesta.
- Cada módulo estudia una capa y declara qué está probado y qué no.
- El hilo conductor es siempre la misma pregunta: **¿qué control protege qué, y cómo lo demuestro?**
- El estado de cada control importa tanto como el control: no es lo mismo un diseño que una evidencia.
- El objetivo del portfolio es mostrar criterio técnico y trabajo real, no acumular documentación.

Si solo lees una frase, que sea esta: **cada módulo es una capa de la misma API, no un tema suelto.**

## 2. Qué no es este portfolio

- **No es un curso.** No enseña ciberseguridad desde cero; documenta trabajo técnico y su evidencia.
- **No es producción.** Los laboratorios son locales o de diseño; no hay recursos Azure desplegados.
- **No es un pentest de terceros.** Todo se limita a un laboratorio propio y a datos sintéticos.
- **No está todo validado.** Hay módulos validados, parciales, en diseño y pendientes. La tabla de estado lo dice.
- **No contiene secretos ni datos reales.** Los identificadores y credenciales están redactados.

## 3. Cómo se lee un módulo

Cada módulo sigue el mismo patrón. No hace falta leerlo entero la primera vez:

| Parte | Pregunta que responde |
|---|---|
| `README.md` | ¿Por qué existe, qué alcance tiene y en qué estado está? |
| `practicas/` | ¿Qué se hizo y con qué controles? |
| `runbook.md` | ¿Cómo se reproduce, paso a paso? |
| `evidencias/` | ¿Qué se observó realmente? |
| `bitacora/` | ¿Qué se aprendió, qué falló y qué queda pendiente? |

**Orden para una primera lectura:** README → práctica → evidencia. El runbook y la bitácora se leen cuando quieres reproducir o entender las decisiones.

## 4. Glosario mínimo

| Término | En una línea |
|---|---|
| **API** | Contrato entre sistemas: un conjunto de endpoints para leer o modificar datos. |
| **Endpoint** | Una URL y un método HTTP (`GET /api/orders`, `POST /api/products`). |
| **Token** | Credencial que el cliente presenta para acceder a la API. |
| **JWT** | Formato de token firmado: `header.payload.signature`. Está codificado, no cifrado. |
| **OAuth 2.0** | Marco de autorización para que una aplicación acceda a una API en nombre de un usuario. |
| **PKCE** | Extensión de OAuth para clientes públicos: ata el código de autorización a quien lo pidió. |
| **RBAC** | Permisos asignados por rol, no por usuario individual. |
| **NSG** | Cortafuegos de Azure por subred o tarjeta de red: filtra IP, puerto y protocolo. |
| **Private Endpoint** | Dirección privada para acceder a un servicio PaaS sin salir a Internet. |
| **SIEM** | Sistema que centraliza logs y permite detectar y correlacionar eventos. |
| **IaC** | Infraestructura como código: la red y los recursos se declaran en Bicep u otra plantilla. |
| **SAST / SCA** | Análisis estático del código / análisis de dependencias y vulnerabilidades. |
| **BOLA / BFLA** | Fallos de autorización a nivel de objeto / de función: acceder a lo ajeno o a una operación privilegiada. |

## 5. Tres rutas de lectura

### Ruta 0 — 15 minutos: entender qué es esto

1. [`README.md`](../README.md) del portfolio.
2. Esta guía.
3. [Índice de evidencias](laboratorio-final/evidencias/README.md).
4. Tabla de estados del README.

**Al terminar:** sabrás qué carga de trabajo se protege, qué capas existen y qué está demostrado.

### Ruta 1 — 60–90 minutos: el hilo identidad + API

1. [Arquitectura de referencia](laboratorio-final/arquitectura.md).
2. [Módulo 01 — OAuth 2.0, PKCE y JWT](../01-seguridad-azure/README.md): documentos 01, 02 y 03.
3. [Módulo 11 — Hacking ético de APIs](../11-hacking-etico-api/README.md): práctica 01 y su [evidencia](laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md).
4. [Módulo 12 — Forense y respuesta](../12-forense-cloud-respuesta/README.md): el playbook, el runbook y su [acta de tabletop](laboratorio-final/evidencias/2026-10-22-12-tabletop/README.md).

**Al terminar:** entenderás cómo se autentica una petición, cómo se autoriza por propietario y qué se puede demostrar con una prueba local.

### Ruta 2 — 3–4 horas: recorrido por capas

1. **AppSec e identidad:** módulos [01](../01-seguridad-azure/README.md) y [11](../11-hacking-etico-api/README.md).
2. **Entrega segura:** módulo [07](../07-devsecops/README.md).
3. **Red:** módulo [08](../08-seguridad-red-azure/README.md).
4. **Detección:** módulos [10](../10-elk-stack-security/README.md) y [09](../09-microsoft-sentinel/README.md).
5. **Respuesta:** módulo [12](../12-forense-cloud-respuesta/README.md).
6. **Cierre:** [laboratorio final](laboratorio-final/README.md) y [matriz de cumplimiento](../cumplimiento-normativo/README.md).

**Al terminar:** tendrás el mapa completo y sabrás qué capas están validadas y cuáles son diseño.

### Ruta 3 — 20 minutos: revisión técnica o reclutamiento

1. README del portfolio.
2. Índice de evidencias.
3. Evidencia local de BOLA/BFLA y módulo 11.
4. Módulo 07: pipeline y controles de supply chain.
5. Matriz de cumplimiento.
6. Repositorio de la API: tests, CI y Bicep.

**Al terminar:** sabrás qué se ha ejecutado, qué se ha documentado y qué queda pendiente, sin leer los doce módulos.

## 6. Mapa de módulos

| # | Módulo | Pregunta que responde | Estado |
|---|---|---|---|
| 01 | [OAuth 2.0, PKCE y JWT](../01-seguridad-azure/README.md) | ¿Cómo se autentica una API y se valida un token? | Parcial: JWT validado en CI; PKCE manual sin evidencia estandarizada |
| 02 | [Identity Security](../02-identity-security/README.md) | ¿Cómo se protege la identidad y el acceso privilegiado? | Validado en laboratorio (documental) |
| 03 | [Cloud Audits](../03-cloud-audits/README.md) | ¿Cómo se audita la postura cloud? | Validado en laboratorio (documental) |
| 04 | [Defender for Cloud](../04-defender-for-cloud/README.md) | ¿Cómo se detectan y priorizan riesgos cloud? | Validado en laboratorio (documental) |
| 05 | [Defender Suite](../05-defender-suite/README.md) | ¿Cómo se cubre identidad, endpoint y XDR? | Parcial |
| 06 | [Identity Protection](../06-identity-protection/README.md) | ¿Cómo se aplican Conditional Access y PIM/JIT? | Diseño |
| 07 | [DevSecOps](../07-devsecops/README.md) | ¿Cómo se integra seguridad en el pipeline? | Validado en CI |
| 08 | [Seguridad de red](../08-seguridad-red-azure/README.md) | ¿Cómo se segmenta y se aísla la carga? | Diseño + IaC |
| 09 | [Microsoft Sentinel](../09-microsoft-sentinel/README.md) | ¿Cómo se detecta con KQL y se automatiza? | Diseño en curso |
| 10 | [ELK Stack Security](../10-elk-stack-security/README.md) | ¿Cómo se centralizan logs y se consultan? | Validado en local |
| 11 | [Hacking ético de APIs](../11-hacking-etico-api/README.md) | ¿Cómo se prueban BOLA, BFLA y mass assignment? | Validado en local; BFLA parcial |
| 12 | [Forense cloud y respuesta](../12-forense-cloud-respuesta/README.md) | ¿Cómo se preserva evidencia y se responde? | Parcial: tabletop ejecutado; recolección técnica pendiente |
| — | [Cumplimiento normativo](../cumplimiento-normativo/README.md) | ¿Qué control cubre qué requisito? | Documentado |

## 7. Cómo verificar sin confiar en la narrativa

El portfolio distingue explícitamente entre **Diseño**, **Runbook preparado**, **Parcial**, **Validado** y **Pendiente**. Clasifica la evidencia de lo validado como **de ejecución**, **documental** o **verificable**. Para comprobarlo:

- [Índice de evidencias](laboratorio-final/evidencias/README.md): qué se ejecutó, cuándo y con qué resultado.
- **Runbooks:** cada comando no ejecutado está marcado como tal; no se inventan salidas.
- **Tests y CI:** en el repositorio [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure).
- **Bicep:** la infraestructura está validada estáticamente; no se presenta como desplegada.
- **Datos:** sintéticos, sin secretos ni identificadores reales.

Si una afirmación no apunta a una evidencia, trátala como hipótesis o diseño.

## 8. Preguntas para comprobar que lo has entendido

1. ¿Cuál es la carga de trabajo del portfolio y por qué se usa una API?
2. ¿Dónde se valida un JWT y qué se comprueba?
3. ¿Por qué un acceso a un objeto ajeno devuelve `404` y no `403`?
4. ¿Qué diferencia hay entre **validado**, **parcial** y **diseño**?
5. Si un NSG permite SSH desde `0.0.0.0/0`, ¿qué harías y qué capturarías antes?

Si puedes responderlas sin mirar, ya tienes el hilo. Si no, vuelve a la Ruta 1.

## 9. Siguiente paso

- Si te interesa la **identidad**: empieza por el [módulo 01](../01-seguridad-azure/README.md).
- Si te interesa la **API**: ve al [módulo 11](../11-hacking-etico-api/README.md) y su evidencia.
- Si te interesa la **operación**: sigue por [detección](../09-microsoft-sentinel/README.md) y [respuesta](../12-forense-cloud-respuesta/README.md).
- Si quieres ver **qué está probado**: abre el [índice de evidencias](laboratorio-final/evidencias/README.md).

## 10. Mantenimiento

- **Última revisión:** 2026-10-21.
- **Actualizar cuando:** cambie el estado de un módulo, se añada o retire una evidencia, cambie la estructura de módulos o enlaces, o se añada una ruta de lectura.
- **No actualizar por:** cambios internos que no afecten a lo que el lector necesita para orientarse.
- **Fuente única:** esta guía vive aquí; la web y el perfil solo enlazan.
- **Checklist rápida:** enlaces locales, estados del mapa, fecha y rutas.

---

**Licencia:** el contenido se distribuye bajo licencia MIT. No acredita configuraciones de producción ni certificaciones.
