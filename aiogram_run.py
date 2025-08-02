import asyncio


from create_bot import bot, dispatcher
from handlers.admin_handler import admin_router
from handlers.inline_handler import inline_router
from handlers.start import start_router
from utils.commands import set_commands


async def main():
    dispatcher.include_router(admin_router)
    dispatcher.include_router(start_router)
    dispatcher.include_router(inline_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())