# Checklist de Seguimiento del Proyecto Final
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Proyecto:** Analítica de Redes Sociales — Claro República Dominicana (YouTube Data API v3)  
**Equipo:** Audric Rosario & Orlando Benítez  
**Estado General:** Fase de Implementación Completa (Listo para revisión individual)

---

## 📌 Estado de los Componentes y Entregables

- [x] **Fase 1: Configuración del Entorno y Repositorio**
  - [x] Repositorio Git inicializado y vinculado a GitHub (`main`).
  - [x] Creación de `.gitignore` para Python, entornos virtuales y secretos.
  - [x] Creación de `requirements.txt` con librerías gratuitas (Pandas, Plotly, Transformers, Python-docx, Scikit-learn, etc.).
  - [x] Configuración del entorno virtual `.venv` con dependencias instaladas.
  - [x] Creación de `AGENTS.md` con delimitaciones, roles y directrices metodológicas.

- [x] **Fase 2: Adquisición de Datos Reales (YouTube Data API v3)**
  - [x] Módulo modular `src/extractor_youtube.py` con sanitización de consola Windows.
  - [x] Lectura segura de API Key desde variable de entorno `.env` (`YT_API_KEY`).
  - [x] Ejecución en vivo: **799 comentarios únicos reales** extraídos de **56 videos corporativos y reseñas**.
  - [x] Consumo prudente de cuota: solo 649 unidades de 10,000 (6.49% del límite gratuito diario).
  - [x] Congelación de datos en `data/raw/youtube_claro_raw.csv` y `data/raw/youtube_claro_raw.json`.
  - [x] Datos mock aislados ordenadamente en `data/mocks/`.

- [x] **Fase 3: Procesamiento y Modelado NLP**
  - [x] Módulo de limpieza y preprocesamiento en español `src/preprocesamiento.py` (stop words de telco, normalización).
  - [x] Clasificación de tópicos (Fibra Óptica, Red 5G, Atención al Cliente, Facturación, Planes).
  - [x] Arquitectura de modelo Transformer preentrenado (`src/modelado_nlp.py`) para análisis de sentimiento.
  - [x] Ejecución del pipeline y generación de `data/processed/youtube_claro_processed.csv`.
  - [x] Hallazgos calculados: 81.0% Neutro, 12.4% Positivo, 6.6% Negativo, **Net Sentiment Score = +5.76%**.

- [x] **Fase 4: Dashboard Ejecutivo (Plotly)**
  - [x] Script generador `dashboard/generar_dashboard.py`.
  - [x] Dashboard ejecutivo interactivo `dashboard/dashboard_ejecutivo_claro.html` con 4 KPIs gerenciales y 5 gráficos clave.

- [x] **Fase 5: Documentación y Entregables Académicos (21 Secciones)**
  - [x] Generación de `INFORME_FINAL_CLARO.md` con las 21 secciones académicas completas (6.1 a 6.21 según rúbrica UAPA).
  - [x] Script de compilación `src/compilar_docx.py` para generar `INFORME_FINAL_CLARO.docx`.
  - [x] Notebook interactivo `notebooks/analitica_claro_youtube.ipynb` estructurado para Google Colab y Jupyter (Entregable 2).

- [x] **Fase 6: Guiones de Presentación, Video y Diapositivas PPTX**
  - [x] Guion detallado para el **Video Oficial de 5 a 8 minutos (Entregable 5)** con división de diálogo minuto a minuto entre Audric Rosario y Orlando Benítez (`GUION_VIDEO_Y_PRESENTACION.md`).
  - [x] Guion y estructura para la **Presentación en Clase de 5 minutos** con guía diapositiva por diapositiva para el futuro PPTX (`GUION_VIDEO_Y_PRESENTACION.md`).
  - [x] **Diapositivas PPTX para el Video Oficial:** [`PRESENTACION_VIDEO_OFICIAL.pptx`](PRESENTACION_VIDEO_OFICIAL.pptx) (8 diapositivas en formato panorámico 16:9 con notas de orador integradas e indicaciones de transición a código/dashboard).
  - [x] **Diapositivas PPTX para la Clase de 5 Minutos:** [`PRESENTACION_CLASE_5MIN.pptx`](PRESENTACION_CLASE_5MIN.pptx) (6 diapositivas con cronómetro y parlamento optimizado).
  - [x] Sincronización completa del repositorio en GitHub (`main`) con Conventional Commits.
