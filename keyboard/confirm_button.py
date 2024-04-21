from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator


async def confirm(key: str, translator: LocalizedTranslator):
    keyBild = InlineKeyboardBuilder()
    if key == 'lang':
        return keyBild.add(InlineKeyboardButton(text=translator.get('confirmLang').split(', ')[1], callback_data='conf_lang')).as_markup()