from aiogram.dispatcher.filters.state import StatesGroup, State

class Registration(StatesGroup):
    step_login = State()
    step_password = State()
    step_db = State()