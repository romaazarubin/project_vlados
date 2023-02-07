from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_basic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Покупка'),
        ]
    ],
    resize_keyboard=True
)