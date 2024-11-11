import Chip

class Player:
    def __init__(self, color):
        self.chips = []
        self.isMove = True
        self.count_of_thrown = 0
        for i in range(15):
            chip = Chip.Chip(1, 1, color)
            self.chips.append(chip)
        self.dice_values = [0, 0]

    def make_move(self):
        dice_sum = sum(self.dice_values)

    def get_data(self):
        return {
            "chips": [chip.get_data() for chip in self.chips],
            "count_of_thrown": self.count_of_thrown,
            "dice_values": self.dice_values
        }