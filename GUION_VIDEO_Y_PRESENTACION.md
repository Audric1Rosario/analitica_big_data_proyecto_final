# GUIONES DE PRESENTACIÓN: VIDEO OFICIAL Y PITCH EN CLASE
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Proyecto:** Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3  
**Caso de Estudio:** Claro República Dominicana  
**Equipo:** Audric Rosario & Orlando Benítez  

---

# PARTE I — GUION DEL VIDEO OFICIAL DEL PROYECTO (5 A 8 MINUTOS)
*Entregable 5 obligatorio para la evaluación final. Ambos integrantes participan activamente.*

### Resumen de Distribución de Tiempo
* **Duración Total:** 7 minutos con 30 segundos.
* **Orlando Benítez:** ~3 minutos y 45 segundos (Contexto de Negocio, Dashboard, Solución y Presupuesto).
* **Audric Rosario:** ~3 minutos y 45 segundos (Extracción API, Pipeline NLP Transformer, Métricas Técnicas y Conclusiones).

---

### [00:00 - 01:15] Bloque 1: Apertura, Empresa y Problema de Negocio
**Orador:** **Orlando Benítez**  
**En Pantalla:** Portada formal del proyecto y diapositiva con el logotipo de Claro RD y el mapa del problema de negocio.  
**Instrucción de Cámara:** Cámara web de Orlando encendida en esquina superior derecha.

> **Orlando:**  
> "Saludos cordiales al facilitador y a los compañeros de la asignatura *Aplicaciones Analíticas de Big Data*. Mi nombre es **Orlando Benítez** y junto a mi compañero **Audric Rosario**, presentamos nuestro proyecto final de analítica aplicada: *Auditoría de Experiencia del Cliente y Sentimiento de Marca en Telecomunicaciones mediante Procesamiento de Lenguaje Natural y la YouTube Data API v3*, enfocado en **Claro República Dominicana**.
> 
> En un mercado donde Claro atiende a más de cinco millones de suscriptores, la calidad percibida del servicio es el factor número uno que determina si un cliente se queda o se porta a la competencia. Las encuestas tradicionales por llamada o SMS tienen una tasa de respuesta inferior al 4% y tardan semanas en tabularse. Mientras tanto, en los canales digitales públicos como YouTube, miles de usuarios comentan diariamente sobre caídas de fibra óptica, cobertura 5G o quejas de atención al cliente. Nuestro objetivo fue transformar esa voz no solicitada del cliente en inteligencia accionable en tiempo real."

---

### [01:15 - 02:30] Bloque 2: Objetivos y Estrategia de Datos con YouTube API v3
**Orador:** **Audric Rosario**  
**En Pantalla:** Diapositiva técnica con la arquitectura de extracción y captura de pantalla de los archivos en `data/raw/`.  
**Instrucción de Cámara:** Cambio a cámara web de Audric.

> **Audric:**  
> "Gracias, Orlando. Para responder a este reto empresarial, planteamos un pipeline técnico que abarca desde la adquisición de datos hasta el modelado predictivo. 
> 
> En apego estricto a las normas de la universidad, utilizamos **herramientas 100% gratuitas**. Mediante la **YouTube Data API v3** en Google Cloud, programamos un extractor modular en Python optimizado para la prudencia de cuota. Con apenas 649 unidades de cuota —menos del 7% del límite diario gratuito de 10,000 unidades— recopilamos **799 comentarios únicos reales** provenientes de **56 videos corporativos**, tutoriales de la App Mi Claro y pruebas de velocidad en República Dominicana.
> 
> Los datos crudos se congelaron en formatos CSV y JSON para asegurar una reproducibilidad perfecta y auditable por el evaluador."

---

### [02:30 - 04:00] Bloque 3: Preprocesamiento y Modelo NLP Transformer
**Orador:** **Audric Rosario**  
**En Pantalla:** Compartir pantalla mostrando el código en `src/preprocesamiento.py` y `src/modelado_nlp.py` o el Notebook interactivo.

