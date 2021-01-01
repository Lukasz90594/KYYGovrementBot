# - *- coding: utf-8 - *-
import information, config
import time
from methods import commandList
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

app = Client(config.bot_username, bot_token=config.token)
mainMenu = ReplyKeyboardMarkup(
    [
        ['О KYY', 'Гражданины', 'ОР'],
        ['ЦОН', 'О боте', 'Конституция']
    ], resize_keyboard=True
)
konst_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Раздел I", callback_data='konst1'
            )
        ],
        [
            InlineKeyboardButton(
                "Раздел II", callback_data='konst2'
            )
        ],
        [
            InlineKeyboardButton(
                "Раздел III", callback_data='konst3'
            )
        ],
        [
            InlineKeyboardButton(
                "Раздел IV", callback_data='konst4'
            )
        ]
    ]
)
konst_back = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                'Назад', callback_data='konst_back'
            )
        ]
    ]
)


@app.on_callback_query()
def konst_resiver(client, callback_query):
    if callback_query.data == "konst1":
        client.edit_message_text(callback_query.message.chat.id, callback_query.message.message_id,
                                 information.konst1, reply_markup=konst_back)
    elif callback_query.data == "konst2":
        client.edit_message_text(callback_query.message.chat.id, callback_query.message.message_id,
                                 information.konst2, reply_markup=konst_back)
    elif callback_query.data == "konst3":
        client.edit_message_text(callback_query.message.chat.id, callback_query.message.message_id,
                                 information.konst3, reply_markup=konst_back)
    elif callback_query.data == "konst4":
        client.edit_message_text(callback_query.message.chat.id, callback_query.message.message_id,
                                 information.konst4, reply_markup=konst_back)
    if callback_query.data == "konst_back":
        client.edit_message_text(callback_query.message.chat.id, callback_query.message.message_id,
                                 information.konst, reply_markup=konst_menu)


@app.on_message(filters.command(commandList(["test"])) | filters.regex("test"))
def start(client, message):
    messageT = client.send_message(message.chat.id, "Тестовая хуйня. Через секунду")
    time.sleep(1)
    client.edit_message_text(messageT.chat.id, messageT.message_id, "Оно поменяет текст")


@app.on_message(filters.command(commandList(["start", "help"])) | filters.regex("О боте"))
def start(client, message):
    if message.chat.type == "private":
        client.send_message(message.chat.id, information.about_bot, reply_markup=mainMenu)
    else:
        client.send_message(message.chat.id, information.about_bot)
#    print(message)


@app.on_message(filters.command(commandList(["about"])) | filters.regex("О KYY"))
def start(client, message):
    if message.chat.type == "private":
        client.send_message(message.chat.id, information.about_KYY, reply_markup=mainMenu)
    else:
        client.send_message(message.chat.id, information.about_KYY)
#    print(message)


@app.on_message(filters.command(commandList(["or"])) | filters.regex("ОР"))
def start(client, message):
    if message.chat.type == "private":
        client.send_message(message.chat.id, information.or_inf, reply_markup=mainMenu)
    else:
        client.send_message(message.chat.id, information.or_inf)
#    print(message)


@app.on_message(filters.command(commandList(["citizens"])) | filters.regex("Гражданины"))
def start(client, message):
    if message.chat.type == "private":
        client.send_message(message.chat.id, information.citizens, reply_markup=mainMenu)
    else:
        client.send_message(message.chat.id, information.citizens)
#    print(message)


@app.on_message(filters.command(commandList(["con"])) | filters.regex("ЦОН"))
def start(client, message):
    if message.chat.type == "private":
        client.send_message(message.chat.id, information.con, reply_markup=mainMenu)
    else:
        client.send_message(message.chat.id, information.con)
#    print(message)


@app.on_message(filters.command(commandList(["konst"])) | filters.regex("Конституция"))
def start(client, message):
    client.send_message(message.chat.id, information.konst, reply_markup=konst_menu)
#    print(message)


app.run()
