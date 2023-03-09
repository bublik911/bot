from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="📕Проверить клиентскую базу")
    keyboard.button(text="✏Добавить клиента")
    keyboard.button(text="✉Рассылка")
    return keyboard.as_markup(resize_keyboard=True)