from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData("cart", "action", "user_id", "good")


def genmarkup(user_id, good):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(text='Оплата прошла', callback_data=cb.new(action='add', user_id=user_id, good=good)))
    markup.add(InlineKeyboardButton(text='Оплата не прошла',
                                    callback_data=cb.new(action='delete', user_id=user_id, good=good)))
    return markup
