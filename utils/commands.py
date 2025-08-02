from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='ping', description='ping'),
                BotCommand(command='hello', description='Привет'),
                BotCommand(command='special_keyboard', description='Спец возможности'),
                BotCommand(command='rating_keyboard', description='Рейтинг'),
                BotCommand(command='base', description='Базовые функции'),
                BotCommand(command='faq',description='FAQ')
                ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