> **Audric:**  
> "El texto en redes sociales dominicanas es complejo: incluye regionalismos, contracciones informales y expresiones como *'nítido'*, *'avería'* o *'hartura'*. Diseñamos un pipeline de limpieza que normaliza acentos unicode, elimina stopwords genéricas y palabras vacías específicas del canal de telecomunicaciones.
> 
> Para la técnica analítica, implementamos una arquitectura basada en **Transformers preentrenados en español** con mecanismos de autoatención bidireccional. Esto nos permite interpretar el contexto real de la frase, las negaciones compuestas y el sarcasmo.
> 
> Cada comentario fue clasificado en tres estados: Positivo, Negativo o Neutro, asignándole además su tópico de servicio: Fibra Óptica, Red 5G, Facturación o Soporte Técnico. 
> 
> El resultado global reveló: un **81.0% de comentarios neutros**, que corresponden a consultas de usuarios; un **12.4% positivos**; y un **6.6% negativos**. Esto sitúa a Claro con un **Net Sentiment Score de +5.8%**, una percepción favorable pero con puntos vulnerables que ahora Orlando nos mostrará en el dashboard ejecutivo."

---

### [04:00 - 05:30] Bloque 4: Visualizaciones y Demostración en Vivo del Dashboard Plotly
**Orador:** **Orlando Benítez**  
**En Pantalla:** Compartir pantalla con el navegador interactuando en vivo con `dashboard_ejecutivo_claro.html`. Orlando pasa el cursor sobre las gráficas y KPIs.

> **Orlando:**  
> "Aquí tienen en pantalla nuestro **Dashboard Ejecutivo Interactivo**, desarrollado íntegramente con **Plotly** y diseñado para la alta gerencia de Claro.
> 
> En la parte superior destacamos nuestros 4 KPIs clave: el volumen de 799 opiniones auditadas, el Net Sentiment Score de +5.8%, la tasa de aprobación del 12.4%, y el indicador rojo que enciende las alarmas: el área de **Atención al Cliente y Soporte** es el principal foco de descontento, con un sentimiento neto negativo de **-3.2%**.
> 
> Si observamos la gráfica de barras por servicio, podemos ver el contraste: la **Red 5G y Cobertura Móvil** es el activo más admirado de Claro, con un índice neto de satisfacción de **+14.0%**. Sin embargo, en el gráfico de dispersión de interacciones, descubrimos un patrón crítico: **los comentarios negativos reciben cuatro veces más 'likes' que los positivos**. Cuando un usuario reclama por una avería en el soporte telefónico del 107 o lentitud en la fibra nocturna, la comunidad respalda masivamente la queja, amplificando el daño reputacional."

---

### [05:30 - 06:45] Bloque 5: Propuesta de Solución, Plan de Acción y Presupuesto
**Orador:** **Orlando Benítez**  
**En Pantalla:** Diapositiva con la arquitectura de 'Claro Sentinel', tabla del presupuesto anual de USD 4,850 y diagrama de Gantt de 16 semanas.

> **Orlando:**  
> "Ante esta realidad, no basta con mirar gráficos; se requiere una decisión de negocio. Por ello formulamos la solución **'Claro Sentinel NLP'**: un sistema de escucha social automatizada que conecta el análisis de YouTube directamente con el CRM de Claro.
> 
> Cada vez que nuestro modelo detecta un reclamo técnico con alta probabilidad de insatisfacción, se genera un pre-ticket prioritario para que un agente de soporte responda al usuario en el mismo canal público en menos de 2 horas.
> 
> Implementar esta solución en una infraestructura cloud real tiene un costo estimado de **$4,850 dólares al año** entre servidores de inferencia y almacenamiento, utilizando la cuota gratuita de la API. Con retener apenas 15 clientes residenciales de fibra al mes que estaban a punto de mudarse a Altice, el sistema se paga solo en menos de 90 días."

---

### [06:45 - 07:30] Bloque 6: Conclusiones Finales y Cierre
**Oradores:** **Audric Rosario** & **Orlando Benítez** (Cámaras activas en pantalla dividida).

> **Audric:**  
> "En conclusión, demostramos con evidencia cuantitativa que la analítica de Big Data y el NLP permiten transformar la voz informal del cliente en decisiones estratégicas de retención y calidad de red."  
> 
> **Orlando:**  
> "Agradecemos la atención de nuestro facilitador y los invitamos a consultar el código fuente completo, el dataset y el informe formal en nuestro repositorio de GitHub. ¡Muchas gracias!"

---
---

# PARTE II — GUION PARA LA PRESENTACIÓN EN CLASE (5 MINUTOS)
*Estructura diapositiva por diapositiva para preparar el archivo PPTX para la exposición presencial.*

### Distribución de Diapositivas y Tiempos Estrictos

