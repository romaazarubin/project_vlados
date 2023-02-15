from main import dp, db
from aiogram.types import CallbackQuery
from keyboards.buyer_menu.basic_menu import menu_basic
from keyboards.buyer_menu.product_list import all_product
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains='back_search_sellers', state=None)
async def back_search_sellers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='Для поиска продавца нажмите "покупки"', reply_markup=menu_basic)


@dp.callback_query_handler(text_contains='all_good1')
async def all_good(call: CallbackQuery):
    data = await db.all_good(0)
    count = await db.count_good()
    await call.message.edit_text(text='Все товары', reply_markup=all_product(data=data, count=count))
