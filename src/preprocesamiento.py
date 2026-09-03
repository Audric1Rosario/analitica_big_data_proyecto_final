"""
Módulo de Preprocesamiento y Limpieza de Texto en Español
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez
"""

import re
import unicodedata
import pandas as pd

# Stopwords en español frecuentes para análisis de telecomunicaciones
SPANISH_STOPWORDS = {
    "a", "al", "algo", "algunas", "algunos", "ante", "antes", "como", "con", "contra",
    "cual", "cuando", "de", "del", "desde", "donde", "durante", "e", "el", "ella", "ellas",
    "ellos", "en", "entre", "era", "erais", "eran", "eras", "eres", "es", "esa", "esas",
    "ese", "eso", "esos", "esta", "estaba", "estabais", "estaban", "estabas", "estad",
    "estada", "estadas", "estado", "estados", "estamos", "estando", "estar", "estaremos",
    "estará", "estarán", "estarás", "estaré", "estaréis", "estaría", "estaríais", "estaríamos",
    "estarían", "estarías", "estas", "este", "estemos", "esto", "estos", "estoy", "estuve",
    "estuviera", "estuvierais", "estuvieran", "estuvieras", "estuvieron", "estuviese",
    "estuvieseis", "estuviesen", "estuvieses", "estuvimos", "estuviste", "estuvisteis",
    "estuviéramos", "estuviésemos", "estuvo", "está", "estábamos", "estáis", "están",
    "estás", "esté", "estéis", "estén", "estés", "fue", "fuera", "fuerais", "fueran",
    "fueras", "fueron", "fuese", "fueseis", "fuesen", "fueses", "fui", "fuimos", "fuiste",
    "fuisteis", "fuéramos", "fuésemos", "ha", "habida", "habidas", "habido", "habidos",
    "habiendo", "habremos", "habrá", "habrán", "habrás", "habré", "habréis", "habría",
    "habríais", "habríamos", "habrían", "habrías", "habéis", "había", "habíais", "habíamos",
    "habían", "habías", "han", "has", "hasta", "hay", "haya", "hayamos", "hayan", "hayas",
    "hayáis", "he", "hemos", "hube", "hubiera", "hubierais", "hubieran", "hubieras",
    "hubieron", "hubiese", "hubieseis", "hubiesen", "hubieses", "hubimos", "hubiste",
    "hubisteis", "hubiéramos", "hubiésemos", "hubo", "la", "las", "le", "les", "lo", "los",
    "me", "mi", "mis", "mucho", "muchos", "muy", "más", "mía", "mías", "mío", "míos",
    "nada", "ni", "no", "nos", "nosotras", "nosotros", "nuestra", "nuestras", "nuestro",
    "nuestros", "o", "os", "otra", "otras", "otro", "otros", "para", "pero", "poco", "por",
    "porque", "que", "quien", "quienes", "qué", "se", "sea", "seamos", "sean", "seas",
    "seremos", "será", "serán", "serás", "seré", "seréis", "sería", "seríais", "seríamos",
    "serían", "serías", "seáis", "sido", "siendo", "sin", "sobre", "sois", "somos", "son",
    "soy", "su", "sus", "suya", "suyas", "suyo", "suyos", "sí", "también", "tanto", "te",
    "tendremos", "tendrá", "tendrán", "tendrás", "tendré", "tendréis", "tendría", "tendríais",
    "tendríamos", "tendrían", "tendrías", "tened", "tenemos", "tenga", "tengamos", "tengan",
    "tengas", "tengáis", "tengo", "tenida", "tenidas", "tenido", "tenidos", "teniendo",
    "tenéis", "tenía", "teníais", "teníamos", "tenían", "tenías", "ti", "tiene", "tienen",
    "tienes", "todo", "todos", "tu", "tus", "tuve", "tuviera", "tuvierais", "tuvieran",
    "tuvieras", "tuvieron", "tuviese", "tuvieseis", "tuviesen", "tuvieses", "tuvimos",
    "tuviste", "tuvisteis", "tuviéramos", "tuviésemos", "tuvo", "tuya", "tuyas", "tuyo",
    "tuyos", "un", "una", "unas", "uno", "unos", "vosotras", "vosotros", "vuestra",
    "vuestras", "vuestro", "vuestros", "y", "ya", "yo", "él", "éramos"
}

