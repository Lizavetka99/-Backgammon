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


