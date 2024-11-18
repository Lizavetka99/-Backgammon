import pickle
import os
import Chip
SAVE_FILE = "data.pickle"


def save(player, enemy, white_chips, black_chips, dict_dicts_main):
    player_dict = player.get_data()
    enemy_dict = enemy.get_data()

    white_chips_dict = {'white_chips': white_chips}
    black_chips_dict = {'black_chips': black_chips}
    diction = player_dict | enemy_dict
    #print(white_chips)
    diction = diction | white_chips_dict | black_chips_dict
    print(diction)
    save_game(diction)


def load(data):
    player_dict = {key: value for key, value in data.items() if key in ['count_of_thrown', 'player_dice_values']}
    enemy_dict = {key: value for key, value in data.items() if key in ['is_enemy_move', 'is_enemy_move_throw_dices',
                                                                       'throw_count',
                                                                       'enemy_dice_values']}
    print(2324, data)
    white_chips = data['white_chips']
    black_chips = data['black_chips']
    w_chips = []
    b_chips = []
    for i in range(len(white_chips)):

        white = Chip.Chip(white_chips[i]["x"], white_chips[i]["y"], white_chips[i]["owner"],
                                 white_chips[i]["count_moves"], white_chips[i]["position_number"],
                                 white_chips[i]["can_move"])
        white.rect = white_chips[i]["rect"]
        w_chips.append(white)
        black = Chip.Chip(black_chips[i]["x"], black_chips[i]["y"], black_chips[i]["owner"],
                                 black_chips[i]["count_moves"], black_chips[i]["position_number"],
                                 black_chips[i]["can_move"])
        black.rect = black_chips[i]["rect"]
        b_chips.append(black)
    # Chip.count_of_occupied = data["count_of_occupied"]
    # Chip.owner_of_occupied = data["owner_of_occupied"]
    print("мяу", Chip.count_of_occupied)
    #print(data["count_of_occupied"])
    return player_dict, enemy_dict, w_chips, b_chips


def save_game(data):
    with open(SAVE_FILE, 'wb') as file:
        print("save completed")
        print(data)

        pickle.dump(data, file)


def load_game():
    if os.path.exists('data.pickle') and os.path.getsize(SAVE_FILE) > 0:
        with open('data.pickle', 'rb') as file:
            data = pickle.load(file)
            return load(data)
    return None, None, None, None
