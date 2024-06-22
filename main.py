"""
==========================================
 Title:        Pyrogram Bot Template
 Description:  Template for creating a Pyrogram bot.
 Author:       Nuhman (https://github.com/nuhmanpk)
 Created:      22-Jun-2024
 License:      MIT License
==========================================
"""

import os
from pyrogram import Client


Bot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    plugins = dict(root="bot")
)


Bot.run(print('Bot is Cooking...'))
