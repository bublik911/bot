from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.url_admin_keyboard import url_admin_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}! "
                         f"Я буду помогать Вам делать рассылку клиентам, работающих с Вами!"
                         f" Если вам нужна помощь, обратитесь к нашему администратору. Он сможет вам помочь!",
                         reply_markup=url_admin_keyboard())
