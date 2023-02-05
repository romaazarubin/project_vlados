from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, ReplyKeyboardRemove
from keyboards.menu_basic.start_menu import menu_back_main
from keyboards.seller_menu.entry_menu import seller_menu, product_display, menu_basic
from aiogram.dispatcher import FSMContext
from state.state_sell import Sell


@dp.callback_query_handler(text_contains='seller')
async def seller(call: CallbackQuery):
    await db.add_user(call.from_user.id, call.from_user.username)
    await call.message.edit_text(text='Продажа', reply_markup=seller_menu)


@dp.callback_query_handler(text_contains='sell', state=None)
async def sell(call: CallbackQuery):
    await call.message.edit_text(text='Введите название товара')

    await Sell.step_name.set()


@dp.message_handler(state=Sell.step_name)
async def sell_step_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {
            'name': name
        }
    )
    await bot.send_message(message.from_user.id, text='Введите количество товара')

    await Sell.step_quantity.set()


@dp.message_handler(state=Sell.step_quantity)
async def sell_step_name(message: Message, state: FSMContext):
    quantity = message.text
    await state.update_data(
        {
            'quantity': quantity
        }
    )
    await bot.send_message(message.from_user.id, text='Введите курс')

    await Sell.step_rate.set()


@dp.message_handler(state=Sell.step_rate)
async def sell_step_name(message: Message, state: FSMContext):
    rate = message.text
    await state.update_data(
        {
            'rate': rate
        }
    )
    data = await state.get_data()
    await bot.send_message(message.from_user.id, text=f"Товар: {data.get('name')}\n"
                                                      f"Количество: {data.get('quantity')}\n"
                                                      f"Курс: {data.get('rate')}\n"
                                                      f"Выставление товара платное. Оплатите 5$ на счет "
                                                      f"543567834573",
                           reply_markup=menu_basic)
    await Sell.step_pay.set()


@dp.message_handler(state=Sell.step_pay)
async def sell_step_pay(message: Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(message.from_user.id, text="..", reply_markup=ReplyKeyboardRemove())
    if message.text == 'Оплатить и выставить':
        await bot.send_message(454279273, text='Такой пользователь')
        await db.add_good(message.from_user.id, message.from_user.username, data.get('name'), data.get('quantity'),
                          data.get('rate'))
        await bot.send_message(message.from_user.id,
                               text='В скором времени администраторы проверят вашу оплату и выставят ваш слот на продажу\n'
                                    'Проверить выставленный товар можно в меню "Мои товары"',
                               reply_markup=menu_back_main)
    else:
        await bot.send_message(message.from_user.id, text='товар удален', reply_markup=menu_back_main)
    await state.finish()

# k = await db.presence_user(call.from_user.id)
# if k == 1:
#     await call.message.edit_text("Меню продавца")
# else:
#     await call.message.edit_text('Вы не продавец, вернитесь к главноему меню', reply_markup=menu_back_main)
@dp.callback_query_handler(text_contains='prov')
async def prov(call: CallbackQuery):
    await bot.send_message(text=f"{call.message.from_user.id}", reply_markup=seller_menu)