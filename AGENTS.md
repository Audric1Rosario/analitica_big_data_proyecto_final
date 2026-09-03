# AGENTS.md — Delimitaciones y Directrices del Proyecto
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Proyecto:** Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3  
**Caso de Estudio:** Claro República Dominicana (`@clarord`)  
**Equipo de Trabajo:** Audric Rosario & Orlando Benítez  
**Rol del Asistente:** Senior Data Scientist & Business Intelligence Advisor (PhD en Big Data)

---

## 1. Contexto y Objetivos del Proyecto

El presente proyecto académico corresponde a la evaluación final (25 puntos, dedicación estimada de 40 horas, 1 semana de duración) de la asignatura **Aplicaciones Analíticas de Big Data**. El objetivo central es transformar un problema empresarial real en una solución analítica completa, funcional y reproducible siguiendo el flujo metodológico:

$$\text{Problema de Negocio} \longrightarrow \text{Datos} \longrightarrow \text{Preparación} \longrightarrow \text{Modelado NLP} \longrightarrow \text{Visualización} \longrightarrow \text{Hallazgos} \longrightarrow \text{Decisión}$$

---

## 2. Delimitaciones del Proyecto

### 2.1. Delimitación Empresarial y Geográfica
* **Empresa analizada:** Claro República Dominicana (Compañía Dominicana de Teléfonos / América Móvil).
* **Ámbito temático:** Analítica de Redes Sociales aplicada a telecomunicaciones (Sección 4.1 del programa).
* **Focos de servicio evaluados:**
  1. Fibra Óptica e Internet Hogar (velocidad, latencia/ping, estabilidad).
  2. Red Móvil y Cobertura 5G / 4G LTE.
  3. Atención al Cliente, Canales de Soporte (107 / WhatsApp) y App Mi Claro.
  4. Facturación, Planes y Tarifas.

### 2.2. Delimitación de Datos y Consumo de API
* **Fuente de datos:** **YouTube Data API v3** oficial (Google Cloud Platform).
* **Prudencia de Cuota:** El consumo de cuota diaria debe mantenerse estrictamente por debajo de 800 unidades (de 10,000 gratuitas disponibles por día, $<8\%$ de cuota), priorizando endpoints de bajo costo (`commentThreads.list` = 1 unidad por lote de 100 comentarios).
* **Almacenamiento Local (Reproducibilidad):** Los datos crudos extraídos en vivo se congelan y versionan en `data/raw/` (`youtube_claro_raw.csv` y `youtube_claro_raw.json`) con una nota explícita de origen. Esto garantiza que el proyecto sea reproducible offline por los evaluadores sin depender de credenciales activas.
* **Datos Mock:** Cualquier dataset sintético o de prueba generado temporalmente se aísla exclusivamente en `data/mocks/` y no interfiere con los entregables finales.

### 2.3. Delimitación Tecnológica y Herramientas (100% Gratuitas)
* **Lenguaje y Entorno:** Python 3.12, entorno virtual local `.venv`.
* **Procesamiento y ETL:** `pandas`, `numpy`, expresiones regulares y normalización unicode.
* **Modelado NLP:** Arquitectura **Transformer preentrenada** para español (`transformers` / Hugging Face o motor semántico de respaldo de alta fidelidad para telecomunicaciones dominicanas).
* **Visualización y Dashboard:** **Plotly** interactivo (`plotly.express` y `plotly.graph_objects`) compilado en un dashboard autónomo HTML (`dashboard/dashboard_ejecutivo_claro.html`) con 4 KPIs gerenciales y 5 gráficos estratégicos.
* **Reportes y Documentación:** Formato Markdown (`.md`) y Microsoft Word (`.docx`) estructurados según las 21 secciones de la rúbrica oficial (6.1 a 6.21).
* **Control de Versiones:** Git y GitHub (`main`) utilizando **Conventional Commits** (`feat:`, `chore:`, `docs:`, `fix:`).

---

## 3. Matriz de Roles y División del Trabajo (Audric Rosario & Orlando Benítez)

Para optimizar las 40 horas disponibles (20 horas por integrante), se establece la siguiente división técnica y estratégica:

| Integrante | Rol Principal | Responsabilidades Clave | Secciones del Informe Asignadas |
| :--- | :--- | :--- | :--- |
| **Audric Rosario** | **Lead Data Engineering & NLP Modeling** | • Extracción y conexión con YouTube Data API v3.<br>• Pipeline de limpieza de texto y tokenización en español.<br>• Implementación y ajuste del modelo Transformer de sentimiento.<br>• Mantenimiento del repositorio GitHub y reproducibilidad del código. | **6.6** (Datos utilizados)<br>**6.7** (Preparación de datos)<br>**6.8** (Técnica analítica)<br>**6.9** (Análisis técnico)<br>**6.21** (Anexos de código) |
| **Orlando Benítez** | **Lead Business Intelligence & Strategy** | • Definición del contexto empresarial y problemática gerencial.<br>• Especificación e interpretación de KPIs en el Dashboard Plotly.<br>• Formulación de la propuesta de solución y plan de acción.<br>• Elaboración del presupuesto de implementación y cronograma de Gantt. | **6.1 - 6.5** (Portada, Negocio, Problema, Objetivos, Justificación)<br>**6.10 - 6.11** (Visualizaciones y Dashboard)<br>**6.12 - 6.17** (Solución, Plan, Presupuesto, Gantt, Riesgos) |
| **Conjunto** (Audric & Orlando) | **Revisión y Presentación** | • Consolidación del Resumen Ejecutivo (6.2), Conclusiones (6.18) y Recomendaciones (6.19).<br>• Grabación del video oficial de 5 a 8 minutos (50% tiempo c/u).<br>• Exposición presencial de 5 minutos en clase con apoyo de diapositivas. | **6.2, 6.18, 6.19, 6.20**<br>**Entregable 1** (PDF)<br>**Entregable 5** (Video) |

---

## 4. Estructura Obligatoria de los Entregables

1. **Entregable 1 (Informe Final):** Documento formal de 10 a 15 páginas de cuerpo en formato PDF (compilado desde `INFORME_FINAL_CLARO.docx` / `INFORME_FINAL_CLARO.md`), conteniendo rigurosamente las 21 secciones numeradas del 6.1 al 6.21.
2. **Entregable 2 (Evidencia del Análisis):** Notebook interactivo ejecutable (`notebooks/analitica_claro_youtube.ipynb`) y scripts reproducibles en `src/`.
3. **Entregable 3 (Datos):** Repositorio local de datos crudos (`data/raw/`) y enriquecidos (`data/processed/`) con documentación de origen.
4. **Entregable 4 (Dashboard):** Panel ejecutivo interactivo Plotly en `dashboard/dashboard_ejecutivo_claro.html`.
5. **Entregable 5 (Video y Presentación):** Guion técnico y de oratoria para el video de 5 a 8 minutos y la presentación en clase de 5 minutos (`GUION_VIDEO_Y_PRESENTACION.md`).

---

## 5. Criterios de Calidad Académica

* **Cero alucinaciones o datos opacos:** Cada métrica presentada debe provenir del procesamiento reproducible de los 799 comentarios recolectados.
* **Orientación gerencial:** No limitarse a métricas de machine learning (F1-score o Loss); traducir cada hallazgo a impacto comercial, retención de clientes (Churn) y calidad percibida.
* **Normas APA 7ma Edición:** Citar fuentes técnicas, repositorios de modelos y documentación oficial en la Sección 6.20.
