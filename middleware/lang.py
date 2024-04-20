from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery
from fluentogram.src.abc import translator

from database.requests import Request
from language.translator import Translator

class LangMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        request: Request = data['request']
        user_lang = (await request.get_user(event.from_user.id)).lang
        translator: Translator = data['translator']
        data['translator'] = translator(language=user_lang)
        return await handler(event, data)