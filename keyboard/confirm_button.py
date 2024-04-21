from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator


async def confirm(key: str, translator: LocalizedTranslator, lang: str | None = None):
    keyBild = InlineKeyboardBuilder()
    if key == 'lang':
        return keyBild.add(
            InlineKeyboardButton(text=translator.get('confirmLang').split(', ')[1], callback_data='conf_lang'),
            InlineKeyboardButton(text=translator.get('back'), callback_data=f'back_lang_{lang}')
            ).as_markup()