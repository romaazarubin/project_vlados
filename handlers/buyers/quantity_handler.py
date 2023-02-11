from main import dp, bot, db
from aiogram.types import Message, CallbackQuery
from state.state_buy import Buy
from keyboards.Reply_markup.start_menu import menu
from keyboards.buyer_menu.product_list import cd_value_product, keyboard_buy, cd_buy_product
from keyboards.seller_menu.product import payment_confirmation
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(cd_value_product.filter(action='value'))
async def value(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(
        {
            'user_id': callback_data.get('user_id'),
            'name_good': callback_data.get('name_good'),
            'rate_good': callback_data.get('rate_good'),
            'value': callback_data.get('quantity')
        }
    )
    await call.message.answer(text='Введите количество товара')
    await Buy.step_value.set()
@dp.message_handler(state=Buy.step_value)
async def step_value(message: Message, state: FSMContext):
    value_prod = message.text
    if message.text == 'Оплатить и выставить' or message.text == '/start' or message.text == '/help' or message.text == '/admin':
        await state.finish()
        await bot.send_message(message.from_user.id, text='Выберите роль', reply_markup=menu)
    else:
        data = await state.get_data()
        rows = await db.wallet_sellers_currency(data.get('user_id'), data.get("name_good"))
        for i in rows:
            wallet = i["wallet"]
            currency = i["currency"]
        if int(data.get('value')) < int(value_prod) or int(value_prod) == 0:
            await bot.send_message(message.from_user.id,
                                   text='Вы превысили количество товаров, укажите доступное кол-во товара')
            await Buy.step_value.set()
        else:
            await bot.send_message(message.from_user.id,
                                   text=f'Продукт:{data.get("name_good")}, кол-во: {value_prod}, курс:{data.get("rate_good")}\n'
                                        f'Итого вам нужно перевести на кошелек продавца {wallet}\n'
                                        f'сумму {float(data.get("rate_good")) * int(value_prod)}{currency}\n'
                                        f'На ваш кошелек, который вы указали при выборе роли покупателя придет товар',
                                   reply_markup=keyboard_buy(data.get('user_id'), data.get("name_good"), value_prod))
            await state.finish()


@dp.callback_query_handler(cd_buy_product.filter(action='buy'))
async def buy(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=None)
    await db.edit_value_buyer(callback_data.get('user_id'), callback_data.get('name_good'), callback_data.get('value'))
    await call.message.answer(text='Продавец в скором времени проверит оплату и отправит вам товар', reply_markup=menu)
    wallet_user = await db.wallet_user(call.from_user.id)
    await bot.send_message(callback_data.get('user_id'),
                           text=f'Покупатель {call.from_user.username} оплачивает '
                                f'и ждет свой товар - {callback_data.get("name_good")}\n'
                                f'в количестве {callback_data.get("value")} '
                                f'на кошелек {wallet_user}',
                           reply_markup=payment_confirmation(callback_data.get("name_good"),
                                                             callback_data.get("value"),
                                                             user_id=call.from_user.id))


@dp.callback_query_handler(text_contains='btn_back_main_menu')
async def btn_back_main_menu(call: CallbackQuery):
    await call.message.edit_text(text='Вы отменили покупку', reply_markup=None)
    await call.message.answer(text='Выберите роль', reply_markup=menu)
