### Reproductor de videos directo de youtube

import tkinter as tk
from tkinter import ttk
import webbrowser
import requests
import json
from urllib.parse import quote

def get_video_info(query, limit=10):
  query = quote(query)

  data = {'context': {
             'client': {
                 'clientName': 'WEB',
                 'clientVersion': '2.20201021.03.00',
             }
          },
          'query': query,
        }

  API_KEY = "AIzaSyBy3Qhu3XjUv2GxiW7QxxO9N5IKdm-UaVw"
  url = f"https://www.youtube.com/youtubei/v1/search?key={API_KEY}"
  r = requests.post(url, json.dumps(data).encode('utf8'), 
                    headers={'content-type': 'application/json'} )
  j = r.json()

  # Extraer lista de resultados
  results = (j["contents"]['twoColumnSearchResultsRenderer']['primaryContents']
             ['sectionListRenderer']['contents'][0]
             ['itemSectionRenderer']['contents'])
  # Construir lista simplificada
  info_list = []
  for video in results:
    info = video.get("videoRenderer")
    if not info:
      continue           # Saltarse los resultados que son publicidad
    # Extraer solo título e id
    title = info["title"]["runs"][0]["text"]
    video_id = info["videoId"]
    info_list.append((video_id, title))

    if len(info_list) == limit:  # Detenerse cuando haya suficientes
      break
  return info_list

def reproduce_video(video_url):
    # Abre la URL en el navegador web predeterminado
    webbrowser.open(video_url)
    return 0


busqueda = input("Escribe lo que quieras reproducir: ")
print(type(busqueda))

resultados = get_video_info(busqueda)
#print("\n".join("   ".join(data) for data in resultados))

url_video = "https://www.youtube.com/watch?v={}".format(resultados[0][0])

if url_video:
    print("URL del primer video:", url_video)
else:
    print("No se encontraron videos.")

# Crea la ventana principal
root = tk.Tk()
root.withdraw()

reproduce_video(url_video)

#reproduce_video(url_video)