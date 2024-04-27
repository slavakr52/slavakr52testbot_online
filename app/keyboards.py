from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать работу', callback_data='menu')]
])

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🧑 Обо мне', callback_data='about'), InlineKeyboardButton(text='📞 Контакты', callback_data='contacts')],
    [InlineKeyboardButton(text='🌐 Перейти на сайт', url='https://mail.ru/')],
    [InlineKeyboardButton(text='💬 Задать вопрос', callback_data='write_us')]
])

go_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='menu')]
])

user_phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажмите на кнопку ниже')

admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Общая рассылка', callback_data='admin_sendall')],
    [InlineKeyboardButton(text='Написать сообщение', callback_data='admin_sendone')],
    [InlineKeyboardButton(text='Статистика', callback_data='admin_statistics')],
    [InlineKeyboardButton(text='Выход', callback_data='menu')]
])

admin_mess_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить', callback_data='admin_accept_one')],
    [InlineKeyboardButton(text='Отмена', callback_data='admin_cancel')]
])

admin_mess_all = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить', callback_data='admin_accept_all')],
    [InlineKeyboardButton(text='Отмена', callback_data='admin_cancel')]
])

admin_picture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='photo_yes')],
    [InlineKeyboardButton(text='Нет', callback_data='preview')]
])

admin_picture_ok= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='preview')]
])
