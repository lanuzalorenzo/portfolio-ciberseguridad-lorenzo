# Evidencia — Tabletop forense del módulo 12 (INC-2026-001)

> **Tipo:** ejecución — ruta B (decisión) de [`plantillas/evidencia-template.md`](../../../plantillas/evidencia-template.md), sin recolección técnica.
> **Resultado:** PASS en los cuatro criterios del runbook, con las limitaciones de la sección 8.
> **Fecha:** 2026-10-22.
> **Runbook utilizado:** [`12-forense-cloud-respuesta/practicas/03-playbook-respuesta/runbook.md`](../../../12-forense-cloud-respuesta/practicas/03-playbook-respuesta/runbook.md).
> **Entorno:** ninguno. Simulacro sobre documentación, datos sintéticos, sin suscripción de Azure.
> **Coste:** 0.
> **Limpieza:** no aplica.
> **Recursos desplegados:** 0.

> Alguien entra por una puerta abierta y usa la identidad de la aplicación para leer una contraseña guardada. El ejercicio mide si se cierra la puerta correcta: aquí era la identidad, no el cortafuegos. No se ejecutó nada; las pistas las puso el facilitador.

## 1. El caso

`INC-2026-001` sobre el laboratorio `rg-lab-forense`. La API `app-api-lab` es una aplicación .NET que corre en App Service con identidad gestionada y lee su cadena de conexión del secreto `sql-conn` en `kv-lab-forense`. La red se controla con `nsg-app`.

Los hechos, en orden:

| Hora | Fuente | Hecho |
|---|---|---|
| 07:43Z | Entra ID AuditLogs | Se añade una **credencial nueva** (secret) a la aplicación registrada de `ops-red@lab`. Sin ticket de cambios |
| 07:58Z | Activity Log | `ops-red@lab` (**Network Contributor**) añade a `nsg-app` la regla `Allow-Any-SSH`: `22/tcp` desde `Internet` a la subred de aplicación. Por portal |
| 08:14Z | Key Vault audit | `app-api-lab` lee `sql-conn` desde `203.0.113.45`, fuera del rango habitual. La API responde con normalidad |
| 08:20–08:35Z | App Service / Log Analytics | Pico de **`401`** en `POST /api/orders`: de ~2/min a ~140/min. Sin `5xx` |
| 09:47Z | Key Vault audit | Segunda lectura de `sql-conn` (**versión 2**) desde `198.51.100.77`, misma identidad |
| T+45 | Dirección | Presión para restablecer el servicio en hora punta |

**Qué hace difícil el caso.** Tres planos distintos se cruzan y cada uno pide una contención diferente:

- **Red:** el puerto 22 abierto a Internet. Se cierra con el NSG, que es *stateful*: no corta sesiones ya establecidas.
- **Identidad:** `app-api-lab` leyó el secreto. Un token emitido **no se revoca** cerrando puertos ni rotando el secreto; caduca solo.
- **Datos:** el secreto `sql-conn` está filtrado. Rotarlo lo invalida, pero si la identidad sigue teniendo permiso, lee la versión nueva.

Mientras no se distingan esos tres planos, cualquier decisión parece razonable y ninguna es suficiente.

## 2. Timeline de decisiones

| Marca | Decisión tomada |
|---|---|
| T+00 | Severidad **ALTA**, escalada a **CRÍTICA** si se confirma acceso a datos. Orden: contener → bloquear IP → rotar connection string → investigar |
| T+10 | Capturar el NSG y revertir **después**. Autoriza Cloud; comprobar el IaC. Hipótesis: el incidente empieza en **red** |
| T+20 | El pico de `401` es **ataque**. No se correlaciona con la connection string. Severidad al alza |
| T+30 | Compromiso declarado: **la identidad**. No rotar el secreto. Capturar y **aislar el host** |
| T+45 | **Mantener el aislamiento** frente a la presión. `ops-red@lab` tratada como cuenta comprometida. Restauración en **2 h** condicionada a vigilancia |

## 3. Propuestas del responsable y valoración

