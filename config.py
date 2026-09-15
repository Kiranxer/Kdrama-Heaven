# ---------------------------------------------------
# File Name: Config.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# YouTube: https://youtube.com/@MyselfNeon
# Created: 2025-10-21
# Last Modified: 2025-10-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import os
import logging

# --- Bot Credentials --- #
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8816625790:AAEfVekof8lzrSwBdTCiz-55k3FIl_bHlfk")
API_ID = int(os.environ.get("API_ID", "25462888"))
API_HASH = os.environ.get("API_HASH", "dcf629af1bc903b05a120354aaeeecaa")

OWNER_ID = int(os.environ.get("OWNER_ID", "7908181216"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://kxr0291_db_user:LLajBmeVn4w9BYXg@cluster0.pm768wv.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004497495303"))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003999122961"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1003999122961"))

FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "600"))  # auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# --- Admins --- #
ADMINS = [7908181216]
try:
    for x in os.environ.get("ADMINS", "7908181216").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER_ID)

# --- Bot Messages --- #
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == "True"

BOT_UPTIME_TEXT = "<b><i>Bᴏᴛ Uᴘᴛɪᴍᴇ</i> :</b>\n{uptime}"
USER_REPLY_TEXT = "<b><i>Baka !! You are not my Senpai 😏</i></b>"

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b><i>Hᴇʟʟᴏ {mention} ✨ \n\nI ᴀᴍ Pᴇʀᴍᴀɴᴇɴᴛ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.\n"
    "Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ <a href=\"tg://user?id=7908181216\">KiranXer</a>.\n\n"
    "Gᴇᴛ Rᴇᴅɪʀᴇᴄᴛᴇᴅ Fʀᴏᴍ Cᴏʀʀᴇᴄᴛ Lɪɴᴋs Tᴏ Gᴇᴛ Tʜᴇ Fɪʟᴇs 🖇️</i></b>"
)

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/i6wlle.png")

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b><i>🚫 Aᴄᴄᴇss Rᴇsᴛʀɪᴄᴛᴇᴅ 🚫\n\n"
    "Tᴏ Usᴇ Tʜɪs ʙᴏᴛ ᴀɴᴅ Aᴄᴄᴇss Fɪʟᴇs ᴏʀ Fᴇᴀᴛᴜʀᴇs, ʏᴏᴜ Nᴇᴇᴅ ᴛᴏ Bᴇ ᴀ Pᴀʀᴛ ᴏғ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ 🗓️</i></b>"
)

# --- Logging (Console only) --- #
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# --- Keep-Alive URL --- #
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
