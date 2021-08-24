import greet as g
import weather as w


message = g.greet_random()
weather = w.weather_get()

def daily(user):
  user_str = "<u>Good morning " + user + "</u> \n"
  break_str = "++++++++++++++++++++++++++++++++++++++++++++++\n"
  msg_str = "<b>Here is your random greeting of the day 🤓</b>\n" + message + " \n"
  weather_str = "<b>Weather</b>\n" + weather + " \n"
  final_str = user_str + break_str + msg_str + break_str + weather_str
  return final_str