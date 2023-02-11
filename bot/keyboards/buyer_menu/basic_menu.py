from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_basic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Покупка'),
        ],
        [
            KeyboardButton(text='Вернуться на главное меню')
        ]
    ],
    resize_keyboard=True
)

menu_basic_not_buy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вернуться на главное меню')
        ]
    ],
    resize_keyboard=True
)