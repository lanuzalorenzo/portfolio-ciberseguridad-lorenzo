# 03 | Protección de cargas de trabajo

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB EP-1, EP-2, PV-1, PV-5, LT-2.

El CSPM mira la configuración, pero no ve que alguien acaba de ejecutar un binario sospechoso dentro de una máquina. Eso lo hace la protección de cargas de trabajo: instala un sensor en el sistema operativo y manda su telemetría a Defender for Endpoint.

## Qué se activó

| Capacidad | Plan | Estado |
|---|---|---|
| Detección y respuesta en máquinas virtuales | Servers Plan 1 | Activado; sensor instalado solo |
| Escaneo de vulnerabilidades (MDVM) | Servers Plan 2 | Evaluado, no activado |
| Detección de malware en blobs | Defender for Storage | Evaluado, no activado |

## Validación

| Prueba | Resultado observado |
|---|---|
| Extensión `MDE.Windows` o `MDE.Linux` | Presente y aprovisionada en la VM de prueba |
| Cobertura en *Workload protections* | Máquinas listadas con estado de protección |
| Alerta con malware simulado | **No ejecutada**: requiere un entorno aislado |

## Lecciones

- La integración con Defender for Endpoint es transparente: activar el plan instala el sensor sin onboarding aparte.
- Un plan activado y sin alertas probadas es una promesa, no una capacidad demostrada; esta práctica lo dice y lo deja pendiente.
- El aprovisionamiento automático puede reiniciar máquinas: en producción se hace en ventana de mantenimiento.

## Más detalle

- [Capacidades por plan y cobertura](docs/informe-tecnico.md)
