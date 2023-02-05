from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice
from keyboards.menu_basic.start_menu import menu_main, menu_back_main

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите роль',
                           reply_markup=menu_main)

@dp.callback_query_handler(text_contains='main_menu')
async def seller(call: CallbackQuery):
    await call.message.edit_text(text='Выберите роль', reply_markup=menu_main)