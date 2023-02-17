from aiogram.dispatcher.filters import Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.buyer_menu.product_list import menu_product_for_buyer
from keyboards.buyer_menu.basic_menu import menu_basic, menu_basic_not_buy
from keyboards.Reply_markup.start_menu import menu
from aiogram.dispatcher import FSMContext
from state.state_buy import Buy
from state.state_registr import Registration
from keyboards.buyer_menu.selection_menu import select_menu, back_button


@dp.message_handler(Text(equals='Покупатель'), state=None)
async def buyer(message: Message):
    await bot.send_message(message.from_user.id, text='Введите свой кошелек', reply_markup=menu_basic_not_buy)
    await Registration.step_wallet.set()


@dp.message_handler(content_types=['text'], state=Registration.step_wallet)
async def wallet(message: Message, state: FSMContext):
    k = await db.presence_buyer(message.from_user.id)
    if message.text == 'Вернуться на главное меню' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id,
                               text='Выберите роль',
                               reply_markup=menu)
    else:
        if not k:
            await db.add_buyer(message.from_user.id, message.from_user.username, message.text)
            await bot.send_message(message.from_user.id, text='Нажмите покупку, для поиска товара',
                                   reply_markup=menu_basic)
            await state.finish()
        else:
            await db.update_buyer(message.from_user.id, message.from_user.username, message.text)
            await bot.send_message(message.from_user.id, text='Нажмите покупку, для поиска товара',
                                   reply_markup=menu_basic)
            await state.finish()


@dp.message_handler(Text(equals='Покупка'))
async def buy(message: Message):
    await bot.send_message(message.from_user.id, text='Выберите способ поиска', reply_markup=select_menu)


@dp.callback_query_handler(text_contains='choosing_role')
async def choosing_role(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Выберите роль',
                              reply_markup=menu)

@dp.callback_query_handler(text_contains='search_by_name')
async def search_by_name(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите название товара', reply_markup=menu_basic_not_buy)
    await Buy.step_search.set()

@dp.message_handler(state=Buy.step_search)
async def name_buyer(message: Message, state: FSMContext):
    name = message.text.lower()
    if name == 'вернуться на главное меню' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await state.finish()
        await bot.send_message(message.from_user.id, text='выберите роль', reply_markup=menu)
    else:
        await state.update_data(
            {
                'name': name
            }
        )

        try:
            rows = await db.good(name)
            await state.finish()
            await bot.send_message(message.from_user.id, text=f"Все товары {name}'a,",
                                   reply_markup=menu_product_for_buyer(rows))

        except:
            await bot.send_message(message.from_user.id, text='произошла ошибка, введите название товара повторно')
            await Buy.step_search.set()
