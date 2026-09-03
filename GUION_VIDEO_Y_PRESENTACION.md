# GUIONES DE PRESENTACIÓN: VIDEO OFICIAL Y PITCH EN CLASE
**Asignatura:** Aplicaciones Analíticas de Big Data (UAPA)  
**Proyecto:** Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3  
**Caso de Estudio:** Claro República Dominicana  
**Equipo:** Audric André Rosario Rosario (100089140) & Orlando Benítez Ventura (100090873)  

---

# PARTE I — GUION DEL VIDEO OFICIAL DEL PROYECTO (5 A 8 MINUTOS)
*Entregable 5 obligatorio para la evaluación final. Ambos integrantes participan activamente.*

### Resumen de Distribución de Tiempo
* **Duración Total Estimada:** 7 minutos con 30 segundos.
* **Orlando Benítez Ventura:** ~3 minutos y 45 segundos (Contexto de Negocio, Demostración del Dashboard, Solución 'Claro Sentinel' y Presupuesto).
* **Audric André Rosario Rosario:** ~3 minutos y 45 segundos (Extracción YouTube API v3, Demostración de Código en VS Code/Notebook, Modelo Transformer NLP y Conclusiones).

---

### [00:00 - 01:15] Bloque 1: Apertura, Empresa y Problema de Negocio
* **Orador:** **Orlando Benítez**  
* **🎬 ELEMENTO EN PANTALLA:** **[PRESENTACIÓN PPT: Diapositiva 1 (Portada) y Diapositiva 2 (El Problema de Negocio)]**  
* **Instrucción de Transición:** Iniciar mostrando Diapositiva 1 con cámara de Orlando en recuadro superior derecho. Al segundo 0:35, cambiar a Diapositiva 2 (Infografía de Encuestas Tradicionales vs. Redes Sociales).

> **Orlando:**  
> *(Con Diapositiva 1 en pantalla)*  
> "Saludos cordiales a nuestro facilitador, el profesor **Luis Eduardo Bayonet Robles**, y a los compañeros de la asignatura *Aplicaciones Analíticas de Big Data*. Mi nombre es **Orlando Benítez Ventura** (matrícula 100090873) y junto a mi compañero **Audric André Rosario Rosario** (matrícula 100089140), presentamos nuestro proyecto final: *Auditoría de Experiencia del Cliente y Sentimiento de Marca en Telecomunicaciones mediante Procesamiento de Lenguaje Natural y la YouTube Data API v3*, enfocado en **Claro República Dominicana**.
> 
> *(Cambiar a Diapositiva 2: El Problema de Negocio)*  
> En un mercado donde Claro atiende a más de cinco millones de suscriptores, la calidad percibida del servicio es el factor decisivo para evitar que un usuario se porte a la competencia. Las encuestas tradicionales por llamada o SMS tienen una tasa de respuesta menor al 4% y tardan semanas en consolidarse. Mientras tanto, en los canales digitales públicos como YouTube, miles de dominicanos comentan voluntariamente sobre caídas de internet de fibra óptica, velocidad de la red 5G o dificultades de atención. Nuestro objetivo fue transformar esa voz no solicitada del consumidor en inteligencia de negocio accionable en tiempo real."

---

### [01:15 - 02:30] Bloque 2: Objetivos y Estrategia de Datos con YouTube API v3
* **Orador:** **Audric Rosario**  
* **🎬 ELEMENTO EN PANTALLA:** **[TRANSICIÓN: De PPT Diapositiva 3 a VS CODE / DATA RAW]**  
* **Instrucción de Transición:** Mostrar Diapositiva 3 (Arquitectura de Datos) de 01:15 a 01:45. Al segundo 01:45, **compartir pantalla con VS Code** mostrando el archivo [`src/extractor_youtube.py`](src/extractor_youtube.py) y la carpeta [`data/raw/`](data/raw/).

