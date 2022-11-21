from aiogram import types
from create_bot import bot


async def hello(message: types.Message, total: int, max: int):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!\n'
                                                 f'Давай поиграем в игру "Конфетки"!\n'
                                                 f'Правила просты: на столе лежит {total} конфет. '
                                                 f'Играют два игрока, делая ход друг за другом. '
                                                 f'За один ход можно забрать максимум {max} конфет. '
                                                 f'Победит тот, кто заберёт оставшиеся на столе конфеты последним.\n'
                                                 f'Удачи!\n\n'
                                                 f'/new - начать новую игру\n/finish - завершить игру\n/settings - показать настройки')


async def other_value(message: types.Message):
    await bot.send_message(message.from_user.id, f'Так делать нельзя!')


async def bye(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, пока!')


async def playerTurn(message: types.Message, count: int, maxGet: int):
    await bot.send_message(message.from_user.id, f'На столе {count} конфет.\nТвой ход! '
                                                 f'Сколько конфет ты возьмешь от 1-{maxGet}?')


async def botTurn(message: types.Message, count: int, get: int):
    await bot.send_message(message.from_user.id,
                           f'На столе осталось {count} конфет.\nЯ забираю {get}.')


async def endOfTheGame(message: types.Message, winPlayer: bool):
    await bot.send_message(message.from_user.id,
                           f'На столе не осталось конфет...')
    if winPlayer:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name},ты победил(а) меня, поздравляю!\n'
                               f'Если хочешь сыграть ещё раз, набери команду /new\n'
                               f'а если захочешь поменять настройки, нажми /settings')
    else:
        await bot.send_message(message.from_user.id,
                               f'Я победил тебя, {message.from_user.first_name}.\n'
                               f'Если хочешь сыграть ещё раз, набери команду /new\n'
                               f'а если захочешь поменять настройки, нажми /settings')


async def endThisGame(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Для вызова настроек закончи текущую игру')


async def showSettings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, что ты хочешь поменять?\n'
                           f'/candies - начальное количество конфет на столе\n'
                           f'/max - максимальное количество конфет, которое можно взять за ход\n'
                           f'/difficulty - уровень сложности')


async def changeTotal(message: types.Message, count: int):
    await bot.send_message(message.from_user.id,
                           f'Сейчас на столе лежит {count} конфет.\n'
                           f'Введи новое количество конфет на столе (50 - 300), '
                           f'или нажми /cancel для отмены.')


async def changeMax(message: types.Message, count: int, totalCount):
    await bot.send_message(message.from_user.id,
                           f'Сейчас максимально за ход можно взять {count} конфет.\n'
                           f'Введите новое количество (2-{totalCount - 1}) '
                           f'или нажми /cancel для отмены.')


async def changeDifficulty(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Выбери сложность игры:\n'
                           f'/low - лёгкий уровень\n'
                           f'/hard - сложный уровень')
