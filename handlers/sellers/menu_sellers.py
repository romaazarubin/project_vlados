from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, ReplyKeyboardRemove
#from keyboards.menu_basic.start_menu import menu_back_main
#from keyboards.seller_menu.entry_menu import seller_menu, menu_basic
from keyboards.Reply_markup.start_menu import menu_back_main, seller_menu, menu, menu_basic
from keyboards.admin_keyboard.admin import genmarkup
from aiogram.dispatcher import FSMContext
from state.state_sell import Sell




@dp.message_handler(Text(equals='Продавец'))
async def seller(message: Message):
    #await db.add_user(message.from_user.id, message.from_user.username)
    await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)

@dp.message_handler(Text(equals='Выставить на продажу'), state=None)
async def sale(message: Message):
    await bot.send_message(message.from_user.id, text='Введите название товара', reply_markup=ReplyKeyboardRemove())
    await Sell.step_name.set()


@dp.message_handler(state=Sell.step_name)
async def state_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {
            'name': name
        }
    )
    await bot.send_message(message.from_user.id, text='Введите количество товара')
    await Sell.step_quantity.set()

@dp.message_handler(state=Sell.step_quantity)
async def sell_step_quantity(message: Message, state: FSMContext):
    quantity = message.text
    await state.update_data(
        {
            'quantity': quantity
        }
    )
    await bot.send_message(message.from_user.id, text='Введите курс')

    await Sell.step_rate.set()


@dp.message_handler(state=Sell.step_rate)
async def sell_step_rate(message: Message, state: FSMContext):
    rate = message.text
    await state.update_data(
        {
            'rate': rate
        }
    )
    await bot.send_message(message.from_user.id, text='Введите ваш кошелек')
    await Sell.step_wallet.set()

@dp.message_handler(state=Sell.step_wallet)
async def sell_step_wallet(message: Message, state: FSMContext):
    wallet = message.text
    await state.update_data(
        {
            'wallet': wallet
        }
    )
    data = await state.get_data()
    await bot.send_message(message.from_user.id, text=f"Товар: {data.get('name')}\n"
                                                      f"Количество: {data.get('quantity')}\n"
                                                      f"Курс: {data.get('rate')}\n"
                                                      f"Кошелек: {data.get('wallet')}\n"
                                                      f"Выставление товара платное. Оплатите 5$ на счет "
                                                      f"543567834573",
                           reply_markup=menu_basic)
    await Sell.step_pay.set()

@dp.message_handler(state=Sell.step_pay)
async def sell_step_pay(message: Message, state: FSMContext):
    data = await state.get_data()
    #await bot.send_message(message.from_user.id, text="..", reply_markup=ReplyKeyboardRemove())
    if message.text == 'Оплатить и выставить':
        await bot.send_message(454279273,
                               text='Такой пользователь',
                               reply_markup=genmarkup(message.from_user.id, data.get('name')))
        #await db.add_good(message.from_user.id, message.from_user.username, data.get('name'), data.get('quantity'),
                          #data.get('rate'), data.get('wallet'))
        await bot.send_message(message.from_user.id,
                               text='В скором времени администраторы проверят вашу оплату и выставят ваш слот на продажу\n'
                                    'Проверить выставленный товар можно в меню "Мои товары"',
                               reply_markup=menu_back_main)
    else:
        await bot.send_message(message.from_user.id, text='товар удален', reply_markup=menu_back_main)
    await state.finish()
