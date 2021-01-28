from telethon import TelegramClient, events, functions
from telethon.tl.custom import Button
import information, config
import asyncio
from methods import *
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 1660159
api_hash = '6e583efbc76417b8bbcfe215d7462126'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=config.token)

main_menu = [
    [Button.text('О KYY', resize=True), Button.text('Паспорт'), Button.text('ОР')],
    [Button.text('ЦОН'), Button.text('О боте'), Button.text('Конституция')]
]
konst_menu = [
    [Button.inline("Раздел I", data='konst1')],
    [Button.inline("Раздел II", data='konst2')],
    [Button.inline("Раздел III", data='konst3')],
    [Button.inline("Раздел III", data='konst3')]
]
konst_back = [
    [Button.inline('Назад', data='konst_back')]
]
con_menu = [
    [Button.inline('Поменять псевдоним', data='ch_alias')]
]


@client.on(events.CallbackQuery)
async def konst_resiver(event):
    if event.data == b"konst1":
        await event.edit(information.konst1, buttons=konst_back)
    elif event.data == b"konst2":
        await event.edit(information.konst2, buttons=konst_back)
    elif event.data == b"konst3":
        await event.edit(information.konst3, buttons=konst_back)
    elif event.data == b"konst4":
        await event.edit(information.konst4, buttons=konst_back)
    if event.data == b"konst_back":
        await event.edit(information.konst, buttons=konst_menu)
    if event.data == b'ch_alias':
        # print(event.stringify())
        await event.edit("Отправьте ваш новый псевдоним (16 символов)")
        chat_id = (await (await event.get_message()).get_chat()).id
        try:
            async with client.conversation(chat_id, timeout=120) as cv:
                messageT = await cv.send_message("У вас есть 120 секунд что бы ответить")
                alias = (await cv.get_response()).raw_text
                if len(alias) > 16:
                    await event.reply(f"Псевдоним ```{alias}``` \n слишком дилнное(16 символов максимум)")
                    return
                await messageT.delete()
                new_text = f"Ваш новый псевдоним {alias}"
            await event.edit(new_text)
            update_alias(chat_id, alias)
            if get_status(chat_id) >= 1:
                await client.edit_admin(config.group_id,
                                        chat_id,
                                        change_info=True,
                                        delete_messages=None,
                                        ban_users=None,
                                        invite_users=None,
                                        pin_messages=None,
                                        add_admins=None,
                                        manage_call=True,
                                        title=get_alias(chat_id)
                                        )
                await event.edit(new_text + "\nПсевдоним в группе так же обновлён")
        except asyncio.exceptions.TimeoutError:
            await event.edit("Время вышло! Попробуйте снова")
            await messageT.delete()

@client.on(events.NewMessage(pattern="test"))
async def hui(event):
    await event.reply("Отправьте ваш новый псевдоним (16 символов)")
    async with client.conversation(event.chat_instance) as cv:
        await cv.send_message("У вас есть 30 секунд что бы ответить")
        alias = await cv.get_response().raw_text
        if len(alias) > 16:
            event.reply(f"Псевдоним ```{alias}``` \n слишком дилнное(16 символов максимум)")
            return
    await event.edit(f"Ваш новый псевдоним {alias}")


@client.on(events.NewMessage(pattern=commands(['start', 'help']) + "|" + "^О боте$"))
async def start(event):
    sender = await event.get_sender()
    buttons = main_menu if event.is_private else None
    await event.reply(information.about_bot, buttons=buttons)
    if not registered(sender.id):
        create_user(sender.id)
        await event.reply(information.registration.format(name=sender.first_name), buttons=buttons)


@client.on(events.NewMessage(pattern=commands(['about']) + "|" + "^О KYY$"))
async def about(event):
    buttons = main_menu if event.is_private else None
    await event.reply(information.about_KYY, buttons=buttons)


@client.on(events.NewMessage(pattern=commands(['or']) + "|" + "^ОР$"))
async def or_command(event):
    sender = await event.get_sender()
    buttons = main_menu if event.is_private else None
    if len(event.raw_text.split()) < 2:
        await event.reply(f"Ваши Очки Репутации: {get_rp(sender.id)}", buttons=buttons)
    else:
        try:
            or_value = int(event.raw_text.split()[1])
        except ValueError:
            await event.reply("Это должно быть число!")
            return
        if event.is_reply:
            reply_message = await event.get_reply_message()
            reply_sender = await reply_message.get_sender()
            if get_status(sender.id) >= 2:
                change_rp(reply_sender.id, or_value)
                await event.reply("Очки Репутации были обновлёны!")
            else:
                await event.reply("У вас не достаточно прав!")
        else:
            await event.reply("О ком собственна идёт речь?")


