from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_button = InlineKeyboardButton('⚙ Help', callback_data='help')
about_button = InlineKeyboardButton('About 🔰', callback_data='about')
close_button = InlineKeyboardButton('Close ✖️', callback_data='close')
home_button = InlineKeyboardButton('🏘 Home', callback_data='home')


START_BUTTONS = InlineKeyboardMarkup(
    [
        [help_button, about_button, close_button]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [home_button, about_button, close_button]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [home_button, help_button, close_button]
    ]
)

CLOSE_BUTTON = InlineKeyboardMarkup(
    [
        [close_button]
    ]
)
