"""
Extractor de Datos en Vivo - YouTube Data API v3 para Claro Dominicana
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez

Este módulo extrae comentarios y metadatos reales de YouTube mediante la API oficial,
optimizando el consumo de cuota diaria (presupuesto prudente < 800 unidades de 10,000).
"""

import os
import sys
import json
import time
import re
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Asegurar soporte de caracteres especiales y emojis en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Cargar variables de entorno desde .env
load_dotenv()

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False


def sanitizar_consola(texto: str) -> str:
    """Elimina caracteres no ASCII o problemáticos únicamente para impresiones en terminal."""
    if not isinstance(texto, str):
        return ""
    return re.sub(r"[^\x00-\x7FáéíóúÁÉÍÓÚñÑüÜ¿?¡!\s\.,;:\-_]", "", texto)


class YouTubeLiveExtractor:
    """Extractor prudente y optimizado de la API de YouTube Data v3."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("YT_API_KEY") or os.getenv("YOUTUBE_API_KEY")
        if not self.api_key:
            raise ValueError("[ERROR] No se encontró la API Key. Define YT_API_KEY en el archivo .env")

        if not GOOGLE_API_AVAILABLE:
            raise ImportError("[ERROR] La librería google-api-python-client no está instalada en el entorno.")

        print(f"[AUTH] Conectando a YouTube Data API v3 con clave: {self.api_key[:6]}...{self.api_key[-4:]}")
        self.youtube = build("youtube", "v3", developerKey=self.api_key)
        self.quota_used = 0

    def buscar_videos_objetivo(self, query: str = "Claro Republica Dominicana", max_results: int = 10) -> list:
        """
        Busca videos relevantes en YouTube en español.
        Costo de cuota: 100 unidades por llamada.
        """
        print(f"\n[SEARCH] Buscando videos para: '{sanitizar_consola(query)}' (máx: {max_results})...")
        videos = []
        try:
            req = self.youtube.search().list(
                part="snippet",
                q=query,
                type="video",
                relevanceLanguage="es",
                maxResults=max_results,
                order="relevance"
            )
            resp = req.execute()
            self.quota_used += 100

            for item in resp.get("items", []):
                vid_id = item["id"]["videoId"]
                snippet = item["snippet"]
                videos.append({
                    "video_id": vid_id,
                    "video_title": snippet.get("title", ""),
                    "channel_title": snippet.get("channelTitle", ""),
                    "published_at": snippet.get("publishedAt", "")
                })

            print(f"[SEARCH] Se encontraron {len(videos)} videos. Cuota acumulada: {self.quota_used}")
        except HttpError as e:
            print(f"[ERROR] Error al buscar videos: {e}")

        return videos

    def extraer_comentarios_video(self, video_id: str, video_title: str, max_comments: int = 100) -> list:
        """
        Extrae comentarios de un video específico.
        Costo de cuota: 1 unidad por llamada (hasta 100 comentarios).
        """
        comments = []
        try:
            req = self.youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=min(max_comments, 100),
                textFormat="plainText",
                order="relevance"
            )
            resp = req.execute()
            self.quota_used += 1

            for item in resp.get("items", []):
                top_comment = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "comment_id": item["id"],
                    "video_id": video_id,
                    "video_title": video_title,
                    "channel_title": top_comment.get("channelTitle", "Claro RD"),
                    "author": top_comment.get("authorDisplayName", "Anónimo"),
                    "comment_text": top_comment.get("textDisplay", ""),
                    "published_at": top_comment.get("publishedAt", ""),
                    "like_count": top_comment.get("likeCount", 0),
                    "reply_count": item["snippet"].get("totalReplyCount", 0)
                })

        except HttpError as e:
            err_reason = str(e)
            if "commentsDisabled" in err_reason:
                print(f"        [INFO] Comentarios deshabilitados para video {video_id}.")
            else:
                print(f"        [AVISO] No se pudieron extraer comentarios de {video_id}.")

        return comments

    def inferir_categoria(self, texto: str) -> str:
        """Asigna una categoría temática de telecomunicaciones según palabras clave."""
        t = texto.lower()
        if any(k in t for k in ["fibra", "internet", "wifi", "modem", "ping", "megas", "router", "lento", "subida", "bajada"]):
            return "Fibra Óptica e Internet Hogar"
        elif any(k in t for k in ["5g", "cobertura", "senal", "datos", "4g", "lte", "roaming", "linea", "apn", "chip"]):
            return "Red Móvil y Cobertura 5G"
        elif any(k in t for k in ["servicio", "atencion", "soporte", "call center", "tecnico", "oficina", "reporte", "queja"]):
            return "Atención al Cliente y Soporte"
        elif any(k in t for k in ["factura", "cobro", "precio", "pago", "caro", "recarga", "corte", "tarifa", "pesos"]):
            return "Facturación y Tarifas"
        elif any(k in t for k in ["promo", "oferta", "plan", "pospago", "prepago", "equipo", "celular", "paquetico"]):
            return "Planes y Promociones"
        else:
            return "Experiencia General de Marca"

    def ejecutar_extraccion_completa(self, queries: list = None, max_videos_por_query: int = 10, max_comentarios_por_video: int = 100) -> pd.DataFrame:
        """
        Ejecuta la extracción multipropósito optimizando la cuota de YouTube API.
        """
        if queries is None:
            queries = [
                "Claro Republica Dominicana oficial",
                "Claro RD fibra optica internet opiniones",
                "Claro RD 5G cobertura velocidad",
                "Claro RD servicio al cliente atencion quejas",
                "Altice vs Claro Republica Dominicana comparativa",
                "Claro RD factura app mi claro"
            ]

        todos_los_comentarios = []
        videos_procesados = set()

        print(f"[INICIO] Iniciando extracción prudente con YouTube API v3...")
        print(f"[INFO] Consultas planificadas: {len(queries)} consultas temáticas.")

        for q in queries:
            vids = self.buscar_videos_objetivo(q, max_results=max_videos_por_query)
            for v in vids:
                v_id = v["video_id"]
                if v_id in videos_procesados:
                    continue
                videos_procesados.add(v_id)

                titulo_seguro = sanitizar_consola(v["video_title"][:40])
                print(f"[VIDEO] Extrayendo: {v_id} - '{titulo_seguro}...'")
                comms = self.extraer_comentarios_video(v_id, v["video_title"], max_comments=max_comentarios_por_video)
                print(f"        -> {len(comms)} comentarios obtenidos.")
                todos_los_comentarios.extend(comms)
                time.sleep(0.2)  # Pausa de cortesía

        df = pd.DataFrame(todos_los_comentarios)
        if not df.empty:
            # Eliminar posibles comentarios duplicados por ID
            df = df.drop_duplicates(subset=["comment_id"]).reset_index(drop=True)
            df["service_category"] = df.apply(lambda row: self.inferir_categoria(str(row["video_title"]) + " " + str(row["comment_text"])), axis=1)
            # Ordenar por fecha cronológica descendente
            df = df.sort_values(by="published_at", ascending=False).reset_index(drop=True)

        print("\n" + "="*55)
        print(f"[RESUMEN] Extracción en vivo finalizada exitosamente.")
        print(f"[RESUMEN] Comentarios únicos recolectados: {len(df)}")
        print(f"[RESUMEN] Videos procesados: {len(videos_procesados)}")
        print(f"[RESUMEN] Cuota consumida: {self.quota_used} de 10,000 unidades ({(self.quota_used/10000)*100:.2f}%)")
        print("="*55 + "\n")

        return df


if __name__ == "__main__":
    os.makedirs("data/raw", exist_ok=True)
    extractor = YouTubeLiveExtractor()
    df_real = extractor.ejecutar_extraccion_completa()

    if not df_real.empty:
        csv_out = "data/raw/youtube_claro_raw.csv"
        json_out = "data/raw/youtube_claro_raw.json"
        df_real.to_csv(csv_out, index=False, encoding="utf-8-sig")
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(df_real.to_dict(orient="records"), f, ensure_ascii=False, indent=2)
        print(f"[GUARDADO] Datos en vivo guardados en:\n - {csv_out}\n - {json_out}")
    else:
        print("[AVISO] No se obtuvieron comentarios de los videos consultados.")
