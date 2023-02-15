from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

select_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Поиск по названию товара', callback_data='search_by_name')
        ],
        [
            InlineKeyboardButton(text='Все товары', callback_data='all_good1')
        ],
        [
            InlineKeyboardButton(text='Вернуться на выбор роли', callback_data='choosing_role')
        ]
    ]
)

back_button = InlineKeyboardMarkup()
back_button.add(InlineKeyboardButton(text='Назад', callback_data='back_search_sellers'))

