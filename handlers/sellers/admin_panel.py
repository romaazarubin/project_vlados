from handlers.sellers.menu_sellers import cart_cb
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(cart_cb.filter(action=["add"]))
async def stoptopupcall(call: CallbackQuery, callback_data: dict):
    await db.confirmation(callback_data.get("product_id"))
    await call.message.edit_text(text='Оплата подтверждена')