from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.temporary_db import questions


def inline_link_kb() -> InlineKeyboardMarkup:
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой хабр", url='https://github.com/EliseevIlya')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=gghostwar')],
        [InlineKeyboardButton(text="Яндекс Музыка", web_app=WebAppInfo(url="https://music.yandex.ru/"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def inline_user_kb() -> InlineKeyboardMarkup:
    inline_kb_list = [
        [InlineKeyboardButton(text='Получить пользователя', callback_data='get_user')],
        [InlineKeyboardButton(text='Выход', callback_data='base_home')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def faq_inline_kb(questions: dict = questions) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for question_id, question_data in questions.items():
        builder.row(
            InlineKeyboardButton(
                text=question_data.get('qst'),
                callback_data=f'qst_{question_id}'
            )
        )
    builder.row(
        InlineKeyboardButton(
            text='На главную',
            callback_data='base_home'
        )
    )
    # Настраиваем размер клавиатуры
    builder.adjust(1)
    return builder.as_markup()


def faq_answer_kb() -> InlineKeyboardMarkup:
    inline_kb_list = [
        [InlineKeyboardButton(text='ДА', callback_data='faq')],
        [InlineKeyboardButton(text='НЕТ', callback_data='base_home')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def admin_inline_kb() -> InlineKeyboardMarkup:
    inline_kb_list = [
        [InlineKeyboardButton(text='Settings', callback_data='admin_settings')],
        [InlineKeyboardButton(text='Statistic', callback_data='admin_statistic')],
        [InlineKeyboardButton(text='Admin commands', web_app=WebAppInfo(
            url="https://github.com/EliseevIlya/FirstAiogramBot/blob/master/templates/admin-command.html"))],
        [InlineKeyboardButton(text="⬅️ Выйти", callback_data="base_home")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def admin_settings_kb():
    buttons = [
        [InlineKeyboardButton(text="➕ Добавить админа", callback_data="add_admin")],
        [InlineKeyboardButton(text="➕ Добавить вопрос", callback_data="add_question")],
        [InlineKeyboardButton(text="📋 Список вопросов", callback_data="list_questions")],
        [InlineKeyboardButton(text="⬅️ Выйти", callback_data="base_home")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
