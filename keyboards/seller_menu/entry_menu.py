from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_basic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оплатить и выставить'),
        ],
        [
            KeyboardButton(text='Отменить выставление, удалить товар')
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
