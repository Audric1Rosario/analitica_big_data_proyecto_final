# Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3

> **Proyecto Final — Aplicaciones Analíticas de Big Data**  
> **Universidad Abierta Para Adultos (UAPA)**  
> **Caso de Estudio:** Claro República Dominicana (`@clarord`)  
> **Herramientas:** 100% Gratuitas y de Código Abierto  

---

## Equipo de Trabajo y Roles

* **Audric André Rosario Rosario** (Matrícula: 100089140) — *Lead Data Engineering & NLP Modeling*
  * Configuración y consumo optimizado de la YouTube Data API v3.
  * Pipeline de higienización de texto y lematización en español.
  * Implementación de inferencia profunda de sentimiento con arquitectura Transformer BETO (finiteautomata/beto-sentiment-analysis) en PyTorch sin fallbacks léxicos.
  * Arquitectura técnica del repositorio y reproducibilidad en GitHub.

* **Orlando Benítez Ventura** (Matrícula: 100090873) — *Lead Business Intelligence & Executive Strategy*
  * Formulación del problema de negocio y objetivos empresariales.
  * Especificación de KPIs gerenciales y diseño del Dashboard Ejecutivo Plotly.
  * Propuesta de solución de negocio ("Claro Sentinel NLP") y plan de acción.
  * Presupuesto de implementación cloud (USD $4,850/año) y cronograma de Gantt.

---

## Resumen Ejecutivo del Proyecto

Este proyecto aplica técnicas avanzadas de **Procesamiento de Lenguaje Natural (NLP)** y **Big Data** para auditar en tiempo real la opinión pública de los clientes de **Claro República Dominicana**. 

Frente a las limitaciones de las encuestas tradicionales (baja tasa de respuesta y lentitud), se construyó un pipeline automatizado que extrajo **799 comentarios únicos reales** provenientes de **39 videos con comentarios disponibles** en YouTube, a partir de búsquedas corporativas y comparativas técnicas. La extracción consumió 649 unidades de cuota (6.49% del límite diario gratuito).

### Métricas Clave Obtenidas (Modelo Transformer BETO)
* **Total de Interacciones Auditadas:** 799 comentarios únicos.
* **Net Sentiment Score (NSS / NPS Estimado):** **-11.51%** (Alerta operativa y foco de fricción).
* **Distribución de Sentimiento:**
  * **Positivo:** 21.40% (171 comentarios — Cobertura 5G, fidelidad y orgullo de marca).
  * **Negativo:** 32.92% (263 comentarios — Averías de fibra óptica, disputas de facturación y soporte).
  * **Neutro:** 45.68% (365 comentarios — Consultas operacionales de soporte y cobertura).
* **Hallazgo Crítico:** Las quejas concentran focos severos en Facturación (-32.53% NSS) y Fibra Óptica (-29.14% NSS), acumulando 554 likes comunitarios y picos de hasta 40 reacciones por averías sin respuesta.

---

## Stack Tecnológico

| Capa | Herramienta / Tecnología | Propósito | Costo |
| :--- | :--- | :--- | :---: |
| **Ingesta de Datos** | YouTube Data API v3 (GCP) | Extracción ética de comentarios y metadatos | **Gratuito** |
| **Entorno y Core** | Python 3.12 / uv package manager | Gestión determinista de dependencias (`pyproject.toml`) | **Gratuito** |
| **Manipulación** | Pandas / NumPy | Estructuración y cálculo dinámico de métricas | **Gratuito** |
| **Modelado NLP** | Hugging Face Transformers (`BETO`) / PyTorch | Autoatención profunda bidireccional en español (Cero Fallback) | **Gratuito** |
| **Dashboard BI** | Plotly Express & Graph Objects | Dashboard ejecutivo interactivo autónomo HTML | **Gratuito** |
| **Documentación** | Python-docx / Markdown / Git | Informe formal (21 secciones UAPA) y control de versiones | **Gratuito** |

---

## Estructura del Repositorio

```text
proyecto_final/
├── README.md                      # Documentación ejecutiva del proyecto
├── requirements.txt               # Dependencias de Python gratuitas
├── .gitignore                     # Exclusión de entornos virtuales, temporales y secretos
├── .env.example                   # Plantilla para API Key de YouTube
├── data/
│   ├── raw/                       # 799 Comentarios reales extraídos en vivo de la API
│   │   ├── README.md              # Metadatos de la extracción oficial
│   │   ├── youtube_claro_raw.csv  # Dataset tabular crudo
│   │   └── youtube_claro_raw.json # Dataset en formato JSON
│   └── processed/                 # Dataset higienizado con scoring NLP Transformer
│       └── youtube_claro_processed.csv
├── dashboard/
│   ├── generar_dashboard.py       # Script generador del tablero interactivo Plotly
│   └── dashboard_ejecutivo_claro.html # Dashboard ejecutivo autónomo
├── notebooks/
│   └── analitica_claro_youtube.ipynb # Notebook interactivo pre-ejecutado (Entregable 2)
├── entregables/
│   ├── upload/                    # Archivos listos para subir a la plataforma UAPA
│   └── base/                      # Documentos fuente y enunciado oficial
├── docs/
│   └── images/                    # 8 Figuras analíticas en alta resolución
└── src/
    ├── extractor_youtube.py       # Extractor prudente de YouTube Data API v3
    ├── preprocesamiento.py        # Limpieza fonética y stopwords de telecomunicaciones
    ├── modelado_nlp.py            # Inferencia profunda con Transformer BETO en PyTorch
    ├── procesar_pipeline.py       # Pipeline integral de ejecución
    ├── generar_imagenes_reporte.py# Generador de figuras para el informe
    ├── generar_presentaciones.py  # Generador de presentaciones ejecutivas PPTX
    ├── ejecutar_notebook.py       # Ejecución y población de salidas del notebook
    └── compilar_docx.py           # Compilador de informe formal en formato Word
```

---

## Guía de Reproducción Rápida

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
# Genera el informe formal en formato Word
```

---

## Entregables Académicos (Conforme a la Rúbrica UAPA de 25 Puntos)

1. **Entregable 1 (Informe Final):** [`entregables/upload/Informe Final.pdf`](entregables/upload/Informe%20Final.pdf) con las **21 secciones oficiales (6.1 a 6.21)** desarrolladas con rigor de posgrado.
2. **Entregable 2 (Evidencia del Análisis):** [`notebooks/analitica_claro_youtube.ipynb`](notebooks/analitica_claro_youtube.ipynb) y scripts modulares en `src/`.
3. **Entregable 3 (Datos Utilizados):** [`data/raw/youtube_claro_raw.csv`](data/raw/youtube_claro_raw.csv) con documentación de origen.
4. **Entregable 4 (Dashboard):** [`dashboard/dashboard_ejecutivo_claro.html`](dashboard/dashboard_ejecutivo_claro.html) (Plotly interactivo).
5. **Entregable 5 (Video de Presentación):** Enlace oficial al video en YouTube ([ver video](https://youtu.be/g5HPaWA3JwU) / [`entregables/upload/Enlace al Video.txt`](entregables/upload/Enlace%20al%20Video.txt)) con distribución equitativa de tiempo entre Audric Rosario y Orlando Benítez.
