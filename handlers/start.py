from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from keyboards.main_keyboard import main_kb
from keyboards.function_keyboard import special_kb, rating_kb

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

