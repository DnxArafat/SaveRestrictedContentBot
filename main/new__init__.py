#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("24266722", default=None, cast=int)
API_HASH = config("5dd6bedd030fd733bb5997a1d62a9b2a", default=None)
BOT_TOKEN = config("7531297522:AAGHKt2RYE2GLnTocUnxrNNSNsdU-woMQhM", default=None)
SESSION = config("BQFyR-IAPg0pJs56iu2ummr_hjfiILPXHPey5RbIh4_whFE-J8ZYlfEmaWqATeX3PmzszFl2jNzOh0EN3VYxYudXLY-c35ilvekJOVEIjTwyGWNzONURrqSrXte1sUwXF1PdVorWu7Zt9Ka1i-0ZtwOhctLYLF0sDpmItYRq1PMN316QSf73yyJCoTJ6P-vy0fHLymUW63b4blFBISfjKhWlLbjPjG5hzGztzh9KJGkWTiDK_TZxZkr50s31Ps5bcdSfZ6T8xiaiTDvn2tpOccOCO1Olj5vgRfuxk-M-k9MjHZzJk7QpoEGJCMTrrEp4F-S14KL6o2kfwtcZy_SvMUyxTbHfIgAAAAGm6WZPAA", default=None)
FORCESUB = config("BinaryPaidLeaker", default=None)
AUTH = config("5091918803", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
