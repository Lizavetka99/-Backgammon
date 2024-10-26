import Chip
from Dice import Dice
import Chip_data
import random

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

        print("enemy", self.dice_values)
        moves = 0
        any_can_move = False
        if self.dice_values[0] == self.dice_values[1]:
            moves = 4
        else:
            moves = 2
        i = 0
        while moves > 0:
            print("enemy moves", moves)
            for chip in Chip_data.white_chips[::-1]:
                i += 1
                helps = chip.create_help_chips(self.dice_values, black_chips, white_chips, self)
                print("enemy:", i, [j.current_dice_value for j in helps])
                if len(helps) == 0:
                    continue

                any_can_move = True
                print()
                random_help = random.randint(1, len(helps)) - 1
                print(random_help, "рандом хелп")
                if len(helps) > 0:
                    if (chip.position_number <= 23):
                        Chip.count_of_occupied[chip.position_number] -= 1
                        if Chip.count_of_occupied[chip.position_number] == 0:
                            Chip.owner_of_occupied[chip.position_number] = None
                    chip.count_moves += helps[random_help].current_dice_value
                    chip.rect = helps[random_help].rect

                    chip.x = helps[random_help].x
                    chip.y = helps[random_help].y
                    chip.position_number += helps[random_help].current_dice_value
                    if (chip.position_number <= 23):
                        Chip.count_of_occupied[chip.position_number] += 1
                        Chip.owner_of_occupied[chip.position_number] = "white"
                    print("bbb",helps[random_help].current_dice_value,  self.dice_values)
                    if len(self.dice_values) == 2 and helps[random_help].current_dice_value == self.dice_values[0] + self.dice_values[1] + 2:
                        moves = 0
                    else:
                        moves -= 1
                        if len(self.dice_values) == 2 and (self.dice_values[0] != self.dice_values[1]):
                            if helps[random_help].current_dice_value - 1 == self.dice_values[0]:
                                self.dice_values.remove(self.dice_values[0])
                                self.dice_values.append(-1)

                            else:
                                self.dice_values.remove(self.dice_values[1])
                                self.dice_values.append(-1)

                    break
            if any_can_move == False:
                self.is_enemy_move = False
                self.is_enemy_move_throw_dices = False
                moves = 0
                break
        print(Chip.count_of_occupied)
        self.is_enemy_move = False
        return