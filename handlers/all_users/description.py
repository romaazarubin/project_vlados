from aiogram import types

def set_default_commands(dp):
    return dp.bot.set_my_commands([
        types.BotCommand("start", "В случае зависание бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("admin", "Меню администратора"),
    ])