> **Audric:**  
> *(Con Diapositiva 3 en pantalla)*  
> "Gracias, Orlando. Para abordar este reto empresarial, diseñamos un pipeline analítico reproducible de extremo a extremo, utilizando exclusivamente **herramientas 100% gratuitas**.
> 
> *(Cambiar pantalla a VS Code mostrando `src/extractor_youtube.py`)*  
> Como pueden apreciar aquí en nuestro código en Python, programamos un extractor modular conectado a la **YouTube Data API v3** en Google Cloud. Fuimos extremadamente prudentes con las políticas de cuota gratuita: consumimos únicamente 649 unidades de cuota de las 10,000 diarias disponibles, lo que representa menos del 7% del límite.
> 
> Con esta consulta en vivo recopilamos **799 comentarios únicos reales** provenientes de **56 videos corporativos**, tutoriales de la App Mi Claro y pruebas de velocidad de fibra óptica. 
> 
> *(Mostrar brevemente el archivo `data/raw/youtube_claro_raw.csv`)*  
> Los datos crudos fueron congelados localmente en formatos CSV y JSON para garantizar que el proyecto pueda ser auditado y reproducido sin depender de claves activas."

---

### [02:30 - 04:00] Bloque 3: Preprocesamiento y Modelo NLP Transformer
* **Orador:** **Audric Rosario**  
* **🎬 ELEMENTO EN PANTALLA:** **[TRANSICIÓN: De VS CODE a JUPYTER NOTEBOOK y PPT Diapositiva 4]**  
* **Instrucción de Transición:** Mostrar en pantalla [`notebooks/analitica_claro_youtube.ipynb`](notebooks/analitica_claro_youtube.ipynb) ejecutando las celdas de limpieza y clasificación. Al segundo 03:20, volver a la Diapositiva 4 (Métricas NLP) de la presentación.

> **Audric:**  
> *(Mostrando Jupyter Notebook: celdas de limpieza fonética)*  
> "El lenguaje de redes sociales en República Dominicana posee particularidades léxicas complejas: modismos como *'nítido'*, regionalismos y términos técnicos como *'ping'*, *'megas'* o *'avería'*. Diseñamos un módulo de preprocesamiento que normaliza acentos unicode, elimina URLs, menciones y filtra stopwords específicas del sector telecomunicaciones.
> 
> *(Mostrando celda de inferencia Transformer)*  
> Para la técnica analítica, implementamos una arquitectura basada en **Transformers preentrenados en español** con atención profunda. Esto nos permite interpretar el contexto sintáctico real y capturar negaciones complejas e ironías que los modelos tradicionales como Naive Bayes pasan por alto.
> 
> *(Cambiar a PPT Diapositiva 4: Hallazgos Estadísticos)*  
> Como resultado, clasificamos cada interacción en positivo, negativo o neutro, asociándola a su área de servicio. Hallamos un **81.0% de comentarios neutros**, que corresponden a consultas de soporte; un **12.4% de comentarios positivos**; y un **6.6% de quejas negativas**, situando a Claro con un **Net Sentiment Score de +5.8%**. Ahora Orlando nos mostrará cómo interactúa la gerencia con estos hallazgos en el dashboard ejecutivo."

---

### [04:00 - 05:30] Bloque 4: Visualizaciones y Demostración en Vivo del Dashboard Plotly
* **Orador:** **Orlando Benítez**  
* **🎬 ELEMENTO EN PANTALLA:** **[NAVEGADOR WEB: DASHBOARD INTERACTIVO PLOTLY EN VIVO]**  
* **Instrucción de Transición:** Compartir pantalla completa con el navegador web ejecutando [`dashboard/dashboard_ejecutivo_claro.html`](dashboard/dashboard_ejecutivo_claro.html). Orlando pasa el ratón sobre los 4 KPIs superiores y luego interactúa con las gráficas de Plotly.

> **Orlando:**  
> *(Navegador web mostrando la cabecera y tarjetas de KPIs)*  
> "Aquí observamos el **Dashboard Ejecutivo Interactivo**, desarrollado en Python con **Plotly** y compilado en una interfaz autónoma sin costo de hosting.
> 
> En la parte superior, la directiva cuenta con 4 KPIs estratégicos: 799 opiniones auditadas, el Net Sentiment Score de +5.8%, la tasa de aprobación del 12.4%, y la señal de alarma gerencial: el área de **Atención al Cliente y Soporte** es el mayor foco de reclamos, con un sentimiento neto negativo de **-3.2%**.
> 
> *(Hacer hover con el mouse sobre el gráfico de barras por servicio)*  
> Al interactuar con el gráfico por categorías, vemos un hallazgo contundente: la **Red Móvil y Cobertura 5G** es la fortaleza indiscutible de Claro con un índice neto de satisfacción de **+14.0%**. Los clientes reconocen su estabilidad en provincias.
> 
> *(Hacer scroll y mostrar el Box Plot de reacciones y términos críticos)*  
> Sin embargo, este gráfico de resonancia revela el riesgo comercial más severo: **los comentarios negativos reciben cuatro veces más 'likes' que los positivos**. Cuando un usuario reclama por una avería en la fibra nocturna o demoras en el 107, la comunidad lo viraliza, amplificando el descontento y alimentando la portabilidad hacia operadores rivales."

