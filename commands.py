
import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot


async def start(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await view.hello(message)
    await asyncio.sleep(3)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player(player)
    if (message.text).isdigit():
        if 0 < int(message.text) < 29:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await view.info(message, player_take, total)
            if model.check_win(total):
                await view.win_player(message, player)
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await view.wrong_take(message)
    else:
        await view.other_value(message)

async def enemy_turn(player):
    # emeny_take = await model.bot_take()
    # await model.set_total_candies(emeny_take)
    total_count = model.get_total_candies()
    if 0 > total_count < 29:
        enemy_take = total_count
    else:
        enemy_take = (total_count - 1) % 28

    total = total_count - enemy_take

    await view.bot_take(enemy_take)  # ?

    if model.check_win(total):
        await view.win_bot()  # ?
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(player)

async def await_player(player):
    max_take = model.get_max_take()
    await view.max_take_player(max_take)  #?

async def set_total_candies(message: types.Message):
    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет изменили на '
                                                 f'{count}')