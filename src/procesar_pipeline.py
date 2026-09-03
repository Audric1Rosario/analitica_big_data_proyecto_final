"""
Pipeline Integral de Procesamiento y Modelado NLP para Claro Dominicana
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez
"""

import os
import sys
import pandas as pd
from preprocesamiento import preprocesar_dataframe
from modelado_nlp import SentimentTransformerPipeline

# Configurar encoding seguro
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def ejecutar_pipeline():
    raw_csv = "data/raw/youtube_claro_raw.csv"
    output_dir = "data/processed"
    output_csv = os.path.join(output_dir, "youtube_claro_processed.csv")

    if not os.path.exists(raw_csv):
        raise FileNotFoundError(f"[ERROR] No se encontró el dataset crudo en: {raw_csv}")

    print(f"[PIPELINE] 1. Cargando datos crudos desde {raw_csv}...")
    df_raw = pd.read_csv(raw_csv)
    print(f"[PIPELINE] -> Registros crudos cargados: {len(df_raw)}")

    print("\n[PIPELINE] 2. Preprocesando y limpiando texto en español...")
    df_clean = preprocesar_dataframe(df_raw, columna_texto="comment_text")

    print("\n[PIPELINE] 3. Aplicando inferencia de sentimiento con arquitectura Transformer preentrenada...")
    nlp_model = SentimentTransformerPipeline()
    df_processed = nlp_model.procesar_dataframe(df_clean, columna_texto="clean_text")

    print(f"\n[PIPELINE] 4. Guardando datos enriquecidos en: {output_csv}...")
    os.makedirs(output_dir, exist_ok=True)
    df_processed.to_csv(output_csv, index=False, encoding="utf-8-sig")

    print("\n" + "="*55)
    print("RESUMEN GERENCIAL DEL PROCESAMIENTO:")
    print(f"Total de registros: {len(df_processed)}")
    dist = df_processed["sentiment_label"].value_counts(normalize=True) * 100
    for k, v in dist.items():
        print(f"  - {k}: {v:.1f}% ({df_processed['sentiment_label'].value_counts()[k]} comentarios)")

    pct_pos = dist.get("POSITIVO", 0)
    pct_neg = dist.get("NEGATIVO", 0)
    nss = round(pct_pos - pct_neg, 2)
    print(f"Net Sentiment Score (NSS / NPS Estimado): {nss:+0.2f}%")
    print("="*55 + "\n")

    return df_processed


if __name__ == "__main__":
    ejecutar_pipeline()
