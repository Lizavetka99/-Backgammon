import pygame, Button, Chip, Chip_data

import Player
import image_settings
from Dice import Dice

pygame.init()

# window size settings
screen_width = image_settings.WIDTH
screen_height = image_settings.HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))

# game elements initialization
player = Player.Player("white")
bg_image = pygame.image.load("Assets/background.jpg")
img_data = image_settings.images_data
background = pygame.transform.scale(bg_image,
                                    (img_data["background"]["width"],
                                     img_data["background"]["height"]))

dice_table_image = pygame.image.load("Assets/dice_table.png")
dice_table = pygame.transform.scale(dice_table_image,
                                    (img_data["dice_table"]["width"],
                                     img_data["dice_table"]["height"]))

field_image = pygame.image.load("Assets/field.png")
field = pygame.transform.scale(field_image,
                               (img_data["field"]["width"],
                                img_data["field"]["height"]))

score_desk_image = pygame.image.load("Assets/score_desk.png")
score_desk = pygame.transform.scale(score_desk_image,
                                    (img_data["score_desk"]["width"],
                                    img_data["score_desk"]["height"]))

dice_button_image = pygame.image.load("Assets/dice_button.png")
dice_button = Button.Button(dice_button_image, "dice_button")

white_chip = Chip.Chip(1, 1, "white")
black_chip = Chip.Chip(1, 1, "black")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
        # Проверка, нажата ли кнопка
            if dice_button.rect.collidepoint(event.pos):
                dice_1, dice_2 = Dice.throw(), Dice.throw()
                player.dice_values[0] = dice_1
                player.dice_values[1] = dice_2
                dice_table.blit(dice_1, (Dice.x_pos_1, Dice.y_pos_1))
                dice_table.blit(dice_2, (Dice.x_pos_2, Dice.y_pos_2))
    screen.fill((0, 0, 0))

    # adding game elements to screen
    screen.blit(background, img_data["background"]["pos"])
    screen.blit(field, img_data["field"]["pos"])
    screen.blit(dice_table, img_data["dice_table"]["pos"])
    screen.blit(score_desk, img_data["score_desk"]["pos"])
    screen.blit(dice_button.texture, dice_button.pos)
    for coord in Chip_data.white_coordinates_start:
        field.blit(white_chip.texture, coord)
    for coord in Chip_data.black_coordinates_start:
        field.blit(black_chip.texture, coord)

    pygame.display.flip()

pygame.quit()
