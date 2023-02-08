from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice
from keyboards.Reply_markup.start_menu import menu

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите роль',
                           reply_markup=menu)

@dp.message_handler(Text(equals='Вернуться на главное меню'))
async def seller(message: Message):
    await bot.send_message(message.from_user.id, text='Выберите роль', reply_markup=menu)