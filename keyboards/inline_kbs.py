from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой хабр", url='https://github.com/EliseevIlya')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=gghostwar')],
        [InlineKeyboardButton(text="Яндекс Музыка", web_app=WebAppInfo(url="https://music.yandex.ru/"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def inline_user_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Получить пользователя', callback_data='get_user')],
        [InlineKeyboardButton(text='Выход', callback_data='back')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
