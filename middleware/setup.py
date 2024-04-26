from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import sessionmaker

from .lang import LangMiddleware
from .request import RequestMiddleware
from .check_user import RegisterMiddleware
from .apschel import ApsMiddleware

def setup_middlewares(dp: Dispatcher, session_maker: sessionmaker, scheduler: AsyncIOScheduler):
    dp.update.outer_middleware.register(RequestMiddleware(session_maker))
    dp.message.outer_middleware.register(RegisterMiddleware())
    dp.callback_query.outer_middleware.register(RegisterMiddleware())
    dp.message.middleware.register(LangMiddleware())
    dp.callback_query.middleware.register(LangMiddleware())
    dp.update.middleware.register(ApsMiddleware(scheduler))
