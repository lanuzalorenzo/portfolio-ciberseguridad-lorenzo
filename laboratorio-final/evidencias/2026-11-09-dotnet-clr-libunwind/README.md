# Evidencia — Laboratorio final / caída intermitente del CLR por libunwind

> **Identificador:** `2026-11-09-dotnet-clr-libunwind`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** **Validado en local**
>
> **Runbook:** no aplica; es un caso de diagnóstico, no una práctica reejecutable.

Un fallo intermitente es como una bombilla que parpadea solo cuando la tocas: si no repites la maniobra, no sabes si el problema es la bombilla, el interruptor o la instalación. Aquí la maniobra era compilar y probar una solución .NET; el parpadeo, un `Internal CLR error` que abortaba el proceso en varias tandas. La evidencia separa lo medido de lo deducido y atribuye la causa al issue upstream, no a este repositorio.

**In English.** An intermittent failure is like a bulb that flickers only when you touch it: unless you repeat the action, you cannot tell whether the fault is the bulb, the switch or the wiring. Here the action was building and testing a .NET solution; the flicker was an `Internal CLR error` that aborted the process in several batches. This evidence separates measurement from inference and attributes the cause to the upstream issue, not to this repository.

## 1. Contexto

- **Fecha:** 2026-11-09.
- **Responsable:** autor del repositorio.
- **Entorno:** Ubuntu 26.04.1 LTS, kernel 7.0.0-38-generic, glibc 2.43; .NET SDK 10.0.114 y runtime 10.0.14 empaquetados por Ubuntu (snap `dotnet-sdk-100`, revisión 40); `libunwind8` 1.8.3-0ubuntu1 (biblioteca de desenrollado de pila).
- **Objetivo:** una solución .NET local de varios proyectos. No se publica su nombre ni su ruta; la prueba no se ejecutó sobre EcommerceApi.
- **Alcance:** reproducir la caída, descartar dos hipótesis, leer un minivolcado y medir una mitigación. No se instalan binarios oficiales ni se cambia la distribución.
- **Datos:** no se usan datos personales, credenciales ni recursos cloud.
- **Autorización:** no aplica; todo local.
- **Procedencia:** criterio del [módulo 07](../../../07-devsecops/README.md) sobre lo que la pipeline no detecta; este README es el informe y no hay runbook previo. Las cifras del registro original se citan como contexto y no se reejecutaron aquí.

## 2. Síntoma

En tandas secuenciales de `dotnet build` y `dotnet test`, el CLR (Common Language Runtime, el runtime de .NET) abortaba de forma intermitente con código 134:

```text
Fatal error.
Internal CLR error. (0x80131506)
```

El sistema registraba el aviso de apport con señal 6 y `core limit 0`; el proceso que caía era `dotnet`, no el `timeout` que aparecía en el nombre del informe. No hubo pérdida de datos ni daño en discos o servicios. El fallo cortaba tandas de pruebas y desviaba el diagnóstico hacia el componente equivocado.

## 3. Fuentes consultadas

