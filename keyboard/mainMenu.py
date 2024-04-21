from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from language.translator import LocalizedTranslator

async def menu(translator: LocalizedTranslator):
    keybild = InlineKeyboardBuilder()
    list_command = translator.get('menuButton').split(', ')
    buttons = [InlineKeyboardButton(text=list_command[i],
    callback_data=str(i)) for i in range(len(list_command))]
    return keybild.add(*buttons).adjust(2).as_markup()