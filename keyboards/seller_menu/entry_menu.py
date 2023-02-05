from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# firts_lvl = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Вход', callback_data='input')
#         ],
#         [
#             InlineKeyboardButton(text='Регистрация', callback_data='registration')
#         ]
#     ]
# )
#
# back_to_first_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Назад', callback_data='back_to_first_menu')
#         ]
#     ]
# )
#
# finish_registration = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Завершить регистрацию', callback_data='finish_registration')
#         ]
#     ]
# )
seller_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мои товары', callback_data='my_good')
        ],
        [
            InlineKeyboardButton(text='Выставить на продажу', callback_data='sell')
        ],
        [
            InlineKeyboardButton(text='<<<', callback_data='main_menu')
        ]
    ]
)
product_display = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатить и выставить', callback_data='pay')
        ],
        [
            InlineKeyboardButton(text='Отменить выставление, удалить товар', callback_data='delete_good')
        ]
    ]
)
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
    #one_time_keyboard=True
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Проверка', callback_data='prov')
        ]
    ]
)