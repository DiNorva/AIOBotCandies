from random import randint as r

players = 0
player_take = 0
set_none = 0
set_total = 1
set_turn = 2
set_dif = 3
low_dif = 0
hard_dif = 1
total_candies = 150
min_candies = 50
max_candies = 300
max_take = 28

setting: int = set_none
difficulty: int = low_dif
candies: int = 0
is_player_turn: bool = None


def reset_game():
    global candies, is_player_turn, setting
    candies = total_candies
    is_player_turn = None
    setting = set_none


def change_player():
    global is_player_turn
    is_player_turn = r(0, 1) == player_take if is_player_turn == None else not is_player_turn
    return is_player_turn


def get_max_take():
    global candies, max_take
    get_max = candies if candies <= max_take else max_take
    return get_max


def get_candies():
    global candies
    return candies


def bot_take():
    global candies, max_take
    if candies == total_candies:
        bot_get = r(1, max_take)
        candies -= bot_get
        return bot_get
    bot_get = candies
    if candies > max_take:
        bot_get = (candies - 1) % max_take
        if bot_get == 0 or difficulty == low_dif:
            bot_get = r(1, max_take)
    candies -= bot_get
    return bot_get


def get_player(count: int):
    global candies
    candies -= count


def no_game():
    global candies, is_player_turn
    candies = 0
    is_player_turn = None


def set_max_take(count: int):
    global max_take, setting
    max_take = count
    setting = set_none


def set_total_candies(count: int):
    global total_candies, setting
    total_candies = count
    setting = set_none


def set_difficulty(new_difficulty: int):
    global difficulty, setting
    difficulty = new_difficulty
    setting = set_none


def reset_settings():
    global setting
    setting = set_none


def activate_setting(set_mode: int):
    global setting
    setting = set_mode


def get_setting_mode():
    global setting
    return setting


def get_start_total():
    global total_candies
    return total_candies


def get_cur_max():
    global max_take
    return max_take
