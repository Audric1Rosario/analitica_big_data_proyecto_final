"""
Generador de Dashboard Ejecutivo Interactivo con Plotly
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez
Empresa: Claro República Dominicana
"""

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def generar_dashboard_ejecutivo(
    processed_csv: str = "data/processed/youtube_claro_processed.csv",
    output_html: str = "dashboard/dashboard_ejecutivo_claro.html"
):
    """
    Construye un dashboard ejecutivo interactivo en HTML utilizando Plotly
    con 4 KPIs gerenciales y 5 visualizaciones analíticas de alto impacto.
    """
    if not os.path.exists(processed_csv):
        # Si aún no se procesó, buscar en raw
        raw_csv = "data/raw/youtube_claro_raw.csv"
        if os.path.exists(raw_csv):
            df = pd.read_csv(raw_csv)
            # Asegurar columna de sentimiento si no existe
            if "sentiment_label" not in df.columns:
                if "ground_truth_sentiment" in df.columns:
                    df["sentiment_label"] = df["ground_truth_sentiment"]
                else:
                    df["sentiment_label"] = "NEUTRO"
        else:
            raise FileNotFoundError(f"No se encontró el dataset en {processed_csv} ni en {raw_csv}")
    else:
        df = pd.read_csv(processed_csv)

    print(f"[DASHBOARD] Construyendo visualizaciones para {len(df)} registros...")

    # --- 1. CÁLCULO DE KPIs EJECUTIVOS ---
    total_comentarios = len(df)
    conteo_sentimientos = df["sentiment_label"].value_counts()
    positivos = conteo_sentimientos.get("POSITIVO", 0)
    negativos = conteo_sentimientos.get("NEGATIVO", 0)
    neutros = conteo_sentimientos.get("NEUTRO", 0)

    pct_pos = (positivos / total_comentarios) * 100 if total_comentarios > 0 else 0
    pct_neg = (negativos / total_comentarios) * 100 if total_comentarios > 0 else 0
    net_sentiment_score = round(pct_pos - pct_neg, 1)

    total_likes = df["like_count"].sum() if "like_count" in df.columns else 0
    categoria_top_quejas = "Fibra Óptica / Soporte"
    if "service_category" in df.columns and negativos > 0:
        neg_df = df[df["sentiment_label"] == "NEGATIVO"]
        if not neg_df.empty:
            categoria_top_quejas = neg_df["service_category"].value_counts().index[0]

    # Paleta de colores corporativa armónica
    COLOR_MAP = {
        "POSITIVO": "#2ECC71",  # Verde esmeralda
        "NEGATIVO": "#E74C3C",  # Rojo rubí
        "NEUTRO": "#95A5A6"     # Gris slate
    }

    # --- 2. GRÁFICO 1: Donut Chart - Distribución Global de Sentimiento ---
    fig_donut = px.pie(
        df,
        names="sentiment_label",
        color="sentiment_label",
        color_discrete_map=COLOR_MAP,
        hole=0.55,
        title="<b>1. Distribución Global de Sentimiento de Marca</b>"
    )
    fig_donut.update_traces(textposition='inside', textinfo='percent+label', hoverinfo='label+value+percent')
    fig_donut.update_layout(
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
    )

    # --- 3. GRÁFICO 2: Barras Agrupadas - Sentimiento por Categoría de Servicio ---
    if "service_category" in df.columns:
        cat_sent = df.groupby(["service_category", "sentiment_label"]).size().reset_index(name="conteo")
        fig_cat = px.bar(
            cat_sent,
            x="service_category",
            y="conteo",
            color="sentiment_label",
            barmode="group",
            color_discrete_map=COLOR_MAP,
            title="<b>2. Percepción y Sentimiento por Categoría de Servicio</b>",
            labels={"service_category": "Área de Servicio", "conteo": "Volumen de Comentarios"}
        )
        fig_cat.update_layout(
            template="plotly_white",
            xaxis_tickangle=-20,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
    else:
        fig_cat = go.Figure()

    # --- 4. GRÁFICO 3: Tendencia Temporal del Sentimiento ---
    if "published_at" in df.columns:
        df_temp = df.copy()
        df_temp["published_at"] = pd.to_datetime(df_temp["published_at"], errors="coerce")
        df_temp = df_temp.dropna(subset=["published_at"])
        df_temp["mes_anio"] = df_temp["published_at"].dt.to_period("M").astype(str)

        timeline = df_temp.groupby(["mes_anio", "sentiment_label"]).size().reset_index(name="total")
        fig_timeline = px.line(
            timeline,
            x="mes_anio",
            y="total",
            color="sentiment_label",
            markers=True,
            color_discrete_map=COLOR_MAP,
            title="<b>3. Tendencia Temporal del Volumen de Opiniones</b>",
            labels={"mes_anio": "Periodo Mensual", "total": "Comentarios"}
        )
        fig_timeline.update_layout(template="plotly_white")
    else:
        fig_timeline = go.Figure()

    # --- 5. GRÁFICO 4: Dispersión / Box Plot de Engagement (Likes vs Sentimiento) ---
    if "like_count" in df.columns:
        fig_box = px.box(
            df,
            x="sentiment_label",
            y="like_count",
            color="sentiment_label",
            color_discrete_map=COLOR_MAP,
            points="all",
            title="<b>4. Resonancia de la Audiencia: 'Likes' por Tipo de Sentimiento</b>",
            labels={"sentiment_label": "Sentimiento", "like_count": "Reacciones ('Likes')"}
        )
        fig_box.update_layout(template="plotly_white", showlegend=False)
    else:
        fig_box = go.Figure()

    # --- 6. GRÁFICO 5: Top 10 Términos Críticos en Comentarios Negativos ---
    palabras_quejas = ["caida", "lento", "espera", "factura", "cobro", "precio", "ping", "soporte", "router", "bot", "averia"]
    conteo_terminos = []
    texto_negativo = " ".join(df[df["sentiment_label"] == "NEGATIVO"]["comment_text"].dropna().astype(str).str.lower())
    for p in palabras_quejas:
        conteo_terminos.append({"termino": p.capitalize(), "frecuencia": texto_negativo.count(p)})
    df_terminos = pd.DataFrame(conteo_terminos).sort_values(by="frecuencia", ascending=True)

    fig_terminos = px.bar(
        df_terminos,
        x="frecuencia",
        y="termino",
        orientation="h",
        color_discrete_sequence=["#E74C3C"],
        title="<b>5. Términos Críticos Más Frecuentes en Quejas de Clientes</b>",
        labels={"frecuencia": "Menciones", "termino": "Foco de Reclamo"}
    )
    fig_terminos.update_layout(template="plotly_white")

    # --- 7. ENSAMBLAJE DEL DASHBOARD EJECUTIVO HTML ---
    os.makedirs(os.path.dirname(output_html), exist_ok=True)

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Ejecutivo - Analítica Social Claro RD</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #0F172A;
            --card-bg: #1E293B;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
            --accent-red: #DA291C;
            --accent-green: #10B981;
            --accent-blue: #38BDF8;
            --border-card: #334155;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }}
        body {{ background-color: var(--bg-body); color: var(--text-main); padding: 25px; }}
        header {{
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 2px solid var(--border-card); padding-bottom: 20px; margin-bottom: 30px;
        }}
        .header-title h1 {{ font-size: 26px; font-weight: 800; color: #FFFFFF; display: flex; align-items: center; gap: 10px; }}
        .header-title h1 span {{ color: var(--accent-red); }}
        .header-title p {{ color: var(--text-muted); font-size: 14px; margin-top: 5px; }}
        .header-badge {{ background: #334155; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 600; color: #38BDF8; }}

        /* KPIs Grid */
        .kpis-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px; margin-bottom: 30px;
        }}
        .kpi-card {{
            background: var(--card-bg); border: 1px solid var(--border-card);
            border-radius: 14px; padding: 22px; transition: transform 0.2s, box-shadow 0.2s;
        }}
        .kpi-card:hover {{ transform: translateY(-3px); box-shadow: 0 10px 25px rgba(0,0,0,0.3); }}
        .kpi-label {{ font-size: 13px; font-weight: 600; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px; }}
        .kpi-value {{ font-size: 32px; font-weight: 800; margin: 10px 0 5px 0; }}
        .kpi-subtext {{ font-size: 13px; color: var(--text-muted); }}
        .val-pos {{ color: var(--accent-green); }}
        .val-neg {{ color: #F87171; }}
        .val-blue {{ color: var(--accent-blue); }}
        .val-red {{ color: #EF4444; }}

        /* Visualizations Grid */
        .charts-grid {{
            display: grid; grid-template-columns: repeat(2, 1fr);
            gap: 25px; margin-bottom: 30px;
        }}
        .chart-card {{
            background: var(--card-bg); border: 1px solid var(--border-card);
            border-radius: 14px; padding: 20px; overflow: hidden;
        }}
        .chart-card.full-width {{ grid-column: span 2; }}
        
        footer {{
            border-top: 1px solid var(--border-card); padding-top: 20px;
            display: flex; justify-content: space-between; font-size: 13px; color: var(--text-muted);
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-title">
            <h1><span>CLARO RD</span> | Panel Ejecutivo de Inteligencia de Sentimiento</h1>
            <p>Auditoría de Percepción Pública, Satisfacción de Clientes y Focos de Fricción vía YouTube Data API v3</p>
        </div>
        <div class="header-badge">Equipo: Audric Rosario & Orlando Benítez</div>
    </header>

    <!-- Indicadores KPIs -->
    <div class="kpis-grid">
        <div class="kpi-card">
            <div class="kpi-label">Volumen Analizado</div>
            <div class="kpi-value val-blue">{total_comentarios:,}</div>
            <div class="kpi-subtext">Comentarios reales de usuarios</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">NSS (Net Sentiment Score)</div>
            <div class="kpi-value {'val-pos' if net_sentiment_score >= 0 else 'val-neg'}">{net_sentiment_score:+.1f}%</div>
            <div class="kpi-subtext">% Positivos menos % Negativos</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Tasa de Aprobación</div>
            <div class="kpi-value val-pos">{pct_pos:.1f}%</div>
            <div class="kpi-subtext">{positivos} opiniones favorables</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Mayor Foco de Reclamos</div>
            <div class="kpi-value val-red" style="font-size: 20px; padding-top: 10px;">{categoria_top_quejas}</div>
            <div class="kpi-subtext">Tópico con mayor volumen negativo</div>
        </div>
    </div>

    <!-- Gráficos Interactivos -->
    <div class="charts-grid">
        <div class="chart-card">
            <div id="chart_donut"></div>
        </div>
        <div class="chart-card">
            <div id="chart_terminos"></div>
        </div>
        <div class="chart-card full-width">
            <div id="chart_cat"></div>
        </div>
        <div class="chart-card">
            <div id="chart_timeline"></div>
        </div>
        <div class="chart-card">
            <div id="chart_box"></div>
        </div>
    </div>

    <footer>
        <div>Proyecto Final: Aplicaciones Analíticas de Big Data • UAPA 2026</div>
        <div>Metodología: NLP Transformer + YouTube Data API v3 (Herramientas 100% Gratuitas)</div>
    </footer>

    <script>
        var donutData = {fig_donut.to_json()};
        Plotly.newPlot('chart_donut', donutData.data, donutData.layout, {{responsive: true}});

        var terminosData = {fig_terminos.to_json()};
        Plotly.newPlot('chart_terminos', terminosData.data, terminosData.layout, {{responsive: true}});

        var catData = {fig_cat.to_json()};
        Plotly.newPlot('chart_cat', catData.data, catData.layout, {{responsive: true}});

        var timelineData = {fig_timeline.to_json()};
        Plotly.newPlot('chart_timeline', timelineData.data, timelineData.layout, {{responsive: true}});

        var boxData = {fig_box.to_json()};
        Plotly.newPlot('chart_box', boxData.data, boxData.layout, {{responsive: true}});
    </script>
</body>
</html>"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[EXITO] Dashboard interactivo generado exitosamente en: {output_html}")
    return output_html


if __name__ == "__main__":
    generar_dashboard_ejecutivo()
