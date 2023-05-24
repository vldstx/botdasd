import configparser
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3


db = sqlite3.connect('support.db')
sql = db.cursor()


config = configparser.ConfigParser()
config.read('config.ini')

token = config.get('MAIN', 'bot_token')
logging = config.get('MAIN', 'logging')
save_logging = config.get('MAIN', 'save_logging')

bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

