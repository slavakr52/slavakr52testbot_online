from loader import dp, bot
from aiogram.types import Message
from config import admin_id
from i_keyboards import kb_start

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    # print(message.from_user.id)
    await message.answer(f'{message.from_user.first_name}, привет)\nЭто тестовый бот. Начнём?', reply_markup=kb_start)
    # await bot.send_message(chat_id=admin_id, text=f'{message.from_user.first_name}, мне только что написали start, держу в курсе')