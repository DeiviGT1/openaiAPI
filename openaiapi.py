import openai
import os
from dotenv import load_dotenv

load_dotenv()

#authentication stuff
openai.api_key = os.getenv("OPENAI_API_KEY")
# engine = "text-davinci-edit-001"
engine = "text-davinci-003" #or "curie-001"



def generar_respuesta(song_name, artista):
  prompt = (f"Recomendación de canciones similares a '{song_name}'\n"
              f"Descripción: Escriba el nombre de una canción y obtendrá recomendaciones de otras canciones similares.\n"
              f"Contexto: El modelo debe considerar la letra, el género musical, el artista y la popularidad de la canción de entrada para generar las recomendaciones.\n"
              f"Ejemplo de entrada: '{song_name}'\n"
              f"Instrucciones: El modelo debe generar una lista de las 10 canciones más similares a '{song_name if song_name else 'No sabe igual'} {'de ' if artista else ''} {artista if artista else ''}', teniendo en cuenta la letra, el género musical, el artista y la popularidad de la canción.")
  completions = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.75,
  )

  message = completions.choices[0].text.strip()
  song_recommendations = message.split("\n")[1:-1] # elimina la primera y última línea de la respuesta que contienen información adicional
  song_recommendations = list(set(song_recommendations))
  return song_recommendations