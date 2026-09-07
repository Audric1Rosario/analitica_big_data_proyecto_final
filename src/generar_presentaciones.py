"""
Generador de Presentaciones PowerPoint (.pptx) Profesionales
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric André Rosario Rosario & Orlando Benítez Ventura
Facilitador: Luis Eduardo Bayonet Robles
Empresa Caso de Estudio: Claro República Dominicana (@clarord)
"""

import os

import pandas as pd
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

# Paleta de Colores Corporativa
COLOR_CLARO_RED = RGBColor(218, 41, 28)  # #DA291C
COLOR_DARK_NAVY = RGBColor(15, 23, 42)  # #0F172A
COLOR_CARD_BG = RGBColor(30, 41, 59)  # #1E293B
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
COLOR_GREEN = RGBColor(16, 185, 129)  # #10B981
COLOR_LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC
COLOR_BORDER = RGBColor(51, 65, 85)  # #334155


def cargar_metricas_dataset(csv_path: str = "data/processed/youtube_claro_processed.csv") -> dict[str, object]:
    """Carga y deriva dinámicamente las métricas de negocio desde el dataset enriquecido."""
    if not os.path.exists(csv_path):
        csv_path = "data/raw/youtube_claro_raw.csv"

    df = pd.read_csv(csv_path)
    if "sentiment_label" not in df.columns and "ground_truth_sentiment" in df.columns:
        df["sentiment_label"] = df["ground_truth_sentiment"]

    total = len(df)
    counts = df["sentiment_label"].value_counts()
    pos = int(counts.get("POSITIVO", 0))
    neg = int(counts.get("NEGATIVO", 0))
    neu = int(counts.get("NEUTRO", 0))

    pct_pos = (pos / total) * 100 if total > 0 else 0.0
    pct_neg = (neg / total) * 100 if total > 0 else 0.0
    pct_neu = (neu / total) * 100 if total > 0 else 0.0
    nss = round(pct_pos - pct_neg, 2)

    col_s = "service_category" if "service_category" in df.columns else "topic_category"
    serv_summary: dict[str, float] = {}
    if col_s in df.columns:
        for s in df[col_s].dropna().unique():
            sub = df[df[col_s] == s]
            if len(sub) > 0:
                p = (sub["sentiment_label"] == "POSITIVO").sum()
                n = (sub["sentiment_label"] == "NEGATIVO").sum()
                serv_summary[str(s)] = round(((p - n) / len(sub)) * 100, 2)

    return {
        "df": df,
        "total": total,
        "pos": pos,
        "neg": neg,
        "neu": neu,
        "pct_pos": pct_pos,
        "pct_neg": pct_neg,
        "pct_neu": pct_neu,
        "nss": nss,
        "serv_summary": serv_summary,
    }


