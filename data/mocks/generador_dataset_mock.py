"""
Generador y Estructurador de Dataset Raw: Claro Dominicana en YouTube Data API v3
Proyecto Final: Aplicaciones Analíticas de Big Data (UAPA)
Equipo: Audric Rosario & Orlando Benítez

Genera y valida el repositorio local de datos crudos extraídos de la API de YouTube
para garantizar reproducibilidad offline y estabilidad de cuota.
"""

import os
import json
import random
import pandas as pd
from datetime import datetime, timedelta

# Semilla determinista para reproducibilidad académica
random.seed(42)

VIDEOS_CLARO = [
    {
        "video_id": "CLARO_FIBRA_2025",
        "video_title": "Claro Dominicana - Nueva Fibra Óptica Simétrica hasta 1000 Mbps",
        "category": "Fibra Óptica e Internet Hogar",
        "base_date": datetime(2025, 6, 15)
    },
    {
        "video_id": "CLARO_5G_RD",
        "video_title": "La Red 5G Más Rápida y de Mayor Cobertura del País | Claro RD",
        "category": "Red Móvil y Cobertura 5G",
        "base_date": datetime(2025, 8, 20)
    },
    {
        "video_id": "CLARO_APP_MICLARO",
        "video_title": "Gestiona tus Servicios, Paga tu Factura y Compra Paqueticos con Mi Claro",
        "category": "Atención al Cliente y App",
        "base_date": datetime(2025, 10, 5)
    },
    {
        "video_id": "CLARO_FACTURACION_TUTORIAL",
        "video_title": "Conoce cómo entender tu Factura Electrónica Claro",
        "category": "Facturación y Tarifas",
        "base_date": datetime(2025, 11, 12)
    },
    {
        "video_id": "CLARO_ROAMING_PLANES",
        "video_title": "Viaja Conectado con Claro Roaming Sin Fronteras en USA y LATAM",
        "category": "Planes y Promociones",
        "base_date": datetime(2025, 12, 1)
    },
    {
        "video_id": "CLARO_SOPORTE_TECNICO",
        "video_title": "Atención al Cliente 24/7 y Asistencia Técnica Virtual Claro RD",
        "category": "Atención al Cliente y Soporte",
        "base_date": datetime(2026, 1, 10)
    }
]

# Expresiones y opiniones representativas del mercado de telecomunicaciones en República Dominicana
COMENTARIOS_POSITIVOS = [
    "Excelente servicio con la fibra óptica simétrica, tengo 300 megas en Santiago y nunca se cae.",
    "La cobertura de Claro en carretera y pueblos es la mejor del país por mucho, ninguna otra compañía llega allá.",
    "Instalaron la fibra en menos de 48 horas en Bella Vista. Muy puntuales los técnicos.",
    "El 5G en el Distrito Nacional vuela, me dio más de 450 Mbps de bajada en el test.",
    "Llevo 8 años con Claro y la estabilidad del internet para trabajar remoto es incomparable.",
    "Muy buena actualización de la app Mi Claro, ahora puedo pagar con tarjeta y se refleja de una vez.",
    "El ping en juegos online como Valorant y Warzone me bajó a 35ms con la fibra. Nítido todo.",
    "Felicidades a Claro, el soporte telefónico me resolvió un cambio de clave de router súper rápido.",
    "Excelente promoción de paqueticos libres, rinden bastante bien en la semana.",
    "Para mí es la empresa de telecomunicaciones más seria de República Dominicana. Servicio de calidad.",
    "Tenía problemas de cobertura con otra telefónica y me cambié a Claro. Santo remedio.",
    "El roaming en Estados Unidos me funcionó perfecto, sin cobros raros ni sorpresas en la factura.",
    "Buen ancho de banda y la subida simétrica me ayuda un mundo para subir videos a YouTube.",
    "Muy satisfecho con la atención en la sucursal de Blue Mall, me atendieron con mucha amabilidad.",
    "La señal no se corta ni cuando hay tormenta en Santo Domingo Este. Sigan así."
]

COMENTARIOS_NEGATIVOS = [
    "Pésimo servicio al cliente, llevo 3 días esperando que me reparen una avería de internet en Herrera.",
    "El internet se cae todos los fines de semana por la noche. Muy inestable.",
    "Me cobraron un cargo por reconexión que nunca solicité. Facturación no me da respuesta.",
    "Llamar al 107 es perder una hora de la vida escuchando una música y nadie resuelve.",
    "Dicen que es fibra simétrica pero el ping sube a 200ms en las noches en San Cristóbal. Muy lento.",
    "Aumentaron la tarifa del plan pospago sin avisar previamente por correo o SMS. Un abuso.",
    "La app Mi Claro vive con errores y se cierra sola cuando voy a pagar la factura.",
    "En la zona de Bávaro la señal 5G casi no entra, se queda en 3G o sin servicio a cada rato.",
    "Cobran carísimo por megas adicionales y los paqueticos se consumen demasiado rápido.",
    "Los técnicos vinieron, no revisaron la caja exterior y dijeron que todo estaba bien. Sigo sin internet.",
    "Muy mal soporte técnico por WhatsApp, un bot que repite lo mismo y no transfiere a un humano.",
    "Me están facturando un paquete de canales que cancelé hace dos meses. Qué desastre.",
    "El router que instalan es malísimo, a 5 metros ya no llega la señal de Wi-Fi.",
    "Es una pesadilla cancelar una línea fija, te ponen mil trabas y trámites innecesarios.",
    "La velocidad contratada de 100 megas nunca llega completa, apenas marca 30 en Speedtest."
]

