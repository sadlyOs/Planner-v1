from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from language.translator import LocalizedTranslator
from aiogram.filters.callback_data import CallbackData

class Pagination(CallbackData, prefix=""):
    action: str
    page: int

async def choice_buttons(translator: LocalizedTranslator):
    keyBild = InlineKeyboardBuilder()
    list_titles = translator.get('types_of_tasks').split(', ')

    buttons = [InlineKeyboardButton(text=list_titles[i], callback_data=f'choice_{i}') for i in range(len(list_titles))]
    buttons.append(InlineKeyboardButton(text=translator.get('back_to_menu'), callback_data='back_to_menu'))

    return keyBild.add(*buttons).adjust(2).as_markup()


async def paginator(translator: LocalizedTranslator, page: int = 0, ids: str | None = None, key: str = 'False'):
    keyBild = InlineKeyboardBuilder()
    keyBild.add(
        InlineKeyboardButton(text="◀️", callback_data=Pagination(action=f'prev_{key}', page=page).pack()),
        InlineKeyboardButton(text="▶️", callback_data=Pagination(action=f'next_{key}', page=page).pack()),
        InlineKeyboardButton(text=translator.get('back_to_menu'), callback_data='back_to_menu')
    )
    if ids is not None:
        complete_text = translator.get('completeAsk').split(', ')[0]
        keyBild.add(InlineKeyboardButton(text=complete_text, callback_data=f'comp_{"0"}_{ids}'))

    return keyBild.adjust(2).as_markup()
