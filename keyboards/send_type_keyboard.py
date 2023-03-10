from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def send_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Рассылка всем", callback_data="all_sending")
    keyboard.button(text="Рассылка ко дню рождения", callback_data="birthday_sending")
    return keyboard.as_markup(resize_keyboard=True)