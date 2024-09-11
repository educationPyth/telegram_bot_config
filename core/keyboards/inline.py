from aiogram.utils.keyboard import InlineKeyboardBuilder


def set_contract():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Загрузите контракт', callback_data='user_contract')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def set_photo():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Загрузите фото', callback_data='user_photo')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def set_links():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Загрузите 3(три) ссылки через пробел', callback_data='user_links')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

