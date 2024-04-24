from loader import dp
from aiogram.filters.command import Command
from aiogram.types import Message

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!")