Cada propuesta se evalúa por separado: si es válida, si lo es solo en parte, o si no se sostiene. La corrección se aplica en la sección 4.

### 3.1 Severidad ALTA con escalada a CRÍTICA

**Válida.** Una identidad de aplicación leyendo una credencial de producción desde una IP fuera de rango ya justifica ALTA sin confirmar acceso a datos: el secreto está comprometido por el hecho de haberse leído. El matiz que faltaba: la escalada no depende de «acceso a la base de datos», sino de **si la identidad tiene permiso sobre el secreto** (que lo tiene, porque lo leyó). La severidad debía ser ALTA desde el primer minuto y CRÍTICA en cuanto apareció la segunda lectura desde otra IP.

### 3.2 Contener bloqueando la IP en el NSG

**Parcialmente válida.** Cierra el flujo de red desde esa IP y es barato. No resuelve el caso por tres motivos:

1. La lectura de Key Vault ocurre en el **plano de datos con un token**; el NSG no la ve ni la corta.
2. Una IP es un indicador efímero: el T+30 lo demuestra con una segunda IP distinta.
3. Un cambio manual en el NSG lo revierte el siguiente despliegue si lo gestiona IaC.

### 3.3 Rotar la connection string antes de investigar

**No válida como primera acción.** Tres costes y ningún beneficio inmediato:

- Destruye la **versión exacta del secreto** que usó el atacante: se pierde la correlación entre secreto, hora y uso posterior.
- Puede **tumbar la aplicación** si no recarga bien la configuración.
- **No detiene** a una identidad comprometida: con permiso vigente, lee la versión nueva.

La rotación es necesaria, pero **después** de capturar metadatos y **a la vez** que se corta la identidad.

### 3.4 Evidencia: Key Vault audit y reglas efectivas del NSG

**Válida pero incompleta.** El orden elegido (audit log, luego NSG) respeta bien la volatilidad de la configuración. Faltaba la pieza **más volátil**: el estado del host (`who`, `last`, `ss -tnp`, procesos). Si hay una sesión SSH viva, o se captura en minutos o se pierde para siempre.

### 3.5 Revertir el NSG solo después de capturarlo

**Válida, con dos condiciones que faltaban.** Es correcto preservar la regla antes de sobrescribirla. Faltaba:

- **Hora límite** para la contención: con el puerto 22 abierto a Internet, «cuando acabe de capturar» es exposición indefinida. La regla del runbook es capturar lo barato (2–5 min) y contener.
- **Advertencia de NSG *stateful*:** revertir la regla no cierra una sesión ya establecida. Sin mirar el host, la contención es aparente.

El razonamiento sobre el IaC —comprobar que el despliegue no reabre el puerto— era correcto y se mantiene.

### 3.6 Hipótesis: el incidente empieza en la red

**Plausible pero no demostrada.** Es la hipótesis más probable y la cadena existe: SSH abierto → entrada al host → uso de la identidad del App Service → lectura del secreto. Pero le faltaban dos eslabones sin probar: **cómo se entró** en el host (credencial, clave o vulnerabilidad) y **con qué identidad** se leyó el secreto. Con dos IPs distintas en T+30, la hipótesis correcta pasa a ser «la identidad está comprometida», y la red queda como **vector de entrada probable, no como causa**.

### 3.7 El pico de `401` es ataque porque una aplicación rota daría `500`

**Parcialmente válida.** La intuición acierta en el caso de un fallo de base de datos: ahí se espera `5xx`. Falla en dos puntos:

- Si lo que se rompe al rotar es una credencial **de identidad** (client secret, clave de firma de JWT), la API no valida tokens y responde **`401`**, no `500`. Es decir: el `401` podría ser consecuencia de la propia respuesta, no del atacante.
- El dato que separa ataque de aplicación rota es la **cardinalidad**: un pico desde **una** IP repitiendo el mismo token sugiere reintento o app rota; desde **muchas** IPs con tokens distintos, fuerza bruta. Ese dato no se pidió, así que «ataque» era una lectura razonable, no una conclusión.

El acierto que sí se sostiene: **no correlacionar** la connection string con el `401`. Una cadena de conexión da acceso a la base de datos, no a la API.

