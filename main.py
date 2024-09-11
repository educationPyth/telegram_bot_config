import asyncio
import logging  
from aiogram import Bot, Dispatcher  
from aiogram.filters import Command  
from aiogram import F
from core.handlers.basic import *
from core.settings import settings
from core.utils.commands import set_commands

# Инициализация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()  # Создаём диспетчер без бота

    # Регистрация обработчиков
    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(start_settings, Command(commands='start_settings'))



    try:
        await bot.get_me()  # Проверка, работает ли бот
        logging.info('Бот работает!')
        await start_bot(bot)  # Запускаем бота и отправляем сообщение об этом
        await dp.start_polling(bot)  # Передаём объект бота для запуска опроса
    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')
    finally:
        await stop_bot(bot)  # Отправляем сообщение об остановке бота
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

