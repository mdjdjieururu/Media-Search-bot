import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, START_IMG 
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴, url=f"https://t.me/im_odiyan"),
                    InlineKeyboardButton(🍁ʙᴏᴛ ɢʀᴏᴜᴘ🍁, url=f"https://t.me/Movie_factorys")
                 ],[
                    InlineKeyboardButton(🍿ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ🍿, url=f"https://t.me/joinchat/x6V1RmEmmGBhMjQ1")
            ]
          ]
        ),
        reply_to_message_id=message.message_id
    )
