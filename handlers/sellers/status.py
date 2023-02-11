from main import dp, bot, db
from aiogram.types import CallbackQuery
from keyboards.seller_menu.product import cb_product, cb_status_true, keyboard_status_false, menu_product, \
    cb_back_to_cart, cb_payment_confirmation
from keyboards.admin_keyboard.admin import cb, genmarkup


@dp.callback_query_handler(cb_product.filter(action='info'))
async def info(call: CallbackQuery, callback_data: dict):
    if callback_data.get('status').lower() == 'true':
        await call.message.edit_text(text='Информация о товаре', reply_markup=keyboard_status_false('status_true',
                                                                                                    callback_data.get(
                                                                                                        'user_id'),
                                                                                                    callback_data.get(
                                                                                                        'good')))
    else:
        await call.message.edit_text(text='Информация о товаре', reply_markup=keyboard_status_false('status_false',
                                                                                                    callback_data.get(
                                                                                                        'user_id'),
                                                                                                    callback_data.get(
                                                                                                        'good')))


@dp.callback_query_handler(cb_back_to_cart.filter(back_to_cart='back_to_cart'))
async def back_to_cart1(call: CallbackQuery, callback_data: dict):
    cart_product = await db.cart(call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=menu_product(cart_product, callback_data.get('user_id')))


@dp.callback_query_handler(cb.filter(action='delete_product'))
async def delete_product(call: CallbackQuery, callback_data: dict):
    await db.delete_product(callback_data.get('user_id'), callback_data.get('good'))
    await call.message.answer(text='Товар удален')


@dp.callback_query_handler(cb_status_true.filter(status='unconfirmed'))
async def uncinfirmed(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Запрос отправлен на проверку повторно')
    await bot.send_message(454279273,
                           text=f'Пользователь {call.from_user.username} проверяет оплату '
                                f'на выставление товара {callback_data.get("good")}',

                           reply_markup=genmarkup(callback_data.get('user_id'), callback_data.get('good')))


@dp.callback_query_handler(cb_payment_confirmation.filter(action='payment'))
async def payment_confirmation(call: CallbackQuery, callback_data: dict):
    await call.message.edit_text(text='Операция прошла успешно')
    await bot.send_message(callback_data.get('user_id'), text='Продавец отправил вам товар')
    quantity = await db.check_value(call.from_user.id, callback_data.get('name_good'))
    if int(quantity) == 0:
        await db.delete_product(call.from_user.id, callback_data.get('name_good'))



@dp.callback_query_handler(cb_payment_confirmation.filter(action='cancellation'))
async def payment_confirmation(call: CallbackQuery, callback_data: dict):
    await db.edit_value_seller(call.from_user.id, callback_data.get('name_good'), callback_data.get('value'))
    await call.message.edit_text(text='продажа отменена')
    await bot.send_message(callback_data.get('user_id'),
                           text='Продавец удалил вашу заявку, т.к оплата не была произведена')
