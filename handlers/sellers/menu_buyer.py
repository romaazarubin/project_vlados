from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, ReplyKeyboardRemove
from keyboards.seller_menu.entry_menu import product_display
from keyboards.buyer_menu.basic_menu import menu_basic
from keyboards.Reply_markup.start_menu import seller_menu, menu, menu_back_main
from aiogram.dispatcher import FSMContext
from state.state_buy import Buy


@dp.message_handler(Text(equals='Покупатель'))
async def buyer(message: Message):
    await bot.send_message(message.from_user.id, text='меню', reply_markup=menu_basic)


@dp.message_handler(Text(equals='Покупка'), state=None)
async def buy(message: Message):
    await bot.send_message(message.from_user.id, text='Введите ник продавца', reply_markup=ReplyKeyboardRemove())

    await Buy.step_search.set()


@dp.message_handler(state=Buy.step_search)
async def name_buyer(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {
            'name': name
        }
    )
    rows = await db.good(name)
    cart = []
    for i in rows:
        good = i
        name_good = good['name_good']
        quatity_good = good['quantity']
        rate_good = good['rate']
        get_good = f'Товар: {name_good}, Количество: {quatity_good}, курс: {rate_good}'
        cart.append(get_good)
    text = ''
    count = len(cart)
    for t in range(count):
        text += f"{cart[t]}\n"

    await bot.send_message(message.from_user.id, text=text)
    await bot.send_message(message.from_user.id, text='Введите количество товара')
    await Buy.step_value.set()


@dp.message_handler(state=Buy.step_value)
async def val(message: Message, state: FSMContext):
    value = int(message.text)
    data = await state.get_data()
    quantity = await db.quantity(data['name'])
    if value > int(quantity):
        await bot.send_message(message.from_user.id, text='Вы привысили количество товара')
        #await Buy.step_search.set()
    else:
        await state.update_data(
            {
                'value': value
            }
        )
        rows = await db.price(data['name'])
        cart = []
        for i in rows:
            good = i
            cart.append(good['rate'])
            cart.append(good['wallet'])
            cart.append(good['user_id'])
        await bot.send_message(message.from_user.id,
                               text=f'Оплатите {int(cart[0]) * value} на данный кошелек {cart[1]} '
                                                          f',указав в информации платежа свой ник тг, '
                                                          f'и дождитесь отправки товара',
                               reply_markup=menu)
        await db.edit_quantity(cart[2], value)
        await bot.send_message(cart[2], text=f'{message.from_user.username} оплачивает товар на кошелек {cart[1]} '
                                             f'в размере {int(cart[0]) * value}')
        await state.finish()
