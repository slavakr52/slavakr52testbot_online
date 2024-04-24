from loader import dp
from aiogram.types import Message

@dp.message()
async def mes_all(message: Message):
    await message.answer(f'{message.from_user.first_name}, не знаю что с этим делать. Воспользуйся кнопками в главном меню')