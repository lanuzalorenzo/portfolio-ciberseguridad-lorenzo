# 🔐 Informe técnico — Práctica 14: Ataque Simulado + Correlación XDR

## 🧩 Introducción
Esta práctica ejecuta un ataque controlado para validar detección, correlación y análisis mediante Microsoft Defender XDR y toda la suite Defender.

---

## 🔥 Ejecución del ataque simulado
Se ejecutaron ataques controlados:
- Phishing simulado.
- Token theft.
- Lateral movement.
- Malware EICAR.
- Exfiltración ficticia.

---

## 🛡 Detección por productos Defender
### Defender for Endpoint
- Detección de malware.  
- Detección de movimiento lateral.  
- Alertas de comportamiento.

### Defender for Identity
- Detección de Pass-the-Token.  
- Anomalías de autenticación.

### Defender for Cloud Apps
- Actividad anómala en SaaS.  
- Descargas masivas.  
- Sesiones sospechosas.

### Defender for Cloud
- Alertas de workloads.  
- Actividad sospechosa en recursos cloud.

---

## 🔗 Correlación en Microsoft Defender XDR
Se revisó:
- Incidente generado automáticamente.
- Correlación entre señales.
- Cronología del ataque.
- Técnicas MITRE ATT&CK.
- Entidades implicadas.

---

## 🧠 Conclusiones técnicas
- La suite Defender detectó el ataque en múltiples capas.  
- XDR correlacionó señales correctamente.  
- La cronología permitió reconstruir el ataque completo.  
- Se identificaron mejoras futuras:
  - Hardening de identidades.  
  - Reducción de superficie de ataque.  
  - Automatización de respuesta.

---

## ⚖️ Aviso Legal
Este laboratorio es 100% controlado y educativo.
No contiene actividad real maliciosa ni afecta a sistemas externos.
