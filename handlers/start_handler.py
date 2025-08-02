from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

from create_bot import bot
from keyboards.main_keyboard import main_kb
from keyboards.function_keyboard import special_kb, rating_kb
import html

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    command_args: str = command.args
    if command_args:
        await message.answer(
            f'/start используя фильтр CommandStart() с меткой <b>{command_args}</b>')
    else:
        await message.answer(
            f'/start используя фильтр CommandStart() без метки')


@start_router.message(Command('ping'))
async def cmd_ping(message: Message):
    await message.answer('pong - используя фильтр Command()')


@start_router.message(F.text == '/hello')
async def cmd_hello(message: Message):
    await message.answer('Привет -  используя магический фильтр F.text!')


@start_router.message(Command('special_keyboard'))
async def cmd_special_keyboard(message: Message):
    await message.answer("Специальные возможности", reply_markup=special_kb())


@start_router.message(F.text == '/rating_keyboard')
async def cmd_rating_keyboard(message: Message):
    await message.answer("Рейтинг", reply_markup=rating_kb())


@start_router.message(F.text == '/base')
async def cmd_base(message: Message):
    await message.answer("Базовые функции", reply_markup=main_kb(message.from_user.id))


@start_router.message(F.location)
async def cmd_location(message: Message):
    await message.answer("LOCATION")


@start_router.message(Command(commands=['settings', 'config', 'setup']))
async def cmd_settings(message: Message, command: CommandObject):
    command_args: str = command.args
    if command_args:
        await message.answer(f'setting {command_args}')
    await message.answer(f'settings')


@start_router.message(Command(commands=['html_format']))
async def cmd_html_format(message: Message):
    text = (
        "<b>Жирный</b>\n"
        "<i>Курсив</i>\n"
        "<u>Подчеркнутый</u>\n"
        "<s>Зачеркнутый</s>\n"
        "<tg-spoiler>Спойлер (нажми, чтобы увидеть)</tg-spoiler>\n"
        "<a href='https://example.com'>Ссылка</a>\n"
        "<code>Код</code>\n"
        "<pre>Большой кодовый блок</pre>"
    )
    await message.reply(text)


@start_router.message(Command(commands=['html_raw']))
async def cmd_html_raw(message: Message):
    text = """
    <b>Жирный</b>
    <i>Курсив</i>
    <u>Подчеркнутый</u>
    <s>Зачеркнутый</s>
    <tg-spoiler>Спойлер (скрытый текст)</tg-spoiler>
    <a href="http://www.example.com/">Ссылка в тексте</a>
    <code>Код с копированием текста при клике</code>
    <pre>Спойлер с копированием текста</pre>
    """.strip()
    escaped_text = html.escape(text)
    await bot.send_message(chat_id=message.chat.id, text=escaped_text, reply_to_message_id=message.message_id)
    await message.forward(chat_id=message.from_user.id)
