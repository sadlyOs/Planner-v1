from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery

from database.requests import Request

class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        request: Request = data['request']
        user = await request.get_user(event.from_user.id)
        if not user:
            await request.create_user(event.from_user.id)
        return await handler(event, data)