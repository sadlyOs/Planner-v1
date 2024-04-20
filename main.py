import logging
import asyncio

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config_data.config import config
from database.models import Base
from services import bot_commands
from handlers import setup_message_routers
from middleware.setup import setup_middlewares
from language.translator import Translator

# from database.models import create_db, async_session
# from middleware.dbmiddleware import DbSession
# from aiogram.fsm.storage.redis import RedisStorage


async def on_startup(logger):
    logger.info("START BOT")


async def on_shutdown(logger):
    logger.info("STOP BOT")


# Подключаем базу данных
async def _conf_postgres():
    engine = create_async_engine(
        config.url,
        future=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)



async def main():
    logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s')
    
    logger = logging.getLogger(__name__)

    bot = Bot(token=await config.bot_token)
    dp = Dispatcher(logger=logger)
    session_maker = await _conf_postgres()

    setup_middlewares(dp, session_maker)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(setup_message_routers())
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot, translator=Translator())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    asyncio.run(main())