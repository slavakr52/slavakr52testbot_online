from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import cb_data


kb_start = InlineKeyboardMarkup(row_width=3)

btn_start = InlineKeyboardButton(text='Погнали!', callback_data=cb_data.new(btn_data='btn_start'))

kb_start.add(btn_start)