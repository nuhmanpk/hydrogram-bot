from .database import db
from .admin import add_user
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .buttons import HELP_BUTTONS, START_BUTTONS,ABOUT_BUTTONS,CLOSE_BUTTON
from .constants import START_TEXT,HELP_TEXT,ABOUT_TEXT

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message, cb=False):
    await add_user(message.from_user.id)
    # something here

@Client.on_message(filters.private & filters.command(["help"]))
async def help(bot, message, cb=False):
    await add_user(message.from_user.id)
    if cb:
        await message.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )

@Client.on_message(filters.private & filters.command(["about"]))
async def about(bot, message, cb=False):
    await add_user(message.from_user.id)
    text = ABOUT_TEXT.format((await bot.get_me()).username)
    if cb:
        await message.message.edit_text(
            text=text,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.reply_text(
            text=text,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )