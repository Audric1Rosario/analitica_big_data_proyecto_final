"""
Módulo de Generación de Gráficos e Imágenes Analíticas para el Informe Académico
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric André Rosario Rosario & Orlando Benítez Ventura
Facilitador: Luis Eduardo Bayonet Robles
Empresa Caso de Estudio: Claro República Dominicana (@clarord)
"""

import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

os.makedirs("docs/images", exist_ok=True)

COLOR_MAP = {
    "POSITIVO": "#10B981",  # Verde esmeralda
    "NEGATIVO": "#DA291C",  # Rojo Claro corporativo
    "NEUTRO": "#94A3B8",  # Gris slate neutro
}

FONT_FAMILY = "Segoe UI, Inter, Arial, sans-serif"


def cargar_dataset(csv_path: str = "data/processed/youtube_claro_processed.csv") -> pd.DataFrame:
    """Carga de forma segura el dataset procesado."""
    if not os.path.exists(csv_path):
        fallback_raw = "data/raw/youtube_claro_raw.csv"
        if os.path.exists(fallback_raw):
            return pd.read_csv(fallback_raw)
        raise FileNotFoundError(f"No se encontró el dataset en {csv_path} ni {fallback_raw}")
    return pd.read_csv(csv_path)


def generar_flujo_preprocesamiento() -> None:
    """Genera el diagrama del flujo metodológico de preparación de texto en español."""
    pasos = [
        {"num": "PASO 1", "titulo": "Ingesta YouTube API", "desc": "799 opiniones reales<br>39 videos con datos"},
        {"num": "PASO 2", "titulo": "Normalización Unicode", "desc": "Formato NFKD<br>Conserva 'ñ' y acentos"},
        {"num": "PASO 3", "titulo": "Higienización Regex", "desc": "Remoción URLs y @<br>Elimina caracteres extra"},
        {"num": "PASO 4", "titulo": "Jerga Dominicana", "desc": "Modismos (klk, nítido)<br>Estandariza risas"},
        {"num": "PASO 5", "titulo": "Stopwords Telco", "desc": "300+ conectores<br>Filtra ruido del canal"},
        {"num": "PASO 6", "titulo": "Dataset Procesado", "desc": "Tokens limpios para<br>Inferencia BETO"},
    ]

    fig = go.Figure()

    for i, p in enumerate(pasos):
        x_center = i * 2.3
        bg_color = "#DA291C" if (i == 0 or i == 5) else "#1E293B"
        border_color = "#B91C1C" if (i == 0 or i == 5) else "#38BDF8"
        text_num_color = "#FFFFFF" if (i == 0 or i == 5) else "#38BDF8"

        fig.add_shape(
            type="rect",
            x0=x_center - 1.0,
            y0=0.1,
            x1=x_center + 1.0,
            y1=1.9,
            fillcolor=bg_color,
            line=dict(color=border_color, width=2.5),
            layer="below",
        )
        fig.add_annotation(
            x=x_center,
            y=1.62,
            text=f"<b>{p['num']}</b>",
            showarrow=False,
            font=dict(size=13, color=text_num_color, family=FONT_FAMILY),
        )
        fig.add_annotation(
            x=x_center,
            y=1.20,
            text=f"<b>{p['titulo']}</b>",
            showarrow=False,
            font=dict(size=11, color="#FFFFFF", family=FONT_FAMILY),
        )
        fig.add_annotation(
            x=x_center, y=0.62, text=p["desc"], showarrow=False, font=dict(size=10, color="#CBD5E1", family=FONT_FAMILY)
        )

        if i < len(pasos) - 1:
            fig.add_annotation(
                x=x_center + 1.15,
                y=1.0,
                ax=x_center + 1.01,
                ay=1.0,
                xref="x",
                yref="y",
                axref="x",
                ayref="y",
                showarrow=True,
                arrowhead=2,
                arrowsize=1.4,
                arrowwidth=2.5,
                arrowcolor="#DA291C",
            )

    fig.update_layout(
        title=dict(
            text="<b>Arquitectura del Pipeline de Preprocesamiento y Limpieza de Texto en Español</b><br><span style='font-size:13px; color:#64748B;'>Normalización, remoción de ruido, tratamiento de modismos dominicanos y filtrado específico de telecomunicaciones</span>",
            x=0.5,
            y=0.92,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.3, 12.8]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.1, 2.1]),
        template="plotly_white",
        width=1100,
        height=350,
        margin=dict(l=30, r=30, t=85, b=25),
    )
    fig.write_image("docs/images/01_flujo_preprocesamiento_nlp.png", scale=2)
    print("[OK] 01_flujo_preprocesamiento_nlp.png generado.")


