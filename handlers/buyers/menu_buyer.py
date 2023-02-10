from aiogram.dispatcher.filters import Text
from main import dp, bot, db
from aiogram.types import Message, ReplyKeyboardRemove, ContentType
from keyboards.buyer_menu.product_list import menu_product_for_buyer
from keyboards.buyer_menu.basic_menu import menu_basic, menu_basic_not_buy
from keyboards.Reply_markup.start_menu import menu
from aiogram.dispatcher import FSMContext
from state.state_buy import Buy
from state.state_registr import Registration


@dp.message_handler(Text(equals='Покупатель'), state=None)
async def buyer(message: Message):
    await bot.send_message(message.from_user.id, text='Введите свой кошелек', reply_markup=menu_basic_not_buy)
    await Registration.step_wallet.set()


@dp.message_handler(content_types=['text'], state=Registration.step_wallet)
async def wallet(message: Message, state: FSMContext):
    try:
        await db.add_buyer(message.from_user.id, message.from_user.username, message.text)
    except:
        await db.update_buyer(message.from_user.id, message.from_user.username, message.text)
    finally:
        await bot.send_message(message.from_user.id, text='Нажмите покупку, для поиска продавца',
                               reply_markup=menu_basic)
        await state.finish()


@dp.message_handler(Text(equals='Покупка'))
async def buy(message: Message):
    await bot.send_message(message.from_user.id, text='Введите ник продавца', reply_markup=menu_basic_not_buy)

    await Buy.step_search.set()


@dp.message_handler(state=Buy.step_search)
async def name_buyer(message: Message, state: FSMContext):
    name = message.text.lower()
    if name == 'вернуться на главное меню':
        await state.finish()
    else:
        await state.update_data(
            {
                'name': name
            }
        )

        try:
            rows = await db.good(name)
            await state.finish()
            await bot.send_message(message.from_user.id, text=f"Все товары {name}'a",
                                   reply_markup=menu_product_for_buyer(rows))

        # await state.finish()
        except:
            await bot.send_message(message.from_user.id, text='произошла ошибка, введите имя продавца')
            await Buy.step_search.set()
