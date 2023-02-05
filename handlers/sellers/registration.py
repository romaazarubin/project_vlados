from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice
from keyboards.menu_basic.start_menu import menu_back_main
#from keyboards.seller_menu.entry_menu import firts_lvl, finish_registration
from aiogram.dispatcher import FSMContext
from state.state_registr import Registration


# @dp.callback_query_handler(text_contains='registration', state=None)
# async def registration_1(call: CallbackQuery, state: FSMContext):
#     await call.message.edit_text(text='Введите логин')
#
#     await Registration.step_login.set()
#
#
# @dp.message_handler(state=Registration.step_login)
# async def registration_2(message: Message, state: FSMContext):
#     login = message.text
#     await state.update_data(
#         {
#             'login': login
#         }
#     )
#     await bot.send_message(message.from_user.id, text="Введите пароль")
#
#     await Registration.step_password.set()
#
#
# @dp.message_handler(state=Registration.step_password)
# async def registration_2(message: Message, state: FSMContext):
#     password = message.text
#     await state.update_data(
#         {
#             'password': password
#         }
#     )
#     await bot.send_message(message.from_user.id, text="Нажмите ктопку, чтобы завершить регистрацию",
#                            reply_markup=finish_registration)
#     await Registration.step3.set()
#
#
# @dp.callback_query_handler(text_contains='finish_registration', state=Registration.step3)
# async def registration_3(call: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     try:
#         await db.registration_user(call.from_user.id, call.from_user.username, data.get('login'),
#                                    data.get('password'))
#         await state.finish()
#
#         await call.message.edit_text(text='Вы успешно зарегистрировались, теперь вы можете войти',
#                                      reply_markup=firts_lvl)
#     except:
#         await call.message.edit_text(text='Такой пользователь уже существует',
#                                      reply_markup=firts_lvl)

