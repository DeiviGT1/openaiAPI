import openai
import os

#authentication stuff
openai.api_key = os.getenv("OPENAI_API_KEY")
engine = "text-davinci-003" #or "curie-001"

#Uses OpenAI to generate tags for a song that user inputs, with DaVinci 3 engine
def get_song_tags(song_title):
  prompt = f"Generate 5-7 one word tags (separated by commas) for this song that are in lowercase. Do not include anything else except the letters.'{song_title}'."
  response = openai.Completion.create(
      engine=engine,
      prompt=prompt,
      max_tokens=200,
      n=1,
      stop=None,
      temperature=0.75,
  )
  tags = response.choices[0].text.strip()
  return tags

#Uses OpenAI to make a playlist of songs that match the tags
def generate_playlist(tags):
  prompt=f"Generate a playlist of 10, real songs, that match these tags: '{tags}'"
  response = openai.Completion.create(
      engine=engine,
      prompt=prompt,
      max_tokens=100,
      n=1,
      stop=None,
      temperature=0.25,
  )
  playlist = response.choices[0].text.strip()
  return playlist