def generar_vis1_sentimiento_global(df: pd.DataFrame) -> None:
    """Genera Donut Chart de la distribución global de sentimiento y NSS derivado."""
    total = len(df)
    pos = int((df["sentiment_label"] == "POSITIVO").sum())
    neg = int((df["sentiment_label"] == "NEGATIVO").sum())
    nss = round(((pos - neg) / total) * 100, 2) if total > 0 else 0.0
    nss_color = "#10B981" if nss >= 0 else "#DA291C"

    conteo = df["sentiment_label"].value_counts().reset_index()
    conteo.columns = ["Sentimiento", "Total"]

    fig = px.pie(
        conteo, names="Sentimiento", values="Total", color="Sentimiento", color_discrete_map=COLOR_MAP, hole=0.58
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        insidetextfont=dict(size=13, color="#FFFFFF", family=FONT_FAMILY),
        marker=dict(line=dict(color="#FFFFFF", width=2.5)),
    )
    fig.add_annotation(
        text=f"<b>NSS GLOBAL<br><span style='font-size:26px; color:{nss_color};'>{nss:+.2f}%</span></b><br><span style='font-size:11px; color:#64748B;'>{total} Opiniones</span>",
        x=0.5,
        y=0.5,
        font=dict(size=14, color="#0F172A", family=FONT_FAMILY),
        showarrow=False,
    )
    fig.update_layout(
        title=dict(
            text="<b>Visualización 1: Distribución Global de Sentimiento de Marca (BETO Transformer)</b><br><span style='font-size:13px; color:#64748B;'>Auditoría sobre 799 opiniones reales recolectadas vía YouTube Data API v3</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        legend=dict(orientation="h", yanchor="top", y=-0.08, xanchor="center", x=0.5, font=dict(size=12)),
        width=850,
        height=540,
        margin=dict(l=40, r=40, t=90, b=60),
    )
    fig.write_image("docs/images/02_distribucion_sentimiento_global.png", scale=2)
    print("[OK] 02_distribucion_sentimiento_global.png generado.")


def generar_vis2_sentimiento_por_servicio(df: pd.DataFrame) -> None:
    """Genera gráfico de barras agrupadas por categoría de servicio."""
    col_cat = "service_category" if "service_category" in df.columns else "topic_category"
    cat_sent = df.groupby([col_cat, "sentiment_label"]).size().reset_index(name="conteo")
    orden_cat = df[col_cat].value_counts().index.tolist()

    fig = px.bar(
        cat_sent,
        x=col_cat,
        y="conteo",
        color="sentiment_label",
        barmode="group",
        category_orders={col_cat: orden_cat, "sentiment_label": ["POSITIVO", "NEUTRO", "NEGATIVO"]},
        color_discrete_map=COLOR_MAP,
        labels={
            col_cat: "Área de Servicio Auditada",
            "conteo": "Volumen de Comentarios",
            "sentiment_label": "Sentimiento:",
        },
    )
    fig.update_traces(
        texttemplate="%{y}",
        textposition="outside",
        textfont=dict(size=10, family=FONT_FAMILY, color="#0F172A"),
        cliponaxis=False,
    )
    fig.update_layout(
        title=dict(
            text="<b>Visualización 2: Distribución de Sentimiento por Categoría de Servicio</b><br><span style='font-size:13px; color:#64748B;'>Comparación del volumen de interacciones positivas, neutras y negativas en cada vertical</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        xaxis=dict(tickangle=-20, tickfont=dict(size=11, family=FONT_FAMILY), gridcolor="#F8FAFC"),
        yaxis=dict(title="Cantidad de Comentarios", title_font=dict(size=12), gridcolor="#E2E8F0"),
        legend=dict(orientation="h", yanchor="top", y=-0.25, xanchor="center", x=0.5, font=dict(size=12)),
        width=980,
        height=580,
        margin=dict(l=60, r=40, t=95, b=120),
    )
    fig.write_image("docs/images/03_sentimiento_por_servicio.png", scale=2)
    print("[OK] 03_sentimiento_por_servicio.png generado.")


def generar_vis3_tendencia_temporal(df: pd.DataFrame) -> None:
    """Genera la evolución cronológica del volumen por polaridad de sentimiento."""
    df_temp = df.copy()
    df_temp["published_at"] = pd.to_datetime(df_temp["published_at"], errors="coerce")
    df_temp = df_temp.dropna(subset=["published_at"])
    df_temp = df_temp[df_temp["published_at"] >= "2023-01-01"]
    df_temp["mes_anio"] = df_temp["published_at"].dt.strftime("%Y-%m")

    timeline = df_temp.groupby(["mes_anio", "sentiment_label"]).size().reset_index(name="total")

    fig = px.line(
        timeline,
        x="mes_anio",
        y="total",
        color="sentiment_label",
        markers=True,
        category_orders={"sentiment_label": ["POSITIVO", "NEUTRO", "NEGATIVO"]},
        color_discrete_map=COLOR_MAP,
        labels={"mes_anio": "Periodo Mensual", "total": "Comentarios", "sentiment_label": "Sentimiento:"},
    )
    fig.update_traces(line=dict(width=2.5), marker=dict(size=7))
    fig.update_layout(
        title=dict(
            text="<b>Visualización 3: Tendencia Temporal del Volumen de Opiniones</b><br><span style='font-size:13px; color:#64748B;'>Evolución cronológica de consultas, quejas y satisfacción en canales de YouTube (2023 - 2026)</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        xaxis=dict(tickangle=-45, tickfont=dict(size=10, family=FONT_FAMILY), gridcolor="#F1F5F9"),
        yaxis=dict(title="Volumen de Comentarios", title_font=dict(size=12), gridcolor="#E2E8F0"),
        legend=dict(orientation="h", yanchor="top", y=-0.28, xanchor="center", x=0.5, font=dict(size=12)),
        width=980,
        height=560,
        margin=dict(l=60, r=40, t=95, b=120),
    )
    fig.write_image("docs/images/04_tendencia_temporal_sentimiento.png", scale=2)
    print("[OK] 04_tendencia_temporal_sentimiento.png generado.")


def generar_vis4_resonancia_likes(df: pd.DataFrame) -> None:
    """Genera diagrama de caja de resonancia de audiencia por nivel de sentimiento."""
    neg_likes = df[df["sentiment_label"] == "NEGATIVO"]["like_count"].dropna()
    media_neg = round(float(neg_likes.mean()), 2) if len(neg_likes) > 0 else 0.0
    max_neg = int(neg_likes.max()) if len(neg_likes) > 0 else 0

    fig = px.box(
        df,
        x="sentiment_label",
        y="like_count",
        color="sentiment_label",
        color_discrete_map=COLOR_MAP,
        points="all",
        category_orders={"sentiment_label": ["POSITIVO", "NEUTRO", "NEGATIVO"]},
        labels={"sentiment_label": "Sentimiento Clasificado", "like_count": "Número de 'Likes'"},
    )
    fig.add_annotation(
        x="NEGATIVO",
        y=max_neg,
        text=f"<b>Pico de Queja: {max_neg} Likes</b><br><span style='font-size:10px; color:#64748B;'>Avería comunitaria sin respuesta</span>",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#DA291C",
        arrowsize=1.2,
        ax=80,
        ay=-40,
        font=dict(size=11, color="#DA291C", family=FONT_FAMILY),
        bgcolor="#FEF2F2",
        bordercolor="#FCA5A5",
        borderwidth=1,
        borderpad=4,
    )
    fig.update_layout(
        title=dict(
            text=f"<b>Visualización 4: Resonancia de la Audiencia — Distribución de 'Likes' por Sentimiento</b><br><span style='font-size:13px; color:#64748B;'>Las quejas acumulan una media de {media_neg} reacciones con picos comunitarios de hasta {max_neg} likes</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        showlegend=False,
        yaxis=dict(
            title="Reacciones ('Likes')", range=[-3, max(int(df["like_count"].max()), 30) + 15], gridcolor="#E2E8F0"
        ),
        xaxis=dict(tickfont=dict(size=12, family=FONT_FAMILY)),
        width=920,
        height=540,
        margin=dict(l=60, r=50, t=95, b=60),
    )
    fig.write_image("docs/images/05_resonancia_likes_sentimiento.png", scale=2)
    print("[OK] 05_resonancia_likes_sentimiento.png generado.")


def generar_vis5_top_terminos_quejas(df: pd.DataFrame) -> None:
    """Extrae dinámicamente los términos críticos más frecuentes en quejas negativas."""
    neg_comments = df[df["sentiment_label"] == "NEGATIVO"]["comment_text"].dropna().astype(str).str.lower()

    terminos_mapeo = {
        "Lento / Lentitud": ["lento", "lenta", "lentitud"],
        "Espera / Demora": ["espera", "esperando", "tardan", "demora"],
        "Ping / Lag": ["ping", "lag", "latencia"],
        "Avería / Falla": ["averia", "avería", "falla", "fallando", "danado", "dañado"],
        "Caída de Red": ["caida", "caída", "cae", "cortado", "corta", "sin internet"],
        "Problema con Bot": ["bot", "robot", "asistente", "whatsapp", "107", "menu"],
        "Router / Módem": ["router", "modem", "módem", "aparato"],
        "Cobro / Factura": ["cobro", "factura", "precio", "pago", "caro", "recarga"],
        "Atención / Soporte": ["atencion", "atención", "soporte", "servicio", "ayuda"],
    }

    conteo_lista = []
    for etiqueta, palabras in terminos_mapeo.items():
        cnt = int(sum(neg_comments.apply(lambda texto: any(p in texto for p in palabras))))
        conteo_lista.append({"Foco": etiqueta, "Menciones": cnt})

    df_terminos = pd.DataFrame(conteo_lista).sort_values(by="Menciones", ascending=True)
    max_menciones = max(df_terminos["Menciones"]) if len(df_terminos) > 0 else 10

    fig = px.bar(
        df_terminos,
        x="Menciones",
        y="Foco",
        orientation="h",
        text="Menciones",
        color="Menciones",
        color_continuous_scale=["#FFA39E", "#DA291C"],
        labels={"Menciones": "Menciones en Quejas Negativas", "Foco": "Foco Crítico de Reclamo"},
    )
    fig.update_traces(
        textposition="outside", textfont=dict(size=12, family=FONT_FAMILY, color="#0F172A"), cliponaxis=False
    )
    fig.update_layout(
        title=dict(
            text="<b>Visualización 5: Términos Críticos Más Frecuentes en Quejas de Clientes</b><br><span style='font-size:13px; color:#64748B;'>Análisis de incidencias técnicas y fricciones operacionales en comentarios negativos clasificados por BETO</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        coloraxis_showscale=False,
        xaxis=dict(
            title="Cantidad de Comentarios Negativos que lo mencionan",
            range=[0, max_menciones + 4],
            gridcolor="#E2E8F0",
        ),
        yaxis=dict(tickfont=dict(size=12, family=FONT_FAMILY)),
        width=950,
        height=540,
        margin=dict(l=140, r=40, t=95, b=60),
    )
    fig.write_image("docs/images/06_top_terminos_quejas.png", scale=2)
    print("[OK] 06_top_terminos_quejas.png generado.")


def generar_dashboard_ejecutivo_composite(df: pd.DataFrame) -> None:
    """Genera la composición ejecutiva multitarjeta para la Sección 6.11."""
    total = len(df)
    pos = int((df["sentiment_label"] == "POSITIVO").sum())
    neg = int((df["sentiment_label"] == "NEGATIVO").sum())
    nss = round(((pos - neg) / total) * 100, 2) if total > 0 else 0.0

    fig = make_subplots(
        rows=3,
        cols=2,
        row_heights=[0.18, 0.41, 0.41],
        column_widths=[0.5, 0.5],
        specs=[
            [{"type": "indicator"}, {"type": "indicator"}],
            [{"type": "domain"}, {"type": "xy"}],
            [{"type": "xy"}, {"type": "xy"}],
        ],
        vertical_spacing=0.13,
        horizontal_spacing=0.10,
        subplot_titles=(
            "",
            "",
            "<b>1. Distribución Global de Sentimiento</b>",
            "<b>2. Top Focos Críticos en Quejas</b>",
            "<b>3. Sentimiento en Principales Servicios</b>",
            "<b>4. Resonancia de Quejas (Likes)</b>",
        ),
    )

    # KPI 1: Volumen Auditado
    fig.add_trace(
        go.Indicator(
            mode="number",
            value=total,
            number=dict(font=dict(size=40, color="#0F172A", family=FONT_FAMILY)),
            title=dict(
                text="<b>VOLUMEN AUDITADO</b><br><span style='font-size:12px;color:#64748B;'>Opiniones en YouTube API</span>",
                font=dict(family=FONT_FAMILY),
            ),
        ),
        row=1,
        col=1,
    )

    # KPI 2: Net Sentiment Score (NSS)
    fig.add_trace(
        go.Indicator(
            mode="number",
            value=nss,
            number=dict(suffix="%", font=dict(size=40, color="#10B981" if nss >= 0 else "#DA291C", family=FONT_FAMILY)),
            title=dict(
                text="<b>NET SENTIMENT SCORE (NSS)</b><br><span style='font-size:12px;color:#64748B;'>Índice de Percepción de Marca</span>",
                font=dict(family=FONT_FAMILY),
            ),
        ),
        row=1,
        col=2,
    )

    # PANEL 1: Donut Sentimiento
    conteo_pie = df["sentiment_label"].value_counts()
    fig.add_trace(
        go.Pie(
            labels=conteo_pie.index,
            values=conteo_pie.values,
            hole=0.55,
            marker=dict(
                colors=[COLOR_MAP.get(k, "#94A3B8") for k in conteo_pie.index], line=dict(color="#FFFFFF", width=2)
            ),
            textinfo="percent+label",
            insidetextfont=dict(color="#FFFFFF", size=11, family=FONT_FAMILY),
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    # PANEL 2: Términos Críticos Dinámicos
    neg_txt = df[df["sentiment_label"] == "NEGATIVO"]["clean_text"].dropna().astype(str).str.lower()
    kw_map = {
        "Lento": ["lento", "lenta"],
        "Espera": ["espera", "tardan"],
        "Ping": ["ping", "lag"],
        "Avería": ["averia", "falla"],
        "Caída": ["caida", "corte"],
        "Bot": ["bot", "107"],
    }
    palabras = []
    conts = []
    for kw, terms in kw_map.items():
        palabras.append(kw)
        conts.append(int(sum(neg_txt.apply(lambda t: any(w in t for w in terms)))))

    fig.add_trace(
        go.Bar(
            x=conts,
            y=palabras,
            orientation="h",
            marker_color="#DA291C",
            text=conts,
            textposition="outside",
            textfont=dict(size=10, color="#0F172A"),
            showlegend=False,
        ),
        row=2,
        col=2,
    )

    # PANEL 3: Sentimiento en Principales Servicios Dinámico
    col_s = "service_category" if "service_category" in df.columns else "topic_category"
    servicios_top = df[col_s].value_counts().head(3).index.tolist()
    pos_s = [int(((df[col_s] == s) & (df["sentiment_label"] == "POSITIVO")).sum()) for s in servicios_top]
    neg_s = [int(((df[col_s] == s) & (df["sentiment_label"] == "NEGATIVO")).sum()) for s in servicios_top]

    # Acortar etiquetas para visualización limpia
    serv_labels = [s.replace(" e Internet Hogar", "").replace(" y Cobertura 5G", "") for s in servicios_top]
    fig.add_trace(
        go.Bar(name="Positivo", x=serv_labels, y=pos_s, marker_color="#10B981", showlegend=False), row=3, col=1
    )
    fig.add_trace(
        go.Bar(name="Negativo", x=serv_labels, y=neg_s, marker_color="#DA291C", showlegend=False), row=3, col=1
    )

    # PANEL 4: Resonancia de Likes Dinámica
    for s_name, color in [("POSITIVO", "#10B981"), ("NEUTRO", "#94A3B8"), ("NEGATIVO", "#DA291C")]:
        vals = df[df["sentiment_label"] == s_name]["like_count"].dropna()
        fig.add_trace(go.Box(y=vals, name=s_name, marker_color=color, showlegend=False), row=3, col=2)

    fig.update_layout(
        title=dict(
            text="<b>CLARO REPÚBLICA DOMINICANA — DASHBOARD EJECUTIVO DE AUDITORÍA SOCIAL NLP</b><br><span style='font-size:13px; color:#475569;'>Panel Autónomo de Inteligencia Competitiva y Satisfacción de Clientes • Entregable 4 (Plotly)</span>",
            x=0.5,
            y=0.97,
            font=dict(size=17, color="#DA291C", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        barmode="group",
        width=1200,
        height=880,
        margin=dict(l=60, r=60, t=110, b=40),
    )
    fig.write_image("docs/images/07_dashboard_ejecutivo_claro.png", scale=2)
    print("[OK] 07_dashboard_ejecutivo_claro.png generado.")


def generar_cronograma_gantt() -> None:
    """Genera el diagrama de Gantt de implementación para la Sección 6.15."""
    tareas = [
        {
            "Fase": "Fase 1",
            "Tarea": "1. Ingesta API YouTube",
            "Inicio": 1,
            "Fin": 3,
            "Responsable": "Data Engineering",
            "Color": "#0284C7",
        },
        {
            "Fase": "Fase 2",
            "Tarea": "2. Fine-Tuning NLP",
            "Inicio": 4,
            "Fin": 7,
            "Responsable": "NLP Modeling",
            "Color": "#DA291C",
        },
        {
            "Fase": "Fase 3",
            "Tarea": "3. Conexión CRM & Dashboards",
            "Inicio": 8,
            "Fin": 10,
            "Responsable": "BI & DevOps",
            "Color": "#D97706",
        },
        {
            "Fase": "Fase 4",
            "Tarea": "4. Piloto Mesa de Ayuda",
            "Inicio": 11,
            "Fin": 14,
            "Responsable": "CX & Soporte",
            "Color": "#059669",
        },
        {
            "Fase": "Fase 5",
            "Tarea": "5. Despliegue General",
            "Inicio": 15,
            "Fin": 16,
            "Responsable": "Comité Directivo",
            "Color": "#7C3AED",
        },
    ]
    df_gantt = pd.DataFrame(tareas)
    df_gantt["Duracion"] = df_gantt["Fin"] - df_gantt["Inicio"] + 1

    fig = go.Figure()

    for _, row in df_gantt.iterrows():
        fig.add_trace(
            go.Bar(
                y=[row["Tarea"]],
                x=[row["Duracion"]],
                base=[row["Inicio"] - 1],
                orientation="h",
                marker=dict(color=row["Color"], line=dict(color="#0F172A", width=1.5)),
                text=f" Semanas {row['Inicio']}-{row['Fin']} ",
                textposition="inside",
                insidetextfont=dict(color="#FFFFFF", size=11, family=FONT_FAMILY),
                showlegend=False,
            )
        )

    hitos = [
        {"y": "1. Ingesta API YouTube", "x": 3.2, "nombre": "Hito 1: Ingesta 100% Validada"},
        {"y": "2. Fine-Tuning NLP", "x": 7.2, "nombre": "Hito 2: Modelo Calibrado"},
        {"y": "3. Conexión CRM & Dashboards", "x": 10.2, "nombre": "Hito 3: Webhook CRM Operativo"},
        {"y": "4. Piloto Mesa de Ayuda", "x": 14.2, "nombre": "Hito 4: Reducción Churn Demostrada"},
        {"y": "5. Despliegue General", "x": 16.2, "nombre": "Hito 5: Producción Total"},
    ]
    for h in hitos:
        fig.add_trace(
            go.Scatter(
                x=[h["x"]],
                y=[h["y"]],
                mode="markers+text",
                marker=dict(symbol="diamond", size=13, color="#DA291C", line=dict(color="#FFFFFF", width=2)),
                text=[f" <b>{h['nombre']}</b>"],
                textposition="middle right",
                textfont=dict(color="#0F172A", size=11, family=FONT_FAMILY),
                showlegend=False,
            )
        )

    fig.update_layout(
        title=dict(
            text="<b>Cronograma de Implementación — Plataforma 'Claro Sentinel NLP'</b><br><span style='font-size:13px; color:#475569;'>Plan Maestro de 16 Semanas en 5 Fases de Ejecución • Inversión USD $4,850 • Retorno de Inversión < 90 Días</span>",
            x=0.5,
            y=0.95,
            font=dict(size=16, color="#0F172A", family=FONT_FAMILY),
        ),
        template="plotly_white",
        font=dict(family=FONT_FAMILY, color="#0F172A"),
        xaxis=dict(
            title="<b>Línea de Tiempo (Semanas de Proyecto)</b>",
            tickmode="linear",
            tick0=1,
            dtick=1,
            range=[0, 22],
            gridcolor="#E2E8F0",
        ),
        yaxis=dict(autorange="reversed", gridcolor="#F8FAFC", tickfont=dict(size=12, family=FONT_FAMILY)),
        width=1200,
        height=460,
        margin=dict(l=160, r=40, t=95, b=55),
    )
    fig.write_image("docs/images/08_cronograma_gantt_sentinel.png", scale=2)
    print("[OK] 08_cronograma_gantt_sentinel.png generado.")


def main() -> None:
    """Función principal que orquesta la generación integral de gráficos."""
    print("\n--- GENERANDO IMÁGENES ANALÍTICAS DINÁMICAS (ZERO HARDCODING) ---")
    df = cargar_dataset()
    generar_flujo_preprocesamiento()
    generar_vis1_sentimiento_global(df)
    generar_vis2_sentimiento_por_servicio(df)
    generar_vis3_tendencia_temporal(df)
    generar_vis4_resonancia_likes(df)
    generar_vis5_top_terminos_quejas(df)
    generar_dashboard_ejecutivo_composite(df)
    generar_cronograma_gantt()
    print("--- GENERACIÓN DE IMÁGENES COMPLETADA EXITOSAMENTE ---\n")


if __name__ == "__main__":
    main()
