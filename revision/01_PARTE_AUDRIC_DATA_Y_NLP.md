# PARTE 1: GUÍA DE REVISIÓN TÉCNICA (DATA ENGINEERING & NLP)
**Responsable:** Audric André Rosario Rosario (Matrícula: 100089140)  
**Rol:** Lead Data Engineering & NLP Modeling  
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Facilitador:** Luis Eduardo Bayonet Robles  

---

## 🎯 Alcance de la Revisión de Audric
Audric es responsable de auditar y dar el visto bueno a toda la **arquitectura de datos, scripts de procesamiento, modelo Transformer de NLP, notebook de Google Colab y las secciones técnicas del informe**.

### 📊 Puntos de la Rúbrica Evaluados en esta Parte: **12 / 25 Puntos**
* **Datos utilizados y preparación (Secciones 6.6 y 6.7):** 3 Puntos
* **Selección y aplicación de la técnica analítica (Sección 6.8):** 5 Puntos
* **Análisis e interpretación técnica de resultados (Sección 6.9):** 4 Puntos

---

## 🌿 1. Paso a Paso en Git para Audric
```bash
# 1. Asegurarte de estar en la versión más reciente de main
git checkout main
git pull origin main

# 2. Crear tu rama personal de trabajo
git checkout -b audric/revision-tecnica

# 3. Realizar los ajustes necesarios y registrar con Conventional Commits:
git add .
git commit -m "feat(nlp): afinar umbral de clasificación de neutralidad"

# 4. Subir tu rama a GitHub para revisión
git push -u origin audric/revision-tecnica
```

---

## 📁 2. Archivos y Código bajo Responsabilidad de Audric

| Archivo | Función Principal | Qué debes verificar |
| :--- | :--- | :--- |
| [`src/extractor_youtube.py`](../src/extractor_youtube.py) | Extractor de YouTube Data API v3 | Que lea `YT_API_KEY` desde `.env`, no exponga credenciales y mantenga el consumo $< 800$ unidades de cuota. |
| [`src/preprocesamiento.py`](../src/preprocesamiento.py) | Higienización y stopwords en español | Normalización NFKD, regex para URLs/menciones y stopwords dominicanas (`klk`, `jevi`, `paquetico`). |
| [`src/modelado_nlp.py`](../src/modelado_nlp.py) | Inferencia con Transformer preentrenado | Clasificación en Positivo, Negativo, Neutro y cálculo de scores calibrados. |
| [`src/procesar_pipeline.py`](../src/procesar_pipeline.py) | Pipeline unificado de ETL | Conexión directa entre `data/raw/` y `data/processed/`. |
| [`notebooks/analitica_claro_youtube.ipynb`](../notebooks/analitica_claro_youtube.ipynb) | Notebook ejecutable (Entregable 2) | Que abra con todas sus celdas ya ejecutadas (1 a 8), mostrando tablas y gráficos sin errores. |
| [`data/raw/youtube_claro_raw.csv`](../data/raw/youtube_claro_raw.csv) | Dataset crudo real (Entregable 3) | 799 comentarios auditables extraídos de 56 videos. |

---

## 📝 3. Secciones del Informe Asignadas a Audric

Debes revisar y validar la redacción en [`INFORME_FINAL_CLARO.md`](../INFORME_FINAL_CLARO.md) de:

### ✅ Sección 6.6: Datos Utilizados
* [ ] ¿Están documentados los 799 comentarios, los 56 videos y el consumo de 649 unidades de cuota?
* [ ] ¿Está clara la tabla con los tipos de datos de las variables (`comment_id`, `video_id`, `published_at`, `like_count`)?

### ✅ Sección 6.7: Preparación de los Datos
* [ ] ¿El diagrama Mermaid representa fielmente el flujo de limpieza?
* [ ] ¿Se justifica la remoción de URLs, tratamiento de risas y stopwords telco dominicanas?

### ✅ Sección 6.8: Técnica o Modelo Analítico
* [ ] ¿Se explica claramente por qué un Transformer preentrenado con autoatención bidireccional supera a modelos simples tipo Naive Bayes?
* [ ] ¿Está presente la fórmula matemática del Net Sentiment Score (NSS)?
  $$\text{NSS} = \% \text{Positivos} - \% \text{Negativos}$$

### ✅ Sección 6.9: Análisis de Resultados (Técnico)
* [ ] ¿Están respondidas las 4 preguntas obligatorias del profesor para cada hallazgo?
  * *¿Qué encontramos?*
  * *¿Qué significa?*
  * *¿Por qué es importante?*
  * *¿Qué decisión podría tomar la organización?*
* [ ] ¿Coinciden las cifras: 81.0% Neutro (647), 12.4% Positivo (99), 6.6% Negativo (53) $\rightarrow$ NSS = **+5.76%**?

### ✅ Sección 6.21: Anexos
* [ ] ¿Están los enlaces al repositorio GitHub, dashboard HTML y dataset crudo?
* [ ] ¿Está incluida la Declaración de Integridad y Validación de IA (Sección 12)?

---

## 🎥 4. Participación de Audric en el Video Oficial y la Clase

### En el Video Oficial (5 a 8 min):
* **Tu Bloque Principal:** Minuto **01:15 a 03:30** (~2 minutos y 15 segundos).
* **Qué debes mostrar en pantalla:**
  1. Cambiar a **VS Code**: mostrar brevemente `src/extractor_youtube.py` y `data/raw/`.
  2. Abrir **Jupyter Notebook** (`notebooks/analitica_claro_youtube.ipynb`) y mostrar la celda de inferencia con el Transformer y el resumen de métricas (NSS +5.76%).
  3. Cierre conjunto en el minuto 05:45 a 07:30.

### En la Presentación en Clase (5 min):
* **Minuto 2:** Explicar la ingesta ética con YouTube API v3 (649 unidades de cuota) y normalización del español dominicano.
* **Minuto 4:** Explicar el modelo Transformer y la arquitectura técnica de "Claro Sentinel NLP".
