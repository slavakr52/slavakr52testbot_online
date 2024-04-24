#!/usr/bin/python3

# from aiogram import executor
from handlers import dp

async def on_start(_):
    print('Bot is running')

if __name__ == '__main__':
    dp.start_polling(dp, skip_updates=True, on_startup=on_start)