from aiogram.fsm.state import StatesGroup, State

class CreateTask(StatesGroup):
    name = State()
    description = State()
    date = State()
    confirm = State()