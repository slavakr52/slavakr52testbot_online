from loader import dp
from aiogram.types import Message
from i_keyboards import kb_back

@dp.message_handler()
async def mes_all(message: Message):
    await message.answer(f'{message.from_user.first_name}, не знаю что с этим делать. Воспользуйся кнопками в главном меню', reply_markup=kb_back)