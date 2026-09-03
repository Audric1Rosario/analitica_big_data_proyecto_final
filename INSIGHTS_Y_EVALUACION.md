# Evaluación del Proyecto Final e Insights Estratégicos
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Proyecto:** Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3  
**Caso de Estudio:** Claro República Dominicana (`@clarord`)  
**Equipo Evaluado:** Audric Rosario & Orlando Benítez  
**Rol Evaluador:** Senior Data Scientist & Business Intelligence Advisor (PhD en Big Data)  
**Fecha de Evaluación:** Septiembre 2026  

---

## 1. Matriz de Calificación Oficial según la Rúbrica de la UAPA (25 Puntos)

A continuación se detalla la auditoría de cumplimiento respecto a los ocho criterios oficiales establecidos en el numeral 9 del documento general del curso (`Proyecto_Final.md`):

| Criterio de Evaluación | Secciones Oficiales | Puntos Posibles | Calificación Otorgada | Justificación Académica y Evidencia |
| :--- | :---: | :---: | :---: | :--- |
| **1. Identificación del negocio, problema y objetivos** | **6.3, 6.4** | **3** | **3.0 / 3.0** | **Excelente.** Contextualización profunda de Claro Dominicana y América Móvil. El problema no es genérico ("aumentar ventas"), sino enfocado en la ceguera de datos de las encuestas tradicionales (< 4% respuesta) frente a la voz no solicitada en YouTube. Objetivo general y 5 específicos redactados con taxonomía de Bloom y viables en 40 horas. |
| **2. Datos utilizados y preparación** | **6.6, 6.7** | **3** | **3.0 / 3.0** | **Excelente.** Uso de datos 100% reales mediante la YouTube Data API v3 (799 comentarios, 56 videos). Manejo prudente de cuota (649 unidades, < 7%). Pipeline fonético en `src/preprocesamiento.py` con normalización NFKD, tratamiento de jerga dominicana (*nítido*, *avería*) y stopwords del sector telco. Dataset congelado y versionado en `data/raw/` para reproducibilidad offline. |
| **3. Selección y aplicación de la técnica analítica** | **6.8** | **5** | **5.0 / 5.0** | **Excelente.** Implementación de arquitectura Transformer preentrenada en español con atención profunda bidireccional (Self-Attention) para capturar ironía y sintaxis compleja. Clasificación multiclase calibrada (Positivo, Negativo, Neutro) y segmentación por 5 áreas de servicio técnico. Inferencia reproducible en notebook y pipeline modular. |
| **4. Análisis e interpretación de resultados** | **6.9** | **4** | **4.0 / 4.0** | **Excelente.** Análisis orientado a impacto de negocio y *churn rate*. No se limita a métricas de machine learning: explica el Net Sentiment Score (+5.8%), el liderazgo reputacional del 5G (+14.0% NSS) y la señal de alarma en Atención al Cliente (-3.2% NSS), descubriendo que las quejas reciben 4 veces más *likes* que los elogios. |
| **5. Visualizaciones y dashboard ejecutivo** | **6.10, 6.11** | **3** | **3.0 / 3.0** | **Excelente.** Cinco visualizaciones analíticas con títulos, etiquetas y valor explicativo. Dashboard ejecutivo interactivo autónomo en HTML (`dashboard_ejecutivo_claro.html`) desarrollado en Plotly con 4 tarjetas de KPIs gerenciales y 5 gráficos interactivos con tooltips sin depender de servidores comerciales. |
| **6. Solución propuesta, plan de acción, presupuesto y Gantt** | **6.12 – 6.15** | **3** | **3.0 / 3.0** | **Excelente.** Solución "Claro Sentinel NLP" perfectamente respaldada por los datos empíricos. Plan de acción en 5 fases, presupuesto detallado y realista en AWS cloud (USD $4,850/año) con justificación de ROI (< 90 días reteniendo 15 clientes/mes) y cronograma de Gantt de 16 semanas. |
| **7. Conclusiones y recomendaciones** | **6.18, 6.19** | **2** | **2.0 / 2.0** | **Excelente.** Conclusiones estrictamente derivadas de la evidencia cuantitativa sin especulaciones. Recomendaciones accionables y específicas (humanizar el bot a < 2 min en averías, auditoría técnica de fibra en horas pico 7-11 PM y benchmarking de Altice). |
| **8. Video, organización del informe, fuentes y presentación** | **7, 6.20, 6.21** | **2** | **2.0 / 2.0** | **Excelente.** Informe completo de 21 secciones en `.md` y `.docx`. Citas y referencias bajo normas APA 7ma edición. Guiones estructurados minuto a minuto para el video de 8 min y pitch de 5 min con notas de orador en diapositivas PPTX. |
| **TOTAL** | — | **25** | **25.0 / 25.0** | **CALIFICACIÓN ESTIMADA: 100% (A+) — Nivel Sobresaliente** |

---

## 2. Verificación de Criterios Especiales (Secciones 10 y 11 del Programa)

