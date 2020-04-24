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
		markup1 = telebot.types.InlineKeyboardMarkup()
		markup1.add(telebot.types.InlineKeyboardButton(text='Раздел I. Госудаство', callback_data=1))
		markup1.add(telebot.types.InlineKeyboardButton(text='Раздел II. Гражданкий кодекс', callback_data=2))
		markup1.add(telebot.types.InlineKeyboardButton(text='Раздел III. Уголовно-админестративный кодекс', callback_data=3))
		markup1.add(telebot.types.InlineKeyboardButton(text='Раздел IV. Суды и правосудие ', callback_data=4))
		markup1.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=0))
		bot.send_message(message.chat.id, 'Выберите раздел Конституции:', reply_markup=markup1)


#Konstitucia's work
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='аааааа')
    answer = ''
    if call.data == '1':
        answer = 'ещё не написано'
    elif call.data == '2':
        answer = 'ещё не написано'
    elif call.data == '3':
        answer = 'ещё не написано'
    elif call.data == '4':
        answer = 'ещё не написано'

    bot.send_message(call.message.chat.id, answer)




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
	if message.text == 'Назад':
		bot.send_message(message.chat.id,'Домашнее меню:',reply_markup=keyboard1)
	if message.text == 'Раздел I. Госудаство':
		bot.send_message(message.chat.id,inforation.konst1,reply_markup=markup1)
	if message.text == 'Раздел II. Гражданкий кодекс':
		bot.send_message(message.chat.id,inforation.konst2,reply_markup=markup1)
	if message.text == 'Раздел III. Уголовно-админестративный кодекс':
		bot.send_message(message.chat.id,inforation.konst3,reply_markup=markup1)
	if message.text == 'Раздел IV. Суды и правосудие':
		bot.send_message(message.chat.id,inforation.konst4,reply_markup=markup1)