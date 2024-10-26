import Chip
from Dice import Dice
import Chip_data

class Enemy:
    def __init__(self):
        self.is_enemy_move = False
        self.is_enemy_move_throw_dices = False
        self.dice_1 = []
        self.dice_2 = []
        self.dice_values = []
    def throw_dices(self):
        self.dice_1, self.dice_2 = Dice.throw(), Dice.throw()
        self.is_enemy_move_throw_dices = True
        self.dice_values = [self.dice_1[1], self.dice_2[1]]

    def make_move(self, black_chips, white_chips):
        for chip in Chip_data.white_chips[::-1]:
            helps = chip.create_help_chips([self.dice_1[1], self.dice_2[1]], black_chips, white_chips, self)
            print("ВРАГИ ПОМОЩЬ", len(helps))
            if len(helps) == 0:
                self.is_enemy_move = False
                self.is_enemy_move_throw_dices = False
            for help in helps:
                print(help.x, help.y)
            if len(helps) > 0:
                Chip.count_of_occupied[chip.position_number] -= 1
                if Chip.count_of_occupied[chip.position_number] == 0:
                    Chip.owner_of_occupied[chip.position_number] = None
                chip.count_moves += helps[0].current_dice_value
                chip.rect = helps[0].rect

                chip.x = helps[0].x
                chip.y = helps[0].y
                chip.position_number = helps[0].position_number
                Chip.count_of_occupied[chip.position_number] += 1
                Chip.owner_of_occupied[chip.position_number] = "white"

                self.is_enemy_move = False
                break
        return