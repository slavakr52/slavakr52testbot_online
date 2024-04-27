from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

user_phone = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить номер', )]
])

admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассылка всем', callback_data='admin_sendall')],
    [InlineKeyboardButton(text='Рассылка одному', callback_data='admin_sendone')],
    [InlineKeyboardButton(text='Заблокировать пользователя', callback_data='admin_block')],
    [InlineKeyboardButton(text='Выход', callback_data='menu')]
])

admin_message = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить', callback_data='admin_accept')],
    [InlineKeyboardButton(text='Отмена', callback_data='admin_cancel')]
])

admin_picture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='photo_yes')],
    [InlineKeyboardButton(text='Нет', callback_data='preview')]
])

admin_picture_ok= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='preview')]
])