---

### [05:30 - 06:45] Bloque 5: Solución 'Claro Sentinel', Plan de Acción y Presupuesto
* **Orador:** **Orlando Benítez**  
* **🎬 ELEMENTO EN PANTALLA:** **[PRESENTACIÓN PPT: Diapositiva 5 (Solución Claro Sentinel), Diapositiva 6 (Presupuesto) y Diapositiva 7 (Gantt)]**  
* **Instrucción de Transición:** Volver a la presentación PPT. Mostrar Diapositiva 5 (Arquitectura Sentinel) de 05:30 a 06:05. Luego Diapositiva 6 (Presupuesto y ROI) y Diapositiva 7 (Gantt) de 06:05 a 06:45.

> **Orlando:**  
> *(Con Diapositiva 5: Solución Claro Sentinel)*  
> "Para transformar esta analítica en decisiones de negocio, diseñamos la solución **'Claro Sentinel NLP'**: un sistema que enlaza el monitoreo continuo de YouTube con el CRM corporativo de Claro. Cuando nuestro modelo detecta un reclamo con alto grado de frustración, genera un pre-ticket prioritario para que un agente contacte al cliente en el mismo hilo público en menos de 2 horas.
> 
> *(Cambiar a Diapositiva 6: Presupuesto y Retorno de Inversión)*  
> El presupuesto para implementar esta solución en producción es de tan solo **$4,850 dólares anuales** en infraestructura en la nube, aprovechando el nivel gratuito de la API. Con retener a solo 15 clientes de fibra al mes que iban a portarse a Altice, el proyecto se amortiza en menos de 90 días con un ROI superior al 300%.
> 
> *(Cambiar a Diapositiva 7: Diagrama de Gantt)*  
> El plan de implementación contempla 16 semanas de trabajo estructuradas en 5 fases, desde la conexión segura de datos hasta la salida en producción y capacitación de los agentes."

---

### [06:45 - 07:30] Bloque 6: Conclusiones Finales y Cierre
* **Oradores:** **Audric Rosario** & **Orlando Benítez**  
* **🎬 ELEMENTO EN PANTALLA:** **[PRESENTACIÓN PPT: Diapositiva 8 (Conclusiones y Recomendaciones)]**  
* **Instrucción de Transición:** Mostrar Diapositiva 8 con ambas cámaras web encendidas en recuadro.

> **Audric:**  
> "En conclusión, demostramos con rigor metodológico que las herramientas de código abierto y los modelos Transformer en español permiten transformar la voz desestructurada de redes sociales en ventaja competitiva tangible."  
> 
> **Orlando:**  
> "Nuestras recomendaciones estratégicas apuntan a humanizar el canal de soporte virtual reduciendo los menús del bot y auditar la estabilidad nocturna de la fibra óptica. Agradecemos la atención de nuestro profesor y compañeros, invitándolos a consultar nuestro repositorio oficial en GitHub. ¡Muchas gracias!"

---
---

# PARTE II — GUION PARA LA PRESENTACIÓN EN CLASE (5 MINUTOS)
*Diseñado para acompañar la presentación `PRESENTACION_CLASE_5MIN.pptx` en la defensa presencial.*

### Distribución de Diapositivas y Tiempos Estrictos

| Diapositiva | Título en Diapositiva | Responsable | 🎬 Apoyo Visual | Tiempo |
| :---: | :--- | :---: | :--- | :---: |
| **Slide 1** | **Auditoría de Experiencia y Sentimiento Claro RD** | Orlando Benítez | PPT Slide 1 (Portada y Logotipo) | 0:00 - 0:45 (45s) |
| **Slide 2** | **El Reto Empresarial: Puntos Ciegos de CX** | Orlando Benítez | PPT Slide 2 (Comparativa Encuestas vs YouTube) | 0:45 - 1:30 (45s) |
| **Slide 3** | **Arquitectura Big Data: API YouTube + Transformer** | Audric Rosario | PPT Slide 3 (Diagrama de Flujo Técnico) | 1:30 - 2:30 (60s) |
| **Slide 4** | **Hallazgos Clave y Dashboard Ejecutivo Plotly** | Audric Rosario | PPT Slide 4 (Captura Dashboard + 4 KPIs) | 2:30 - 3:30 (60s) |
| **Slide 5** | **Propuesta 'Claro Sentinel NLP', Presupuesto y ROI** | Orlando Benítez | PPT Slide 5 (Flujo CRM + Tabla de Presupuesto) | 3:30 - 4:30 (60s) |
| **Slide 6** | **Conclusiones, Recomendaciones y Ronda de Preguntas** | Ambos | PPT Slide 6 (3 Conclusiones y Cierre) | 4:30 - 5:00 (30s) |

