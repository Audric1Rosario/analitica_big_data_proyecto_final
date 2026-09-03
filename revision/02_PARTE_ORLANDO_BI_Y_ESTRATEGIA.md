# PARTE 2: GUÍA DE REVISIÓN ESTRATÉGICA (BI, DASHBOARD & SOLUCIÓN)
**Responsable:** Orlando Benítez Ventura (Matrícula: 100090873)  
**Rol:** Lead Business Intelligence & Executive Strategy  
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Facilitador:** Luis Eduardo Bayonet Robles  

---

## 🎯 Alcance de la Revisión de Orlando
Orlando es responsable de auditar y dar el visto bueno a toda la **contextualización empresarial, formulación del problema gerencial, diseño e interactividad del Dashboard Ejecutivo Plotly, solución de negocio "Claro Sentinel", presupuesto AWS, cronograma de Gantt y recomendaciones gerenciales**.

### 📊 Puntos de la Rúbrica Evaluados en esta Parte: **9 / 25 Puntos**
* **Identificación del negocio, problema y objetivos (Secciones 6.3 y 6.4):** 3 Puntos
* **Visualizaciones y Dashboard Ejecutivo (Secciones 6.10 y 6.11):** 3 Puntos
* **Solución propuesta, plan de acción, presupuesto y Gantt (Secciones 6.12 a 6.15):** 3 Puntos

---

## 🌿 1. Paso a Paso en Git para Orlando
```bash
# 1. Asegurarte de estar en la versión más reciente de main
git checkout main
git pull origin main

# 2. Crear tu rama personal de trabajo (o configurarla en Codex / tu asistente)
git checkout -b orlando/revision-estrategica

# 3. Realizar los ajustes necesarios y registrar con Conventional Commits:
git add .
git commit -m "docs(bi): enriquecer justificación de ROI en presupuesto AWS"

# 4. Subir tu rama a GitHub para revisión mutua
git push -u origin orlando/revision-estrategica
```

---

## 📁 2. Archivos bajo Responsabilidad de Orlando

| Archivo | Función Principal | Qué debes verificar |
| :--- | :--- | :--- |
| [`dashboard/dashboard_ejecutivo_claro.html`](../dashboard/dashboard_ejecutivo_claro.html) | Dashboard Ejecutivo autónomo (Entregable 4) | Abrir con doble clic en el navegador. Probar los 5 gráficos interactivos, tooltips y los 4 KPIs superiores. |
| [`PRESENTACION_VIDEO_OFICIAL.pptx`](../PRESENTACION_VIDEO_OFICIAL.pptx) | Diapositivas para el Video (8 min) | Revisar que tus notas de orador en las diapositivas 1, 2, 5, 6, 7 y 8 fluyan naturalmente. |
| [`PRESENTACION_CLASE_5MIN.pptx`](../PRESENTACION_CLASE_5MIN.pptx) | Diapositivas para la Clase (5 min) | Comprobar que los tiempos de tus intervenciones (minutos 1, 3 y 5) estén ajustados. |
| [`INFORME_FINAL_CLARO.md`](../INFORME_FINAL_CLARO.md) | Informe Maestro | Validar tus secciones asignadas (6.1 a 6.5 y 6.10 a 6.17). |

---

## 📝 3. Secciones del Informe Asignadas a Orlando

Debes revisar y validar la redacción en [`INFORME_FINAL_CLARO.md`](../INFORME_FINAL_CLARO.md) de:

### ✅ Secciones 6.1 a 6.5: Negocio, Problema, Objetivos y Justificación
* [ ] **6.1 Portada:** ¿Aparecen los nombres completos, matrículas correctas y el profesor **Luis Eduardo Bayonet Robles**?
* [ ] **6.3 Contexto y Problema:** ¿Queda claro por qué las encuestas tradicionales tienen baja tasa de respuesta (< 4%) y cómo YouTube resuelve la ceguera de datos?
* [ ] **6.4 Objetivos:** ¿Hay **exactamente cuatro (4) objetivos específicos** con verbos medibles?
* [ ] **6.5 Justificación:** ¿Se explica el impacto del costo de adquisición (CAC) vs. retención y se justifican las herramientas 100% gratuitas?

### ✅ Secciones 6.10 y 6.11: Visualizaciones y Dashboard Ejecutivo
* [ ] **6.10 Visualizaciones:** ¿Tienen las 5 visualizaciones su pregunta de negocio, ejes, unidades, fuente e interpretación?
* [ ] **6.11 Dashboard:** ¿Está incluido el esquema visual del dashboard dentro del texto para que el evaluador lo aprecie en el informe?

### ✅ Secciones 6.12 a 6.17: Solución Empresarial y Factibilidad
* [ ] **6.12 Solución Propuesta ("Claro Sentinel NLP"):** ¿Se explica con claridad la integración de la analítica social con el CRM para disparar pre-tickets de soporte técnico?
* [ ] **6.13 Plan de Acción:** ¿Están definidas las 5 fases en la tabla (con responsables, duración y entregables esperados)?
* [ ] **6.14 Presupuesto:** ¿Suma exactamente **$4,850.00 USD anuales** sin licencias pagadas, con fuentes oficiales de AWS Pricing Calculator? ¿Se explica que reteniendo 15 clientes al mes se amortiza en menos de 90 días?
* [ ] **6.15 Diagrama de Gantt:** ¿Guarda correspondencia temporal con las 16 semanas del plan de acción?
* [ ] **6.16 Condiciones para el Éxito:** ¿Se listan **exactamente cinco (5) condiciones** sólidas?
* [ ] **6.17 Matriz de Riesgos:** ¿Incluye riesgos tecnológicos, operacionales y organizacionales con sus mitigaciones?

---

## 🎥 4. Participación de Orlando en el Video Oficial y la Clase

### En el Video Oficial (5 a 8 min):
* **Tu Bloque 1 (Apertura y Problema):** Minuto **00:00 a 01:15** (~1 min 15 seg).
  * *Pantalla:* Diapositiva 1 (Portada) $\rightarrow$ Diapositiva 2 (Infografía de Encuestas vs. YouTube).
* **Tu Bloque 2 (Dashboard en Vivo y Solución Sentinel):** Minuto **03:30 a 05:45** (~2 min 15 seg).
  * *Pantalla:* **Transición al Navegador**: interactuar en vivo con `dashboard_ejecutivo_claro.html` mostrando los 4 KPIs y pasando el cursor por los gráficos $\rightarrow$ Diapositiva 6 (Arquitectura Sentinel) $\rightarrow$ Diapositiva 7 (Presupuesto AWS y ROI).
* **Cierre Conjunto:** Minuto 05:45 a 07:30.

### En la Presentación en Clase (5 min):
* **Minuto 1:** Presentar la problemática de retención de Claro RD y el fallo de las encuestas tradicionales.
* **Minuto 3:** Explicar los hallazgos del Dashboard: fortaleza en 5G (+14%), alerta en soporte (-3.2%) y efecto multiplicador 4:1 de likes en quejas.
* **Minuto 5:** Cierre de recomendaciones y sesión de preguntas.
