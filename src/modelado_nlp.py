"""
Módulo de Modelado NLP: Análisis de Sentimiento con Transformadores Preentrenados (BETO)
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric André Rosario Rosario & Orlando Benítez Ventura
Empresa Caso de Estudio: Claro República Dominicana (@clarord)

Arquitectura: Transformer Bidireccional para Español (Deep Learning).
Política de Calidad: Cero fallback léxico. Inferencia pura basada en autoatención.
"""

from typing import Any

import pandas as pd

try:
    import torch
    from transformers import pipeline

    TRANSFORMERS_AVAILABLE = True
except ImportError as err:
    TRANSFORMERS_AVAILABLE = False
    _IMPORT_ERROR = err


class SentimentTransformerPipeline:
    """
    Pipeline de Clasificación de Sentimiento basado estrictamente en Arquitectura Transformer
    preentrenada para idioma español (finiteautomata/beto-sentiment-analysis).
    """

    def __init__(self, model_name: str = "finiteautomata/beto-sentiment-analysis", use_gpu: bool = False) -> None:
        if not TRANSFORMERS_AVAILABLE:
            raise RuntimeError(
                "[ERROR CRÍTICO] La biblioteca 'transformers' o 'torch' no está instalada en el entorno. "
                "Según la directiva de calidad del proyecto, está prohibido degradar la inferencia a fallbacks léxicos. "
                f"Detalle del error: {_IMPORT_ERROR}. Ejecute 'uv sync' o 'uv add transformers torch'."
            )

        self.model_name = model_name
        self.device = 0 if (use_gpu and torch.cuda.is_available()) else -1

        print(f"[NLP] Inicializando modelo Transformer preentrenado: {model_name}...")
        print(f"[NLP] Dispositivo de cómputo seleccionado: {'GPU (CUDA)' if self.device >= 0 else 'CPU'}")

        try:
            self.nlp_pipeline = pipeline(
                "sentiment-analysis", model=self.model_name, device=self.device, truncation=True, max_length=512
            )
            print("[NLP] Modelo Transformer cargado exitosamente en memoria.")
        except Exception as exc:
            raise RuntimeError(
                f"[ERROR CRÍTICO] Falló la carga de los pesos del modelo Transformer '{model_name}'. "
                "No se aplicará fallback léxico conforme a las directivas de integridad analítica. "
                f"Causa original: {exc}"
            ) from exc

    def _mapear_etiqueta(self, raw_label: str) -> str:
        """Mapea las salidas estándar de BETO (POS, NEG, NEU) a la nomenclatura corporativa."""
        lbl = raw_label.upper().strip()
        if "POS" in lbl:
            return "POSITIVO"
        if "NEG" in lbl:
            return "NEGATIVO"
        return "NEUTRO"

    def predecir_sentimiento_individual(self, texto: str) -> dict[str, Any]:
        """
        Clasifica un único comentario retornando la etiqueta ('POSITIVO', 'NEGATIVO', 'NEUTRO')
        y el puntaje de confianza probabilístico (score: 0.0 a 1.0).
        """
        if not isinstance(texto, str) or not texto.strip():
            return {"label": "NEUTRO", "score": 0.50}

        resultado = self.nlp_pipeline(texto[:512])[0]
        label = self._mapear_etiqueta(resultado["label"])
        score = round(float(resultado["score"]), 4)
        return {"label": label, "score": score}

    def procesar_dataframe(
        self, df: pd.DataFrame, columna_texto: str = "clean_text", batch_size: int = 32
    ) -> pd.DataFrame:
        """
        Aplica inferencia de sentimiento por lotes (batch processing) con autoatención bidireccional
        a todo el DataFrame, optimizando el rendimiento sobre CPU o GPU.
        """
        df_res = df.copy()
        textos_originales = df_res[columna_texto].tolist()

        # Preparar textos higienizados para el pipeline (manejo seguro de nulos y vacíos)
        textos_a_procesar = [
            str(txt)[:512] if (isinstance(txt, str) and txt.strip()) else "comentario" for txt in textos_originales
        ]

        total = len(textos_a_procesar)
        print(f"[NLP] Ejecutando inferencia Transformer profunda para {total} comentarios (batch_size={batch_size})...")

        # Inferencia por lotes optimizada en PyTorch
        raw_predicciones = self.nlp_pipeline(textos_a_procesar, batch_size=batch_size, truncation=True)

        labels: list[str] = []
        scores: list[float] = []

        for i, pred in enumerate(raw_predicciones):
            original = textos_originales[i]
            if not isinstance(original, str) or not original.strip():
                labels.append("NEUTRO")
                scores.append(0.50)
            else:
                labels.append(self._mapear_etiqueta(pred["label"]))
                scores.append(round(float(pred["score"]), 4))

        df_res["sentiment_label"] = labels
        df_res["sentiment_score"] = scores

        # Cálculo dinámico de métricas gerenciales (Zero Hardcoding)
        pos = int((df_res["sentiment_label"] == "POSITIVO").sum())
        neg = int((df_res["sentiment_label"] == "NEGATIVO").sum())
        neu = int((df_res["sentiment_label"] == "NEUTRO").sum())

        pct_pos = (pos / total) * 100 if total > 0 else 0.0
        pct_neg = (neg / total) * 100 if total > 0 else 0.0
        pct_neu = (neu / total) * 100 if total > 0 else 0.0
        nss = round(pct_pos - pct_neg, 2)

        print("[RESULTADOS TRANSFORMER REAL]")
        print(f"  • Total registros procesados: {total}")
        print(f"  • Positivos: {pos} ({pct_pos:.2f}%)")
        print(f"  • Negativos: {neg} ({pct_neg:.2f}%)")
        print(f"  • Neutros:   {neu} ({pct_neu:.2f}%)")
        print(f"  • Net Sentiment Score (NSS): {nss:+.2f}%")

        return df_res
