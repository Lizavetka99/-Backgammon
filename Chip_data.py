import pygame
from image_settings import images_data as img_data


textures_dict = {
    "white": pygame.transform.scale(pygame.image.load("Assets/white_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
    "black": pygame.transform.scale(pygame.image.load("Assets/black_chip.png"),
                                     (img_data["chip"]["width"],
                                      img_data["chip"]["height"])),
}


white_coordinates_start = [ (60, 620-15*i) for i in range(15)]
black_coordinates_start = [ (620, 70+15*i) for i in range(15)]
