from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice
from keyboards.menu_basic.start_menu import menu_back_main
#from keyboards.seller_menu.entry_menu import firts_lvl
from state.state_input import Input_prof


# @dp.callback_query_handler(text_contains='input', state=None)
# async def input_1(call: CallbackQuery):
#     # t = await db.sel(call.from_user.id)
#     # await call.message.answer(text=t)
#
#     await call.message.edit_text(text='Введите логин')
#
#     await Input_prof.step1.set()
#
#
# @dp.message_handler(state=Input_prof.step1)
# async def input_2(message: Message, state: FSMContext):
#     login = message.text
#     k = await db.presence_user(message.from_user.id)
#     if k == login:
#         await state.update_data(
#             {
#                 'login': login
#             }
#         )
#         await bot.send_message(message.from_user.id, text="Введите пароль")
#
#         await Input_prof.step2.set()
#     else:
#         await bot.send_message('Такого пользователя нет, вам необходимо зарегистрироваться',
#                                reply_markup=menu_back_main)
#         await state.finish()
#
#
# @dp.message_handler(state=Input_prof.step2)
# async def input_3(message: Message, state: FSMContext):
#     password = message.text
#     password_db = await db.sel(message.from_user.id)
#     if password == password_db:
#
#         await bot.send_message(message.from_user.id, text="Вы успешно авторизовались")
#         await state.finish()
#     else:
#         await message.edit_text('Неправильный логин или пароль, попробуйте еще раз',
#                                 reply_markup=firts_lvl)
#         await state.finish()
