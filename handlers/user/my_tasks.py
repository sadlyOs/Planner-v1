from aiogram import F, Router
from aiogram.types import CallbackQuery
from database.requests import Request
from keyboard.my_tasks_buttons import choice_buttons, paginator, Pagination
from language.translator import LocalizedTranslator
from keyboard.mainMenu import menu
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

my_tasks = Router()

@my_tasks.callback_query(F.data == '2')
async def show_choice(call: CallbackQuery, translator: LocalizedTranslator):
    await call.message.edit_text(text=translator.get('choiceText'), reply_markup=await choice_buttons(translator=translator))
    
@my_tasks.callback_query(F.data == 'choice_0')
async def excpectation_task(call: CallbackQuery, translator: LocalizedTranslator, request: Request):
    tasks = [i for i in await request.get_excpectation(user=call.from_user) if i is not None]
    optTask = translator.get('optionTask').split(', ')
    try:
        await call.message.edit_text(text=f"{optTask[0]} ☑️: {tasks[0].title}\n\n🗒{optTask[1]}: {tasks[0].description}\n🕥{optTask[2]}: {tasks[0].due_datetime}",
                                    reply_markup=await paginator(translator=translator, ids=tasks[0].id, key='True'))
    except (IndexError):
        await call.message.edit_text(text=translator.get('there_are_not_tasks'), reply_markup=await menu(translator))


@my_tasks.callback_query(F.data == 'choice_1')
async def completed_task(call: CallbackQuery, translator: LocalizedTranslator, request: Request):
    tasks = [i for i in await request.get_completed(user=call.from_user) if not None]
    optTask = translator.get('optionTask').split(', ')
    try:
        await call.message.edit_text(text=f"{optTask[0]} ☑️: {tasks[0].title}\n\n🗒{optTask[1]}: {tasks[0].description}\n🕥{optTask[2]}: {tasks[0].due_datetime}",
                                    reply_markup=await paginator(translator=translator))
    except (IndexError, AttributeError):
        await call.message.edit_text(text=translator.get('there_are_not_tasks_v2'), reply_markup=await menu(translator))

@my_tasks.callback_query(Pagination.filter(F.action.startswith(('prev_', 'next_'))))
async def paginator_excpectation_task(call: CallbackQuery, translator: LocalizedTranslator, request: Request, callback_data: Pagination):
    page_num = int(callback_data.page)
    action = callback_data.action.split('_')
    tasks_expect = [i for i in await request.get_excpectation(user=call.from_user) if i is not None]
    tasks_complet = [i for i in await request.get_completed(user=call.from_user) if i is not None]
    optTask = translator.get('optionTask').split(', ')

    if action[0] == 'prev':
        page = page_num - 1 if page_num > 0 else 0
    else:
        if action[1] == 'True':
            page = page_num + 1 if page_num < (len(tasks_expect) - 1) else page_num
        else:
            page = page_num + 1 if page_num < (len(tasks_complet) - 1) else page_num

    with suppress(TelegramBadRequest):
        if action[1] == 'True':
            print(1)
            await call.message.edit_text(text=f"{optTask[0]} ☑️: {tasks_expect[page].title}\n\n🗒{optTask[1]}: {tasks_expect[page].description}\n🕥{optTask[2]}: {tasks_expect[page].due_datetime}",
                                        reply_markup=await paginator(page=page, translator=translator, ids=tasks_expect[page].id, key='True'))
        else:
            print(2)
            await call.message.edit_text(text=f"{optTask[0]} ☑️: {tasks_complet[page].title}\n\n🗒{optTask[1]}: {tasks_complet[page].description}\n🕥{optTask[2]}: {tasks_complet[page].due_datetime}",
                                        reply_markup=await paginator(page=page, translator=translator))
    await call.answer('')


@my_tasks.callback_query(F.data == 'back_to_menu')
async def back_to_menu(call: CallbackQuery, translator: LocalizedTranslator):
    with suppress(TelegramBadRequest):
        await call.message.edit_text(text=translator.get('welcome'), reply_markup=await menu(translator))
