from aiogram.dispatcher.filters.state import StatesGroup, State

class Buy(StatesGroup):
    step_search = State()
    step_wallet = State()
    step_value = State()
