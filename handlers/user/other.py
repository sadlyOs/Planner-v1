from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from keyboard.mainMenu import menu
from language.translator import LocalizedTranslator

other = Router()


@other.message(CommandStart())
async def start(msg: Message, translator: LocalizedTranslator):
    await msg.answer(text=translator.get('welcome'), reply_markup=await menu(translator))

@other.message(F.photo)
async def process_photo_command(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(file_id)

@other.message()
async def process_other_hanlders(message: Message, translator: LocalizedTranslator):
    await message.answer(text=translator.get('test'))