from aiogram import Bot
from database.requests import Request
from aiogram.types import User
from language.translator import LocalizedTranslator
from keyboard.complete_buttons import complete_ask


async def send_message_time(user: User, bot: Bot, request: Request, ids: str, translator: LocalizedTranslator):
    data = await request.get_task(ids)
    optTask = translator.get('optionTask').split(', ')
    await bot.send_message(chat_id=user.id, text=translator.get('endTask'))
    await bot.send_message(chat_id=user.id, text=f"☑️<b>{optTask[0]}</b>: {data.title}\n\n🗒<b>{optTask[1]}</b>: {data.description}\n🕥<i>{optTask[2]}</i>:{data.due_datetime}",
                           reply_markup=await complete_ask(translator=translator, ids=ids))
    
