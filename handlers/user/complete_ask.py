from aiogram import F, Router
from aiogram.types import CallbackQuery
from database.requests import Request
from language.translator import LocalizedTranslator
from keyboard.mainMenu import menu

complete = Router()

@complete.callback_query(F.data.startswith('comp_'))
async def complete_asking(call: CallbackQuery, translator: LocalizedTranslator, request: Request):
    if call.data.split('_')[1] == '0':
        await request.edit_completed(ids=call.data.split('_')[2])
        await request.edit_excpectation(ids=call.data.split('_')[2])
        await call.message.edit_text(text=translator.get('completed'), reply_markup=await menu(translator=translator))
    else:
        await request.edit_excpectation(ids=call.data.split('_')[2], expectation=True)
        await call.message.edit_text(text=translator.get('laterTask'), reply_markup=await menu(translator=translator))