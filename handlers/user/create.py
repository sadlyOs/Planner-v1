import uuid

from aiogram import F, Bot, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.requests import Request

from States.task_create import CreateTask
from keyboard.mainMenu import menu
from keyboard.confirm_button import confirm, move_back
from language.translator import LocalizedTranslator
from datetime import datetime
from services.time_messages import send_message_time


create = Router()

@create.callback_query(F.data == '0')
async def start_create(call: CallbackQuery, translator: LocalizedTranslator, state: FSMContext):
    await call.answer('')
    await call.message.edit_text(text=f"{translator.get('panelCreate')}\n\n{translator.get('actionCreate')}", reply_markup=await move_back(key='create', translator=translator, add_info='nothing'))
    await state.set_state(CreateTask.name)

@create.message(CreateTask.name)
async def create_name(msg: Message, translator: LocalizedTranslator, state: FSMContext):
    if len(msg.text) <= 2:
        await msg.answer(translator.get('errors_message').split('_')[0], reply_markup=await move_back(key='create', translator=translator, add_info='name'))
    else:
        await state.update_data(title=msg.text)
        await msg.answer(translator.get('descCreate'), reply_markup=await move_back(key='create', translator=translator, add_info='name'))
        await state.set_state(CreateTask.description)

@create.message(CreateTask.description)
async def create_description(msg: Message, translator: LocalizedTranslator, state: FSMContext):
    if len(msg.text) <= 10:
        await msg.answer(translator.get('errors_message').split('_')[1], reply_markup=await move_back(key='create', translator=translator, add_info='description'))
    else:
        await state.update_data(description=msg.text)
        await msg.answer(translator.get('dateCreate'), reply_markup=await move_back(key='create', translator=translator, add_info='description'))
        await state.set_state(CreateTask.date)

@create.message(CreateTask.date)
async def create_date(msg: Message, translator: LocalizedTranslator, state: FSMContext, logger):
    date = msg.text.split(' ')
    if (len(date) == 2):
        try:
            datetime.strptime(msg.text, "%Y-%m-%d %H:%M")
            await state.update_data(date=msg.text)
            state_dates = await state.get_data()
            await msg.answer(f"{translator.get('confirmCreate')}\n\n"\
                            f"{state_dates['title']}\n{state_dates['description']}\n{translator.get('startTask')} {state_dates['date']}",
                            reply_markup=await confirm(key='okey', translator=translator))
            await state.set_state(CreateTask.confirm)
        except ValueError as f:
            logger.error(f)
            await msg.answer(translator.get('errors_message').split('_')[2], reply_markup=await move_back(key='create', translator=translator, add_info='description'))
  
    else:
        await msg.answer(translator.get('errors_message').split('_')[2], reply_markup=await move_back(key='create', translator=translator, add_info='description'))
    

@create.callback_query(F.data == 'conf', CreateTask.confirm)
async def confirm_task(call: CallbackQuery, translator: LocalizedTranslator, state: FSMContext, request: Request, apscheduler: AsyncIOScheduler, bot: Bot):
    state_dates = await state.get_data()
    random_uuid = uuid.uuid4()
    print(str(random_uuid))
    await request.create_task(ids=random_uuid, user=call.from_user, title=state_dates['title'], description=state_dates['description'], due_datetime=datetime.strptime(state_dates['date'], "%Y-%m-%d %H:%M"))

    await call.message.edit_text(text=translator.get('addTask'), reply_markup=await menu(translator))
    await state.clear()
    apscheduler.add_job(send_message_time, trigger='date', run_date=datetime.strptime(state_dates['date'], "%Y-%m-%d %H:%M"),
                              kwargs={'user': call.from_user, 'bot': bot, 'request': request, 'translator': translator, 'ids': str(random_uuid)})

@create.callback_query(F.data == 'back', CreateTask.confirm)
async def back_task(call: CallbackQuery, translator: LocalizedTranslator, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_text(text=translator.get('cancelCreateTask'), reply_markup=await menu(translator))
    await state.clear()

@create.callback_query(F.data.startswith('create_'))
async def move_back_process(call: CallbackQuery, translator: LocalizedTranslator, state: FSMContext):
    await call.answer('')
    info = call.data.split('_')[2]
    if info == 'nothing':
        await call.message.edit_text(text=translator.get('welcome'), reply_markup=await menu(translator))
        await state.clear()
    elif info == 'name':
        await call.message.edit_text(text=f"{translator.get('panelCreate')}\n\n{translator.get('actionCreate')}", reply_markup=await move_back(key='create', translator=translator, add_info='nothing'))
        await state.set_state(CreateTask.name)
    elif info == 'description':
        await call.message.edit_text(translator.get('descCreate'), reply_markup=await move_back(key='create', translator=translator, add_info='name'))
        await state.set_state(CreateTask.description)
    else:
        await call.message.edit_text(translator.get('dateCreate'), reply_markup=await move_back(key='create', translator=translator, add_info='description'))
        await state.set_state(CreateTask.date)