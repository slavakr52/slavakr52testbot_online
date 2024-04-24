from loader import dp, bot
from aiogram.types import CallbackQuery
from i_keyboards import cb_data, kb_back
from data import about_text

@dp.callback_query_handler(cb_data.filter(btn_data='btn_about'))
async def print_cb(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    mes_id = callback.message.message_id
    new_text = about_text
    await dp.bot.edit_message_text(chat_id=chat_id, message_id=mes_id, text=new_text, reply_markup=kb_back, parse_mode="Markdown")