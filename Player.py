import Chip

class Player:
    def __init__(self, color, count_of_thrown=0, dice_values=None):
        self.chips = []
        self.isMove = True
        self.count_of_thrown = count_of_thrown
        for i in range(15):
            chip = Chip.Chip(1, 1, color)
            self.chips.append(chip)
        if dice_values is None:
            self.dice_values = [0, 0]
        else: self.dice_values = dice_values

    def make_move(self):
        dice_sum = sum(self.dice_values)

    def get_data(self):
        return {
            #"player_chips": [chip.get_data() for chip in self.chips],
            "count_of_thrown": self.count_of_thrown,
            "player_dice_values": self.dice_values}