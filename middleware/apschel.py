from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class ApsMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler) -> None:
        self.scheduler = scheduler


    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        data['apscheduler'] = self.scheduler
        return await handler(event, data)