@client.on(events.NewMessage(pattern=commands(['passport']) + "|" + "^Паспорт$"))
async def passport(event):
    sender = await event.get_sender()
    buttons = main_menu if event.is_private else None
    await event.reply(information.passport.format(
        id=sender.id,
        first=sender.first_name if sender.first_name is not None else "",
        last=sender.last_name if sender.last_name is not None else "",
        alias=get_alias(sender.id),
        status=get_status(sender.id),
        rp=get_rp(sender.id),
        balance=get_balance(sender.id)
    ), buttons=buttons)


@client.on(events.NewMessage(pattern=commands(['get_passport'])))
async def passport(event):
    sender = await event.get_sender()
    if event.is_reply:
        if get_status(sender.id) >= 2:
            reply_message = await event.get_reply_message()
            reply_sender = await reply_message.get_sender()
            await event.reply(information.passport.format(
                id=reply_sender.id,
                first=reply_sender.first_name if reply_sender.first_name is not None else "",
                last=reply_sender.last_name if reply_sender.last_name is not None else "",
                alias=get_alias(reply_sender.id),
                status=get_status(reply_sender.id),
                rp=get_rp(reply_sender.id),
                balance=get_balance(reply_sender.id)
            ))
        else:
            await event.reply("У вас не достаточно прав!")
    else:
        await event.reply("О ком собственна идёт речь?")


@client.on(events.NewMessage(pattern=commands(['con']) + "|" + "^ЦОН$"))
async def con(event):
    buttons = con_menu if event.is_private else None
    text = information.con if event.is_private else "ЦОН доступен только в приватном чате с ботом"
    await event.reply(text, buttons=buttons)


@client.on(events.NewMessage(pattern=commands(['konst']) + "|" + "^Конституция$"))
async def konst(event):
    buttons = konst_menu
    await event.reply(information.konst, buttons=buttons)


@client.on(events.NewMessage(pattern=commands(['up_status'])))
async def up_status(event):
    sender = await event.get_sender()
    if len(event.raw_text.split()) < 2:
        await event.reply("Вы не верно ввели команду!")
    else:
        try:
            status_value = int(event.raw_text.split()[1])
        except ValueError:
            event.reply("Это должно быть число!")
            return
        if event.is_reply:
            reply_message = await event.get_reply_message()
            reply_sender = await reply_message.get_sender()
            if get_status(sender.id) >= 2 and (reply_sender.id != int(config.admin_id)) and status_value <= 2:
                update_status(reply_sender.id, status_value)
                await event.reply("Статус был обновлён!")
            else:
                await event.reply("У вас не достаточно прав!")
        else:
            event.reply("О ком собственна идёт речь?")


@client.on(events.NewMessage(pattern=commands(['f', 'forward'])))
async def forward(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
        if len(event.raw_text.split()) < 2:
            await event.reply(reply_message)
        else:
            await event.reply("Функция пересылания нескольких сообщений в разработке...")
    else:
        await event.reply("О чём собственна идёт речь?")


@client.on(events.NewMessage(pattern=commands(['b', 'balance'])))
async def balance(event):
    sender = await event.get_sender()
    if len(event.raw_text.split()) < 2:
        await event.reply(f"Ваш баланс: {get_balance(sender.id)}")
    else:
        try:
            balance_value = int(event.raw_text.split()[1])
        except ValueError:
            await event.reply("Это должно быть число!")
            return
        if event.is_reply:
            reply_message = await event.get_reply_message()
            reply_sender = await reply_message.get_sender()
            if can_change_balance(sender.id, -balance_value) and balance_value >= 0:
                change_balance(sender.id, -balance_value)
                change_balance(reply_sender.id, balance_value)
                await event.reply(f"Вы упешно перевели {balance_value} на счёт {reply_sender.first_name}! \
                \n У вас осталось {get_balance(sender.id)}")
            elif balance_value < 0:
                await event.reply("Воровать плохо!")
            else:
                await event.reply(f"У вас недостаточно сретств, баланс: {get_balance(sender.id)}")
        else:
            await event.reply("Кому вы хотели перевести?")


@client.on(events.NewMessage(pattern=commands(['init'])))
async def initial(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    print(chat.id)
    if get_status(sender.id) >= 2:
        if not event.is_group:
            event.reply("Работает только в супергруппе!")
            return
        citizens = get_all_citizens()
        for i in range(len(citizens)):
            if str(citizens[i][1]) != config.admin_id:
                await client.edit_admin(chat.id,
                                        citizens[i][1],
                                        change_info=True,
                                        delete_messages=None,
                                        ban_users=None,
                                        invite_users=None,
                                        pin_messages=None,
                                        add_admins=None,
                                        manage_call=True,
                                        title=get_alias(citizens[i][1])
                                        )
        await event.reply("Инициализация завершена!")
    else:
        await event.reply("У вас недостаточно прав!")


print("Started working...")
client.run_until_disconnected()
