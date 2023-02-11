from aiogram.dispatcher.filters.state import StatesGroup, State

class Sell(StatesGroup):
    step_one = State()
    step_two = State()