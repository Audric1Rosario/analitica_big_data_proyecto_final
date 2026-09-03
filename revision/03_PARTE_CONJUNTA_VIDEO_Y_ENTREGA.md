# PARTE 3: GUÍA CONJUNTA (VIDEO, PRESENTACIÓN Y ENTREGA FINAL)
**Responsables:** Audric André Rosario Rosario & Orlando Benítez Ventura  
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Facilitador:** Luis Eduardo Bayonet Robles  

---

## 🎯 Alcance de la Revisión Conjunta
Esta guía coordina las secciones compartidas del informe, la **grabación del video oficial de 8 minutos (Entregable 5)**, la preparación de la **defensa presencial de 5 minutos** y la **generación del PDF final (Entregable 1)** para someter en la plataforma UAPA.

### 📊 Puntos de la Rúbrica Evaluados en esta Parte: **4 / 25 Puntos**
* **Conclusiones y recomendaciones (Secciones 6.18 y 6.19):** 2 Puntos
* **Video oficial, organización del informe, fuentes APA y presentación (Sección 7 y 6.20):** 2 Puntos

---

## 📝 1. Secciones Compartidas del Informe a Validar Juntos

En [`INFORME_FINAL_CLARO.md`](../INFORME_FINAL_CLARO.md):

### ✅ Sección 6.2: Resumen Ejecutivo
* [ ] ¿Tiene aproximadamente una página y puede ser comprendido rápidamente por un directivo?
* [ ] ¿Menciona empresa (Claro RD), datos (799 comentarios de YouTube API), técnica (Transformer en español), métricas (NSS +5.76%), solución (Claro Sentinel) e inversión ($4,850 USD)?

### ✅ Sección 6.18: Conclusiones
* [ ] ¿Responden directamente a los objetivos específicos planteados en 6.4?
* [ ] ¿Se basan en evidencia real (fortaleza 5G vs. debilidad en soporte y ratio 4:1 de viralidad en quejas)?

### ✅ Sección 6.19: Recomendaciones
* [ ] ¿Son **exactamente cuatro (4) recomendaciones accionables** (no genéricas)?
  1. Humanizar el bot de soporte en menos de 2 minutos para averías.
  2. Estabilización técnica nocturna de fibra GPON de 7:00 PM a 11:00 PM.
  3. Despliegue de "Claro Sentinel NLP" para responder quejas en menos de 2 horas.
  4. Monitoreo competitivo continuo contra Altice Dominicana.

### ✅ Sección 6.20: Referencias
* [ ] ¿Cumplen con el formato **Normas APA 7ma Edición** (América Móvil, Devlin BERT, Google Cloud, INDOTEL, Pérez pysentimiento, Plotly)?

---

## 🎬 2. Plan de Grabación del Video Oficial (7:30 min - Entregable 5)

* **Guion Maestro:** [`GUION_VIDEO_Y_PRESENTACION.md`](../GUION_VIDEO_Y_PRESENTACION.md) — Parte I.
* **Diapositivas de Apoyo:** [`PRESENTACION_VIDEO_OFICIAL.pptx`](../PRESENTACION_VIDEO_OFICIAL.pptx).
* **Distribución de Tiempo Equitativa:**
  * **Orlando:** 3 min y 45 seg (Apertura, Problema de Negocio, Dashboard Plotly en vivo, Solución Sentinel y Presupuesto).
  * **Audric:** 3 min y 45 seg (Ingesta YouTube API, Pipeline NLP en VS Code/Notebook, Métricas NSS y Cierre).

### Pasos Operativos:
1. Conectarse en una llamada de **Google Meet, Teams o Zoom**.
2. Orlando comparte pantalla con las diapositivas y el navegador; Audric comparte cuando le toque VS Code y el Notebook.
3. Grabar la sesión (duración meta: **entre 6 y 8 minutos**).
4. Subir el video a **YouTube** (en modo *No listado* o *Público*) o **Google Drive** con acceso para cualquier persona que tenga el enlace.
5. **Reemplazar el enlace del video** en la portada (6.1) y anexo (6.21) del informe.

---

## 🎤 3. Preparación para la Defensa en Clase (5 Minutos)

* **Diapositivas de Apoyo:** [`PRESENTACION_CLASE_5MIN.pptx`](../PRESENTACION_CLASE_5MIN.pptx).
* **Estructura Diapositiva por Diapositiva:**
  * **Minuto 1 (Orlando):** Portada y el Problema: $0 CAC perdido vs. encuestas tradicionales < 4% respuesta.
  * **Minuto 2 (Audric):** Metodología: 799 comentarios, cuota de 649 unidades, Transformer preentrenado.
  * **Minuto 3 (Orlando):** Hallazgos clave: NSS +5.8%, 5G líder (+14%), crisis en soporte (-3.2%), efecto multiplicador 4:1.
  * **Minuto 4 (Audric):** Solución Claro Sentinel: triaje social a CRM, inversión de $4,850 USD, repago en < 90 días.
  * **Minuto 5 (Ambos):** 4 recomendaciones clave y preguntas del profesor Luis Eduardo Bayonet Robles.

---

## 📄 4. Compilación del Entregable 1 en PDF (10 a 15 Páginas)

1. Una vez que acuerden todos los cambios en `INFORME_FINAL_CLARO.md`, compilen el documento Word ejecutando:
   ```bash
   python src/compilar_docx.py
   ```
2. Abran el archivo [`INFORME_FINAL_CLARO.docx`](../INFORME_FINAL_CLARO.docx) en Microsoft Word.
3. Asegúrense de que el enlace del video en la Portada sea el definitivo.
4. Exporten o Guarden como PDF con el nombre:
   `INFORME_FINAL_CLARO_BENITEZ_ROSARIO.pdf`
5. Verifiquen que las páginas de cuerpo neto se mantengan en el rango recomendado de **10 a 15 páginas**.

---

## 🚀 5. Checklist Final de los 5 Entregables

* [ ] **Entregable 1:** `INFORME_FINAL_CLARO_BENITEZ_ROSARIO.pdf` (PDF formal de 21 secciones).
* [ ] **Entregable 2:** `notebooks/analitica_claro_youtube.ipynb` (Notebook pre-ejecutado con salidas).
* [ ] **Entregable 3:** `data/raw/youtube_claro_raw.csv` (799 comentarios reales).
* [ ] **Entregable 4:** `dashboard/dashboard_ejecutivo_claro.html` (Dashboard Plotly interactivo).
* [ ] **Entregable 5:** Enlace funcional al video de 8 minutos colocado en la portada del PDF.
