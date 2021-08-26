import requests, json
meme_url = "https://meme-api.herokuapp.com/gimme/1"

def random_meme():
  response = requests.get(meme_url)
  x = response.json()
  data = x["memes"]
  meme = data[0]["url"]
  return meme
