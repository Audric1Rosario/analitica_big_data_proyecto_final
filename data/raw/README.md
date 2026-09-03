# Repositorio de Datos Crudos (Raw Data) - Claro República Dominicana

Este directorio contiene los datos crudos extraídos en tiempo real mediante la **YouTube Data API v3** (Google Cloud Platform) para publicaciones, tutoriales, comparativas y videos oficiales relacionados con **Claro República Dominicana** (`@clarord`).

## Origen y Metadatos de la Extracción

* **Fuente:** YouTube Data API v3 (Google Cloud Platform)
* **Credencial:** Clave de API autorizada en `.env` (`YT_API_KEY`)
* **Fecha de Extracción:** Septiembre 2026 (consolidación en vivo)
* **Total de Registros Recolectados:** 799 comentarios únicos
* **Videos Analizados:** 56 videos (corporativos, tutoriales de Mi Claro, cobertura 5G, pruebas de velocidad de fibra óptica y canales de soporte)
* **Consumo de Cuota de API:** 649 unidades de 10,000 diarias disponibles (6.49% de uso de cuota, garantizando nivel gratuito estricto)
* **Archivos Disponibles:**
  * `youtube_claro_raw.csv`: Formato tabular delimitado por comas con codificación UTF-8 con BOM.
  * `youtube_claro_raw.json`: Estructura jerárquica nativa en formato JSON.

## Estructura de Campos

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `comment_id` | String | Identificador alfanumérico único de YouTube |
| `video_id` | String | Identificador del video consultado |
| `video_title` | String | Título del video publicado en YouTube |
| `channel_title` | String | Canal emisor (Claro RD o creador de contenido analizado) |
| `author` | String | Nombre del usuario que emitió el comentario |
| `comment_text` | String | Texto íntegro del comentario |
| `published_at` | DateTime | Marca temporal de publicación (ISO 8601) |
| `like_count` | Integer | Cantidad de 'me gusta' otorgados al comentario |
| `reply_count` | Integer | Número de respuestas en el hilo del comentario |
| `service_category`| String | Clasificación temática del servicio (Fibra, 5G, Soporte, Facturación, Planes) |
