import os
import telebot
## external modules
import greet as g
import weather_forecast as w
import daily as d
import spotify as s
import troll as t
import inspire as i
## external modules
import spotipy
import requests, json
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from telegram import ReplyKeyboardMarkup
from telebot import types
from datetime import datetime
import pprint
# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 

# getMe

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY,parse_mode ="HTML")


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
client_id = os.getenv('spotify_client_id')
client_secret = os.getenv('spotify_client_secret')

auth_manager = SpotifyClientCredentials(client_id,client_secret)
# auth_manager = SpotifyOAuth(client_id=client_id,
#                                                client_secret=client_secret,
#                                                redirect_uri="YOUR_APP_REDIRECT_URI",
#                                                scope="playlist-read-private")
sp = spotipy.Spotify(auth_manager=auth_manager)


# To display commands associated with this bot
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 
    """ Hello you have activated the Help function :)
        Here are the commands to guide you along
        /help - Display this message duh
        /greet - Display random greetings
        /forecast - 3 Hour Weather Forecast for Singapore
        /daily - Daily Greetings and Current Weather
        /troll - Display Random Troll Messages
        /inspire - Display Random Inspirational Quotes
        ---------------Spotify---------------
        /sp_a - Spotify Artist Of the Day
        /sp_p - Spotify Featured Playlists
        /sp_s - Spotify Search
        /sp_up - Spotify Show Faiz Top 10 Playlist""")

# To display random greeting :D
@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, g.greet_random())

# To display daily forecast weather
@bot.message_handler(commands=['forecast'])
def forecast(message):
    bot.send_message(message.chat.id, w.weather_get())

# To display current weather and random greeting
@bot.message_handler(commands=['daily'])
def daily(message):
    bot.send_message(message.chat.id, d.daily(message.from_user.first_name))

# To display random troll
@bot.message_handler(commands=['troll'])
def troll(message):
    bot.send_message(message.chat.id, t.troll_random())

# To display random inspirational quotes
@bot.message_handler(commands=['inspire'])
def inspire(message):
    bot.send_message(message.chat.id, i.random_quote())

# To display random inspirational quotes
@bot.message_handler(commands=['inspire'])
def inspire(message):
    bot.send_message(message.chat.id, i.random_quote())

# To display Spotify playlist
@bot.message_handler(commands=['sp_a'])
def choose_vibe(message):
  try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Chill', '80s')
        msg = bot.reply_to(message, 'Choose your <b>Vibe</b> for today', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_artist)
  except Exception as e:
        bot.reply_to(message, 'oooops') 

def choose_artist(message):
  try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vibe = message.text
        if(vibe == u'Chill'):
          for key in s.chill_dict:
            markup.add(key)
        elif(vibe == u'80s'):
          for key in s.eight_dict:
            markup.add(key)
        msg = bot.reply_to(message, 'Choose your <b>Artist</b> of the day', reply_markup=markup)
        bot.register_next_step_handler(msg, show_songs)
  except Exception as e:
        bot.reply_to(message, 'oooops') 

def show_songs(message):
  artist = message.text
  if artist in s.chill_dict.keys():
    artist_id = s.chill_dict.get(artist)
  elif artist in s.eight_dict.keys():
    artist_id = s.eight_dict.get(artist)
  results = sp.artist_top_tracks(artist_id)

  bot.send_message(message.chat.id, "Showing the Top 10 Songs for <b> "
  + artist + "</b>")

  for track in results['tracks'][:10]:
    spotify_link = track['external_urls']['spotify']
    bot.send_message(message.chat.id,spotify_link)
    
# To display Spotify playlist
@bot.message_handler(commands=['sp_p'])
def featured_playlist(message):
  try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        # TODO: More countires soon
        markup.add('Singapore', 'United States')
        msg = bot.reply_to(message, 'Featured Playlists under: (Pick an option)', reply_markup=markup)
        bot.register_next_step_handler(msg, show_playlist)
  except Exception as e:
        bot.reply_to(message, 'oooops')

def show_playlist(message):
  country = message.text
  code = s.country_code.get(country)
  response = sp.featured_playlists(country=code,limit = 10)
  bot.send_message(message.chat.id,"<b>" +response['message'] + "</b>")
  pprint.pprint(response)
  while response:
    playlists = response['playlists']
    for i, item in enumerate(playlists['items']):
      link = item['external_urls']['spotify']
      bot.send_message(message.chat.id, link)

    if playlists['next']:
        response = sp.next(playlists)
    else:
        response = None

# To search songs based on query
@bot.message_handler(commands=['sp_s'])
def search(message):
  try:
        msg = bot.reply_to(message, 'What do you want to search for?')
        bot.register_next_step_handler(msg, result_search)
  except Exception as e:
      bot.reply_to(message, 'oooops')

def result_search(message):
  search_str = message.text
  result = sp.search(search_str,limit =1,type="track",market='SG')
  tracks = result['tracks']
  track_item = tracks['items']
  album = track_item[0]
  spotify_link = album['external_urls']['spotify']
  bot.send_message(message.chat.id,spotify_link)

# To recommend
@bot.message_handler(commands=['sp_up'])
def user_playlist(message):
  playlists = sp.user_playlists(s.user,limit=10)
  pprint.pprint(playlists['items'])
  while playlists:
      for i, playlist in enumerate(playlists['items']):
        bot.send_message(message.chat.id,playlist['external_urls']['spotify'])
          # bot.send_message(message.chat.id,("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name'])))
      if playlists['next']:
          playlists = sp.next(playlists)
      else:
          playlists = None


bot.polling()

