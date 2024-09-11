from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

import asyncio


async def get_start(message: Message, bot: Bot):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,f'Привет {message.from_user.first_name}', parse_mode='HTML')


async def start_settings(message: Message, bot: Bot):
    chat_id = message.chat.id

    await bot.send_message(chat_id, f'{chat_id}')

