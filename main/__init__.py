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
SESSION = config("BQFyR-IAxdA75TqBGb52ugjkiykxEJLnoEUc09a38e0VkDRXnlnb2wwz57Y8dbVmXwaUq_9jxZRqThdus6wKOJe7JyTP8gEdfvszybIkwl8BT5ap0qHu1XWL4utsnhb8NbvymVkjW3oTKUuMXsejv576w0_844QtrFdp-q_Qs1MAykt6pRC7sYeXXC6Lq7b-AanD5A3j8gl72gyU4Wk-Ie4tvHNRZNh-wzV7uMa8aMvkLGBXrQUZkDHv30GQBGDEbxcVGG6hZzo3jt19nGNK_Vn7_mVyrOHm0iiqEnbfjHshagSM5Cr7VN-T6IsxJjz43ffUQfDRDPp7jT0Why5KbC0MQCMSmAAAAAGm6WZPAA", default=None)
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