| Diapositiva | Título / Contenido Visual | Responsable | Tiempo Asignado |
| :---: | :--- | :---: | :---: |
| **Slide 1** | **Portada y Gancho Inicial:** Título, UAPA, Nombres y Planteamiento del Reto Telco. | Orlando Benítez | 0:00 - 0:45 (45 seg) |
| **Slide 2** | **El Problema de Negocio:** Encuestas tradicionales vs. Escucha Social en YouTube. | Orlando Benítez | 0:45 - 1:30 (45 seg) |
| **Slide 3** | **Arquitectura de Big Data & NLP:** YouTube Data API v3 + Transformer en Español. | Audric Rosario | 1:30 - 2:30 (60 seg) |
| **Slide 4** | **Hallazgos Clave & Demostración del Dashboard:** NSS +5.8%, 5G fuerte, quejas en soporte. | Audric Rosario | 2:30 - 3:30 (60 seg) |
| **Slide 5** | **Propuesta de Negocio 'Claro Sentinel', Presupuesto ($4.8k) y ROI:** | Orlando Benítez | 3:30 - 4:30 (60 seg) |
| **Slide 6** | **Conclusiones, Recomendaciones y Ronda de Preguntas:** | Audric & Orlando | 4:30 - 5:00 (30 seg) |

---

### Parlamento Detallado para la Exposición en Clase (5 Minutos)

#### Diapositiva 1: Portada y Gancho Inicial (0:00 - 0:45)
* **Orlando:**  
  *"Buenos días profesor y compañeros. Hoy Audric Rosario y quien les habla, Orlando Benítez, les presentamos cómo la analítica de redes sociales y el Big Data pueden salvar millones de pesos en retención de clientes para Claro República Dominicana. En telecomunicaciones, la batalla no se gana únicamente con antenas, sino con la experiencia del cliente. Hoy les mostraremos qué opinan realmente los dominicanos sobre Claro en YouTube y cómo solucionar sus puntos críticos."*

#### Diapositiva 2: El Problema de Negocio (0:45 - 1:30)
* **Orlando:**  
  *"¿Cuál es el problema? Claro gasta fortunas en encuestas telefónicas que el 96% de la gente no responde. Sin embargo, en videos de YouTube sobre la red 5G o tutoriales de la App Mi Claro, los usuarios dejan voluntariamente miles de opiniones sin filtro sobre fallas de fibra y tiempos de espera. El problema es que esa información vive dispersa y ningún directivo la ve a tiempo para actuar. Nuestro proyecto cierra esa brecha con analítica automatizada."*

#### Diapositiva 3: Arquitectura Técnica y Datos (1:30 - 2:30)
* **Audric:**  
  *"Para capturar esta información utilizamos herramientas 100% gratuitas. Conectamos la YouTube Data API v3 con un consumo de apenas 649 unidades de cuota y extrajimos 799 comentarios reales de 56 videos clave de Claro RD.*  
  *Construimos un pipeline en Python que limpia el dialecto dominicano e implementa un Transformer preentrenado con mecanismos de autoatención. Esto nos permitió clasificar cada opinión con rigor científico en positiva, neutra o negativa, mapeándola a su categoría técnica."*

#### Diapositiva 4: Hallazgos Clave y Dashboard Ejecutivo (2:30 - 3:30)
* **Audric:**  
  *"Los resultados muestran un Net Sentiment Score de +5.8%. El 81% de los comentarios son neutros —consultas de clientes buscando ayuda—. La red 5G es la joya de la corona con un +14% de satisfacción. Pero la alerta roja está en Atención al Cliente con un índice negativo de -3.2% y quejas graves en la estabilidad nocturna de la fibra óptica.*  
  *Además, nuestro dashboard interactivo en Plotly reveló que los reclamos reciben cuatro veces más apoyo que los elogios, convirtiéndose en bombas de tiempo reputacionales si no se atienden de inmediato."*

#### Diapositiva 5: Solución 'Claro Sentinel' y Retorno de Inversión (3:30 - 4:30)
* **Orlando:**  
  *"Como respuesta, diseñamos 'Claro Sentinel': un sistema que detecta automáticamente quejas críticas en YouTube y genera un pre-ticket al CRM para que soporte contacte al usuario en menos de 2 horas.*  
  *El presupuesto total de implementación es de apenas $4,850 dólares al año en infraestructura cloud. Con evitar que tan solo 15 clientes residenciales se cambien a Altice por mes, el proyecto se amortiza en menos de 90 días, generando un ROI superior al 300% en el primer año."*

#### Diapositiva 6: Conclusiones y Preguntas (4:30 - 5:00)
* **Audric:** *"Demostramos que con herramientas gratuitas y modelos de última generación se puede construir analítica de clase empresarial."*  
* **Orlando:** *"Muchas gracias por su atención, quedamos a su completa disposición para la sesión de preguntas."*
