from main import dp, bot, db
from aiogram.types import CallbackQuery
from keyboards.admin_keyboard.admin import cb


@dp.callback_query_handler(cb.filter(action="add"))
async def stoptopupcall(call: CallbackQuery, callback_data: dict):
    try:
        await db.confirmation(callback_data.get("user_id"), callback_data.get("good"), True)
        await call.message.edit_text(text=f'Оплата подтверждена', reply_markup=None)
        await bot.send_message(callback_data.get("user_id"),
                               text=f'Ваш товар выставлен на продажу {callback_data.get("good")}')
    except:
        await call.message.edit_text(text=f'Произошла ошибка')


@dp.callback_query_handler(cb.filter(action="delete"))
async def stoptopupcall(call: CallbackQuery, callback_data: dict):
    try:
        await db.confirmation(callback_data.get("user_id"), callback_data.get("good"), False)
        await call.message.edit_text(text=f'Оплата не подтверждена', reply_markup=None)
        await bot.send_message(callback_data.get("user_id"),
                               text=f'Ваш товар не выставлен на продажу {callback_data.get("good")}')
    except:
        await call.message.edit_text(text=f'Произошла ошибка')
