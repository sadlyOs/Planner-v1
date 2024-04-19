from lexicon.lexicon import LEXICON_RU
from aiogram.types import Message
from aiogram import Router, F
# from database.requests import Request

other = Router()


@other.message(F.photo)
async def process_photo_command(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(file_id)

@other.message()
async def process_other_hanlders(message: Message):
    await message.answer(text=LEXICON_RU['/help_other'])