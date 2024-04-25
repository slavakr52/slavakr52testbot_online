from aiogram import Bot, Dispatcher
import os, logging

# логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
