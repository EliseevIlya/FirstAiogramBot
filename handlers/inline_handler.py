from aiogram import Router
from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery

from keyboards.inline_kbs import inline_link_kb, inline_user_kb
from keyboards.main_keyboard import main_kb
from utils.fake_user import get_random_person

inline_router = Router()


@inline_router.message(F.text == '📖 О нас')
async def inline_handler(message: Message):
    await message.answer('Ссылки на автора', reply_markup=inline_link_kb())


@inline_router.message(F.text == '👤 Профиль')
async def inline_handler(message: Message):
    await message.answer('Профиль', reply_markup=inline_user_kb())


@inline_router.callback_query(F.data == 'get_user')
async def get_random_user(callback_query: CallbackQuery):
    await callback_query.answer("Будет сгененерирован случайный пользователь")
    user = get_random_person()
    reply = (
        f"👤 <b>Имя:</b> {user['name']}\n"
        f"🏠 <b>Адрес:</b> {user['address']}\n"
        f"📧 <b>Email:</b> {user['email']}\n"
        f"📞 <b>Телефон:</b> {user['phone_number']}\n"
        f"🎂 <b>Дата рождения:</b> {user['birth_date']}\n"
        f"🏢 <b>Компания:</b> {user['company']}\n"
        f"💼 <b>Должность:</b> {user['job']}\n"
    )
    await callback_query.message.answer(reply)


@inline_router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.delete()
    await callback_query.message.answer('Базовые функции', reply_markup=main_kb(callback_query.message.from_user.id))
