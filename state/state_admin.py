from aiogram.dispatcher.filters.state import StatesGroup, State

class Edit(StatesGroup):
    step_wallet = State()

class Price_admin(StatesGroup):
    step_price = State()
    step_currency = State()