# Palabras específicas del contexto que no aportan al sentimiento
DOMAIN_STOPWORDS = {"claro", "clarord", "video", "hola", "buenos", "días", "tardes", "noches", "youtube"}


def limpiar_texto(texto: str, remover_stopwords: bool = False) -> str:
    """
    Realiza la limpieza de un comentario de YouTube:
    - Normalización unicode
    - Eliminación de URLs y menciones (@usuario)
    - Remoción de caracteres especiales y números aislados
    - Normalización de espacios
    """
    if not isinstance(texto, str) or not texto.strip():
        return ""

    # Normalizar caracteres unicode
    texto = unicodedata.normalize("NFKD", texto)

    # Eliminar URLs
    texto = re.sub(r"https?://\S+|www\.\S+", " ", texto)

    # Eliminar menciones @
    texto = re.sub(r"@\w+", " ", texto)

    # Convertir a minúsculas
    texto = texto.lower()

    # Reemplazar risas comunes tipo 'jajaja', 'jejeje' por token o reducir
    texto = re.sub(r"\b(ja|je|ji){2,}\b", "risa", texto)

    # Mantener letras en español (incluyendo á, é, í, ó, ú, ñ, ü) y eliminar puntuaciones raras
    texto = re.sub(r"[^a-záéíóúñü\s]", " ", texto)

    # Normalizar espacios en blanco
    tokens = [token.strip() for token in texto.split() if token.strip()]

    if remover_stopwords:
        tokens = [t for t in tokens if t not in SPANISH_STOPWORDS and t not in DOMAIN_STOPWORDS and len(t) > 2]

    return " ".join(tokens)


def clasificar_topico_reglas(texto: str) -> str:
    """
    Identifica el tópico temático principal del comentario según vocabulario telco.
    Categorías: Fibra Óptica, Red Móvil / 5G, Atención al Cliente, Facturación, Planes / Ofertas.
    """
    t = texto.lower()
    if any(k in t for k in ["fibra", "internet", "wifi", "modem", "megas", "ping", "subida", "bajada", "router", "lento"]):
        return "Fibra Óptica e Internet Hogar"
    elif any(k in t for k in ["5g", "senal", "cobertura", "datos", "lte", "4g", "roaming", "linea", "chip", "sim"]):
        return "Red Móvil y Cobertura 5G"
    elif any(k in t for k in ["servicio", "atencion", "soporte", "call center", "tecnico", "espera", "oficina", "reporte"]):
        return "Atención al Cliente y Soporte"
    elif any(k in t for k in ["factura", "cobro", "precio", "pago", "caro", "aumento", "recarga", "corte", "dinero", "pesos"]):
        return "Facturación y Tarifas"
    elif any(k in t for k in ["promo", "oferta", "plan", "pospago", "prepago", "cambio", "equipo", "celular", "upgrade"]):
        return "Planes y Promociones"
    else:
        return "Experiencia General de Marca"


def preprocesar_dataframe(df: pd.DataFrame, columna_texto: str = "comment_text") -> pd.DataFrame:
    """Aplica preprocesamiento a todo un DataFrame de comentarios."""
    df_clean = df.copy()
    df_clean["clean_text"] = df_clean[columna_texto].apply(lambda x: limpiar_texto(x, remover_stopwords=False))
    df_clean["tokens_analisis"] = df_clean[columna_texto].apply(lambda x: limpiar_texto(x, remover_stopwords=True))
    df_clean["topic_category"] = df_clean[columna_texto].apply(clasificar_topico_reglas)
    return df_clean
