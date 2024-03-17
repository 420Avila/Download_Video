import os
import googleapiclient.discovery
import openpyxl

# Clave de API obtenida de la Consola de Desarrolladores de Google
API_KEY = "pon tu API KEY"

# Obtener el servicio autenticado de YouTube
def get_authenticated_service():
    api_service_name = "youtube"
    api_version = "v3"

    # Construye el servicio de YouTube utilizando la clave de API
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    return youtube

# Obtiene los enlaces de los videos en una lista de reproducción
def get_playlist_videos(youtube, playlist_id):
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50  # Puedes ajustar el número de resultados si lo necesitas
    )
    response = request.execute()
    videos = []
    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        videos.append(video_link)
    return videos

# Guarda los enlaces de los videos en un archivo de Excel
def save_to_excel(videos, file_name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Video Links"])
    for video in videos:
        ws.append([video])
    wb.save(file_name)

# ID de tu lista de reproducción de YouTube
playlist_id = "TU playlist_id"

# Nombre del archivo de Excel donde se guardarán los enlaces
file_name = "./videos.xlsx"

# Obtener el servicio autenticado de YouTube
youtube = get_authenticated_service()

# Obtener los enlaces de los videos de la lista de reproducción
videos = get_playlist_videos(youtube, playlist_id)

# Guardar los enlaces en un archivo de Excel
save_to_excel(videos, file_name)

print("Los enlaces de los videos se han guardado en el archivo Excel.")
