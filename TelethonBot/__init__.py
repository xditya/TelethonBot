# By < @xditya >
# // @BotzHub //

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

BotzHub = TelegramClient('BotzHub', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 