import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender

from keyboards.inline_kbs import inline_link_kb, inline_user_kb, faq_inline_kb, faq_answer_kb
from keyboards.main_keyboard import main_kb
from utils.fake_user import get_random_person
from utils.temporary_db import get_answer

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


@inline_router.callback_query(F.data == 'base_home')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.answer("Переход к базовым функциям", show_alert=True)
    await callback_query.message.delete()
    await callback_query.message.answer('Базовые функции', reply_markup=main_kb(callback_query.from_user.id))


@inline_router.message(F.text.lower() == 'faq')
async def faq_handler(message: Message):
    await message.answer('FAQ', reply_markup=faq_inline_kb())


@inline_router.callback_query(F.data == 'faq')
async def faq_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('FAQ', reply_markup=faq_inline_kb())


@inline_router.callback_query(F.data.startswith('qst_'))
async def cmd_start(callback_query: CallbackQuery):
    await callback_query.answer()
    qst_id = int(callback_query.data.replace('qst_', ''))
    message = get_answer(qst_id)
    async with ChatActionSender.typing(bot=callback_query.bot, chat_id=callback_query.from_user.id):
        await asyncio.sleep(1.5)
        await callback_query.message.answer(message, reply_markup=faq_answer_kb())
