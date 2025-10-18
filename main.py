from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from handler import setup_message_router

API_TOKEN = "8452567679:AAEzGRiD8t3Sj22qZf60RKjWa0lf_wPDdC0"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    handler_router = setup_message_router()
    dp.include_router(handler_router)

    await bot.delete_webhook(drop_pending_updates= True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

















