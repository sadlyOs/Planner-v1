import logging
import asyncio
from aiogram import Bot, Dispatcher
from pydantic import config
from config_data.config import Config
from services import bot_commands
from handlers import setup_message_routers
# from database.models import create_db, async_session
# from middleware.dbmiddleware import DbSession
# from aiogram.fsm.storage.redis import RedisStorage


async def on_startup(logger):
    logger.info("START BOT")


async def on_shutdown(logger):
    logger.info("STOP BOT")


async def main():
    logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s')
    
    logger = logging.getLogger(__name__)
    config = Config()

    bot = Bot(token=await config.bot_token)
    dp = Dispatcher(logger=logger)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(setup_message_routers())
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    asyncio.run(main=main())