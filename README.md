# Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3

> **Proyecto Final — Aplicaciones Analíticas de Big Data**  
> **Universidad Abierta Para Adultos (UAPA)**  
> **Caso de Estudio:** Claro República Dominicana (`@clarord`)  
> **Herramientas:** 100% Gratuitas y de Código Abierto  

---

## 👥 Equipo de Trabajo y Roles

* **Audric André Rosario Rosario** (Matrícula: 100089140) — *Lead Data Engineering & NLP Modeling*
  * Configuración y consumo optimizado de la YouTube Data API v3.
  * Pipeline de higienización de texto y lematización en español.
  * Implementación del modelo Transformer preentrenado para inferencia de sentimiento.
  * Arquitectura técnica del repositorio y reproducibilidad en GitHub.

* **Orlando Benítez Ventura** (Matrícula: 100090873) — *Lead Business Intelligence & Executive Strategy*
  * Formulación del problema de negocio y objetivos empresariales.
  * Especificación de KPIs gerenciales y diseño del Dashboard Ejecutivo Plotly.
  * Propuesta de solución de negocio ("Claro Sentinel NLP") y plan de acción.
  * Presupuesto de implementación cloud (USD $4,850/año) y cronograma de Gantt.

---

## 📊 Resumen Ejecutivo del Proyecto

Este proyecto aplica técnicas avanzadas de **Procesamiento de Lenguaje Natural (NLP)** y **Big Data** para auditar en tiempo real la opinión pública de los clientes de **Claro República Dominicana**. 

Frente a las limitaciones de las encuestas tradicionales (baja tasa de respuesta y lentitud), se construyó un pipeline automatizado que extrajo **799 comentarios únicos reales** provenientes de **56 videos corporativos y comparativas técnicas** en YouTube, consumiendo únicamente 649 unidades de cuota (6.49% del límite diario gratuito).

### Métricas Clave Obtenidas
* **Total de Interacciones Auditadas:** 799 comentarios únicos.
* **Net Sentiment Score (NSS / NPS Estimado):** **+5.76%** (Percepción general favorable).
* **Distribución de Sentimiento:**
  * 🟢 **Positivo:** 12.4% (99 comentarios — Liderazgo en cobertura 5G y alcance nacional).
  * 🔴 **Negativo:** 6.6% (53 comentarios — Inestabilidad nocturna en fibra óptica y demoras en call center).
  * ⚪ **Neutro:** 81.0% (647 comentarios — Consultas masivas de soporte, precios y cobertura).
* **Hallazgo Crítico:** Las quejas acumulan hasta **4 veces más reacciones ('likes')** que los comentarios positivos, amplificando el impacto reputacional.

---

## 🛠️ Stack Tecnológico

| Capa | Herramienta / Tecnología | Propósito | Costo |
| :--- | :--- | :--- | :---: |
| **Ingesta de Datos** | YouTube Data API v3 (GCP) | Extracción de comentarios y metadatos | **Gratuito** |
| **Entorno y Core** | Python 3.12 / Virtualenv | Ejecución local y dependencias | **Gratuito** |
| **Manipulación** | Pandas / NumPy | Estructuración y cálculo de métricas | **Gratuito** |
| **Modelado NLP** | Hugging Face Transformers / BETO | Autoatención bidireccional y sentimiento | **Gratuito** |
| **Dashboard BI** | Plotly Express & Graph Objects | Dashboard ejecutivo interactivo autónomo | **Gratuito** |
| **Documentación** | Python-docx / Markdown / Git | Informe formal (21 secciones) y control | **Gratuito** |

---

## 📁 Estructura del Repositorio

