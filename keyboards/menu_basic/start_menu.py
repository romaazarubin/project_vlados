from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продавец', callback_data='seller')
        ],
        [
            InlineKeyboardButton(text='Покупатель', callback_data='buyer')
        ]
    ]
)
menu_back_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться на главное меню', callback_data='main_menu')
        ]
    ]
)