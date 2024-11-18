import Chip_data
import Chip_data as data
import pygame
import image_settings as img_data

count_of_occupied = dict()
for i in range(0, 24):
    count_of_occupied[i] = 0
count_of_occupied[0] = 15
count_of_occupied[12] = 15

owner_of_occupied = dict()
for i in range(0, 24):
    owner_of_occupied[i] = None
owner_of_occupied[0] = "white"
owner_of_occupied[12] = "black"


def get_data_list():
    print(count_of_occupied)
    return {"count_of_occupied": count_of_occupied,
            "owner_of_occupied": owner_of_occupied}


class Chip:

    def __init__(self, x, y, owner, count_moves=0, position_number=None, can_move=False):
        self.x = x
        self.y = y
        self.count_moves = count_moves
        self.owner = owner
        self.texture = data.textures_dict[owner]
        self.is_dragging = False
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_throw = False
        self.current_dice_value = 0
        if position_number is None:
            if owner == "white":
                self.position_number = 0
            else:
                self.position_number = 12
        else:
            self.position_number = position_number
        self.can_move = can_move

    def create_help_chips(self, dice_values, black_chips, white_chips, player):
        helps_chips = []
        is_thrown = False
        for value in (player.dice_values + [sum(player.dice_values)]):
            if (value + 1 + self.count_moves) == 24:
                throw_chip = Chip(440, 500, "help")
                throw_chip.is_throw = True
                throw_chip.current_dice_value = value + 1
                helps_chips.append(throw_chip)
                is_thrown = True
        if (dice_values[0] + 1 + self.count_moves) != 24:
            if (self.count_moves + dice_values[0] + 1) < 24 and dice_values[0] != -1:
                x, y = Chip_data.help_chips[(self.position_number + dice_values[0] + 1) % 24]
                if 12 <= (self.position_number + dice_values[0] + 1) % 24 <= 23:
                    y = 75 + 15 * count_of_occupied[(self.position_number + dice_values[0] + 1) % 24]
                else:
                    y = 615 - 15 * count_of_occupied[(self.position_number + dice_values[0] + 1) % 24]
                help = Chip(x, y, "help")
                help.position_number = (dice_values[0] + 1 + self.position_number) % 24
                is_occupied_by_enemy = False
                if owner_of_occupied[help.position_number] == "white" and self.owner == "black" \
                        or owner_of_occupied[help.position_number] == "black" and self.owner == "white":
                    is_occupied_by_enemy = True
                if not is_occupied_by_enemy:
                    help.current_dice_value = dice_values[0] + 1
                    helps_chips.append(help)
        if (dice_values[1] + 1 + self.count_moves) != 24:
            if (self.count_moves + dice_values[1] + 1) < 24 and dice_values[0] != dice_values[1] and dice_values[
                1] != -1:
                x, y = Chip_data.help_chips[(self.position_number + dice_values[1] + 1) % 24]
                if 12 <= (self.position_number + dice_values[1] + 1) % 24 <= 23:
                    y = 75 + 15 * count_of_occupied[(self.position_number + dice_values[1] + 1) % 24]
                else:
                    y = 615 - 15 * count_of_occupied[(self.position_number + dice_values[1] + 1) % 24]

                help = Chip(x, y, "help")
                help.position_number = (dice_values[1] + 1 + self.position_number) % 24
                is_occupied_by_enemy = False
                if owner_of_occupied[help.position_number] == "white" and self.owner == "black" \
                        or owner_of_occupied[help.position_number] == "black" and self.owner == "white":
                    is_occupied_by_enemy = True
                if not is_occupied_by_enemy:
                    help.current_dice_value = dice_values[1] + 1
                    helps_chips.append(help)
        if ((dice_values[0] + dice_values[1] + 2 + self.count_moves) != 24):
            if (self.count_moves + dice_values[0] + dice_values[1] + 2) < 24 and dice_values[0] != dice_values[1] and \
                    dice_values[0] != -1:
                x, y = Chip_data.help_chips[(self.position_number + sum(dice_values) + 2) % 24]
                if 12 <= (self.position_number + sum(dice_values) + 2) % 24 <= 23:
                    y = 75 + 15 * count_of_occupied[(self.position_number + sum(dice_values) + 2) % 24]
                else:
                    y = 615 - 15 * count_of_occupied[(self.position_number + sum(dice_values) + 2) % 24]
                help = Chip(x, y, "help")
                help.position_number = (sum(dice_values) + 2 + self.position_number) % 24
                is_occupied_by_enemy = False
                if owner_of_occupied[help.position_number] == "white" and self.owner == "black" \
                        or owner_of_occupied[help.position_number] == "black" and self.owner == "white":
                    is_occupied_by_enemy = True
                if not is_occupied_by_enemy:
                    help.current_dice_value = dice_values[0] + dice_values[1] + 2
                    helps_chips.append(help)
        return helps_chips

    def get_data(self):
        return {
            "x": self.x,
            "y": self.y,
            "count_moves": self.count_moves,
            "owner": self.owner,
            "position_number": self.position_number,
            "can_move": self.can_move,
            "rect": self.rect,
            "current_dice_value": self.current_dice_value
        }
