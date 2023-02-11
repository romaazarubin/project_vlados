from aiogram.dispatcher.filters.state import StatesGroup, State

class Registration(StatesGroup):
    step_wallet = State()
