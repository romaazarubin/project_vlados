from aiogram.dispatcher.filters.state import StatesGroup, State

class Sell(StatesGroup):
    step_name = State()
    step_quantity = State()
    step_rate = State()
    step_wallet = State()
    step_pay = State()