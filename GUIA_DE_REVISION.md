# GUÍA MAESTRA DE REVISIÓN POR PARTES DEL PROYECTO FINAL
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Facilitador:** Luis Eduardo Bayonet Robles  
**Caso de Estudio:** Claro República Dominicana (`@clarord`)  
**Equipo de Trabajo:**
* **Audric André Rosario Rosario** (Matrícula: 100089140) — *Lead Data Engineering & NLP Modeling*
* **Orlando Benítez Ventura** (Matrícula: 100090873) — *Lead Business Intelligence & Executive Strategy*

---

## 🎯 Organización de la Revisión por Partes

Para optimizar las 40 horas del proyecto y permitir que cada integrante (y sus respectivos asistentes de IA) trabajen de forma independiente sin interferencias, el proceso de revisión está dividido en **tres partes claramente delimitadas**:

```text
                                PROYECTO FINAL (25 PUNTOS)
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
   PARTE 1: AUDRIC                  PARTE 2: ORLANDO                  PARTE 3: CONJUNTA
(Data Eng. & Modelado NLP)       (BI, Dashboard & Estrategia)       (Video, Cierre & PDF)
   12 / 25 Puntos                    9 / 25 Puntos                     4 / 25 Puntos
         │                                 │                                 │
         ▼                                 ▼                                 ▼
[revision/01_PARTE_AUDRIC]       [revision/02_PARTE_ORLANDO]       [revision/03_PARTE_CONJUNTA]
Rama: audric/revision            Rama: orlando/revision           Rama: main (Fusión final)
```

---

## 📑 Índice de Guías Detalladas por Integrante

### 🔹 [PARTE 1: Guía de Revisión Técnica de Audric Rosario](revision/01_PARTE_AUDRIC_DATA_Y_NLP.md)
* **Rama de trabajo:** `git checkout -b audric/revision-tecnica`
* **Puntuación auditada:** 12 Puntos de la rúbrica (Secciones 6.6, 6.7, 6.8, 6.9, 6.21).
* **Archivos clave bajo su custodia:**
  * [`src/extractor_youtube.py`](src/extractor_youtube.py) (Extracción prudente de YouTube Data API v3).
  * [`src/preprocesamiento.py`](src/preprocesamiento.py) (Limpieza de texto y jerga dominicana).
  * [`src/modelado_nlp.py`](src/modelado_nlp.py) (Transformer preentrenado para sentimiento).
  * [`notebooks/analitica_claro_youtube.ipynb`](notebooks/analitica_claro_youtube.ipynb) (Notebook pre-ejecutado con salidas reales).
  * [`data/raw/youtube_claro_raw.csv`](data/raw/youtube_claro_raw.csv) (799 comentarios reales congelados).
* **Intervención en Video:** Minutos 01:15 a 03:30 (Demostración de código en VS Code y Jupyter Notebook).
* **Intervención en Clase:** Minuto 2 (Extracción y datos) y Minuto 4 (Transformer y arquitectura técnica).

---

### 🔹 [PARTE 2: Guía de Revisión Estratégica de Orlando Benítez](revision/02_PARTE_ORLANDO_BI_Y_ESTRATEGIA.md)
* **Rama de trabajo:** `git checkout -b orlando/revision-estrategica`
* **Puntuación auditada:** 9 Puntos de la rúbrica (Secciones 6.1 a 6.5 y 6.10 a 6.17).
* **Archivos clave bajo su custodia:**
  * [`dashboard/dashboard_ejecutivo_claro.html`](dashboard/dashboard_ejecutivo_claro.html) (Dashboard Plotly interactivo con 4 KPIs y 5 paneles).
  * [`PRESENTACION_VIDEO_OFICIAL.pptx`](PRESENTACION_VIDEO_OFICIAL.pptx) (Diapositivas 16:9 para el video de 8 minutos con notas de orador).
  * [`PRESENTACION_CLASE_5MIN.pptx`](PRESENTACION_CLASE_5MIN.pptx) (Diapositivas cronometradas para la defensa presencial).
  * Secciones de Negocio de [`INFORME_FINAL_CLARO.md`](INFORME_FINAL_CLARO.md) (Problema, Solución Sentinel, Presupuesto AWS de $4,850 USD, Gantt de 16 semanas).
* **Intervención en Video:** Minutos 00:00 a 01:15 (Apertura y problema) y 03:30 a 05:45 (Dashboard Plotly en vivo y Solución Sentinel).
* **Intervención en Clase:** Minuto 1 (Problema de negocio) y Minuto 3 (Hallazgos del Dashboard).

---

