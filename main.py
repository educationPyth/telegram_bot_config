import asyncio
import logging  
from aiogram import Bot, Dispatcher
from core.handlers.basic import *
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import router

bot = Bot(token=settings.bots.bot_token)
dp = Dispatcher()  # Создаём диспетчер без бота


# Инициализация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def start():
    dp.include_router(router)

    try:
        await bot.get_me()  # Проверка, работает ли бот
        logging.info('Бот работает!')
        await dp.start_polling(bot)  # Передаём объект бота для запуска опроса
    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

