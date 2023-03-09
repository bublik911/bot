import asyncio
import os
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token='5775309553:AAHMhvke-BV7XNnIz6r-NEGphfx5XXUks0o')
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())