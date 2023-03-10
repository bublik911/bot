from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def check_client_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button("Всё верно", callback_data="ok_client")
    keyboard.button("Заполнить заново", callback_data="change_client")
    return keyboard.as_markup(resize_keyboard=True)
