from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_edit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Изменить счет оплаты'),
        ],
        [
            KeyboardButton(text='Показать мой кошелек'),
        ],
        [
            KeyboardButton(text='Изменить стоимость выставление товара и валюту'),
        ],
        [
            KeyboardButton(text='Вернуться назад')
        ]
    ],
    resize_keyboard=True
)

menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вернуться назад')
        ]
    ],
    resize_keyboard=True
)
