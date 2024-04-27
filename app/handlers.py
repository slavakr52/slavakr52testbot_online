from aiogram import Router, F 
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import time

from data.db import Database
from app.middleware import Middleware1
from loader import bot
import app.keyboards as kb
import data.texts as my_text
import data.admins as admins

db = Database('data/database.db')

router = Router()
router.message.outer_middleware(Middleware1()) # проверки по сообщениям
router.callback_query.outer_middleware(Middleware1()) # проверки по коллбэкам

# FSM классы

class Sendall(StatesGroup):
    text = State()
    photo = State()

class Userinfo(StatesGroup):
    name = State()
    contact = State()
    question = State()

# хендлеры

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
    await message.answer(message.from_user.first_name + my_text.start, reply_markup=kb.start)

@router.message(Command('admin')) # вход в админку
async def admin(message: Message):
    if int(message.from_user.id) == int(admins.admin1):
        await message.answer(my_text.admin_menu, reply_markup=kb.admin)
    else:
        await message.answer(my_text.admin_denied, reply_markup=kb.go_back)

# коллбэки

@router.callback_query(F.data == 'menu')
async def go(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(my_text.main_menu, reply_markup=kb.main_menu, parse_mode='Markdown')

@router.callback_query(F.data == 'about')
async def about(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(my_text.about, reply_markup=kb.go_back)

@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(my_text.contacts, reply_markup=kb.go_back)

# FSM: Userinfo
    
@router.callback_query(F.data == 'write_us') # Userinfo 1 запрос имени
async def userinfo_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Userinfo.name)
    await callback.message.answer('Ваше имя:')

@router.message(Userinfo.name) # Userinfo 2 запрос номера
async def userinfo_2(message: Message, state: FSMContext):
    await state.update_data(name=message.text, user_id = message.from_user.id)
    await state.set_state(Userinfo.contact)
    await message.answer('Ваш номер телефона:')

@router.message(Userinfo.contact) # Userinfo 3 запрос текста
async def userinfo_3(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(Userinfo.question)
    await message.answer('Какой у вас вопрос?')

@router.message(Userinfo.question) # Userinfo 4 отправка админу
async def userinfo_4(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    data = await state.get_data()
    user_id = data['user_id']
    question = data['question']
    name = data['name']
    contact = data['contact']
    await bot.send_message(admins.admin1, f'🚩 Запрос от {user_id} 🚩\n\n'
                           + question + f'\n\nИмя: {name}'
                           + f'\nКонтактные данные: {contact}')
    await message.answer('Ваш вопрос принят! Свяжемся с вами в ближайшее время!', reply_markup=kb.go_back)
    await state.clear()

# FSM: Sendall (рассылка сообщений всем пользователям, админка)

@router.callback_query(F.data == 'admin_sendall') # Sendall 1 пишем текст
async def sendall_1(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(photo=None)
    await state.set_state(Sendall.text)
    await callback.message.answer('Введите текст, который необходимо отправить:')

@router.message(Sendall.text) # Sendall 2 прикрепляем картинку, если надо
async def sendall_2(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer('Нужно прикрепить картинку?', reply_markup=kb.admin_picture)

@router.callback_query(F.data == 'photo_yes') # Sendall 3 это если картинку надо
async def sendall_3(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Sendall.photo)
    await callback.message.answer('Отправьте нужную картинку')

@router.message(Sendall.photo) # Sendall 4 картинка загружена
async def sendall_4(message: Message, state: FSMContext):
    try:
        await state.update_data(photo=message.photo[-1].file_id)
        await message.answer('Картинка загружена', reply_markup=kb.admin_picture_ok)
    except TypeError:
        print ("Admin entering text instead of photo..")
    
@router.callback_query(F.data == 'preview') # Sendall 5 предпросмотр
async def sendall_5(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Предпросмотр', show_alert=True)
    data = await state.get_data()
    if data['photo']:
        await callback.message.answer_photo(photo=data['photo'],
                                            caption=data['text'],
                                            reply_markup=kb.admin_message)
    else:
        await callback.message.answer(data['text'],
                                      reply_markup=kb.admin_message)
        
@router.callback_query(F.data == 'admin_accept') # 
async def sendall_6(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Рассылка запущена')
    data = await state.get_data()
    users = db.get_users()
    for row in users:
        time.sleep(0.1)
        try:
            if data['photo']:
                await bot.send_photo(row[0],
                                     photo=data['photo'],
                                     caption=data['text'])
            else:
                await bot.send_message(row[0], 
                                       data['text'])
            if int(row[1]) != 1:  # если сообщение дошло до юзера с active=0, то active=1
                db.set_active(row[0], 1)
        except:
            db.set_active(row[0], 0) # если не дошло, то active=0
    await callback.message.answer('⚠️ Рассылка завершена', reply_markup=kb.go_back)
    await state.clear()

@router.callback_query(F.data == 'admin_cancel') # Sendall отмена
async def sendall_0(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(f'Все действия отменены', reply_markup=kb.go_back)
    await state.clear()

# всеядный хендлер

@router.message()
async def mes_all(message: Message):
    await message.answer(message.from_user.first_name + my_text.incorrect, reply_markup=kb.go_back)
   






