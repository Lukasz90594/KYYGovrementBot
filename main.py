# - *- coding: utf-8 - *-

import telebot
from telebot import types
import inforation
import config

print(config.admin_id)
bot = telebot.TeleBot(config.Token)

#keyboard
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('о KYY', 'Гражданины', 'ОР')
keyboard1.row('ЦОН', 'о боте', 'Конституция')

#start message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, inforation.about_bot, reply_markup=keyboard1)

@bot.message_handler(content_types= ['text'])
def chatting(message):
	if message.text == 'о KYY':
		bot.send_message(message.chat.id, inforation.about_KYY)
	elif message.text == 'Гражданины':
		bot.send_message(message.chat.id, 'Пока что в разработке')
	elif message.text == 'ОР':
		bot.send_message(message.chat.id, 'Пока что в разработке')
	elif message.text == 'ЦОН':
		bot.send_message(message.chat.id, 'Пока что в разработке')
	elif message.text == 'о боте':
		bot.send_message(message.chat.id, inforation.about_bot)
	elif message.text == 'Конституция':
		markup1 = telebot.types.ReplyKeyboardMarkup()
		markup1.row(telebot.types.KeyboardButton(text='Раздел I. Госудаство'), telebot.types.KeyboardButton(text='Раздел II. Гражданкий кодекс'))
		markup1.row(telebot.types.KeyboardButton(text='Раздел III. Уголовно-админестративный кодекс'))
		markup1.row(telebot.types.KeyboardButton(text='Раздел IV. Суды и правосудие'))
		markup1.row(telebot.types.KeyboardButton(text='Назад'))
		bot.send_message(message.chat.id, 'Выберите раздел Конституции:', reply_markup=markup1)
    #Конституция
	if message.text == 'Назад':
		bot.send_message(message.chat.id,'Домашнее меню:',reply_markup=keyboard1)
	elif message.text == 'Раздел I. Госудаство':
		bot.send_message(message.chat.id,inforation.konst1)
	elif message.text == 'Раздел II. Гражданкий кодекс':
		bot.send_message(message.chat.id,inforation.konst2)
	elif message.text == 'Раздел III. Уголовно-админестративный кодекс':
		bot.send_message(message.chat.id,inforation.konst3)
	elif message.text == 'Раздел IV. Суды и правосудие':
		bot.send_message(message.chat.id,inforation.konst4)




#bots work
bot.polling(none_stop=True, interval=0)