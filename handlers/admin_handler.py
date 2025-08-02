import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline_kbs import admin_inline_kb
from keyboards.main_keyboard import main_kb

admin_router = Router()


@admin_router.message(F.text == '⚙️ Админ панель')
async def admin_kb(message: Message):
    await message.answer('Панель админа', reply_markup=admin_inline_kb())
