from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator


async def confirm(key: str, translator: LocalizedTranslator, lang: str | None = None):
    keyBild = InlineKeyboardBuilder()
    if key == 'lang':
        return keyBild.add(
            InlineKeyboardButton(text=translator.get('confirmLang').split(', ')[1], callback_data='conf_lang'),
            ).as_markup()
    else:
        return keyBild.add(
            InlineKeyboardButton(text=translator.get('confirmLang').split(', ')[1], callback_data='conf'),
            InlineKeyboardButton(text=translator.get('back'), callback_data=f'back')
            ).as_markup()

async def move_back(key: str, translator: LocalizedTranslator, add_info: str):
    keyBild = InlineKeyboardBuilder()
    return keyBild.add(
            InlineKeyboardButton(text=translator.get('back'), callback_data=f'{key}_back_{add_info}')
            ).as_markup()
    