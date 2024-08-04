from .database import db
from .admin import add_user
from hydrogram import Client
from hydrogram.types import InlineKeyboardMarkup
from .constants import (
    START_TEXT,
    HELP_TEXT,
    ABOUT_TEXT
)
from .buttons import (
    HELP_BUTTONS, 
    START_BUTTONS, 
    ABOUT_BUTTONS,
    CLOSE_BUTTON
)


@Client.on_callback_query()
async def cb_data(_, message):
    await add_user(message.from_user.id)
    if message.data == "home":
        await message.message.delete()
        message = message.message
        await message.reply_text(
        text=START_TEXT,
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True,
        )
    elif message.data == "help":
        await message.message.delete()
        message = message.message
        await message.reply_text(
        text=HELP_TEXT,
        reply_markup=HELP_BUTTONS,
        disable_web_page_preview=True,
        quote=True,
        )
    elif message.data == "about":
        await message.message.delete()
        message = message.message
        await message.reply_text(
        text=ABOUT_TEXT,
        reply_markup=ABOUT_BUTTONS,
        disable_web_page_preview=True,
        quote=True,
        )
    elif message.data == "close":
        await message.message.delete()
