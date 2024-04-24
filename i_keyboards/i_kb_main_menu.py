from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback import cb_data


kb_main_menu = InlineKeyboardMarkup(row_width=2)

btn_main_menu = InlineKeyboardButton(text='🏠 Главное меню', callback_data=cb_data.new(btn_data='btn_main_menu'))
btn_about = InlineKeyboardButton(text='🧑Обо мне', callback_data=cb_data.new(btn_data='btn_about'))
btn_lections = InlineKeyboardButton(text='📖Лекции', callback_data=cb_data.new(btn_data='btn_lections'))
btn_request_examples = InlineKeyboardButton(text='🔍Примеры', callback_data=cb_data.new(btn_data='btn_request_examples'))
btn_contacts = InlineKeyboardButton(text='📞Контакты', callback_data=cb_data.new(btn_data='btn_contacts'))
btn_sign_up = InlineKeyboardButton(text='📆Записаться', callback_data=cb_data.new(btn_data='btn_sign_up'))

kb_main_menu.add(btn_about, btn_lections, btn_request_examples, btn_contacts, btn_sign_up)
