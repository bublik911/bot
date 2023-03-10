from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def send_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Отлично", callback_data="ok_birthday_message")
    keyboard.button(text="Изменить", callback_data="change_birthday_message")
    return keyboard.as_markup(resize_keyboard=True)
