from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator

async def choice_buttons(translator: LocalizedTranslator):
    keyBild = InlineKeyboardBuilder()
    list_titles = translator.get('types_of_tasks').split(', ')
    buttons = [InlineKeyboardButton(text=i, callback_data=i) for i in list_titles]
    return keyBild.add(*buttons).adjust(2).as_markup()