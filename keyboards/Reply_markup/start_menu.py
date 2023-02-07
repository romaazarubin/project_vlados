from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продавец'),
        ],
        [
            KeyboardButton(text='Покупатель')
        ]
    ],
    resize_keyboard=True
)

seller_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мои товары')
        ],
        [
            KeyboardButton(text='Выставить на продажу')
        ],
        [
            KeyboardButton(text='Вернуться на главное меню')
        ]
    ],
    resize_keyboard=True
)

menu_back_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вернуться на главное меню')
        ]
    ],
    resize_keyboard=True
)