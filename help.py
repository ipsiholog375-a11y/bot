from aiogram import types, F
from loader import dp

@dp.message(F.text == "/help")
async def send_help(message: types.Message):
    await message.answer("🌟 Довідка / Help")
