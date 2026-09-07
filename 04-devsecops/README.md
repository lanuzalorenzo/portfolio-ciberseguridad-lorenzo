# 🛡️ 04-devsecops

## 🧾 Descripción
Este módulo implementa una política DevSecOps mínima y obligatoria para todos los repositorios del portfolio.  
Incluye la protección de la rama `main`, la definición de reglas de seguridad, la obligatoriedad de Pull Requests y la documentación de un flujo de trabajo seguro y trazable.

---

## 🎯 Objetivos del módulo
- Establecer una política DevSecOps unificada para todos los repositorios.
- Proteger la rama `main` mediante reglas de seguridad.
- Garantizar que todo cambio pasa por Pull Request y revisión.
- Evitar push directo y force‑push en ramas protegidas.
- Documentar la política DevSecOps de forma clara, técnica y reutilizable.

---

## 🗂️ Estructura del módulo
- `branch-protection/`  
  Práctica técnica donde se documenta la configuración de protección de la rama `main`.

- `devsecops-policy/`  
  Política DevSecOps aplicada al portfolio: reglas, flujo de PR y controles de seguridad.

- `bitacora/`  
  Registros técnicos del trabajo realizado durante la implementación del módulo.

- `docs/`  
  Documentación conceptual, buenas prácticas y referencias relacionadas con DevSecOps.

- `README.md`  
  Documento principal del módulo.

---

## ⚙️ Requisitos
- Cuenta de GitHub con permisos administrativos sobre los repositorios del portfolio.
- Conocimiento básico de:
  - Pull Requests  
  - Branch protection rules  
  - Code review  
  - GitHub Actions (opcional)

---

## 🧪 Alcance del módulo
Este módulo cubre:

- Protección de la rama `main`.  
- Reglas de seguridad aplicadas a repositorios del portfolio.  
- Flujo obligatorio de Pull Requests.  
- Revisión y aprobación de cambios.  
- Trazabilidad completa del código.  
- Política DevSecOps mínima y unificada.

No se abordan aquí temas de CI/CD, pipelines, análisis de código ni automatización avanzada.

---

## 🧩 Prácticas incluidas
### `branch-protection/branch-protection.md`
Configuración de reglas de protección de la rama `main`.

### `devsecops-policy/devsecops-policy.md`
Política DevSecOps aplicada a todos los repositorios del portfolio.

---

## ✍️ Autor
Lorenzo Lanuza

---

## ⚖️ Aviso Legal
Este módulo contiene prácticas educativas y de laboratorio realizadas en repositorios personales.  
No incluye información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas con fines formativos.

---

## 📜 Licencia
MIT
