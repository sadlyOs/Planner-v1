from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator

async def complete_ask(translator: LocalizedTranslator, ids: str):
    keyBild = InlineKeyboardBuilder()
    list_title = translator.get('completeAsk').split(', ')
    buttons = [InlineKeyboardButton(text=list_title[i], callback_data=f'comp_{i}_{ids}') for i in range(len(list_title))]
    return keyBild.add(*buttons).adjust(2).as_markup()