from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def url_admin_keyboard():
    button = InlineKeyboardButton(text="Администратор", url="https://t.me/bublik_c_chaem")
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
