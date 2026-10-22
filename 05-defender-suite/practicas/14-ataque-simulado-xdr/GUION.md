# Guion — Práctica 14: Ataque simulado y correlación XDR

> **En fácil:** este guion lanza un ataque de mentira, por partes y controlado, y comprueba si cada producto de Defender lo ve y si XDR lo une en un solo incidente.

## Objetivo

Ejecutar un ataque controlado y validar detección, correlación y análisis mediante Microsoft Defender XDR.

## Contexto técnico

El ataque simulado permite:

- Validar detección en múltiples productos Defender.
- Revisar correlación automática en XDR.
- Analizar la cronología del ataque.
- Revisar técnicas MITRE ATT&CK.
- Evaluar respuesta automatizada.

## Preparación del entorno

1. Crear máquina víctima.
2. Asegurar que todos los sensores Defender están activos.
3. Validar la ingestión de señales.

## Ejecución del ataque simulado

Ataques recomendados:

- Phishing controlado.
- Token theft.
- Lateral movement.
- Malware simulado (EICAR).
- Exfiltración de datos ficticios.

## Detección por productos Defender

1. **Defender for Endpoint**
   - Detección de malware.
   - Detección de movimiento lateral.
   - Alertas de comportamiento.
2. **Defender for Identity**
   - Detección de Pass-the-Token.
   - Detección de anomalías de autenticación.
3. **Defender for Cloud Apps**
   - Actividad anómala en SaaS.
   - Descargas masivas.
   - Sesiones sospechosas.
4. **Defender for Cloud**
   - Alertas de workloads.
   - Actividad sospechosa en recursos cloud.

## Correlación en Microsoft Defender XDR

1. Revisar el incidente generado.
2. Validar la correlación entre señales.
3. Revisar la cronología del ataque.
4. Revisar las entidades implicadas.
5. Validar las técnicas MITRE ATT&CK.

## Cierre

1. Evaluar la efectividad de detección.
2. Identificar mejoras futuras.
3. Registrar en bitácora al final del módulo.
