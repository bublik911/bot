from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def check_clients_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Всё верно", callback_data="ok_clients")
    keyboard.button(text="Удалить клиента из базы", callback_data="delete_clients")
    return keyboard.as_markup(resize_keyboard=True)
