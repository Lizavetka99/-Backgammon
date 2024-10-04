import Chip_data
import Chip_data as data
import pygame
import image_settings as img_data

class Chip:
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.owner = owner
        self.texture = data.textures_dict[owner]
        self.is_dragging = False
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position_number = 0

    def create_help_chips(self, dice_values):
        helps_chips = []

        x, y = Chip_data.help_chips[self.position_number + dice_values[0] + 1]
        help = Chip(x, y, "help")
        help.position_number = dice_values[0] + 1
        helps_chips.append(help)
        x, y = Chip_data.help_chips[self.position_number + dice_values[1] + 1]
        help = Chip(x, y, "help")
        help.position_number = dice_values[1] + 1
        helps_chips.append(help)
        x, y = Chip_data.help_chips[self.position_number + sum(dice_values) + 2]
        help = Chip(x, y, "help")
        help.position_number = sum(dice_values) + 2
        helps_chips.append(help)
        return helps_chips