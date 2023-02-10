from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

exit_search_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выход из поиска')
        ]
    ],
    resize_keyboard=True
)