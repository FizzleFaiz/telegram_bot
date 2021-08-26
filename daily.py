import greet as g
import weather as w
import inspire as i


g_message = g.greet_random()
i_message = i.random_quote()
weather = w.weather_get()

def daily(user):
  user_str = "<u>Good morning " + user + "</u> \n"
  break_str = "++++++++++++++++++++++++++++++++++++++++++++++\n"
  g_msg_str = "<b>Random greeting of the day 🤓</b>\n" + g_message + " \n"
  i_msg_str = "<b>Random quote of the day 👑</b>\n" + i_message + " \n"
  weather_str = "<b>Weather</b>\n" + weather + " \n"
  final_str = user_str + break_str + g_msg_str + break_str + i_msg_str + break_str + weather_str
  return final_str

def schedule_daily():
  user_str = "Good morning Chloe and Faiz" + "\n"
  break_str = "++++++++++++++++++++++++++++++++++++++++++++++\n"
  g_msg_str = "Random greeting of the day 🤓\n" + g_message + " \n"
  i_msg_str = "Random quote of the day 👑\n" + i_message + " \n"
  weather_str = "Weather\n" + weather + " \n"
  final_str = user_str + break_str + g_msg_str + break_str + i_msg_str + break_str + weather_str
  return final_str