```text
proyecto_final/
├── README.md                      # Documentación ejecutiva del proyecto
├── AGENTS.md                      # Delimitaciones y directrices operativas del equipo
├── CHECKLIST_PROYECTO.md          # Control de avance de fases y entregables
├── requirements.txt               # Dependencias de Python gratuitas
├── .gitignore                     # Exclusión de entornos virtuales, temporales y secretos
├── INFORME_FINAL_CLARO.md         # Informe formal completo (Secciones 6.1 a 6.21)
├── GUION_VIDEO_Y_PRESENTACION.md  # Guiones para video (8 min) y pitch en clase (5 min)
├── data/
│   ├── raw/                       # 799 Comentarios reales extraídos en vivo de la API
│   │   ├── README.md              # Metadatos de la extracción oficial
│   │   ├── youtube_claro_raw.csv  # Dataset tabular crudo
│   │   └── youtube_claro_raw.json # Dataset en formato JSON
│   ├── processed/                 # Dataset higienizado con scoring NLP
│   │   └── youtube_claro_processed.csv
│   └── mocks/                     # Datasets de prueba aislados
├── dashboard/
│   ├── generar_dashboard.py       # Script generador del tablero interactivo Plotly
│   └── dashboard_ejecutivo_claro.html # Dashboard ejecutivo autónomo
├── notebooks/
│   └── analitica_claro_youtube.ipynb # Notebook interactivo (Entregable 2)
└── src/
    ├── extractor_youtube.py       # Extractor prudente de YouTube Data API v3
    ├── preprocesamiento.py        # Limpieza fonética y stopwords de telecomunicaciones
    ├── modelado_nlp.py            # Clasificador de sentimiento con Transformer
    ├── procesar_pipeline.py       # Pipeline integral de ejecución
    └── compilar_docx.py           # Compilador de INFORME_FINAL_CLARO.docx
```

---

## 🚀 Guía de Reproducción Rápida

### 1. Clonar el repositorio y configurar el entorno
```bash
git clone https://github.com/Audric1Rosario/analitica_big_data_proyecto_final.git
cd analitica_big_data_proyecto_final
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Extracción de Datos en Vivo (Opcional - Datos ya incluidos en `data/raw`)
Para volver a consultar la API en vivo, coloca tu API Key gratuita en un archivo `.env`:
```env
YT_API_KEY=tu_api_key_aqui
```
Y ejecuta:
```bash
python src/extractor_youtube.py
```

### 3. Ejecución del Pipeline de NLP
```bash
python src/procesar_pipeline.py
```

### 4. Generar y Visualizar el Dashboard Ejecutivo
```bash
python dashboard/generar_dashboard.py
# Abre dashboard/dashboard_ejecutivo_claro.html en tu navegador preferido
```

### 5. Compilar el Informe Final en Microsoft Word (.docx)
```bash
python src/compilar_docx.py
# Genera INFORME_FINAL_CLARO.docx listo para entrega formal
```

---

## 📄 Entregables Académicos (Conforme a la Rúbrica UAPA de 25 Puntos)

1. **Entregable 1 (Informe Final):** [`INFORME_FINAL_CLARO.md`](INFORME_FINAL_CLARO.md) (y su versión `.docx`) con las **21 secciones oficiales (6.1 a 6.21)** desarrolladas con rigor de posgrado.
2. **Entregable 2 (Evidencia del Análisis):** [`notebooks/analitica_claro_youtube.ipynb`](notebooks/analitica_claro_youtube.ipynb) y scripts modulares en `src/`.
3. **Entregable 3 (Datos Utilizados):** [`data/raw/youtube_claro_raw.csv`](data/raw/youtube_claro_raw.csv) con documentación de origen.
4. **Entregable 4 (Dashboard):** [`dashboard/dashboard_ejecutivo_claro.html`](dashboard/dashboard_ejecutivo_claro.html) (Plotly interactivo).
5. **Entregable 5 (Guion y Video):** [`GUION_VIDEO_Y_PRESENTACION.md`](GUION_VIDEO_Y_PRESENTACION.md) con distribución equitativa de tiempo entre Audric Rosario y Orlando Benítez.
