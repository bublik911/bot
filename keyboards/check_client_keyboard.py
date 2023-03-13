from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def check_client_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button("Всё верно")
    keyboard.button("Заполнить заново")
    return keyboard.as_markup(resize_keyboard=True)
