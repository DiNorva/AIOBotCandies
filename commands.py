import view
from aiogram import types

import model


async def startGame(message: types.Message):
    model.no_game()
    await view.hello(message, model.get_start_total(), model.get_cur_max())


async def newGame(message: types.Message):
    model.reset_game()
    await nextMove(message)


async def finishGame(message: types.Message):
    await view.bye(message)


async def isNotInGame(message: types.Message):
    if (model.candies == 0):
        return True
    await view.endThisGame(message)
    return False


async def setting(message: types.Message):
    if await isNotInGame(message):
        await view.showSettings(message)


async def setTotal(message: types.Message):
    if await isNotInGame(message):
        model.activate_setting(model.set_total)
        await view.changeTotal(message, model.get_start_total())


async def setMax(message: types.Message):
    if await isNotInGame(message):
        model.activate_setting(model.set_turn)
        await view.changeMax(message, model.get_cur_max(), model.get_start_total())


async def setDifficulty(message: types.Message):
    if await isNotInGame(message):
        model.activate_setting(model.set_dif)
        await view.changeDifficulty(message)


async def cancelSettings(message: types.Message):
    await resetSettings(message)


async def setLow(message: types.Message):
    if await isNotInGame(message):
        model.set_difficulty(model.low_dif)
        await resetSettings(message)


async def setHard(message: types.Message):
    if await isNotInGame(message):
        model.set_difficulty(model.hard_dif)
        await resetSettings(message)


async def resetSettings(message: types.Message):
    model.reset_settings()
    await view.hello(message, model.get_start_total(), model.get_cur_max())


async def getNumber(message: types.Message):
    input = message.text
    if input.isnumeric():
        count = int(input)
        if model.get_candies() > 0:
            await playerTurn(message, count)
        else:
            match model.get_setting_mode():
                case model.set_total:
                    await setTotalCount(message, count)
                case model.set_turn:
                    await setMaxCount(message, count)


async def playerTurn(message: types.Message, count: int):
    if 0 < count <= model.get_cur_max():
        model.get_player(int(count))
        await nextMove(message)
    else:
        await view.other_value(message)


async def setTotalCount(message: types.Message, count: int):
    if model.min_candies <= count <= model.max_candies:
        model.set_total_candies(count)
        await resetSettings(message)
    else:
        await view.other_value(message)


async def setMaxCount(message: types.Message, count: int):
    if 1 < count < model.get_start_total():
        model.set_max_take(count)
        await resetSettings(message)
    else:
        await view.other_value(message)


async def nextMove(message: types.Message):
    if model.candies > 0:
        model.change_player()
        if model.is_player_turn:
            await view.playerTurn(message, model.candies, model.get_max_take())
        else:
            await view.botTurn(message, model.candies, model.bot_take())
            await nextMove(message)
    else:
        await endOfTheGame(message)


async def endOfTheGame(message: types.Message):
    await view.endOfTheGame(message, model.is_player_turn)
    model.no_game()