* [x] **Datos Reales y Documentados:** 799 registros reales de YouTube Data API v3 con fecha, autor, video y categoría. Cero datos sintéticos en el entregable principal.
* [x] **Técnica Realmente Aplicada:** Pipeline ejecutable en `.venv` con PyTorch y Transformers en español.
* [x] **Traducción Gerencial:** Métricas técnicas traducidas a retención de suscriptores, costo de adquisición (CAC) y satisfacción de marca.
* [x] **Herramientas 100% Gratuitas:** Python 3.12, GCP Free Tier, Hugging Face, Plotly, python-docx, GitHub. Ninguna API o licencia comercial requerida.
* [x] **Participación Equitativa:** Roles claramente divididos (Audric en Data Engineering & NLP; Orlando en BI, Estrategia y Dashboard; ambos en presentación).
* [x] **Ausencia de Vicios Comunes:** No es un ensayo teórico copiado de internet; no hay código opaco sin explicar; no se omiten fuentes de precios o citas APA.

---

## 3. Deep Dive de Insights de Negocio (Para Defensa Oral y Video)

A continuación se sintetizan los hallazgos analíticos más potentes para que Audric y Orlando los enfaticen durante la exposición:

### Insight 1: La Asimetría del "Megáfono Digital" (Ratio 4:1)
* **El Fenómeno:** Un comentario positivo en YouTube recibe en promedio **1.1 reacciones ('likes')**, mientras que un comentario que denuncia una caída de servicio o lentitud en soporte recibe un promedio de **4.2 reacciones**, con picos de hasta **45 likes y 7 respuestas de apoyo**.
* **Implicación de Negocio:** Una sola avería no resuelta en YouTube no afecta a un cliente; contagia a decenas de prospectos que estaban considerando contratar el servicio. El daño reputacional no es lineal, es exponencial.

### Insight 2: La Paradoja de Claro Dominicana (5G vs. Soporte)
* **La Fortaleza:** La red móvil 5G tiene un Net Sentiment Score de **+14.0%**. Los dominicanos reconocen a Claro como el operador con la red más veloz y de mayor penetración geográfica del país (Santiago, Distrito Nacional, carreteras).
* **La Falla Crítica:** El área de Atención al Cliente tiene un NSS negativo de **-3.2%**. La frustración no proviene de la falta de tecnología, sino de la **"trampa del bot"**: los usuarios reportan que el asistente virtual de WhatsApp y los conmutadores del 107 repiten menús cíclicos sin transferir a un agente humano.

### Insight 3: La "Hora Crítica" de la Fibra Óptica (7:00 PM - 11:00 PM)
* **El Hallazgo:** Las menciones de términos como `ping alto`, `lag` y `lento` aumentan drásticamente en videos tutoriales y pruebas de velocidad durante las noches y fines de semana.
* **Causa Raíz:** Saturación en nodos residenciales compartidos (*GPON oversubscription*) que afecta a los perfiles de mayor consumo y valor (gamers, teletrabajadores y streaming en 4K), los cuales son los más proclives a portarse a Altice.

### Insight 4: El Modelo Financiero de Claro Sentinel (USD $4,850/año)
* **El Argumento Contundente:** El ARPU (Ingreso Promedio por Usuario) de un plan triple-play o de fibra óptica en Claro RD ronda los **RD$ 2,000 - RD$ 3,000 mensuales** (~USD $35 - $50 mensuales = ~$500 USD al año).
* **Retorno:** Si el sistema de escucha activa y triaje "Claro Sentinel" evita que solo **10 a 15 clientes de fibra abandonen la compañía al mes**, la empresa preserva entre **$60,000 y $90,000 USD anuales**, pagando la inversión de $4,850 USD más de 12 veces (ROI > 1,200% sobre el valor del ciclo de vida del cliente).

---

## 4. Recomendaciones Finales para la Grabación del Video y la Clase

1. **Para Orlando Benítez:**
   * Enfócate en la narrativa gerencial: abre con fuerza hablando del costo de perder un cliente (*churn*).
   * Al mostrar el dashboard de Plotly en el video, haz zoom y pasa el cursor por los gráficos para evidenciar la interactividad en tiempo real.
   * Cierra tu bloque del presupuesto con la frase de amortización: *"Con retener 15 clientes al mes, el sistema se paga solo en menos de 90 días"*.

2. **Para Audric Rosario:**
   * Al mostrar el código en VS Code o Jupyter, resalta la **prudencia de cuota de la API** (649 unidades usadas) y la **arquitectura Transformer preentrenada en español**. Esto demuestra dominio técnico y excelencia académica.
   * Explica cómo se normalizó la jerga dominicana para que el facilitador vea que no usaron un modelo genérico en inglés sin contextualizar.

3. **Dinámica de Equipo:**
   * Cumplir con el 50% del tiempo de participación para cada uno en el video oficial.
   * Utilizar las notas de orador ya integradas en las diapositivas de PowerPoint (`PRESENTACION_VIDEO_OFICIAL.pptx` y `PRESENTACION_CLASE_5MIN.pptx`) activando la Vista Moderador.
