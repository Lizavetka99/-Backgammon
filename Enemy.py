from Dice import Dice
import Chip_data

class Enemy:
    def __init__(self):
        self.is_enemy_move = False
        self.is_enemy_move_throw_dices = False
        self.dice_1 = []
        self.dice_2 = []
    def throw_dices(self):
        self.dice_1, self.dice_2 = Dice.throw(), Dice.throw()
        self.is_enemy_move_throw_dices = True

    def make_move(self):
        for chip in Chip_data.white_chips[::-1]:
            helps = chip.create_help_chips([self.dice_1[1], self.dice_2[1]])
            if len(helps) > 0:
                chip.rect = helps[0].rect
                chip.position_number = helps[0].position_number
                self.is_enemy_move = False
                break
        return