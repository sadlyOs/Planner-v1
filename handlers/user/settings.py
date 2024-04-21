from aiogram.types import CallbackQuery
from aiogram import Router, F
from database.requests import Request
from keyboard.confirm_button import confirm
from keyboard.mainMenu import menu
from keyboard.settingKey import edit_lang, setting_menu
from language.translator import LocalizedTranslator


settings = Router()

@settings.callback_query(F.data == '1')
async def setting(call: CallbackQuery, translator: LocalizedTranslator):
    await call.answer('')
    await call.message.edit_text(text=translator.get('settinsHandler'), reply_markup=await setting_menu(translator))

@settings.callback_query(F.data.in_(['Edit language', 'Изменить язык']))
async def select_lang(call: CallbackQuery, translator: LocalizedTranslator):
    await call.answer('')
    await call.message.edit_text(text=translator.get('choiceLang'), reply_markup=await edit_lang())

@settings.callback_query(F.data.startswith(('ru', 'en')))
async def edit_lang_command(call: CallbackQuery, translator: LocalizedTranslator, request:Request):
    await request.change_user_lang(user_id=call.from_user.id, lang=call.data.split('_')[0])
    await call.message.edit_text(text=translator.get('confirmLang').split(', ')[0], reply_markup=await confirm(key='lang', translator=translator))

@settings.callback_query(F.data == 'conf_lang')
async def confirm_lang(call: CallbackQuery, translator: LocalizedTranslator):
    await call.answer(translator.get('newLang'))
    await call.message.edit_text(text=translator.get('welcome'), reply_markup=await menu(translator))
