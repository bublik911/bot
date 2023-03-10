from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def send_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Отправить", callback_data="ok_all_message")
    keyboard.button(text="Написать заново", callback_data="change_all_message")
    return keyboard.as_markup(resize_keyboard=True)
