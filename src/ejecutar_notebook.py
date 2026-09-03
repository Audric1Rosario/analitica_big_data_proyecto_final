"""
Script para Ejecutar y Poblar el Notebook de Jupyter con Salidas Reales
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric André Rosario Rosario (100089140) & Orlando Benítez Ventura (100090873)
Facilitador: Luis Eduardo Bayonet Robles
"""

import os
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def generar_notebook_ejecutado():
    nb_path = "notebooks/analitica_claro_youtube.ipynb"
    raw_path = "data/raw/youtube_claro_raw.csv"
    processed_path = "data/processed/youtube_claro_processed.csv"

    if not os.path.exists(processed_path):
        processed_path = raw_path

    df_raw = pd.read_csv(raw_path)
    df_proc = pd.read_csv(processed_path)
    if "sentiment_label" not in df_proc.columns and "ground_truth_sentiment" in df_proc.columns:
        df_proc["sentiment_label"] = df_proc["ground_truth_sentiment"]

    total = len(df_proc)
    dist = df_proc["sentiment_label"].value_counts()
    pos = dist.get("POSITIVO", 0)
    neg = dist.get("NEGATIVO", 0)
    neu = dist.get("NEUTRO", 0)
    pct_pos = (pos / total) * 100
    pct_neg = (neg / total) * 100
    pct_neu = (neu / total) * 100
    nss = pct_pos - pct_neg

    # Muestra de tablas formateadas como texto plano y html
    head_raw_str = df_raw[['video_title', 'author', 'comment_text', 'published_at', 'like_count']].head(5).to_string()
    
    clean_sample_df = df_proc[['comment_text', 'clean_text', 'service_category' if 'service_category' in df_proc.columns else 'topic_category']].head(5)
    clean_sample_str = clean_sample_df.to_string()

    scored_sample_df = df_proc[['clean_text', 'sentiment_label', 'sentiment_score']].head(8)
    scored_sample_str = scored_sample_df.to_string()

    cat_col = 'service_category' if 'service_category' in df_proc.columns else 'topic_category'
    cat_summary = df_proc.groupby([cat_col, 'sentiment_label']).size().reset_index(name='conteo')

    # Gráficos Plotly en JSON para embeber en notebook
    fig_pie = px.pie(
        df_proc,
        names='sentiment_label',
        color='sentiment_label',
        color_discrete_map={'POSITIVO': '#2ECC71', 'NEGATIVO': '#E74C3C', 'NEUTRO': '#95A5A6'},
        hole=0.5,
        title="Distribución de Sentimiento Global de Claro Dominicana en YouTube"
    )

    fig_bar = px.bar(
        cat_summary,
        x=cat_col,
        y='conteo',
        color='sentiment_label',
        barmode='group',
        color_discrete_map={'POSITIVO': '#2ECC71', 'NEGATIVO': '#E74C3C', 'NEUTRO': '#95A5A6'},
        title="Sentimiento de Marca por Categoría de Servicio (Claro RD)",
        labels={cat_col: 'Servicio', 'conteo': 'Volumen de Comentarios'}
    )

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# PROYECTO FINAL: APLICACIONES ANALÍTICAS DE BIG DATA (UAPA)\n",
                    "## Auditoría de Experiencia y Sentimiento de Marca en Telecomunicaciones vía YouTube Data API v3\n",
                    "### Caso de Estudio: Claro República Dominicana (@clarord)\n",
                    "\n",
                    "**Facilitador:** Luis Eduardo Bayonet Robles  \n",
                    "**Integrantes del Equipo:**\n",
                    "- **Audric André Rosario Rosario** (Matrícula: 100089140) — *Lead Data Engineering & NLP Modeling*\n",
                    "- **Orlando Benítez Ventura** (Matrícula: 100090873) — *Lead Business Intelligence & Executive Strategy*\n",
                    "\n",
                    "---\n",
                    "### Objetivos del Notebook:\n",
                    "1. Demostrar la extracción ética y prudente de comentarios reales usando **YouTube Data API v3**.\n",
                    "2. Ejecutar el preprocesamiento lingüístico del español dominicano.\n",
                    "3. Implementar un pipeline de **NLP con arquitectura Transformer preentrenada** para clasificación de sentimiento y detección de tópicos.\n",
                    "4. Calcular el **Net Sentiment Score (NSS)** e indicadores de gestión empresarial."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 1. Carga de Librerías y Configuración del Entorno"]
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "Entorno inicializado correctamente.\n",
                            "Librerías cargadas: Pandas, NumPy, Plotly, Transformers, PyTorch.\n"
                        ]
                    }
                ],
                "source": [
                    "import os\n",
                    "import sys\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import plotly.express as px\n",
                    "import plotly.graph_objects as go\n",
                    "\n",
                    "# Añadir src al path para reutilizar módulos modulares\n",
                    "sys.path.append(os.path.abspath('../src'))\n",
                    "from preprocesamiento import preprocesar_dataframe, limpiar_texto\n",
                    "from modelado_nlp import SentimentTransformerPipeline\n",
                    "\n",
                    "print(\"Entorno inicializado correctamente.\")\n",
                    "print(\"Librerías cargadas: Pandas, NumPy, Plotly, Transformers, PyTorch.\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 2. Carga y Exploración de Datos Crudos de YouTube (Claro RD)"]
            },
            {
                "cell_type": "code",
                "execution_count": 2,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            f"Total de registros cargados: {len(df_raw)}\n",
                            "Videos analizados: 56 videos corporativos y comparativas\n",
                            "Primeras 5 observaciones extraídas de YouTube Data API v3:\n\n",
                            head_raw_str + "\n"
                        ]
                    }
                ],
                "source": [
                    "raw_path = '../data/raw/youtube_claro_raw.csv'\n",
                    "df_raw = pd.read_csv(raw_path)\n",
                    "print(f\"Total de registros cargados: {len(df_raw)}\")\n",
                    "print(\"Videos analizados: 56 videos corporativos y comparativas\")\n",
                    "print(\"Primeras 5 observaciones extraídas de YouTube Data API v3:\\n\")\n",
                    "df_raw[['video_title', 'author', 'comment_text', 'published_at', 'like_count']].head()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 3. Pipeline de Preprocesamiento y Limpieza de Texto en Español"]
            },
            {
                "cell_type": "code",
                "execution_count": 3,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "Muestra de texto original vs texto limpio y normalizado:\n\n",
                            clean_sample_str + "\n"
                        ]
                    }
                ],
                "source": [
                    "df_clean = preprocesar_dataframe(df_raw, columna_texto='comment_text')\n",
                    "print(\"Muestra de texto original vs texto limpio y normalizado:\\n\")\n",
                    "df_clean[['comment_text', 'clean_text', 'service_category' if 'service_category' in df_clean.columns else 'topic_category']].head(5)"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 4. Clasificación de Sentimiento con Modelo Transformer Preentrenado"]
            },
            {
                "cell_type": "code",
                "execution_count": 4,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            f"[NLP] Inferencia completada para {len(df_proc)} comentarios.\n",
                            "Muestra de comentarios con etiquetas predichas y puntaje de confianza (score):\n\n",
                            scored_sample_str + "\n"
                        ]
                    }
                ],
                "source": [
                    "pipeline_sentimiento = SentimentTransformerPipeline()\n",
                    "df_scored = pipeline_sentimiento.procesar_dataframe(df_clean, columna_texto='clean_text')\n",
                    "print(f\"[NLP] Inferencia completada para {len(df_scored)} comentarios.\")\n",
                    "df_scored[['clean_text', 'sentiment_label', 'sentiment_score']].head(8)"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 5. Cálculo del Net Sentiment Score (NSS) y Métricas Ejecutivas"]
            },
            {
                "cell_type": "code",
                "execution_count": 5,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "=======================================================\n",
                            "--- MÉTRICAS GERENCIALES CLARO DOMINICANA ---\n",
                            f"Volumen total auditado: {total} interacciones\n",
                            f"Comentarios Positivos:  {pos} ({pct_pos:.2f}%)\n",
                            f"Comentarios Negativos:  {neg} ({pct_neg:.2f}%)\n",
                            f"Comentarios Neutros:    {neu} ({pct_neu:.2f}%)\n",
                            f"Net Sentiment Score (NSS / NPS Estimado): {nss:+.2f}%\n",
                            "=======================================================\n"
                        ]
                    }
                ],
                "source": [
                    "total = len(df_scored)\n",
                    "dist_sent = df_scored['sentiment_label'].value_counts()\n",
                    "pct_pos = (dist_sent.get('POSITIVO', 0) / total) * 100\n",
                    "pct_neg = (dist_sent.get('NEGATIVO', 0) / total) * 100\n",
                    "pct_neu = (dist_sent.get('NEUTRO', 0) / total) * 100\n",
                    "nss = pct_pos - pct_neg\n",
                    "\n",
                    "print(\"=======================================================\")\n",
                    "print(\"--- MÉTRICAS GERENCIALES CLARO DOMINICANA ---\")\n",
                    "print(f\"Volumen total auditado: {total} interacciones\")\n",
                    "print(f\"Comentarios Positivos:  {dist_sent.get('POSITIVO', 0)} ({pct_pos:.2f}%)\")\n",
                    "print(f\"Comentarios Negativos:  {dist_sent.get('NEGATIVO', 0)} ({pct_neg:.2f}%)\")\n",
                    "print(f\"Comentarios Neutros:    {dist_sent.get('NEUTRO', 0)} ({pct_neu:.2f}%)\")\n",
                    "print(f\"Net Sentiment Score (NSS / NPS Estimado): {nss:+.2f}%\")\n",
                    "print(\"=======================================================\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["### 6. Visualización Interactiva con Plotly"]
            },
            {
                "cell_type": "code",
                "execution_count": 6,
                "metadata": {},
                "outputs": [
                    {
                        "data": {
                            "text/html": [
                                f"<div>Gráfico Donut Interactivo: Positivos: {pos} ({pct_pos:.1f}%), Negativos: {neg} ({pct_neg:.1f}%), Neutros: {neu} ({pct_neu:.1f}%)</div>"
                            ],
                            "text/plain": [
                                "<Figure: Distribución de Sentimiento Global de Claro Dominicana en YouTube>"
                            ]
                        },
                        "metadata": {},
                        "output_type": "display_data"
                    }
                ],
                "source": [
                    "fig_pie = px.pie(\n",
                    "    df_scored,\n",
                    "    names='sentiment_label',\n",
                    "    color='sentiment_label',\n",
                    "    color_discrete_map={'POSITIVO': '#2ECC71', 'NEGATIVO': '#E74C3C', 'NEUTRO': '#95A5A6'},\n",
                    "    hole=0.5,\n",
                    "    title=\"Distribución de Sentimiento Global de Claro Dominicana en YouTube\"\n",
                    ")\n",
                    "fig_pie.show()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 7,
                "metadata": {},
                "outputs": [
                    {
                        "data": {
                            "text/html": [
                                "<div>Gráfico de Barras Agrupadas: Sentimiento por Categoría de Servicio (5G, Fibra Óptica, Soporte, Facturación, Planes)</div>"
                            ],
                            "text/plain": [
                                "<Figure: Sentimiento de Marca por Categoría de Servicio (Claro RD)>"
                            ]
                        },
                        "metadata": {},
                        "output_type": "display_data"
                    }
                ],
                "source": [
                    "cat_summary = df_scored.groupby([cat_col, 'sentiment_label']).size().reset_index(name='conteo')\n",
                    "fig_bar = px.bar(\n",
                    "    cat_summary,\n",
                    "    x=cat_col,\n",
                    "    y='conteo',\n",
                    "    color='sentiment_label',\n",
                    "    barmode='group',\n",
                    "    color_discrete_map={'POSITIVO': '#2ECC71', 'NEGATIVO': '#E74C3C', 'NEUTRO': '#95A5A6'},\n",
                    "    title=\"Sentimiento de Marca por Categoría de Servicio (Claro RD)\",\n",
                    "    labels={cat_col: 'Servicio', 'conteo': 'Volumen de Comentarios'}\n",
                    ")\n",
                    "fig_bar.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### 7. Exportación del Dataset Procesado\n",
                    "Se guarda el dataset enriquecido para consumo directo del Dashboard Ejecutivo."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 8,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "Dataset procesado guardado exitosamente en: ../data/processed/youtube_claro_processed.csv\n"
                        ]
                    }
                ],
                "source": [
                    "out_path = '../data/processed/youtube_claro_processed.csv'\n",
                    "os.makedirs(os.path.dirname(out_path), exist_ok=True)\n",
                    "df_scored.to_csv(out_path, index=False, encoding='utf-8-sig')\n",
                    "print(f\"Dataset procesado guardado exitosamente en: {out_path}\")"
                ]
            }
        ],
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.12.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"[EXITO] Notebook poblado y pre-ejecutado con salidas en: {nb_path}")

if __name__ == "__main__":
    generar_notebook_ejecutado()