---

### Parlamento Detallado para la Exposición en Clase (5 Minutos)

#### Diapositiva 1: Portada y Gancho Inicial (0:00 - 0:45)
* **Orlando:**  
  *"Buenos días profesor y compañeros. Hoy Audric Rosario y quien les habla, Orlando Benítez, les presentamos cómo la analítica de redes sociales y el Big Data pueden salvar millones de pesos en retención de clientes para Claro República Dominicana. En telecomunicaciones, la batalla no se gana únicamente con antenas, sino con la experiencia del cliente. Hoy les mostraremos qué opinan realmente los dominicanos sobre Claro en YouTube y cómo solucionar sus puntos críticos de servicio."*

#### Diapositiva 2: El Reto Empresarial (0:45 - 1:30)
* **Orlando:**  
  *"¿Cuál es el problema? Claro gasta fortunas en encuestas telefónicas que el 96% de los clientes no responde. Sin embargo, en videos de YouTube sobre la red 5G o tutoriales de la App Mi Claro, los usuarios dejan voluntariamente miles de comentarios sin filtro sobre caídas de fibra óptica y tiempos de espera. El problema es que esa información vive dispersa y ningún directivo la ve a tiempo para actuar. Nuestro proyecto cierra esa brecha con analítica automatizada."*

#### Diapositiva 3: Arquitectura Técnica y Datos (1:30 - 2:30)
* **Audric:**  
  *"Para capturar esta información utilizamos herramientas 100% gratuitas. Conectamos la YouTube Data API v3 con un consumo de apenas 649 unidades de cuota y extrajimos 799 comentarios reales de 56 videos clave de Claro RD.*  
  *Construimos un pipeline en Python que limpia el dialecto dominicano e implementa un Transformer preentrenado con mecanismos de autoatención bidireccional. Esto nos permitió clasificar cada opinión con rigor científico en positiva, neutra o negativa, mapeándola a su categoría técnica."*

#### Diapositiva 4: Hallazgos Clave y Dashboard Ejecutivo (2:30 - 3:30)
* **Audric:**  
  *"Los resultados muestran un Net Sentiment Score de +5.8%. El 81% de los comentarios son neutros —consultas de clientes buscando ayuda—. La red 5G es la joya de la corona con un +14% de satisfacción. Pero la alerta roja está en Atención al Cliente con un índice negativo de -3.2% y quejas graves en la estabilidad nocturna de la fibra óptica.*  
  *Además, nuestro dashboard interactivo en Plotly reveló que los reclamos reciben cuatro veces más apoyo de la comunidad que los elogios, convirtiéndose en bombas de tiempo reputacionales si no se atienden de inmediato."*

#### Diapositiva 5: Solución 'Claro Sentinel' y Retorno de Inversión (3:30 - 4:30)
* **Orlando:**  
  *"Como respuesta, diseñamos 'Claro Sentinel': un sistema que detecta automáticamente quejas críticas en YouTube y genera un pre-ticket al CRM para que soporte contacte al usuario en menos de 2 horas.*  
  *El presupuesto total de implementación es de apenas $4,850 dólares al año en infraestructura cloud. Con evitar que tan solo 15 clientes residenciales se cambien a Altice por mes, el proyecto se amortiza en menos de 90 días, generando un ROI superior al 300% en el primer año."*

#### Diapositiva 6: Conclusiones y Preguntas (4:30 - 5:00)
* **Audric:** *"Demostramos que con herramientas gratuitas y modelos de última generación se puede construir analítica de clase empresarial."*  
* **Orlando:** *"Muchas gracias por su atención, quedamos a su completa disposición para la sesión de preguntas."*
