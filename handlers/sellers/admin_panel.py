from main import dp, bot, db
from aiogram.types import Message, CallbackQuery
from keyboards.admin_keyboard.admin import cb


@dp.callback_query_handler(cb.filter(action="add"))
async def stoptopupcall(call: CallbackQuery, callback_data: dict):
    #await db.confirmation(callback_data.get("product_id"))
    await call.message.edit_text(text=f'Оплата подтверждена {callback_data.get("user_id")}')

@dp.callback_query_handler(cb.filter(action="delete"))
async def stoptopupcall(call: CallbackQuery, callback_data: dict):
    #await db.confirmation(callback_data.get("product_id"))
    await call.message.edit_text(text=f'Оплата не мподтверждена {callback_data.get("user_id")}')