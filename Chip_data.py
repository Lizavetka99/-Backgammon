import pygame, Chip
from image_settings import images_data as img_data

CHIPS_AMOUNT = 15

textures_dict = {
    "white": pygame.transform.scale(pygame.image.load("Assets/white_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
    "black": pygame.transform.scale(pygame.image.load("Assets/black_chip.png"),
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
        black_chips.append(Chip.Chip(black_x, black_y, "black"))



