from aiogram.utils.keyboard import InlineKeyboardBuilder


async def settings():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Создать', callback_data='create_bot')
    keyboard_builder.button(text='Редактировать', callback_data='edit_bot')
    keyboard_builder.button(text='Удалить', callback_data='delete_bot')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def settings_create():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Контракт *', callback_data='contract')
    keyboard_builder.button(text='Картинка', callback_data='photo')
    keyboard_builder.button(text='Ссылки', callback_data='links')
    keyboard_builder.button(text='На главную', callback_data='menu')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def settings_add():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Завершить', callback_data='finish_state')
    keyboard_builder.button(text='Контракт *', callback_data='contract')
    keyboard_builder.button(text='Картинка', callback_data='photo')
    keyboard_builder.button(text='Ссылки', callback_data='links')
    keyboard_builder.button(text='На главную', callback_data='menu')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()