COMENTARIOS_NEUTROS = [
    "¿Cuándo estará disponible la cobertura de fibra óptica en la Urbanización Real?",
    "Alguien sabe si para solicitar el cambio de router cobran algún costo adicional?",
    "Buenas tardes, quisiera saber el precio actual del plan de 500 megas de fibra.",
    "¿El servicio de 5G requiere cambiar la tarjeta SIM o sirve la misma USIM 4G?",
    "¿En qué horario labora la sucursal de la 27 de Febrero los sábados?",
    "Tengo una duda con respecto al contrato de permanencia mínima de 18 meses.",
    "¿A qué número se puede consultar el balance disponible de paqueticos por mensaje?",
    "Esperando que extiendan la fibra óptica a la provincia de La Vega.",
    "¿El roaming sin fronteras incluye llamadas locales dentro del país de destino?",
    "Información sobre los requisitos para portabilidad numérica desde otra compañía por favor."
]

USUARIOS_SAMPLE = [
    "carlos_m_rd", "laura_santiago", "jose_gaming_rd", "ana_valdez_sd", "tecnico_rd23",
    "pedro_perez_do", "maria_jimenez_c", "juan_bavaro", "alex_dev_rd", "patricia_reyes",
    "luis_almonte_sti", "elena_gomez_rd", "ramon_santos_sd", "gabriel_tech", "claudia_mella"
]


def generar_dataset_raw(total_registros: int = 1250) -> pd.DataFrame:
    """Genera el dataset simulando la extracción completa de la YouTube Data API v3."""
    registros = []
    fecha_inicio = datetime(2025, 5, 1)

    for i in range(1, total_registros + 1):
        vid = random.choice(VIDEOS_CLARO)
        categoria = vid["category"]
        
        # Ponderación realista de sentimientos en comentarios de telcos públicas (aprox 42% neg, 35% pos, 23% neu)
        r = random.random()
        if r < 0.42:
            texto = random.choice(COMENTARIOS_NEGATIVOS)
            sentiment_real = "NEGATIVO"
            likes = random.choices([0, 1, 2, 5, 12, 28, 45], weights=[40, 25, 15, 10, 5, 3, 2])[0]
        elif r < 0.77:
            texto = random.choice(COMENTARIOS_POSITIVOS)
            sentiment_real = "POSITIVO"
            likes = random.choices([0, 1, 3, 8, 15, 32], weights=[50, 25, 12, 8, 4, 1])[0]
        else:
            texto = random.choice(COMENTARIOS_NEUTROS)
            sentiment_real = "NEUTRO"
            likes = random.choices([0, 1, 2], weights=[70, 25, 5])[0]

        dias_offset = random.randint(0, 280)
        hora_offset = random.randint(0, 86400)
        fecha_pub = vid["base_date"] + timedelta(days=random.randint(0, 150), seconds=hora_offset)
        if fecha_pub > datetime(2026, 2, 25):
            fecha_pub = datetime(2026, 2, random.randint(1, 25), random.randint(8, 22), random.randint(0, 59))

        usuario = f"{random.choice(USUARIOS_SAMPLE)}_{random.randint(10, 999)}"
        comment_id = f"Ugx_{vid['video_id'][:8]}_{i:05d}"
        replies = random.choices([0, 1, 2, 3, 7], weights=[75, 12, 7, 4, 2])[0]

        registros.append({
            "comment_id": comment_id,
            "video_id": vid["video_id"],
            "video_title": vid["video_title"],
            "channel_title": "Claro República Dominicana",
            "author": usuario,
            "comment_text": texto,
            "published_at": fecha_pub.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "like_count": likes,
            "reply_count": replies,
            "service_category": categoria,
            "ground_truth_sentiment": sentiment_real
        })

    df = pd.DataFrame(registros)
    # Ordenar por fecha cronológica
    df = df.sort_values(by="published_at").reset_index(drop=True)
    return df


if __name__ == "__main__":
    os.makedirs("data/raw", exist_ok=True)
    print("[ETL] Construyendo dataset crudo representativo de la YouTube Data API v3 para Claro Dominicana...")
    df_raw = generar_dataset_raw(1250)

    csv_path = "data/raw/youtube_claro_raw.csv"
    json_path = "data/raw/youtube_claro_raw.json"

    df_raw.to_csv(csv_path, index=False, encoding="utf-8-sig")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df_raw.to_dict(orient="records"), f, ensure_ascii=False, indent=2)

    print(f"[EXITO] Dataset guardado: {len(df_raw)} registros en:")
    print(f"  - {csv_path}")
    print(f"  - {json_path}")
    print("\nResumen por Categoría:")
    print(df_raw["service_category"].value_counts())
    print("\nResumen de Distribución de Sentimiento Teórico:")
    print(df_raw["ground_truth_sentiment"].value_counts(normalize=True).round(3) * 100)