### 3.8 Dos IPs con la misma identidad ⇒ identidad comprometida

**Válida, y es el mejor razonamiento de la sesión.** La rotación de IP descarta un bloqueo por origen y apunta al sujeto que autentica. Es la inferencia que reordena todo el incidente y la que debía haber llegado antes.

### 3.9 No rotar el secreto

**Válida en el fondo, errónea en la conclusión.** Acierta en lo importante: rotar sin cortar la identidad es teatro. Falla al concluir que «no sirve de nada»: deja viva indefinidamente una credencial que sabes filtrada. La secuencia correcta: **capturar metadatos (nombre, versión, hora, identidad — nunca el valor) → cortar la identidad → rotar en ese mismo momento**.

### 3.10 Capturar y aislar el host

**Válida.** Es la decisión que evita destruir prueba y detener el daño a la vez. Dos precisiones: aislar por NSG no mata la sesión establecida, y aislar el App Service implica **aceptar caída de servicio**, que es una decisión de negocio, no técnica.

### 3.11 Mantener el aislamiento frente a la presión de negocio

**Válida y bien priorizada.** Con un host con acceso remoto y una identidad capaz de alterar datos, la disponibilidad cede ante integridad y confidencialidad. Lo que faltaba era la contrapartida: dar a negocio un **criterio verificable** de reapertura, no solo una negativa.

### 3.12 Restauración en 2 horas con vigilancia

**Razonable, pero incompleta.** Dos horas es una estimación defendible para bloquear SSH, retirar la credencial y acotar tokens. Faltaba definir **qué tiene que ser cierto para reabrir**: sesiones cerradas, credencial retirada, roles revisados, secreto rotado, logs de la ventana capturados y vigilancia activa durante un periodo mínimo.

### 3.13 `ops-red@lab` como cuenta comprometida

**Hipótesis razonable, no concluyente.** Una credencial nueva sin ticket, 15 minutos antes del cambio de NSG, es un patrón de persistencia típico. Pero también encaja con un administrador legítimo que no registró el cambio, o con un insider. Lo correcto es tratarla como comprometida **de forma conservadora** (deshabilitar, revocar sesiones, rotar su credencial, revisar sus roles) y **verificarlo en paralelo**, no esperar a tener certeza para actuar.

### 3.14 Propuestas que faltaron

- **Cortar en el plano de identidad** (restringir RBAC sobre el Key Vault, firewall del Key Vault, deshabilitar la cuenta y revocar tokens). Es la contención que realmente detiene el acceso.
- **Comprobación de persistencia** antes de erradicar: credenciales nuevas, roles añadidos, `authorized_keys`, slots de despliegue.
- **Hora límite** de contención y **criterio de reapertura**.
- **Cardinalidad del `401`** y exportación de logs de la ventana.

## 4. Decisiones óptimas y por qué

La secuencia que el caso pide, en orden:

| Orden | Acción | Por qué en ese punto |
|---|---|---|
| 1 | Abrir incidente, severidad **ALTA**, ventana 07:00–10:00Z, responsable SecOps | El secreto ya está comprometido por haberse leído; no hace falta esperar confirmación de acceso a datos |
| 2 | Capturar lo barato y volátil (2–5 min): `who`, `last`, `ss -tnp`, procesos; JSON del NSG; audit log del Key Vault con versión; hashes | Es lo único que no se puede recuperar. El resto de logs tiene retención; la sesión y la configuración, no |
| 3 | **Cortar identidad:** restringir el permiso de `app-api-lab` sobre `kv-lab-forense`, restringir el firewall del Key Vault, deshabilitar `ops-red@lab` y revocar sus sesiones y credenciales | Es el único corte que detiene la lectura del secreto. Cerrar puertos no lo hace; rotar sin cortar tampoco |
| 4 | Cerrar `22/tcp` en el NSG (tras capturar), comprobando que el IaC no lo reabra, y verificar si hay sesiones vivas | El NSG es *stateful*: hay que confirmar en el host que la sesión murió, no suponerlo |
| 5 | **Rotar `sql-conn`** con los metadatos ya capturados, coordinando la recarga de la aplicación | Invalida lo filtrado sin destruir la trazabilidad. Después de cortar la identidad, no antes |
| 6 | Investigar: AuditLogs de las 07:43, Activity Log del NSG, cardinalidad de IPs y tokens del `401`, persistencia (credenciales, roles, `authorized_keys`, slots) | Con la identidad cortada, la investigación no compite con la contención |
| 7 | Restaurar con criterio: sesiones cerradas, credencial retirada, roles revisados, secreto rotado, logs capturados, vigilancia ≥30 min | Reabrir sin criterio es volver al mismo estado con el mismo token vivo |
| 8 | Documentar el riesgo residual: tokens válidos hasta caducar, rotación verificada, lecciones | El incidente no termina cuando el servicio responde |

