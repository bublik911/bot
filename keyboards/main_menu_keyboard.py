from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="📕Проверить клиентскую базу", callback_data="check_client_base")
    keyboard.button(text="✏Добавить клиента", callback_data="add_client")
    keyboard.button(text="✉Рассылка", callback_data="send")
    return keyboard.as_markup(resize_keyboard=True)
