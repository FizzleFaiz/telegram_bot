import os
import telebot
import random
import greet as g
import weather_forecast as w
import spotify as s
import daily as d

# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 

# getMe

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY,parse_mode ="HTML")

#Retrieve Spotify WebHook
# setWebhook
# bot.set_webhook(url="https://fa87293c4021a006f111402e82374aec.m.pipedream.net")

# To display commands associated with this bot
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 
    """ Hello you have activated the Help function :)
        Here are the commands to guide you along
        /help - display this message duh
        /greet - Display random greetings
        /forecast - 3 Hour Weather Forecast for Singapore
        /daily - Daily Greetings and Current Weather
        /spotify - Spotify (WIP)""")

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

# To display Spotify playlist
@bot.message_handler(commands=['spotify'])
def spotify(message):
    bot.send_message(message.chat.id, s.return_playlist())


bot.polling()