**Regla que resume el caso:** se contiene por el plano más privilegiado, no por el más visible. La red es lo que se ve; la identidad es lo que manda.

## 5. Huecos detectados en el playbook

1. **Falta un orden de contención por plano** (identidad → red → secreto → datos). La tabla §6.3 solo distingue «exfiltración activa» de «sin actividad activa».
2. **No hay criterio para distinguir ataque de aplicación rota en un pico `401`**: falta la cardinalidad de IPs y tokens, y el aviso de que rotar una credencial de identidad produce `401`, no `500`.
3. **La tabla de volatilidad asume acceso al host**, pero el workload es App Service: no describe cómo se captura estado en PaaS ni qué es «host» ahí.
4. **No se advierte del NSG *stateful*** ni de la validez de los tokens tras revocar sesiones.
5. **No existe comprobación de persistencia** previa a la erradicación.
6. **No hay criterio de restauración**: hora objetivo, vigilancia mínima ni condiciones de reapertura.
7. **No hay autoridad de caída de servicio declarada de antemano**: la asumió AppSec durante el ejercicio, no por diseño.

## 6. Acciones de mejora

| # | Acción | Responsable | Dónde |
|---|---|---|---|
| 1 | Añadir el **orden de contención por plano** (identidad → red → secreto → datos), con NSG *stateful* y tokens vigentes | SecOps | `practicas/03-playbook-respuesta/` |
| 2 | Añadir la **tabla de decisión del `401`** (cardinalidad de IPs, tokens repetidos, `5xx` frente a `401`) como paso de triaje | AppSec | `practicas/03-playbook-respuesta/` |
| 3 | Definir la **captura de estado del host en App Service** y probarla en la variante de laboratorio | Cloud | Runbook §6.2 |
| 4 | Escribir la **comprobación de persistencia** previa a la erradicación | Cloud | Playbook, fase de erradicación |
| 5 | Fijar el **criterio de restauración** y la autoridad de caída de servicio | SecOps | Playbook, fase de recuperación |
| 6 | Repetir el tabletop como **iteración 2** tras T5, con protocolo ciego, una variable cambiada y la rúbrica de §7 | SecOps | Este runbook, §9 |

## 7. Repetición prevista — iteración 2

**Decisión:** el caso **se repite**, pero no para practicar la respuesta aprendida. Se repite para comprobar si el criterio se ha interiorizado y si el playbook corregido aguanta un escenario distinto.

**Cuándo.** No antes de cerrar T5 (App Service desplegado y con diagnóstico). Dos razones: deja pasar el tiempo suficiente para no medir memoria a corto plazo, y permite que la segunda pasada incluya **telemetría real** en vez de inyecciones. La fecha la fija el plan de trabajo interno, no esta acta.

**Protocolo ciego (el facilitador lo hace cumplir):**

1. Esta acta permanece **sin abrir** hasta que la iteración 2 esté cerrada. Tampoco se releen las lecciones L2 y L3.
2. El facilitador sigue el guion del runbook y **no revela** el orden de las inyecciones.
3. Se registra en carpeta propia: `YYYY-MM-DD-12-tabletop-iter2/`, con el acta y la comparativa.
4. Si en algún momento se consulta esta acta, se declara en la nueva y el resultado se marca como **no ciego**.

