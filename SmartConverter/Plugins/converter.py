"""
This Bot Was Developed By The Owner Of @StrawHat_Network.
Join his network and support him.
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
import shutil
import time
from config import Config 
from SmartConverter.Tools.progress import ( TimeFormatter,
  progress_for_pyrogram
)
import subprocess
import asyncio
from .. import TGBot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from SmartConverter.Plugins.helper import *


@TGBot.on_message(filters.incoming & (filters.video | filters.document))
async def pdf_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
    await message.reply_text("π· No Outsider Allowed β οΈ\n\nThis Bot is For Private Use Only.")
    return
  
  await message.reply_text(
    text="Sα΄Κα΄α΄α΄ TΚα΄ Fα΄Κα΄α΄α΄ Yα΄α΄ Wα΄Ι΄Ι΄α΄ Cα΄Ι΄α΄ α΄Κα΄",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("β«πΏπ³π΅β«", callback_data="pdf"),
          InlineKeyboardButton("β«π΄πΏππ±β«", callback_data="epub"),
          InlineKeyboardButton("β«π²π±πβ«", callback_data="cbz")
        ],
        [
          InlineKeyboardButton("β«π³πΎπ²πβ«",callback_data="docx"),
          InlineKeyboardButton("β«πΌπΎπ±πΈβ«", callback_data="doc"),
          InlineKeyboardButton("β«πππβ«", callback_data="txt")
        ],
        [
          InlineKeyboardButton("β«ππΈπ³π΄πΎ πππΈπ»πβ«", callback_data="video_file")],
      ],
    ),
    quote=True,
    parse_mode="markdown"
  )
  
  
