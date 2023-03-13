from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class AddClient(StatesGroup):
    name = State()
    phone = State()
    month = State()
    day = State()


router = Router()


@router.message(
    Text("✏Добавить клиента")
)
async def start(message: Message, state: FSMContext):
    await message.answer("Введите имя клиента")
    await state.set_state(AddClient.name)


@router.message(
    AddClient.name
)
async def add_client_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddClient.phone)


@router.message(
    AddClient.phone
)
async def add_client_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(AddClient.month)


@router.message(
    AddClient.month
)
async def add_client_month(message: Message, state: FSMContext):
    await state.update_data(month=message.text)
    await state.set_state(AddClient.day)


@router.message(
    AddClient.day
)
async def add_client_day(message: Message, state: FSMContext):
    await state.update_data(day=message.text)
    user_data = await state.get_data()
    await message.answer(f"{user_data['name']}")
