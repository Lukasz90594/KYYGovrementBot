from pyrogram import Client
import config

app = Client(config.bot_username, bot_token=config.token)


def commandList(commands, bot_username=config.bot_username):
    commandsCopy = commands.copy()
    for i in commands:
        commandsCopy.append(i + "@" + bot_username)
    return commandsCopy