**Qué cambia (una sola variable por iteración):**

| Iteración | Variable alterada | Qué prueba |
|---|---|---|
| 2 | El pico de `401` viene de **una sola IP** repitiendo el mismo token | ¿Distingue ataque de aplicación rota por la cardinalidad? |
| 3 | **No hay segunda lectura** del secreto | ¿Busca persistencia o cierra el incidente antes de tiempo? |
| 4 | `ops-red@lab` resulta ser un administrador con **ticket tardío** | ¿Sostiene un falso positivo sin romper el proceso? |
| 5 | El Key Vault **no usa RBAC**: todo el equipo tiene acceso al secreto | ¿Cambia el análisis de identidad al de personas? |

**Rúbrica de comparación** (idéntica al runbook §9):

| Métrica | Iteración 1 (2026-10-22) | Umbral |
|---|---|---|
| Minutos hasta **cortar la identidad** | No se cortó: se propuso rotar antes y luego no rotar | ≤ 10 |
| Evidencia volátil capturada **antes** de contener | 0 de 3 (host no capturado) | ≥ 3 |
| ¿Pidió cardinalidad del `401`? | No | Sí |
| ¿Rotó sin cortar la identidad? | No rotó | No |

La iteración 1 queda como **línea base**. El objetivo de la 2 no es «acertar»: es que las cuatro métricas estén dentro del umbral **sin haber leído esta acta**.

## 8. Limitaciones

- **No se ejecutó nada**: ni consultas, ni comandos, ni accesos. Las «fuentes» son inyecciones del facilitador.
- **Una sola persona** con tres sombreros: sin contraste de roles ni presión real. Las objeciones vinieron del facilitador, no de un equipo.
- **Tiempos ficticios**: no miden detección ni respuesta.
- **Sin Azure**: no se validó telemetría, retención ni coste.
- **Queda abierto** si se rotó la connection string; afecta a la atribución del pico de `401`.
- La evidencia prueba **decisiones trazables**, no capacidades técnicas.

### 8.1 Lo que no se ejecutó y lo que correspondía

| No ejecutado | Lo que correspondía | Momento |
|---|---|---|
| Estado del host (`who`, `last`, `ss -tnp`, procesos) | Capturarlo como evidencia #1 antes de tocar el NSG | T+00 / T+10 |
| Corte de identidad (RBAC, firewall del Key Vault, cuenta `ops-red@lab`) | Proponerlo al abrir el incidente y ejecutarlo en ≤ 10 min | T+00 / T+10 |
| Cardinalidad de IPs y tokens del `401` | Pedir logs HTTP con IP y token antes de calificarlo de ataque | T+20 |
| Comprobación de sesión SSH viva | Verificarla en el host tras revertir el NSG | T+10 |
| AuditLogs de las 07:43 | Revisarlos en cuanto apareció el cambio de NSG: era el indicio de persistencia más antiguo | T+10 |
| Hora límite de contención y criterio de reapertura | Fijarlos al decidir el aislamiento | T+30 |
| Autoridad de caída de servicio | Declararla al abrir el incidente | T+00 |
| Respuesta a si se rotó la connection string | Registrarla al descartar la rotación | T+20 |
| Hot wash formal | Que el participante enumerase los huecos antes que el facilitador | Cierre |
| Versión completa del guion | Justificar la elección de la versión reducida | Inicio |

Estas omisiones son la causa de varias de las acciones de mejora de §6: el acta prueba decisiones, no ejecución.

## 9. Criterio de cierre

| Requisito del runbook §1 | Cumplido |
|---|---|
| Línea temporal con hora, fuente y hecho | Sí (§1 y §2) |
| Decisión de contención con responsable, criterio y hora | Sí (§4) |
| Evidencias en orden de volatilidad con su origen | Sí (§4, pasos 2 y 6) |
| Huecos del playbook y acciones de mejora | Sí (§5 y §6) |

Resultado: **PASS como tabletop**. El módulo 12 pasa a **Parcial**: el simulacro está hecho; la variante de laboratorio, la recolección técnica y la ejecución de KQL sobre datos reales siguen pendientes.
