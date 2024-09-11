from aiogram.utils.keyboard import InlineKeyboardBuilder


def kb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='kb', callback_data='kb')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

