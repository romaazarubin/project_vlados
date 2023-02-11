from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cd_value_product = CallbackData('cd_value', 'action', 'user_id', 'name_good', 'rate_good','quantity')
cd_buy_product = CallbackData('cd_buy', 'action', 'user_id', 'name_good', 'value')


def menu_product_for_buyer(data):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for i in data:
        user_id = i['user_id']
        name_good = i['name_good']
        quatity_good = i['quantity']
        rate_good = i['rate']
        status = i["status"]
        quantity = i["quantity"]
        if status:
            btn_product = InlineKeyboardButton(text=f'Продукт: {name_good}, кол-во: {quatity_good}, курс:{rate_good}',
                                               callback_data=cd_value_product.new(action='value',
                                                                                  user_id=user_id,
                                                                                  name_good=name_good,
                                                                                  rate_good=rate_good,
                                                                                  quantity=quantity))
            markup.add(btn_product)
    btn_back_search_sellers = InlineKeyboardButton(text='Назад', callback_data='back_search_sellers')
    markup.add(btn_back_search_sellers)
    return markup


def keyboard_buy(user_id, name_good, value):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    btn_product_buy = InlineKeyboardButton(text='Проверить оплату',
                                           callback_data=cd_buy_product.new(action='buy',
                                                                            user_id=user_id,
                                                                            name_good=name_good,
                                                                            value=value))
    btn_back_main_menu = InlineKeyboardButton(text='Отменить покупку', callback_data='btn_back_main_menu')
    markup.add(btn_product_buy, btn_back_main_menu)
    return markup
