import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from googletrans import Translator

numbers = [str(i) for i in range(999)]
TOKEN = '6048092727:AAFMG1FfUB1yloziuPyIII4ZFjM8xFJkneU'
bot = telebot.TeleBot(TOKEN)
translator = Translator()

def get_fact_num(message,number):
    print(number)
    text = requests.get(f'http://numbersapi.com/{number}').text
    bot.send_message(message.chat.id, translator.translate(text,dest='ru').text) 

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить факт о случайном числе'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'start', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id, 'Автор: Чивилёв Егор\nБот возвращает факт о данном числе')
 
@bot.message_handler(func=lambda s: 'случайном' in s.text)
def randomNumber(message):
    get_fact_num(message, random.randint(1,999))

@bot.message_handler(commands=numbers)
def getNum(message):
    get_fact_num(message,message.text.strip('/'))
#print(requests.get('http://numbersapi.com/1').text)

bot.infinity_polling()
