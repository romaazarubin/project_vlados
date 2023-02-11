from aiogram.dispatcher.filters import Command, Text
from main import dp, bot, db
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from state.state_admin import Edit, Price_admin
from config import admin_id
from keyboards.admin_keyboard.edit_data import menu_back, menu_edit


@dp.message_handler(Command('admin'))
async def start(message: Message):
    if message.from_user.id == admin_id:
        try:
            await db.add_admin(message.from_user.id)
        except Exception as e:
            pass
        finally:
            await bot.send_message(chat_id=message.from_user.id,
                                   text='Меню',
                                   reply_markup=menu_edit)
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом')


@dp.message_handler(Text(equals='Изменить счет оплаты'), state=None)
async def change(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        if message.text == 'Вернуться назад':
            await state.finish()
            await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
        else:
            await bot.send_message(admin_id, text='Введите номер кошелька', reply_markup=menu_back)
            await Edit.step_wallet.set()
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом')


@dp.message_handler(state=Edit.step_wallet)
async def step_wallet(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        if message.text.lower() == 'вернуться назад' or '/' in message.text:
            await bot.send_message(admin_id,
                                   text='Меню',
                                   reply_markup=menu_edit)
            await state.finish()
        else:
            await db.edit_wallet_admin(admin_id, message.text)
            await bot.send_message(admin_id, text='Номер изменен', reply_markup=menu_edit)
            await state.finish()
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом')


@dp.message_handler(Text(equals='Показать мой кошелек'))
async def change(message: Message):
    if message.from_user.id == admin_id:
        wallet = await db.wallet_admun(admin_id)
        await bot.send_message(admin_id, text=f'Ваш номер кошелька:{wallet}', reply_markup=menu_back)
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом')


@dp.message_handler(Text(equals='Вернуться назад'))
async def change(message: Message):
    if message.from_user.id == admin_id:
        await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом')


@dp.message_handler(Text(equals='Изменить стоимость выставление товара и валюту'), state=None)
async def change(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        await bot.send_message(admin_id, text='Введите цену за выставление товара')
        await Price_admin.step_price.set()
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом!')


@dp.message_handler(state=Price_admin.step_price)
async def change(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        if len(message.text.split()) > 1:
            if message.text == 'Вернуться назад':
                await state.finish()
                await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
            else:
                await bot.send_message(admin_id, text='Введите цену без валюты! Без пробела!')
        else:
            if message.text == '/start' or message.text == '/help' or message.text == '/admin' or '/' in message.text:
                await state.finish()
                await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
            else:
                await state.update_data(
                    {
                        'price': message.text
                    }
                )
                await bot.send_message(admin_id, text='Введите валюту')
                await Price_admin.step_currency.set()
    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом!')


@dp.message_handler(state=Price_admin.step_currency)
async def change(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        if len(message.text.split()) > 1:
            if message.text == 'Вернуться назад':
                await state.finish()
                await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
            else:
                await bot.send_message(admin_id, text='Введите только валюту! Без пробела!')
        else:
            if message.text == '/start' or message.text == '/help' or message.text == '/admin' or '/' in message.text:
                await state.finish()
                await bot.send_message(admin_id, text='Меню', reply_markup=menu_edit)
            else:
                data = await state.get_data()
                await db.edit_price_admin(message.from_user.id, data.get('price'), message.text)
                await state.finish()
                await bot.send_message(admin_id, text='Изменения сохранены', reply_markup=menu_edit)

    else:
        await bot.send_message(message.from_user.id, text='Вы не являетесь админом!')
