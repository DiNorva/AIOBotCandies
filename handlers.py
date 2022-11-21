
from aiogram import types, Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.startGame, commands=['start', 'пуск', 'on'])
    dp.register_message_handler(commands.finishGame, commands=['finish'])
    dp.register_message_handler(commands.newGame, commands=['new'])
    dp.register_message_handler(commands.setting, commands=['settings'])
    dp.register_message_handler(commands.setTotal, commands=['candies'])
    dp.register_message_handler(commands.setMax, commands=['max'])
    dp.register_message_handler(commands.setDifficulty, commands=['difficulty'])
    dp.register_message_handler(commands.cancelSettings, commands=['cancel'])
    dp.register_message_handler(commands.setLow, commands=['low'])
    dp.register_message_handler(commands.setHard, commands=['hard'])
    dp.register_message_handler(commands.getNumber)

    # dp.register_message_handler(commands.player_turn)
