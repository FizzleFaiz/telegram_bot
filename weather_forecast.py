# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import os
import requests, json
from datetime import datetime,timedelta
import pytz

# Enter your API key here
api_key = os.getenv('weather')
# api_key = "Your_API_Key"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/forecast?"

# Give city name
city_name = "Singapore"
units = "metric"
cnt = "1"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + units + "&cnt=" + cnt



def weather_get():
    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    temp_list = x["list"]
    fore_y = temp_list[0]["main"]

    # Current Average Temp
    fore_avg = fore_y["temp"]
    str_fore = "\nAverage: " + str(fore_avg) 

    # Daily Min Temp
    fore_min = fore_y["temp_min"]
    str_min = "\nMinimum: " + str(fore_min) 

    # Daily Max Temp
    fore_max = fore_y["temp_max"]
    str_max = "\nMaximum: " + str(fore_max)

    # Get Current weather
    utc_now = pytz.utc.localize(datetime.utcnow() + timedelta(hours=3))
    sgt_timezone = utc_now.astimezone(pytz.timezone("Asia/Singapore"))
    # d_aware = timezone.localize(d)
    current_time = sgt_timezone.strftime("%B %d, %Y %H:%M:%S") 

    # # Morn Temp
    # fore_morn = fore_y["morn"]
    # str_morn = "\nMorning: " + str(fore_morn) + "\n"


    # # Night Temp
    # fore_night = fore_y["night"]
    # str_night = "\nNight: " + str(fore_night) + "\n"


    # # Eve Temp
    # fore_eve = fore_y["eve"]
    # str_eve = "Evening: " + str(fore_eve) + "\n"


    # print following values
    return("<b>Singapore Forecast Weather in °C by  " +
            current_time + "</b>"
            "\n---------------------------------" +
    str_fore + 
    str_min + 
    str_max + 
    # str_morn + 
    # str_night + 
    # str_eve +
            "\n---------------------------------" +
            "\n Please note this is a free API. Do not spam this :(")