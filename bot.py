import telebot
import time
import json
import requests
from tabulate import tabulate

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

def Male_info():
    response = requests.get('http://www.meteorology.gov.mv/fetchweather/Male')
    data = response.json()
    infos = tabulate([['Station: ', data["station_name"]], ['Humidity: ', data["humidity"]], ['Temperature: ', data["temp"]],
    ['Sunsets: ', data["sunset"]], ['Sunrise: ', data["sunrise"]], ['Description: ', data["description"]] ], headers=['Fields', 'Values'])

    return infos
def Male_new():
    response = requests.get('https://openweathermap.org/data/2.5/weather?q=maale,mv&appid=b6907d289e10d714a6e88b30761fae22')
    data = response.json()
    infos = tabulate([['Station: ', 'Maale'] , ['Humidity: ', data.get('main').get('humidity')] , ['Temperature: ', data.get('main').get('temp')]], headers=['Fields', 'Values'])

    return infos


@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.chat.title
    bot.reply_to(message, 'Welcome! To ' + str(username))

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'To use this bot please contact the admin @rootfs7')


@bot.message_handler(commands=['maaleinfo'])
def send_weather(message):
    info = Male_new()
    bot.reply_to(message, info)

@bot.message_handler(commands=['maaleinfomv'])
def send_weather(message):
    info = Male_info()
    bot.reply_to(message, info)



print("bot is Online!!")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
