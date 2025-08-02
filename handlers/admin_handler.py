import asyncio

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from filters.is_admin import IsAdmin
from keyboards.inline_kbs import admin_inline_kb, admin_settings_kb, faq_inline_kb
from keyboards.main_keyboard import main_kb
from utils.add_admin import add_admin
from utils.temporary_db import add_faq

admin_router = Router()


@admin_router.message(F.text == '⚙️ Админ панель')
async def admin_kb(message: Message):
    await message.answer('Панель админа', reply_markup=admin_inline_kb())


@admin_router.callback_query(F.data == 'admin_statistic', IsAdmin())
async def admin_statistic(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Статистика', reply_markup=admin_inline_kb())


@admin_router.callback_query(F.data == 'admin_settings', IsAdmin())
async def admin_settings(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text('Settings', reply_markup=admin_settings_kb())


@admin_router.callback_query(F.data == "add_admin", IsAdmin())
async def add_admin_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("🆔 Отправьте ID пользователя, которого нужно сделать админом.")
    await state.set_state("waiting_admin_id")
    await callback.answer()


@admin_router.message(StateFilter("waiting_admin_id"), IsAdmin())
async def add_admin_process(message: Message, state: FSMContext):
    user_id = message.text.strip()
    if not user_id.isdigit():
        await message.answer("❌ Это не число. Введите корректный ID.")
        return

    user_id = int(user_id)

    reply_message = add_admin(user_id)

    await message.answer(reply_message)
    await state.clear()


@admin_router.callback_query(lambda c: c.data == "add_question")
async def add_question_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text("📝 Введите текст вопроса:")
    await state.set_state("waiting_question_text")

""""
class AddAdmin(StatesGroup):
    waiting_admin_id = State()

await state.set_state(AddAdmin.waiting_admin_id)

@router.message(AddAdmin.waiting_admin_id)

"""


@admin_router.message(StateFilter("waiting_question_text"))
async def add_question_text(message: Message, state: FSMContext):
    await state.update_data(question_text=message.text)
    await message.answer("💬 Введите ответ на вопрос:")
    await state.set_state("waiting_question_answer")


@admin_router.message(StateFilter("waiting_question_answer"))
async def add_question_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    question_text = data["question_text"]
    answer_text = message.text

    new_id = add_faq(question=question_text, answer=answer_text)

    await message.answer(f"✅ Вопрос добавлен под ID `{new_id}`:\n\n"
                         f"**Вопрос:** {question_text}\n"
                         f"_Ответ:_ {answer_text}", parse_mode="MarkdownV2", reply_markup=admin_inline_kb())
    await state.clear()


# --- Список вопросов ---
@admin_router.callback_query(lambda c: c.data == "list_questions")
async def list_questions(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('FAQ', reply_markup=faq_inline_kb())

