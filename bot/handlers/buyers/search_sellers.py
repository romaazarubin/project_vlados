from bot.main import dp
from aiogram.types import CallbackQuery
from bot.keyboards.buyer_menu.basic_menu import menu_basic
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text_contains='back_search_sellers', state=None)
async def back_search_sellers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='Для поиска продавца нажмите "покупки"', reply_markup=menu_basic)