- [`dotnet/runtime#130577`](https://github.com/dotnet/runtime/issues/130577): «.NET 10.0.9 CoreCLR fatal error (0x80131506) in MSBuild multiproc node IPC on Linux». Abierto el 2026-07-12 y cerrado como *completed* el 2026-11-03; etiquetas `area-VM-coreclr` y `tracking-external-issue`.
- [`libunwind/libunwind#993`](https://github.com/libunwind/libunwind/pull/993): corrección de la condición de carrera en `_mem_validate_pipe` que el issue upstream identifica como arreglo de origen.
- Salida local de `dotnet --info`, `ldd` sobre `libcoreclr.so`, `dpkg-query` para `libunwind8`, y `dotnet-dump analyze` con `setthread`, `pe` y `clrstack -all`.
- No se usaron foros ni blogs; la atribución se apoya en el issue y el PR upstream.

## 4. Tres hipótesis y la prueba de control

| Hipótesis | Qué predecía | Prueba | Resultado | Veredicto |
|---|---|---|---|---|
| **H1. Concurrencia de invocaciones.** Varias builds o tests a la vez saturan el entorno. | Sin invocaciones simultáneas, no habría fallo. | Diez tandas secuenciales, una build y un test cada vez. | El fallo siguió: 4 de 10 tandas en cada una de las tres verificaciones del registro original; 2 de 10 en la reejecución de hoy. | **Descartada.** |
| **H2. Acumulación o reutilización de nodos MSBuild.** Los nodos vivos de ejecuciones anteriores contaminan la siguiente. | Empezar con cero nodos evitaría el fallo. | Verificación original con cero nodos MSBuild al arrancar y `MSBUILDDISABLENODEREUSE=1`. | El fallo siguió: 4 de 10. Los nodos nuevos se creaban durante la tanda, pero no había acumulación previa. | **Descartada.** |
| **H3. Defecto del runtime al crear nodos fuera de proceso.** La caída ocurre en la ruta de nodos de MSBuild y desaparece si no se usan. | El volcado mostraría hilos en `StartNewNode` y `-m:1` evitaría la caída. | Lectura del volcado y diez tandas con `-m:1`. | La excepción aparece sin pila gestionada; 4 y 5 hilos están en `StartNewNode` en los dos volcados; `-m:1` dio 0 de 10 hoy y 0 de 20 en el registro original. | **Compatible; causa atribuida upstream.** |

La prueba de control que descartó H1 y H2 es la del registro original: una ejecución secuencial, sin concurrencia del usuario y con cero nodos al arrancar, siguió fallando. Hoy se repitió la parte secuencial con `MSBUILDDISABLENODEREUSE=1` y volvió a fallar (2 de 10); la condición de cero nodos no se reejecutó. Una variable que se controla y no cambia el resultado deja de ser una explicación viable.

## 5. Lectura del volcado

Los minivolcados (minidumps) se generaron con el volcado integrado del runtime. Para leer el hilo correcto hay que fijarlo primero: `pe` sin `setthread` consulta el hilo 0, y el hilo 0 no es el que aborta.

```text
> setthread 8
> pe
Exception object: 00007d064cc00178
Exception type:   System.ExecutionEngineException
Message:          <none>
InnerException:   <none>
StackTrace (generated):
<none>
StackTraceString: <none>
HResult: 80131506
```

El listado de hilos marca el 8 (`0xD0F5`) como el seleccionado. En el volcado de las 10:30, `setthread 19` (`0x5AB6`) devuelve la misma firma. `clrstack -all` muestra cuatro hilos en la ruta `NodeProviderOutOfProcBase.StartNewNode` → `TryConnectToProcess` → `NamedPipeClientStream.ConnectInternal` en el volcado de las 10:55, y cinco en el de las 10:30.

Lo que prueba el volcado: el CLR aborta con `ExecutionEngineException` 0x80131506 en un hilo sin marco gestionado, y hay actividad de creación de nodos en otros hilos. Lo que no prueba: que esa actividad sea la causa del aborto; el hilo que cae no deja pila. La relación se apoya en la desaparición del fallo con `-m:1` y en el issue upstream.

## 6. Causa upstream

El issue `dotnet/runtime#130577` describe la misma firma en una solución .NET de once proyectos y la atribuye a los binarios de .NET empaquetados por Ubuntu: enlazan la `libunwind` (biblioteca de desenrollado de pila) del sistema en lugar de la copia integrada del runtime, y esa `libunwind` tiene una condición de carrera al desenvolver una excepción. El arreglo está en `libunwind/libunwind#993`; el issue se cerró como problema externo y la actualización queda del lado de Ubuntu.

Cifras del issue, no de esta ejecución:

| Build | Caídas / total |
|---|---:|
| Oficial de Microsoft 10.0.109 | 0 / 200 |
| Ubuntu 10.0.9 | 8 / 25 |
| Oficial con `-m:1` | 0 / 25 |

La comprobación local del enlace coincide con esa explicación: `ldd` sobre `libcoreclr.so` resuelve `libunwind-x86_64.so.8` y `libunwind.so.8` al sistema, y `libunwind8` instalado es 1.8.3-0ubuntu1. No se pudo confirmar que esa versión incluya el arreglo de `libunwind/libunwind#993`; el seguimiento de Ubuntu no estaba resuelto cuando se cerró el issue upstream.

## 7. Mitigación medida

| Configuración | Tandas | Fallos del CLR | Origen |
|---|---:|---:|---|
| Ubuntu 10.0.114/14, paralelismo por defecto | 10 | 2 | Reejecución de hoy; la tasa varía. |
| Ubuntu 10.0.114/14, tres verificaciones previas | 30 | 12 (4 por tanda de 10) | Registro original; no reejecutado en esta evidencia. |
| Ubuntu 10.0.114/14, `-m:1` | 10 | 0 | Reejecución de hoy. |
| Ubuntu 10.0.114/14, `-m:1` | 20 | 0 | Registro original; no reejecutado en esta evidencia. |

Las filas marcadas como registro original son mediciones previas del mismo entorno y no se reejecutaron en esta evidencia. Las de hoy tienen su transcripción en `artefactos/`.

`-m:1` fuerza un solo nodo en proceso y evita la ruta de nodos fuera de proceso. Es una mitigación, no un parche: no corrige la `libunwind` del sistema ni cambia el runtime. Su coste en esta solución fue despreciable; no se midió un impacto de rendimiento con una carga mayor.

## 8. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Reproducir la firma | `ExecutionEngineException` 0x80131506 y código 134 | 2 de 10 tandas hoy; 4 de 10 en cada verificación del registro original | PASS |
| Descartar concurrencia (H1) | el fallo persiste en secuencial | persistió en las verificaciones del registro original y en la de hoy | PASS: hipótesis descartada |
| Descartar acumulación de nodos (H2) | el fallo persiste con cero nodos al arrancar | 4 de 10 en la prueba original con cero nodos | PASS: hipótesis descartada |
| Localizar la excepción en el volcado | `ExecutionEngineException` sin pila gestionada | `setthread 8` y `setthread 19` devuelven la misma firma | PASS |
| Observar la ruta de nodos | hilos en `StartNewNode` | 4 y 5 hilos en los dos volcados | PASS como observación, no como prueba causal |
| Medir la mitigación | 0 fallos con `-m:1` | 0 de 10 hoy y 0 de 20 en el registro original | PASS |
| Probar binarios oficiales en local | 0 fallos | no ejecutado; solo se cita la cifra upstream | **No ejecutada** |
| Confirmar el arreglo en Ubuntu | `libunwind` actualizada y 0 fallos | no ejecutado | **Pendiente** |

## 9. Artefactos

- [`comandos.md`](comandos.md): comandos ejecutados y salida saneada.
- [`artefactos/entorno.txt`](artefactos/entorno.txt): sistema, SDK, runtime, `libunwind` y enlace de `libcoreclr.so`.
- [`artefactos/verificacion.txt`](artefactos/verificacion.txt): diez tandas con paralelismo por defecto.
- [`artefactos/verificacion-m1.txt`](artefactos/verificacion-m1.txt): diez tandas con `-m:1`.
- [`artefactos/dump-1055.txt`](artefactos/dump-1055.txt) y [`artefactos/dump-1030.txt`](artefactos/dump-1030.txt): extractos de `setthread`, `pe` y `clrstack -all`.

Los minivolcados originales no se publican por tamaño (unos 227 MiB, 238 MB, cada uno). Metadatos:

| Volcado | Fecha | Tamaño | SHA-256 |
|---|---|---:|---|
| `dotnet-53485.dmp` | 2026-11-09 10:55 | 238 043 136 bytes | `48b0993c91d751c44db8be5bb4df3e2d3454aa0159ea5f9020dbe2f13ec7dcd1` |
| `dotnet-23203.dmp` | 2026-11-09 10:30 | 238 227 456 bytes | `c3c5b1b4b1d16323cd313b0514a40e27ddeb10469006a984dec53c8db970056c` |

## 10. Coste y limpieza

- **Coste cloud:** 0 €. No se crearon recursos, contenedores ni servicios.
- **Ejecución:** las dos verificaciones tardaron 48 s y 43 s; la lectura de los volcados y la comprobación del enlace, menos de 10 min.
- **Sesión completa (estimación):** 2–3 h con preparación, saneado, redacción y revisión.
- **Limpieza:** no se modificó el entorno ni se instalaron binarios. Los minivolcados quedaron fuera del repositorio; aquí solo se conservan los extractos saneados.

## 11. Límites y lo no ejecutado

- Una máquina, una distribución y una solución. La muestra es pequeña y la tasa varía: 4 de 10 en las verificaciones previas y 2 de 10 hoy.
- El hilo que aborta no deja pila gestionada. La ruta de nodos se observa en otros hilos; la atribución causal viene del issue upstream y de la desaparición con `-m:1`.
- No se instalaron los binarios oficiales de Microsoft en local. La comparación 0/200 frente a 8/25 es del issue, no de esta ejecución.
- No se actualizó `libunwind` ni se comprobó el arreglo en Ubuntu; el seguimiento de la distribución no estaba resuelto cuando se cerró `dotnet/runtime#130577`.
- No es un caso de forense cloud ni una práctica del módulo 12; no se toca ese módulo.
- No se midió rendimiento con `-m:1` bajo carga. La mitigación se valida por ausencia de fallos, no por coste.
- No se prueba que otras soluciones o distribuciones se comporten igual.

## 12. Revisión de redacción

- [x] Sin secretos ni credenciales.
- [x] Sin rutas absolutas del equipo, nombres de repositorios privados ni datos personales.
- [x] Sin direcciones IP internas ni nombres de máquinas.
- [x] Lo medido y lo deducido están separados.
- [x] La causa se atribuye al issue upstream y a `libunwind`, no a este repositorio.
- [x] Lo no ejecutado está marcado como tal.
- [x] Enlaces relativos comprobados.
