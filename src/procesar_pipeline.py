"""
Pipeline Integral de Procesamiento y Modelado NLP para Claro Dominicana (@clarord)
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric André Rosario Rosario & Orlando Benítez Ventura
Facilitador: Luis Eduardo Bayonet Robles
"""

import os
import sys

import pandas as pd

# Asegurar importación de módulos hermanos
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from modelado_nlp import SentimentTransformerPipeline  # noqa: E402
from preprocesamiento import preprocesar_dataframe  # noqa: E402

# Configurar encoding seguro para consola
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def ejecutar_pipeline(
    raw_csv: str = "data/raw/youtube_claro_raw.csv", output_csv: str = "data/processed/youtube_claro_processed.csv"
) -> pd.DataFrame:
    """
    Ejecuta el flujo integral de ingeniería de datos y modelado NLP:
    1. Carga de 799 opiniones reales congeladas de la YouTube Data API v3.
    2. Limpieza léxica, desinfección de jerga y stopwords dominicanas.
    3. Inferencia de sentimiento Deep Learning con Transformer preentrenado (BETO).
    4. Exportación estructurada a CSV procesado y cálculo dinámico de métricas.
    """
    if not os.path.exists(raw_csv):
        raise FileNotFoundError(f"[ERROR CRÍTICO] No se encontró el dataset crudo en: {raw_csv}")

    print(f"[PIPELINE] 1. Ingesta de datos crudos desde {raw_csv}...")
    df_raw = pd.read_csv(raw_csv)
    print(f"[PIPELINE] -> {len(df_raw)} registros crudos cargados exitosamente.")

    print("\n[PIPELINE] 2. Preprocesamiento lingüístico (normalización Unicode, regex, jerga telco)...")
    df_clean = preprocesar_dataframe(df_raw, columna_texto="comment_text")

    print("\n[PIPELINE] 3. Inferencia Deep Learning con Transformer Preentrenado en Español (BETO - Cero Fallback)...")
    nlp_model = SentimentTransformerPipeline(model_name="finiteautomata/beto-sentiment-analysis")
    df_processed = nlp_model.procesar_dataframe(df_clean, columna_texto="clean_text", batch_size=32)

    print(f"\n[PIPELINE] 4. Almacenando dataset enriquecido en: {output_csv}...")
    output_dir = os.path.dirname(output_csv)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    df_processed.to_csv(output_csv, index=False, encoding="utf-8-sig")

    total = len(df_processed)
    dist = df_processed["sentiment_label"].value_counts(normalize=True) * 100
    counts = df_processed["sentiment_label"].value_counts()

    print("\n[RESUMEN GERENCIAL DEL PROCESAMIENTO]")
    print(f"Total de registros auditados: {total}")
    for k in ["POSITIVO", "NEGATIVO", "NEUTRO"]:
        pct = dist.get(k, 0.0)
        cnt = counts.get(k, 0)
        print(f"  • {k}: {pct:.2f}% ({cnt} comentarios)")

    pct_pos = dist.get("POSITIVO", 0.0)
    pct_neg = dist.get("NEGATIVO", 0.0)
    nss = round(pct_pos - pct_neg, 2)
    print(f"Net Sentiment Score (NSS / NPS Estimado): {nss:+.2f}%\n")

    return df_processed


if __name__ == "__main__":
    ejecutar_pipeline()
