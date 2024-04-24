from aiogram import Bot
from aiogram.types import User

async def send_message_time(user: User, bot: Bot):
    await bot.send_message(chat_id=user.id, text='Test')