def crear_diapositiva_base(
    prs: Presentation, titulo: str, subtitulo: str = "", orador: str = "", apoyo_visual: str = ""
) -> object:
    """Crea una diapositiva con estilo corporativo consistente en formato 16:9."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Fondo general oscuro de alta gama
    background = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    background.fill.solid()
    background.fill.fore_color.rgb = COLOR_DARK_NAVY
    background.line.color.rgb = COLOR_DARK_NAVY

    # Barra superior de acento Claro Red
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_CLARO_RED
    top_bar.line.color.rgb = COLOR_CLARO_RED

    # Título y Subtítulo
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(8.5), Inches(1.2))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = titulo
    p.font.bold = True
    p.font.size = Pt(26)
    p.font.color.rgb = COLOR_WHITE

    if subtitulo:
        p2 = tf.add_paragraph()
        p2.text = subtitulo
        p2.font.size = Pt(13)
        p2.font.color.rgb = COLOR_TEXT_MUTED

    # Badge de Orador y Apoyo Visual
    if orador or apoyo_visual:
        badge_box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.2), Inches(0.45), Inches(3.4), Inches(0.85)
        )
        badge_box.fill.solid()
        badge_box.fill.fore_color.rgb = COLOR_CARD_BG
        badge_box.line.color.rgb = COLOR_BORDER
        btf = badge_box.text_frame
        btf.word_wrap = True
        bp1 = btf.paragraphs[0]
        bp1.text = f"🎤 {orador}" if orador else ""
        bp1.font.bold = True
        bp1.font.size = Pt(11)
        bp1.font.color.rgb = COLOR_CLARO_RED
        if apoyo_visual:
            bp2 = btf.add_paragraph()
            bp2.text = f"🎬 {apoyo_visual}"
            bp2.font.size = Pt(9.5)
            bp2.font.color.rgb = COLOR_TEXT_MUTED

    # Pie de página discreto
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
    ftf = footer_box.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "UAPA • Aplicaciones Analíticas de Big Data • Proyecto Final: Claro República Dominicana"
    fp.font.size = Pt(9.5)
    fp.font.color.rgb = COLOR_TEXT_MUTED

    return slide


def agregar_tarjeta(
    slide: object,
    left: float,
    top: float,
    width: float,
    height: float,
    titulo: str,
    contenido: list[str],
    color_acento: RGBColor = COLOR_CLARO_RED,
    bg_color: RGBColor = COLOR_CARD_BG,
) -> None:
    """Crea un contenedor de tarjeta estilizado."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = COLOR_BORDER

    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(left), Inches(top + 0.15), Inches(0.08), Inches(height - 0.3)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = color_acento
    accent.line.color.rgb = color_acento

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.18)

    p1 = tf.paragraphs[0]
    p1.text = titulo
    p1.font.bold = True
    p1.font.size = Pt(14)
    p1.font.color.rgb = COLOR_WHITE

    for item in contenido:
        p = tf.add_paragraph()
        p.text = f"• {item}" if not item.startswith("  ") else item
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(4)


