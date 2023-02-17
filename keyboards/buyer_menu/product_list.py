from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cd_value_product = CallbackData('cd_value', 'action', 'user_id', 'name_good', 'rate_good', 'quantity')
cd_buy_product = CallbackData('cd_buy', 'action', 'user_id', 'name_good', 'value')
cd_all_menu = CallbackData('cd_all_good', 'action', 'user_id', 'name_good', 'rate_good', 'quantity', 'step')
cd_good_next_menu = CallbackData('next', 'action', 'step')
cd_good_back_menu = CallbackData('back', 'action', 'step')
def menu_product_for_buyer(data):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for i in data:
        user_id = i['user_id']
        name_good = i['name_good']
        quantity_good = round((i["quantity"]), 2)
        rate_good = round(i['rate'], 2)
        status = i["status"]
        if status:
            btn_product = InlineKeyboardButton(text=f'Продукт: {name_good}, кол-во: {quantity_good}, курс:{rate_good}',
                                               callback_data=cd_value_product.new(action='value',
                                                                                  user_id=user_id,
                                                                                  name_good=name_good,
                                                                                  rate_good=rate_good,
                                                                                  quantity=quantity_good))
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


def all_product(data, count, step=0):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    k = step
    for i in data:
        user_id = i['user_id']
        name_good = i['name_good']
        quantity_good = round((i["quantity"]), 2)
        rate_good = round(i['rate'], 2)
        status = i["status"]
        if status:
            btn_product = InlineKeyboardButton(text=f'Продукт: {name_good}, кол-во: {quantity_good}, курс:{rate_good}',
                                               callback_data=cd_all_menu.new(action='value',
                                                                             user_id=user_id,
                                                                             name_good=name_good,
                                                                             rate_good=rate_good,
                                                                             quantity=quantity_good,
                                                                             step=k))
            markup.add(btn_product)
    btn_back_search_sellers = InlineKeyboardButton(text='Назад', callback_data='back_search_sellers')
    markup.add(btn_back_search_sellers)
    next = InlineKeyboardButton(text='>>>', callback_data=cd_good_next_menu.new(action='next',
                                                                                step=k + 5))
    back = InlineKeyboardButton(text='<<<', callback_data=cd_good_back_menu.new(action='back',
                                                                                step=k - 5))
    if k < 5:
        markup.add(next)
    elif count <= k:
        markup.add(back)
    else:
        markup.row(back, next)
    return markup
