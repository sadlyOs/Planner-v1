from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery
from fluentogram.src.abc import translator

from database.requests import Request
from services.language.translator import FluentService, TranslationLoader

class LangMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        fluent: FluentService = data['fluent']
        request: Request = data['request']
        user_lang = (await request.get_user(event.from_user.id)).lang
        trans_runner: TranslationLoader = fluent.get_translator_by_locale(user_lang)
        data['i18n'] = trans_runner
        data["i18n_hub"] = fluent.hub
        return await handler(event, data)