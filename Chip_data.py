import pygame, Chip
from image_settings import images_data as img_data

CHIPS_AMOUNT = 15

help_chips = [
(160, 615), (205, 615), (250, 615), (295, 615), (340, 615),
(385, 615), (490, 615), (535, 615), (580, 615), (625, 615),
(670, 615), (715, 615), (715, 75), (670, 75), (625, 75), (580, 75),
(535, 75), (490, 75), (385, 75), (340, 75), (295, 75), (250, 75),
(205, 75), (160, 75)
]

textures_dict = {
    "white": pygame.transform.scale(pygame.image.load("Assets/white_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
    "black": pygame.transform.scale(pygame.image.load("Assets/black_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
    "help": pygame.transform.scale(pygame.image.load("Assets/help_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
}


white_coordinates_start = [ (160, 615-15*i) for i in range(15)]
black_coordinates_start = [ (717, 75+15*i) for i in range(15)]

white_chips = []
black_chips = []


def spawn_chips(field):
    for i in range(CHIPS_AMOUNT):
        white_x, white_y = white_coordinates_start[i]
        black_x, black_y = black_coordinates_start[i]
        white_chips.append(Chip.Chip(white_x, white_y, "white"))
        print(len(white_chips))
        black_chip = Chip.Chip(black_x, black_y, "black")
        black_chip.position_number = 13 - 1
        black_chips.append(black_chip)



