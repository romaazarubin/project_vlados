from aiogram.dispatcher.filters import Command, Text
from bot.main import dp, bot
from aiogram.types import Message
from bot.keyboards.Reply_markup.start_menu import menu
from aiogram.dispatcher import FSMContext
@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите роль',
                           reply_markup=menu)

@dp.message_handler(Text(equals='Вернуться на главное меню'), state=None)
async def seller(message: Message):
    await bot.send_message(message.from_user.id, text='Выберите роль', reply_markup=menu)

@dp.message_handler(Text(equals='Выход из поиска'))
async def exit(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, text='Выберите роль', reply_markup=menu)