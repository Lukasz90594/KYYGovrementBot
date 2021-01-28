if event.data == 'ch_alias':
    await event.edit("Отправьте ваш новый псевдоним (16 символов)")
    text = client.conversation(event.chat_instance).get_response()
    while not len(text.raw_text) > 16:
        event.reply(f"Псевдоним ```{text.raw_text}``` \n слишком дилнное(16 символов максимум)")
    await event.edit(f"Ваш новый псевдоним {text.raw_text}")
    print(event)
    update_alias(callback_query.from_user.id, answer.text)
    if get_status(event.get_message().from_user.id) >= 1:
        await update_alias_group(callback_query.from_user.id, config.group_id, client)
        await callback_query.edit_message_text("Псевдоним в группе так же обновлён")
    else:
        await callback_query.edit_message_text(f"Псевдоним ```{answer.text}``` \n слишком дилнное(16 символов "
                                               f"максимум)")


@client.on(events.NewMessage(pattern=commands(['__init__'])))
async def initial(event):
    sender = await event.get_sender()
    if get_status(sender.id) >= 2:
        if not event.is_group:
            event.reply("Работает только в супергруппе!")
            return
        rights = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=True,
            ban_users=None,
            delete_messages=None,
            pin_messages=True,
            edit_messages=None
        )
        citizens = get_all_citizens()
        for i in range(len(citizens)):
            if str(citizens[i][1]) != config.admin_id:

    else:
        await event.reply("У вас недостаточно прав!")