### 🔹 [PARTE 3: Guía Conjunta de Grabación, Cierre y Entrega](revision/03_PARTE_CONJUNTA_VIDEO_Y_ENTREGA.md)
* **Responsables:** Audric Rosario & Orlando Benítez
* **Puntuación auditada:** 4 Puntos de la rúbrica (Secciones 6.2, 6.18, 6.19, 6.20, Video y PDF).
* **Actividades conjuntas:**
  * Validación del Resumen Ejecutivo (6.2), Conclusiones (6.18), Recomendaciones (6.19) y Referencias APA (6.20).
  * Grabación del Video Oficial de 7:30 min siguiendo [`GUION_VIDEO_Y_PRESENTACION.md`](GUION_VIDEO_Y_PRESENTACION.md).
  * Subida del video a YouTube/Drive y reemplazo del enlace público en la portada del informe.
  * Compilación y exportación de [`INFORME_FINAL_CLARO.docx`](INFORME_FINAL_CLARO.docx) a PDF (`INFORME_FINAL_CLARO_BENITEZ_ROSARIO.pdf`).
  * Fusión final de ramas a `main` y confirmación de los 5 entregables oficiales.

---

## 🗂️ Mapa General de Documentos del Repositorio

Para que no haya documentos sueltos sin propósito definido, este mapa describe la función exacta de cada archivo:

```text
📁 proyecto_final/
├── 📄 README.md                        # Portal de bienvenida y resumen general del repositorio
├── 📄 AGENTS.md                        # Directrices y reglas de colaboración para agentes de IA
├── 📄 GUIA_DE_REVISION.md              # [ESTE ARCHIVO] Mapa maestro de navegación de la revisión
├── 📄 Proyecto_Final.md                # Enunciado y rúbrica oficial proporcionada por la UAPA
├── 📄 requirements.txt                 # Dependencias oficiales de Python
│
├── 📁 revision/                        # GUIAS DE REVISIÓN INDIVIDUALES POR PARTE
│   ├── 📄 01_PARTE_AUDRIC_DATA_Y_NLP.md           # Scope técnico de Audric (12 pts)
│   ├── 📄 02_PARTE_ORLANDO_BI_Y_ESTRATEGIA.md     # Scope estratégico de Orlando (9 pts)
│   └── 📄 03_PARTE_CONJUNTA_VIDEO_Y_ENTREGA.md    # Scope conjunto y grabación (4 pts)
│
├── 📄 INFORME_FINAL_CLARO.md           # Informe académico maestro (21 secciones)
├── 📄 INFORME_FINAL_CLARO.docx         # Documento Word estilizado listo para exportar a PDF (Entregable 1)
├── 📄 PRESENTACION_VIDEO_OFICIAL.pptx  # Presentación para el video de 8 min con notas de orador
├── 📄 PRESENTACION_CLASE_5MIN.pptx     # Presentación de 6 diapositivas para la clase de 5 min
├── 📄 GUION_VIDEO_Y_PRESENTACION.md    # Guion detallado minuto a minuto con cambios de pantalla
├── 📄 INSIGHTS_Y_EVALUACION.md         # Autoevaluación auditada contra la rúbrica (25.0/25.0)
├── 📄 CHECKLIST_PROYECTO.md            # Control de avance de las fases 1 a 6
│
├── 📁 dashboard/                       # ENTREGABLE 4: DASHBOARD EJECUTIVO
│   ├── 🌐 dashboard_ejecutivo_claro.html  # Panel autónomo en HTML con Plotly interactivo
│   └── 🐍 generar_dashboard.py            # Script compilador del dashboard
│
├── 📁 data/                            # ENTREGABLE 3: DATOS
│   ├── 📁 raw/                            # 799 comentarios reales extraídos vía API
│   │   ├── 📄 youtube_claro_raw.csv
│   │   └── 📄 youtube_claro_raw.json
│   ├── 📁 processed/                      # Dataset higienizado con sentimiento y tópicos
│   └── 📁 mocks/                          # Mocks sintéticos aislados temporalmente
│
├── 📁 notebooks/                       # ENTREGABLE 2: NOTEBOOK EJECUTABLE
│   └── 📓 analitica_claro_youtube.ipynb   # Notebook con celdas 1 a 8 ya ejecutadas
│
└── 📁 src/                             # CÓDIGO FUENTE MODULAR REPRODUCIBLE
    ├── 🐍 extractor_youtube.py            # Conexión ética a YouTube Data API v3
    ├── 🐍 preprocesamiento.py             # Normalización y filtrado de jerga dominicana
    ├── 🐍 modelado_nlp.py                 # Pipeline de Transformer preentrenado en español
    ├── 🐍 procesar_pipeline.py            # Ejecución secuencial ETL
    ├── 🐍 compilar_docx.py                # Compilador Markdown -> Word estilizado
    ├── 🐍 generar_presentaciones.py       # Generador automatizado de diapositivas PPTX
    └── 🐍 ejecutar_notebook.py            # Script que pre-ejecuta el notebook con salidas
```

---

## 🚀 Próximos Pasos para Iniciar
1. **Audric:** Abre [`revision/01_PARTE_AUDRIC_DATA_Y_NLP.md`](revision/01_PARTE_AUDRIC_DATA_Y_NLP.md) y crea tu rama `audric/revision-tecnica`.
2. **Orlando:** Abre [`revision/02_PARTE_ORLANDO_BI_Y_ESTRATEGIA.md`](revision/02_PARTE_ORLANDO_BI_Y_ESTRATEGIA.md) y crea tu rama `orlando/revision-estrategica`.
3. Ambos revisan sus partes asignadas de forma paralela y sin conflictos.
