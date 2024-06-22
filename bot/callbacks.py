from .database import db
from .admin import add_user
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from .commands import start, help, about


@Client.on_callback_query()
async def cb_data(_, message):
    await add_user(message.from_user.id)
    if message.data == "home":
        await start(_, message, cb=True)
    elif message.data == "help":
        await help(_, message, cb=True)
    elif message.data == "about":
        await about(_, message, cb=True)
    elif message.data == "close":
        await message.message.delete()