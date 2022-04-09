from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.sozlama import menu
from loader import dp


# from keyboards.inline.languages import button
@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Assalomalekum men tarjimon botman", reply_markup=menu)
