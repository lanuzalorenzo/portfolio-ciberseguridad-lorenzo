# 🛡️ 04-devsecops

## 🧾 Descripción
Este módulo implementa una aceleradora DevSecOps orientada a garantizar la integridad, trazabilidad y seguridad del ciclo de vida del código en todos los repositorios del portfolio.  
Incluye la protección de la rama `main`, la obligatoriedad de Pull Requests, la revisión de cambios y la aplicación de reglas de seguridad que evitan modificaciones no controladas.

---

## 🎯 Objetivos del módulo
- Establecer una política DevSecOps mínima y obligatoria para todos los repositorios del portfolio.
- Proteger la rama `main` mediante reglas de seguridad.
- Garantizar que todo cambio pasa por Pull Request y revisión.
- Evitar push directo y force‑push en ramas protegidas.
- Documentar la aceleradora DevSecOps de forma clara y reutilizable.

---

## 🗂️ Estructura del módulo
- `branch-protection.md`  
  Documento técnico donde se describe la configuración de protección de la rama `main`, incluyendo reglas, validaciones y comportamiento esperado.

- `aceleradora-devsecops.md`  
  Documento que recoge la aceleradora DevSecOps aplicada al portfolio: políticas, requisitos, flujo de trabajo y controles de seguridad.

- `bitacora/`  
  Registros técnicos del trabajo realizado durante la implementación de la aceleradora.

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

No se abordan aquí temas de CI/CD, pipelines, análisis de código, ni automatización avanzada.

---

## 🧩 Prácticas incluidas
### `branch-protection.md`
Configuración de reglas de protección de la rama `main`.

### `aceleradora-devsecops.md`
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
