from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, KeyboardButtonRequestUser, \
    KeyboardButtonRequestChat
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def special_kb() -> ReplyKeyboardMarkup:
    kb_list = [
        [KeyboardButton(text="Отправить геолокацию", request_location=True)],
        [KeyboardButton(text="Поделиться номером", request_contact=True)],
        [KeyboardButton(text="Отправить викторину/опрос", request_poll=KeyboardButtonPollType())],

        # Выбор пользователя
        [KeyboardButton(
            text="👥 Выбрать пользователя",
            request_user=KeyboardButtonRequestUser(
                request_id=1,  # Обязательный уникальный ID
                user_is_bot=False,  # Только не-боты
                user_is_premium=None  # Любые (можно True/False)
            )
        )],

        # Выбор чата
        [KeyboardButton(
            text="💬 Выбрать чат",
            request_chat=KeyboardButtonRequestChat(
                request_id=2,  # Обязательный ID
                chat_is_channel=False,  # Группы или каналы?
                chat_is_forum=None,  # Форум-чаты
                chat_has_username=None,  # Публичные чаты
                chat_is_created=False,  # Созданные пользователем
                user_administrator_rights=None,  # Админ-права
                bot_administrator_rights=None,  # Бот должен быть админом
            )
        )]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   one_time_keyboard=True,
                                   input_field_placeholder="Воспользуйтесь специальной клавиатурой:")
    return keyboard


def rating_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for item in [str(i) for i in range(1, 11)]:
        builder.button(text=item)
    builder.button(text='Назад')
    builder.adjust(4, 4, 2, 1)

    return builder.as_markup(resize_keyboard=True,
                             one_time_keyboard=True,
                             input_field_placeholder="Воспользуйтесь специальной клавиатурой:")
