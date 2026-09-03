"""
Módulo de Modelado NLP: Análisis de Sentimiento con Transformadores Preentrenados
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez
Empresa Caso de Estudio: Claro República Dominicana
"""

import os
import pandas as pd
import numpy as np

# Intentar importar Hugging Face Transformers
try:
    from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False


# Léxico de sentimiento y expresiones dominicanas como respaldo o refinamiento
SENTIMENT_LEXICON_ES = {
    "positivo": [
        "excelente", "bueno", "rapido", "mejor", "calidad", "estabilidad", "estable", "perfecto",
        "recomiendo", "satisfecho", "felicidades", "buenisimo", "genial", "super", "eficiente",
        "puntual", "cumplen", "fluido", "nitido", "aprobado", "incomparable", "gran", "fidelidad"
    ],
    "negativo": [
        "malo", "pesimo", "lento", "caido", "interrupcion", "interrupciones", "robo", "estafa",
        "caro", "desastre", "falla", "fallando", "basura", "incompetente", "engano", "demora",
        "espera", "cansado", "hartura", "abuso", "queja", "inestable", "peor", "descontento",
        "inoperante", "lag", "ping alto", "sin senal", "cortado", "ineficiente"
    ]
}


class SentimentTransformerPipeline:
    """
    Pipeline de Clasificación de Sentimiento basado en Arquitectura Transformer
    (ej. BETO / RoBERTuito adaptado a español o motor híbrido supervisado).
    """

    def __init__(self, model_name: str = "finiteautomata/beto-sentiment-analysis", use_gpu: bool = False):
        self.model_name = model_name
        self.pipeline = None
        self.mode = "heuristic_lexicon"

        if TRANSFORMERS_AVAILABLE:
            try:
                print(f"[NLP] Cargando modelo Transformer preentrenado: {model_name}...")
                device = 0 if use_gpu else -1
                self.pipeline = pipeline("sentiment-analysis", model=model_name, device=device)
                self.mode = "transformer"
                print("[NLP] Modelo Transformer cargado exitosamente.")
            except Exception as e:
                print(f"[AVISO] No fue posible cargar los pesos de Hugging Face ({e}). Activando motor analítico léxico-semántico en español.")
                self.mode = "heuristic_lexicon"
        else:
            print("[AVISO] Librería 'transformers' no encontrada. Utilizando motor léxico optimizado para español.")

    def predecir_sentimiento_individual(self, texto: str) -> dict:
        """
        Clasifica un único comentario retornando la etiqueta ('POSITIVO', 'NEGATIVO', 'NEUTRO')
        y el puntaje de confianza (score: 0.0 a 1.0).
        """
        if not isinstance(texto, str) or not texto.strip():
            return {"label": "NEUTRO", "score": 0.50}

        if self.mode == "transformer" and self.pipeline:
            try:
                # Cortar a máximo 512 tokens para no desbordar atención de BERT
                res = self.pipeline(texto[:512])[0]
                raw_label = res["label"].upper()
                score = round(float(res["score"]), 4)

                # Mapear etiquetas comunes (POS, NEG, NEU o LABEL_0, etc.)
                if "POS" in raw_label or raw_label in ["4 STARS", "5 STARS"]:
                    label = "POSITIVO"
                elif "NEG" in raw_label or raw_label in ["1 STAR", "2 STARS"]:
                    label = "NEGATIVO"
                else:
                    label = "NEUTRO"

                return {"label": label, "score": score}
            except Exception:
                pass

        # Motor de respaldo semántico (Dominican telco lexicon)
        t_clean = texto.lower()
        pos_hits = sum(1 for w in SENTIMENT_LEXICON_ES["positivo"] if w in t_clean)
        neg_hits = sum(1 for w in SENTIMENT_LEXICON_ES["negativo"] if w in t_clean)

        if pos_hits > neg_hits:
            confidence = min(0.65 + (pos_hits * 0.1), 0.98)
            return {"label": "POSITIVO", "score": round(confidence, 3)}
        elif neg_hits > pos_hits:
            confidence = min(0.65 + (neg_hits * 0.1), 0.99)
            return {"label": "NEGATIVO", "score": round(confidence, 3)}
        else:
            return {"label": "NEUTRO", "score": 0.60}

    def procesar_dataframe(self, df: pd.DataFrame, columna_texto: str = "clean_text") -> pd.DataFrame:
        """Aplica la inferencia de sentimiento a todo el conjunto de datos."""
        df_res = df.copy()
        predicciones = []

        print(f"[NLP] Clasificando sentimientos para {len(df_res)} comentarios...")
        for txt in df_res[columna_texto]:
            pred = self.predecir_sentimiento_individual(str(txt))
            predicciones.append(pred)

        df_res["sentiment_label"] = [p["label"] for p in predicciones]
        df_res["sentiment_score"] = [p["score"] for p in predicciones]

        # Calcular métricas globales ejecutivas
        total = len(df_res)
        pos = (df_res["sentiment_label"] == "POSITIVO").sum()
        neg = (df_res["sentiment_label"] == "NEGATIVO").sum()
        neu = (df_res["sentiment_label"] == "NEUTRO").sum()

        pct_pos = (pos / total) * 100
        pct_neg = (neg / total) * 100
        nps_estimado = round(pct_pos - pct_neg, 2)

        print(f"[RESULTADOS] Positivos: {pos} ({pct_pos:.1f}%) | Negativos: {neg} ({pct_neg:.1f}%) | Neutros: {neu} ({(neu/total)*100:.1f}%)")
        print(f"[RESULTADOS] Net Sentiment Score (NSS / NPS Estimado): {nps_estimado}")

        return df_res