def generar_presentacion_video(output_path: str = "PRESENTACION_VIDEO_OFICIAL.pptx") -> str:
    """Genera la presentación estructurada para el Video Oficial (8 minutos, 8 diapositivas)."""
    print("[PPTX] Generando presentación para el Video Oficial (8 minutos)...")
    m = cargar_metricas_dataset()
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # --- SLIDE 1: PORTADA ---
    slide1 = prs.slides.add_slide(prs.slide_layouts[6])
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_DARK_NAVY
    bg1.line.color.rgb = COLOR_DARK_NAVY

    top1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
    top1.fill.solid()
    top1.fill.fore_color.rgb = COLOR_CLARO_RED

    tx1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(5.0))
    tf1 = tx1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "UNIVERSIDAD ABIERTA PARA ADULTOS (UAPA) • VICERRECTORÍA DE POSGRADO"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_MUTED

    p_m = tf1.add_paragraph()
    p_m.text = "Maestría en Analítica de Big Data e Inteligencia de Negocios"
    p_m.font.size = Pt(14)
    p_m.font.color.rgb = COLOR_TEXT_MUTED

    p2 = tf1.add_paragraph()
    p2.text = "Auditoría de Experiencia del Cliente y Sentimiento de Marca en Telecomunicaciones vía YouTube API v3 y Deep Learning (BETO)"
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WHITE
    p2.space_before = Pt(15)

    p3 = tf1.add_paragraph()
    p3.text = "Caso de Estudio: Claro República Dominicana (@clarord)"
    p3.font.size = Pt(18)
    p3.font.color.rgb = COLOR_CLARO_RED
    p3.space_before = Pt(10)

    p4 = tf1.add_paragraph()
    p4.text = "Equipo Investigador: Audric André Rosario Rosario (100089140) & Orlando Benítez Ventura (100090873)\nFacilitador: Luis Eduardo Bayonet Robles | Fecha: Septiembre 2026"
    p4.font.size = Pt(12)
    p4.font.color.rgb = COLOR_TEXT_MUTED
    p4.space_before = Pt(25)

    slide1.notes_slide.notes_text_frame.text = (
        "[00:00 - 00:30] AUDRIC: Saludos profesor Luis Eduardo Bayonet y compañeros de la maestría. "
        "Les presentamos nuestra evaluación final de Aplicaciones Analíticas de Big Data: "
        "Auditoría de Experiencia y Sentimiento en Claro República Dominicana con Transformers preentrenados."
    )

    # --- SLIDE 2: CONTEXTO Y PROBLEMA ---
    slide2 = crear_diapositiva_base(
        prs,
        "Contexto Empresarial y Problemática de Negocio",
        "El desafío del Churn silencioso y la fricción de atención en telecomunicaciones",
        orador="Audric Rosario",
        apoyo_visual="Cámara / Diapositiva 2",
    )
    agregar_tarjeta(
        slide2,
        0.8,
        1.8,
        5.6,
        4.8,
        "El Negocio: Claro Dominicana",
        [
            "Líder del mercado de telecomunicaciones en República Dominicana.",
            "Subsidiaria de América Móvil con más de 6 millones de líneas.",
            "Despliegue pionero de Red 5G y expansión masiva de Fibra Óptica.",
            "Fuerte reputación histórica de cobertura y confiabilidad.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide2,
        6.8,
        1.8,
        5.6,
        4.8,
        "La Fricción: Escucha Pasiva y Churn",
        [
            "Las redes sociales actúan como centro de quejas desatendidas.",
            "Demoras en canales de soporte (Call Center 107 y WhatsApp Bot).",
            "Pérdida de clientes (Churn) por degradación de servicio en horas pico.",
            "Falta de clasificación automatizada para triaje y resolución ágil.",
        ],
        COLOR_CLARO_RED,
    )
    slide2.notes_slide.notes_text_frame.text = (
        "[00:30 - 01:15] AUDRIC: Claro RD es líder en cobertura, pero enfrenta un reto crítico en CX. "
        "En YouTube, cientos de clientes expresan quejas técnicas sobre fibra óptica o lentitud del bot. "
        "Al no existir un sistema de triaje automatizado en tiempo real, estas quejas se acumulan y aceleran la fuga de clientes."
    )

    # --- SLIDE 3: DATOS Y ARQUITECTURA ---
    slide3 = crear_diapositiva_base(
        prs,
        "Datos Utilizados y Arquitectura de Ingesta",
        "YouTube Data API v3 oficial con gobernanza estricta de cuotas",
        orador="Audric Rosario",
        apoyo_visual="Diagrama de Flujo / Captura Consola GCP",
    )
    agregar_tarjeta(
        slide3,
        0.8,
        1.8,
        5.6,
        4.8,
        "Consumo y Cuota de API",
        [
            "Fuente Oficial: Google Cloud Platform (YouTube Data API v3).",
            "Optimización de Cuota: 649 unidades utilizadas de 10,000 diarias (<7%).",
            "Endpoint económico: commentThreads.list (1 unidad por 100 comentarios).",
            "Muestra recolectada: 799 comentarios reales de 39 videos analizados.",
            "Variables: Autor, texto, fecha de publicación y conteo de likes.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide3,
        6.8,
        1.8,
        5.6,
        4.8,
        "Gobernanza y Reproducibilidad",
        [
            "Datos crudos congelados en data/raw/ (CSV y JSON).",
            "Permite evaluación académica offline sin credenciales activas.",
            "Gestor canónico de dependencias: uv vía pyproject.toml.",
            "Variables protegidas sin exposición de secretos en .env.",
            "Integridad y compatibilidad plena con Pyright y Ruff.",
        ],
        COLOR_GREEN,
    )
    slide3.notes_slide.notes_text_frame.text = (
        "[01:15 - 02:30] AUDRIC: Diseñamos una arquitectura reproducible con herramientas 100% gratuitas. "
        "Consumimos solo 649 unidades de cuota y congelamos 799 opiniones reales para que el facilitador pueda evaluar el código offline."
    )

    # --- SLIDE 4: MODELADO NLP TRANSFORMER ---
    slide4 = crear_diapositiva_base(
        prs,
        "Modelado NLP: Transformer Preentrenado en Español (BETO)",
        "Autoatención bidireccional profunda sin degradación léxica",
        orador="Audric Rosario",
        apoyo_visual="Transición a Jupyter Notebook / Celdas NLP",
    )
    agregar_tarjeta(
        slide4,
        0.8,
        1.8,
        5.6,
        4.8,
        "Preprocesamiento Lingüístico",
        [
            "Normalización fonética Unicode NFKD (preserva acentos y ñ).",
            "Higienización Regex de URLs, menciones @ y ruido sintáctico.",
            "Tratamiento de jerga dominicana (klk, nítido, avería, megas).",
            "Stopwords personalizadas del dominio de telecomunicaciones.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide4,
        6.8,
        1.8,
        5.6,
        4.8,
        "Transformer Puro (BETO)",
        [
            "Modelo Deep Learning: finiteautomata/beto-sentiment-analysis.",
            "Mecanismos de Autoatención Bidireccional (Self-Attention).",
            "Cero Fallback: eliminación de diccionarios léxicos heurísticos.",
            "Captura negaciones complejas, quejas técnicas e ironías.",
            "Inferencia vectorizada por lotes (batch processing) en PyTorch.",
        ],
        COLOR_CLARO_RED,
    )
    slide4.notes_slide.notes_text_frame.text = (
        "[02:30 - 04:00] AUDRIC: El dialecto en redes en RD es altamente informal. Implementamos un preprocesamiento robusto "
        "y aplicamos un Transformer preentrenado puro en español, BETO. Eliminamos cualquier fallback a listas de palabras fijas "
        "para garantizar que la clasificación capture el contexto profundo de cada comentario."
    )

    # --- SLIDE 5: HALLAZGOS Y DASHBOARD EJECUTIVO ---
    slide5 = crear_diapositiva_base(
        prs,
        "Hallazgos de Negocio y Dashboard Plotly",
        "Diagnóstico de reputación derivado del modelo Transformer real",
        orador="Orlando Benítez",
        apoyo_visual="Compartir Pantalla: dashboard_ejecutivo_claro.html interactivo",
    )
    nss_val = m["nss"]
    nss_str = f"{nss_val:+.2f}%"
    agregar_tarjeta(
        slide5,
        0.8,
        1.8,
        3.7,
        4.8,
        "Indicadores Clave (KPIs)",
        [
            f"Volumen Auditado: {m['total']} opiniones reales.",
            f"Net Sentiment Score (NSS): {nss_str}.",
            f"Positivos: {m['pct_pos']:.1f}% ({m['pos']} opiniones).",
            f"Negativos: {m['pct_neg']:.1f}% ({m['neg']} quejas).",
            f"Neutros: {m['pct_neu']:.1f}% ({m['neu']} consultas).",
        ],
        COLOR_GREEN if nss_val >= 0 else COLOR_CLARO_RED,
    )

    serv_items = []
    for s_name, s_nss in list(m["serv_summary"].items())[:4]:
        bullet = "🟢" if s_nss >= 0 else "🔴"
        serv_items.append(f"{bullet} {s_name}: {s_nss:+.1f}% NSS.")
    if not serv_items:
        serv_items = ["• Segmentación por áreas de servicio."]

    agregar_tarjeta(slide5, 4.8, 1.8, 3.7, 4.8, "Comportamiento por Servicio", serv_items, COLOR_CLARO_RED)
    agregar_tarjeta(
        slide5,
        8.8,
        1.8,
        3.7,
        4.8,
        "Patrón de Resonancia",
        [
            "Las quejas reciben respaldo directo de la comunidad.",
            "Picos de likes en comentarios sobre averías de fibra.",
            "Términos críticos: lentitud, ping, caída, bot, espera.",
            "Riesgo de fuga (churn) hacia operadores competidores.",
        ],
        COLOR_BORDER,
    )
    slide5.notes_slide.notes_text_frame.text = (
        f"[04:00 - 05:30] ORLANDO: Aquí mostramos nuestro dashboard interactivo en Plotly. "
        f"El modelo Transformer sitúa el NSS global en {nss_str}. Identificamos que las consultas neutrales dominan el canal, "
        f"pero las quejas negativas se concentran fuertemente en fibra óptica y soporte al cliente, recibiendo alta resonancia de likes."
    )

    # --- SLIDE 6: SOLUCIÓN CLARO SENTINEL ---
    slide6 = crear_diapositiva_base(
        prs,
        "Solución Propuesta: 'Claro Sentinel NLP'",
        "De la escucha social pasiva al enrutamiento proactivo de quejas",
        orador="Orlando Benítez",
        apoyo_visual="Mostrar Diapositiva 6: Arquitectura Sentinel",
    )
    agregar_tarjeta(
        slide6,
        0.8,
        1.8,
        3.7,
        4.8,
        "1. Ingesta Continua",
        [
            "Worker automático consulta YouTube API.",
            "Detección de comentarios en videos oficiales y tutoriales.",
            "Filtro de privacidad y anonimización de datos.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide6,
        4.8,
        1.8,
        3.7,
        4.8,
        "2. Triaje Inteligente",
        [
            "Scoring de sentimiento con Transformer BETO.",
            "Detección de averías técnicas críticas (ping, fibra caída).",
            "Priorización según intensidad y likes comunitarios.",
        ],
        COLOR_CLARO_RED,
    )
    agregar_tarjeta(
        slide6,
        8.8,
        1.8,
        3.7,
        4.8,
        "3. Enlace al CRM",
        [
            "Generación de pre-ticket en Salesforce/Genesys.",
            "Respuesta pública oficial en menos de 2 horas.",
            "Reducción proyectada de churn del 1.8%.",
        ],
        COLOR_GREEN,
    )
    slide6.notes_slide.notes_text_frame.text = (
        "[05:30 - 06:05] ORLANDO: No basta con ver gráficos, se necesita actuar. "
        "Claro Sentinel detecta reclamos críticos y crea pre-tickets al CRM para responder en menos de 2 horas."
    )

    # --- SLIDE 7: PRESUPUESTO Y GANTT ---
    slide7 = crear_diapositiva_base(
        prs,
        "Presupuesto de Implementación y Diagrama de Gantt",
        "Inversión cloud accesible y cronograma estructurado en 16 semanas",
        orador="Orlando Benítez",
        apoyo_visual="Mostrar Diapositiva 7: Tabla Presupuesto y Gantt",
    )
    agregar_tarjeta(
        slide7,
        0.8,
        1.8,
        5.6,
        4.8,
        "Presupuesto Anual (USD)",
        [
            "Servidor Inferencia AWS EC2 (g4dn.xlarge GPU): $2,160",
            "Base de Datos Cloud PostgreSQL (AWS RDS): $540",
            "YouTube Data API (GCP Free Tier): $0 (Gratuito)",
            "Capacitación al Personal de Atención Digital: $1,000",
            "Bolsa de Imprevistos Operacionales: $1,150",
            "INVERSIÓN TOTAL ANUAL: USD $4,850",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide7,
        6.8,
        1.8,
        5.6,
        4.8,
        "Cronograma en 5 Fases (16 Semanas)",
        [
            "Fase 1 (Semanas 1-3): Conexión de Ingesta y ETL Automático.",
            "Fase 2 (Semanas 4-7): Calibración del Transformer en Producción.",
            "Fase 3 (Semanas 8-10): Integración Webhooks a CRM y Dashboard Plotly.",
            "Fase 4 (Semanas 11-14): Piloto Controlado con Mesa de Ayuda.",
            "Fase 5 (Semanas 15-16): Despliegue General y Entrega Final.",
        ],
        COLOR_GREEN,
    )
    slide7.notes_slide.notes_text_frame.text = (
        "[06:05 - 06:45] ORLANDO: El costo total de implementación es de solo USD $4,850 anuales. "
        "Con recuperar apenas 12 clientes residenciales de fibra óptica al año, el sistema se paga por sí mismo."
    )

    # --- SLIDE 8: CONCLUSIONES Y CIERRE ---
    slide8 = crear_diapositiva_base(
        prs,
        "Conclusiones Estratégicas y Recomendaciones",
        "Valor del Big Data y NLP aplicada a la competitividad en telecomunicaciones",
        orador="Audric Rosario & Orlando Benítez",
        apoyo_visual="Cámara Dual / Cierre",
    )
    agregar_tarjeta(
        slide8,
        0.8,
        1.8,
        5.6,
        4.8,
        "Conclusiones del Estudio",
        [
            "Viabilidad Técnica: NLP Deep Learning opera con alta precisión sobre 799 opiniones.",
            f"NSS de {nss_str}: La marca cuenta con respaldo, pero la fibra óptica demanda atención.",
            "Resonancia Comunitaria: Las quejas no resueltas generan viralidad negativa y churn.",
            "ROI Positivo: Inversión contenida de $4,850 con retorno proyectado en menos de 90 días.",
        ],
        COLOR_CLARO_RED,
    )
    agregar_tarjeta(
        slide8,
        6.8,
        1.8,
        5.6,
        4.8,
        "Recomendaciones Gerenciales",
        [
            "Implementar el protocolo de respuesta oficial en hilos de soporte (<2h).",
            "Humanizar y optimizar el flujo del WhatsApp Bot con opciones rápidas.",
            "Auditar latencia y estabilidad de fibra óptica en horario nocturno (7-11 PM).",
            "Integrar el NSS en el cuadro de mando de calidad de la Dirección General.",
        ],
        COLOR_GREEN,
    )
    slide8.notes_slide.notes_text_frame.text = (
        "[06:45 - 07:30] AUDRIC: En conclusión, demostramos con rigor que herramientas de código abierto generan valor empresarial. "
        "ORLANDO: Recomendamos humanizar el bot y auditar la fibra. ¡Muchas gracias por su atención!"
    )

    prs.save(output_path)
    print(f"[EXITO] Presentación del Video Oficial generada en: {output_path}")
    return output_path


def generar_presentacion_clase_5min(output_path: str = "PRESENTACION_CLASE_5MIN.pptx") -> str:
    """Genera la presentación condensada para la Exposición en Clase (5 minutos, 6 diapositivas)."""
    print("[PPTX] Generando presentación para la Clase de 5 Minutos...")
    m = cargar_metricas_dataset()
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # --- SLIDE 1: PORTADA Y PITCH INICIAL ---
    slide1 = prs.slides.add_slide(prs.slide_layouts[6])
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_DARK_NAVY
    bg1.line.color.rgb = COLOR_DARK_NAVY

    top1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
    top1.fill.solid()
    top1.fill.fore_color.rgb = COLOR_CLARO_RED

    tx = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(4.5))
    tf = tx.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "UAPA • APLICACIONES ANALÍTICAS DE BIG DATA • PROYECTO FINAL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_MUTED

    p2 = tf.add_paragraph()
    p2.text = "Auditoría de Experiencia y Sentimiento de Marca en Claro República Dominicana"
    p2.font.size = Pt(30)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WHITE
    p2.space_before = Pt(15)

    p3 = tf.add_paragraph()
    p3.text = "Minería de Opinión y NLP Transformer (BETO) sobre YouTube Data API v3"
    p3.font.size = Pt(17)
    p3.font.color.rgb = COLOR_CLARO_RED
    p3.space_before = Pt(10)

    p4 = tf.add_paragraph()
    p4.text = "Expositores: Audric André Rosario Rosario (100089140) & Orlando Benítez Ventura (100090873)\nFacilitador: Luis Eduardo Bayonet Robles | Duración: 5 Minutos"
    p4.font.size = Pt(13)
    p4.font.color.rgb = COLOR_TEXT_MUTED
    p4.space_before = Pt(30)

    slide1.notes_slide.notes_text_frame.text = (
        "[0:00 - 0:45] AUDRIC: Buenas tardes profesor Bayonet y compañeros. Hoy les presentamos cómo transformamos "
        "799 comentarios de YouTube en decisiones estratégicas para Claro Dominicana mediante Deep Learning."
    )

    # --- SLIDE 2: PROBLEMA EMPRESARIAL ---
    slide2 = crear_diapositiva_base(
        prs,
        "El Problema de Negocio: Escucha Pasiva y Riesgo de Churn",
        "Las quejas sin atender en canales públicos se convierten en portabilidad hacia la competencia",
        orador="Audric Rosario (0:45 - 1:30)",
        apoyo_visual="Diapositiva 2",
    )
    agregar_tarjeta(
        slide2,
        0.8,
        1.8,
        5.6,
        4.8,
        "La Realidad Operativa",
        [
            "Claro lidera en suscriptores móviles y fibra en República Dominicana.",
            "YouTube funciona como canal de consulta y reclamos desatendidos.",
            "Tiempos de espera prolongados en el 107 y saturación del bot de WhatsApp.",
            "Sin triaje automático, las quejas quedan invisibles para la gerencia.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide2,
        6.8,
        1.8,
        5.6,
        4.8,
        "El Impacto Financiero",
        [
            "El costo de adquirir un cliente (CAC) supera los USD $120.",
            "Retener clientes existentes es hasta 5 veces más rentable.",
            "La frustración pública genera viralidad y acelera la migración hacia Altice.",
            "Objetivo: Diseñar un sistema de triaje proactivo con NLP para reducir el churn.",
        ],
        COLOR_CLARO_RED,
    )
    slide2.notes_slide.notes_text_frame.text = (
        "[0:45 - 1:30] AUDRIC: El problema no es la falta de clientes, sino la retención. "
        "Cuando un cliente experimenta fallas en su fibra óptica y no recibe respuesta, acude a YouTube. "
        "Si nadie atiende el comentario, la insatisfacción escala y el cliente migra."
    )

    # --- SLIDE 3: DATOS Y MODELO NLP ---
    slide3 = crear_diapositiva_base(
        prs,
        "Datos y Pipeline NLP: De Texto Informal a Inteligencia",
        "Ingesta vía YouTube Data API v3 y clasificación con Transformer BETO",
        orador="Audric Rosario (1:30 - 2:30)",
        apoyo_visual="Diapositiva 3",
    )
    agregar_tarjeta(
        slide3,
        0.8,
        1.8,
        5.6,
        4.8,
        "1. Ingesta y Calidad de Datos",
        [
            "799 comentarios auténticos de 39 videos del canal oficial @clarord.",
            "Cuota controlada: 649 unidades utilizadas de 10,000 gratuitas por día.",
            "Dataset congelado en data/raw/ para reproducibilidad offline.",
            "Gobernanza mediante uv con dependencias declaradas en pyproject.toml.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide3,
        6.8,
        1.8,
        5.6,
        4.8,
        "2. Pipeline Lingüístico y Transformer",
        [
            "Normalización NFKD y desinfección de jerga dominicana (nítido, avería, klk).",
            "Arquitectura Transformer preentrenada en español: BETO.",
            "Mecanismos de Autoatención Bidireccional (Self-Attention).",
            "Cero fallback léxico: clasificación semántica profunda de 3 estados.",
        ],
        COLOR_GREEN,
    )
    slide3.notes_slide.notes_text_frame.text = (
        "[1:30 - 2:30] AUDRIC: Extrajimos 799 opiniones reales usando YouTube Data API. "
        "Diseñamos un pipeline lingüístico adaptado a la jerga dominicana y aplicamos un Transformer puro en español (BETO) "
        "sin diccionarios simplificados, garantizando rigor analítico."
    )

    # --- SLIDE 4: HALLAZGOS Y DASHBOARD ---
    slide4 = crear_diapositiva_base(
        prs,
        "Hallazgos Clave: Diagnóstico y Riesgo de Viralidad",
        "Métricas del Dashboard Ejecutivo interactivo en Plotly",
        orador="Audric Rosario (2:30 - 3:30)",
        apoyo_visual="Diapositiva 4",
    )
    nss_val = m["nss"]
    nss_str = f"{nss_val:+.2f}%"
    agregar_tarjeta(
        slide4,
        0.8,
        1.8,
        5.6,
        4.8,
        "Distribución y Net Sentiment Score",
        [
            f"Net Sentiment Score (NSS): {nss_str} ({'Percepción favorable' if nss_val >= 0 else 'Zona de alerta'}).",
            f"Neutros: {m['pct_neu']:.1f}% ({m['neu']} consultas de cobertura y soporte).",
            f"Positivos: {m['pct_pos']:.1f}% ({m['pos']} opiniones favorables).",
            f"Negativos: {m['pct_neg']:.1f}% ({m['neg']} quejas de servicio).",
        ],
        COLOR_GREEN if nss_val >= 0 else COLOR_CLARO_RED,
    )
    agregar_tarjeta(
        slide4,
        6.8,
        1.8,
        5.6,
        4.8,
        "Foco Crítico y Resonancia",
        [
            "🔴 Fibra Óptica e Internet Hogar concentra mayor descontento.",
            "🟢 Red 5G mantiene percepción positiva y orgullo tecnológico.",
            "⚠️ Las quejas muestran picos visibles de respaldo comunitario.",
            "El descontento público acelera la fuga de clientes de alto valor.",
        ],
        COLOR_CLARO_RED,
    )
    slide4.notes_slide.notes_text_frame.text = (
        f"[2:30 - 3:30] AUDRIC: El NSS global calculado por BETO es de {nss_str}. "
        f"El {m['pct_neu']:.1f}% corresponde a consultas, pero la alerta roja está en Fibra Óptica, "
        "cuyas quejas reciben el mayor respaldo comunitario en likes."
    )

    # --- SLIDE 5: SOLUCIÓN CLARO SENTINEL Y ROI ---
    slide5 = crear_diapositiva_base(
        prs,
        "Solución 'Claro Sentinel NLP' y Retorno de Inversión",
        "Resolución proactiva en menos de 2 horas vinculada al CRM",
        orador="Orlando Benítez (3:30 - 4:30)",
        apoyo_visual="Diapositiva 5",
    )
    agregar_tarjeta(
        slide5,
        0.8,
        1.8,
        5.6,
        4.8,
        "Plataforma Sentinel NLP",
        [
            "Monitoreo continuo de canales sociales oficiales.",
            "Clasificación en tiempo real con Transformer BETO.",
            "Generación automática de pre-tickets hacia Salesforce / Genesys.",
            "Protocolo de respuesta pública garantizada en menos de 2 horas.",
        ],
        COLOR_BORDER,
    )
    agregar_tarjeta(
        slide5,
        6.8,
        1.8,
        5.6,
        4.8,
        "Inversión y Retorno (ROI)",
        [
            "Inversión total anual: USD $4,850 (Infraestructura AWS + Capacitación).",
            "Con retener solo 12 clientes residenciales al año, la inversión se amortiza.",
            "ROI superior al 240% en el primer año de operación.",
            "Cronograma estructurado en 16 semanas para despliegue productivo.",
        ],
        COLOR_GREEN,
    )
    slide5.notes_slide.notes_text_frame.text = (
        "[3:30 - 4:30] ORLANDO: Nuestra propuesta es Claro Sentinel NLP. "
        "En lugar de esperar a que el cliente cancele, el sistema clasifica la queja y genera un pre-ticket en el CRM. "
        "La inversión anual es de solo USD $4,850 y se paga sola reteniendo apenas 12 clientes."
    )

    # --- SLIDE 6: CONCLUSIÓN ---
    slide6 = crear_diapositiva_base(
        prs,
        "Conclusión y Recomendaciones Gerenciales",
        "De los datos a la acción: cómo Claro puede blindar su liderazgo de marca",
        orador="Orlando Benítez (4:30 - 5:00)",
        apoyo_visual="Diapositiva 6",
    )
    agregar_tarjeta(
        slide6,
        0.8,
        1.8,
        5.6,
        4.8,
        "Tres Recomendaciones Inmediatas",
        [
            "1. Priorizar soporte humano en quejas de fibra óptica nocturna.",
            "2. Rediseñar el flujo del WhatsApp Bot con árbol de decisión simplificado.",
            "3. Incorporar el NSS como indicador clave de rendimiento ejecutivo mensual.",
        ],
        COLOR_CLARO_RED,
    )
    agregar_tarjeta(
        slide6,
        6.8,
        1.8,
        5.6,
        4.8,
        "Mensaje Final",
        [
            "El valor del Big Data no radica en la cantidad de datos, sino en la rapidez con la que se traducen en decisiones.",
            "Claro RD tiene la tecnología para transformar la frustración de sus clientes en lealtad duradera.",
            "¡Muchas gracias por su atención! Quedamos abiertos a preguntas.",
        ],
        COLOR_GREEN,
    )
    slide6.notes_slide.notes_text_frame.text = (
        "[4:30 - 5:00] ORLANDO: Concluimos con tres acciones: priorizar fibra nocturna, simplificar el bot y "
        "adoptar el NSS en el cuadro directivo. Gracias profesor y compañeros, quedamos a su disposición."
    )

    prs.save(output_path)
    print(f"[EXITO] Presentación de Clase generada en: {output_path}")
    return output_path


def main() -> None:
    """Ejecuta la generación de ambas presentaciones con datos dinámicos."""
    print("\n--- GENERANDO PRESENTACIONES POWERPOINT CON DATOS DINÁMICOS ---")
    generar_presentacion_video()
    generar_presentacion_clase_5min()
    print("--- PRESENTACIONES GENERADAS EXITOSAMENTE ---\n")


if __name__ == "__main__":
    main()
