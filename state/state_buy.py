from aiogram.dispatcher.filters.state import StatesGroup, State

class Buy(StatesGroup):
    step_search = State()
    step_value = State()
    step_pay = State()