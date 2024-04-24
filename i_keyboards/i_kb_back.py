from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import cb_data


kb_back = InlineKeyboardMarkup(row_width=2)

btn_back_to_main = InlineKeyboardButton(text='🏠 Назад в главное меню', callback_data=cb_data.new(btn_data='btn_back_to_main'))

kb_back.add(btn_back_to_main)
