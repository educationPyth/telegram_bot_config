from aiogram import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from core.utils.callbackdata import UserChannel
import core.keyboards.inline as kb
import logging

router = Router()

@router.message(Command('start'))
async def get_start(message: Message, bot: Bot):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,f'Привет {message.from_user.first_name}\n'
                                   f'Перейдите в группу или канал, где должен работать бот.\n'
                                   f'\n'
                                   f'Дайте боту права Администратор\n'
                                   f'Затем пропишите команду /start_settings и следуйте инструкции', parse_mode='HTML')



@router.message(Command('start_settings'))
async def start_settings(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.update_data(chat=chat_id)
    user_id = message.from_user.id

    await message.answer('Выберите пункты для настройки:', reply_markup=await kb.settings())


@router.message(Command('menu'))
async def view_menu(message: Message):
    await message.answer('Выберите пункты для настройки:', reply_markup=await kb.settings())


@router.callback_query(F.data == 'create_bot')
async def create_bot(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Передайте нужные поля\n\n'
                                     '* - обязательное поле:', reply_markup=await kb.settings_create())


@router.callback_query(F.data == 'menu')
async def get_back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ВЫберите пункты для настройки:', reply_markup=await kb.settings())


@router.callback_query(F.data == 'contract')
async def get_contract(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Введите контракт c coinmarketcap (contract pair):')
    await state.set_state(UserChannel.contract)


@router.message(UserChannel.contract)
async def step_contract(message: Message, state: FSMContext):
    await state.update_data(contract=message.text)

    await message.answer('Контракт получен! Если необходимо добавьте картинку и ссылки', reply_markup=await kb.settings_add() )


@router.callback_query(F.data == 'photo')
async def get_photo(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Вставьте фото!')
    await state.set_state(UserChannel.photo)


@router.message(UserChannel.photo)
async def step_photo(message: Message, state: FSMContext):
    if message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
        await message.answer('Отлично, картинка получена.', reply_markup=await kb.settings_add())
    else:
        await message.answer('Неверный формат, вставьте только картинку.')


@router.callback_query(F.data == 'links')
async def get_links(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Вставьте ссылки через пробел')
    await state.set_state(UserChannel.links)


@router.message(UserChannel.links)
async def step_links(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(links=message.text)
        await message.answer('Ссылки сохранены.', reply_markup=await kb.settings_add())
    else:
        await message.answer('Ссылки должны быть текстом, через пробел')


@router.callback_query(F.data == 'finish_state')
async def finish_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()

    contract = data['contract']
    chat = data['chat']
    photo_id = data.get('photo', '')
    links = data.get('links', '')

    if contract in data:
        # Формируем сообщение с учётом возможных пустых значений
        response_text = f'Ваши данные успешно сохранены:\n' \
                        f'Контракт: {data["contract"]}\n' \
                        f'Картинка: {photo_id if photo_id else "Нет"}\n' \
                        f'Ссылки: {links if links else "Нет"}\n' \

        await callback.message.edit_text(response_text)
        await state.clear()

    else:
        await callback.message.answer('Поле контракт обязательно для заполнения!', reply_markup=await kb.settings_add())



