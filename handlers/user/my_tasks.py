from aiogram import F, Bot, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from database.requests import Request
from keyboard.my_tasks_buttons import choice_buttons
from language.translator import LocalizedTranslator
from keyboard.mainMenu import menu

my_tasks = Router()

@my_tasks.callback_query(F.data == '2')
async def show_choice(call: CallbackQuery, translator: LocalizedTranslator):
    await call.message.edit_text(text=translator.get('choiceText'), reply_markup=await choice_buttons(translator=translator))
    