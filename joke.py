import requests, json
import pprint
meme_url = "https://v2.jokeapi.dev/joke/Any"

def random_joke(j_type):
  #'Single', 'Two Part','Random'
  if(j_type == 'Single'):
    j_url = '?type=single'
  elif(j_type == 'Two Part'):
    j_url = '?type=twopart'
  elif(j_type == 'Random'):
    j_url = ''
  response = requests.get(meme_url+j_url)
  x = response.json()

  # Getting type in json
  x_type = x["type"]
  if(x_type == 'single'):
    joke = x["joke"]
  elif(x_type == 'twopart'):
    setup = x["setup"] +"\n"
    delivery = x["delivery"]
    joke = setup + delivery
  return joke

def daily_joke():
  daily_url = "https://v2.jokeapi.dev/joke/Any?type=single"
  response = requests.get(daily_url)
  x = response.json()
  joke = x["joke"]
  return joke

