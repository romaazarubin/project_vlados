from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from keyboards.admin_keyboard.admin import cb

cb_product = CallbackData("cart_product", "action", "user_id", "good","status")
cb_status_true = CallbackData("info_btn", "status", "user_id", "good")
cb_back_to_cart = CallbackData('back', 'back_to_cart', "user_id", "good")
cb_payment_confirmation = CallbackData('payment', "action", "name_good", "value", "user_id")


def menu_product(data, user_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    for i in data:
        name_good = i['name_good']
        quatity_good = round(i['quantity'],2)
        rate_good = i['rate']
        status = i["status"]
        currency = i["currency"]
        btn_product = InlineKeyboardButton(text=f'Продукт: {name_good}, кол-во: {quatity_good}, курс:{rate_good}',
                                           callback_data=cb_product.new(action='info',
                                                                        user_id=user_id,
                                                                        good=name_good,
                                                                        status=status))
        markup.add(btn_product)
    return markup


def keyboard_status_false(status, user_id, good):
    if status.lower() == 'status_true':
        text = 'Оплата подтверждена'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=text, callback_data='confirmed')
                ],
                [
                    InlineKeyboardButton(text='Вернуться обратно к товарам',
                                         callback_data=cb_back_to_cart.new(back_to_cart='back_to_cart',
                                                                           user_id=user_id,
                                                                           good=good))

                ],
                [
                    InlineKeyboardButton(text='Удалить товар',
                                         callback_data=cb.new(action='delete_product',
                                                              user_id=user_id,
                                                              good=good))
                ]
            ]
        )
    else:
        text = 'Оплата не подтверждена'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=text, callback_data='empty')
                ],
                [
                    InlineKeyboardButton(text='Проверить еще раз',
                                         callback_data=cb_status_true.new(status='unconfirmed',
                                                                          user_id=user_id,
                                                                          good=good))
                ],
                [
                    InlineKeyboardButton(text='Вернуться обратно к товарам',
                                         callback_data=cb_back_to_cart.new(back_to_cart='back_to_cart',
                                                                           user_id=user_id,
                                                                           good=good))
                ],
                [
                    InlineKeyboardButton(text='Удалить товар',
                                         callback_data=cb.new(action='delete_product',
                                                              user_id=user_id,
                                                              good=good))
                ]

            ]
        )
    return markup


def payment_confirmation(name_good, value, user_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Оплата прошла, товар был отправлен',
                                     callback_data=cb_payment_confirmation.new(action='payment',
                                                                               name_good=name_good,
                                                                               value=value,
                                                                               user_id=user_id))
            ]
        ]
    )
    markup.add(InlineKeyboardButton(text='Оплата не прошла, удалить заявку',
                                    callback_data=cb_payment_confirmation.new(action='cancellation',
                                                                              name_good=name_good,
                                                                              value=value,
                                                                              user_id=user_id)))
    return markup
