import Chip

class Player:
    def __init__(self, color):
        self.chips = []
        self.isMove = True
        for i in range(15):
            chip = Chip.Chip(1, 1, color)
            self.chips.append(chip)
        self.dice_values = [0, 0]

    def make_move(self):
        dice_sum = sum(self.dice_values)
        