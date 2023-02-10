from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_stop = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отменить выставлениe'),
        ]
    ],
    resize_keyboard=True
)