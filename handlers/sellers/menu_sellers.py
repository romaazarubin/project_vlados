from aiogram.dispatcher.filters import Text
from main import dp, bot, db
from aiogram.types import Message
from keyboards.Reply_markup.start_menu import menu_back_main, seller_menu, menu_basic
from keyboards.Reply_markup.stop_prod import menu_stop
from keyboards.admin_keyboard.admin import genmarkup
from aiogram.dispatcher import FSMContext
from state.state_sell import Sell
from keyboards.seller_menu.product import menu_product
from config import admin_id


@dp.message_handler(Text(equals='Продавец'))
async def seller(message: Message):
    try:
        await db.add_user(message.from_user.id, message.from_user.username)
    except Exception as e:
        pass
    finally:
        await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)


@dp.message_handler(Text(equals='Выставить на продажу'), state=None)
async def sale(message: Message):
    await bot.send_message(message.from_user.id, text='Введите название товара, максимальная длинна 10 симповолов',
                           reply_markup=menu_stop)
    await Sell.step_name.set()


@dp.message_handler(Text(equals='Мои товары'))
async def cart(message: Message):
    try:
        cart_product = await db.cart(message.from_user.id)
        await bot.send_message(message.from_user.id, text='Ваши товары',
                               reply_markup=menu_product(cart_product, message.from_user.id))
    except:
        await bot.send_message(message.from_user.id, text='Произошла ошибка')


@dp.message_handler(state=Sell.step_name)
async def state_name(message: Message, state: FSMContext):
    name = message.text.lower()
    if message.text == 'Отменить выставлениe' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)
        await state.finish()

    else:
        if name.isdecimal():
            await bot.send_message(message.from_user.id, text='Название товара должны быть буквами! повторите попытку')
            await Sell.step_name.set()
        else:
            if len(name) > 10:
                await bot.send_message(message.from_user.id,
                                       text='Вы превысили длинну, введите название товара повторно')
                await Sell.step_name.set()
            else:
                await state.update_data(
                    {
                        'name': name
                    }
                )
                await bot.send_message(message.from_user.id, text='Введите количество товара, если число не целое, '
                                                                  'то вводите через точку')
                await Sell.step_quantity.set()


@dp.message_handler(state=Sell.step_quantity)
async def sell_step_quantity(message: Message, state: FSMContext):
    quantity = message.text.lower()
    if message.text == 'Отменить выставлениe' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)
        await state.finish()

    else:
        if quantity.replace(".", "").isdigit():
            if len(quantity) > 10:
                await bot.send_message(message.from_user.id,
                                       text='Вы превысили длинну, введите количество товара повторно')
                await Sell.step_quantity.set()
            else:
                await state.update_data(
                    {
                        'quantity': quantity
                    }
                )
                await bot.send_message(message.from_user.id, text='Введите валюту')

                await Sell.step_currency.set()
        else:
            await bot.send_message(message.from_user.id, text='Вы ввели не число, повторите попытку')
            await Sell.step_quantity.set()


@dp.message_handler(state=Sell.step_currency)
async def sell_step_quantity(message: Message, state: FSMContext):
    currency = message.text.lower()
    if message.text == 'Отменить выставлениe' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)
        await state.finish()
    else:
        if currency.isdecimal():
            await bot.send_message(message.from_user.id, text='Курс должнен состоять из букв! повторите попытку')
            await Sell.step_currency.set()
        else:
            if len(currency) > 10:
                await bot.send_message(message.from_user.id,
                                       text='Вы превысили длинну, введите количество товара повторно')
                await Sell.step_quantity.set()
            else:
                await state.update_data(
                    {
                        'currency': currency
                    }
                )
                await bot.send_message(message.from_user.id, text='Введите курс, если число не целое, '
                                                                  'то вводите через точку')

                await Sell.step_rate.set()


@dp.message_handler(state=Sell.step_rate)
async def sell_step_rate(message: Message, state: FSMContext):
    rate = message.text.lower()
    if message.text == 'Отменить выставлениe' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)
        await state.finish()

    else:
        if rate.replace(".", "").isdigit():
            if len(rate) > 10:
                await bot.send_message(message.from_user.id, text='Вы превысили длинну, введите курс товара повторно')
                await Sell.step_rate.set()
            else:
                await state.update_data(
                    {
                        'rate': rate
                    }
                )
                await bot.send_message(message.from_user.id, text='Введите ваш кошелек')
                await Sell.step_wallet.set()
        else:
            await bot.send_message(message.from_user.id, text='Вы ввели не число')
            await Sell.step_rate.set()


@dp.message_handler(state=Sell.step_wallet)
async def sell_step_wallet(message: Message, state: FSMContext):
    try:
        if message.text == 'Отменить выставлениe' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
            await bot.send_message(message.from_user.id, message.text, reply_markup=seller_menu)
            await state.finish()
        else:
            rows = await db.take_price(admin_id=admin_id)
            for i in rows:
                price = i['price']
                currency = i['currency']
                wallet_admin = i['wallet_admin']
            wallet = message.text.lower()
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
                                                              f"Выставление товара платное. Оплатите {price} {currency} "
                                                              f"на {wallet_admin} кошелек,"
                                                              f" в комментарии к транзакции укажите ваше имя в TG",
                                   reply_markup=menu_basic)
            await Sell.step_pay.set()
    except:
        await bot.send_message(message.from_user.id, 'Произошла ошибка', reply_markup=seller_menu)
        await state.finish()


@dp.message_handler(state=Sell.step_pay)
async def sell_step_pay(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == 'Оплатить и выставить' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        try:
            await db.add_good(message.from_user.id, message.from_user.username, data.get('name'), data.get('quantity'),
                              data.get('currency'), data.get('rate'), data.get('wallet'))
            await bot.send_message(admin_id,
                                   text=f'Пользователь {message.from_user.username} проверяет оплату '
                                        f'на выставление товара {data.get("name")}',
                                   reply_markup=genmarkup(message.from_user.id, data.get('name')))
            await bot.send_message(message.from_user.id,
                                   text='В скором времени администраторы проверят вашу оплату '
                                        'и выставят ваш слот на продажу\n'
                                        'Проверить выставленный товар можно в меню "Мои товары"',
                                   reply_markup=menu_back_main)
        except:
            await bot.send_message(message.from_user.id,
                                   text='Вы ввели неправильные значение в информации о товаре',
                                   reply_markup=menu_back_main)
    else:
        await bot.send_message(message.from_user.id, text='товар удален', reply_markup=menu_back_main)
    await state.finish()
