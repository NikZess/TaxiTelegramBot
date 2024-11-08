from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from aiogram.enums import ParseMode

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет🖐️, это бот🤖, который поможет быстро заказать такси🚕")