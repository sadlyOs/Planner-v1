from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from language.translator import LocalizedTranslator

async def setting_menu(translator: LocalizedTranslator):
    keyBild = InlineKeyboardBuilder()
    list_command = translator.get('settinsButton').split(', ')
    buttons = [InlineKeyboardButton(text=list_command[i],
    callback_data=list_command[i]) for i in range(len(list_command))]
    return keyBild.add(*buttons).adjust(2).as_markup()

async def edit_lang():
    keyBild = InlineKeyboardBuilder()
    list_lang = ['ru_Русский🇷🇺', 'en_English🇬🇧']
    buttons = [InlineKeyboardButton(text=i.split('_')[1], callback_data=i.split('_')[0]) for i in list_lang]
    return keyBild.add(*buttons).as_markup()

