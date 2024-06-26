from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update

from sqlalchemy.orm import sessionmaker

from database.requests import Request

class RequestMiddleware(BaseMiddleware):
    def __init__(self, session_maker: sessionmaker) -> None:
        self.session_maker = session_maker

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        async with self.session_maker() as session:
            data['request'] = Request(session)
            return await handler(event, data)