from loader import dp, bot
from aiogram.types import CallbackQuery
from i_keyboards import cb_data, kb_main_menu
from data import main_menu_text

# @dp.callback_query_handler(cb_data.filter(btn_data='btn_main_menu'))
# async def print_cb(callback: CallbackQuery):
#    await bot.answer_callback_query(callback.id)
#    await bot.send_message(callback.from_user.id, '🏠 *Главное меню*\n'
#                           + 'С чем я смогу помочь:\n🔷 Могу то\n🔷 Могу это\n'
#                           + '🔷 Могу и то и это\n🔷 Могу всё', reply_markup=kb_main_menu, parse_mode="Markdown")
   
# @dp.callback_query_handler(cb_data.filter(btn_data='btn_start'))
# async def print_cb(callback: CallbackQuery):
#    await bot.answer_callback_query(callback.id)
#    await bot.send_message(callback.from_user.id, '🏠 *Главное меню*\n'
#                           + 'С чем я смогу помочь:\n🔷 Могу то\n🔷 Могу это\n'
#                           + '🔷 Могу и то и это\n🔷 Могу всё', reply_markup=kb_main_menu, parse_mode="Markdown")
   
@dp.callback_query_handler(cb_data.filter(btn_data='btn_back_to_main'))
async def print_cb(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    mes_id = callback.message.message_id
    new_text = main_menu_text
    await dp.bot.edit_message_text(chat_id=chat_id, message_id=mes_id, text=new_text, reply_markup=kb_main_menu, parse_mode="Markdown")

@dp.callback_query_handler(cb_data.filter(btn_data='btn_start'))
async def print_cb(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    mes_id = callback.message.message_id
    new_text = main_menu_text
    await dp.bot.edit_message_text(chat_id=chat_id, message_id=mes_id, text=new_text, reply_markup=kb_main_menu, parse_mode="Markdown")

