import pygame
import image_settings

pygame.init()

# window size settings
screen_width = image_settings.WIDTH
screen_height = image_settings.HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))

# game elements initialization
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

dice_button_image = pygame.image.load("Assets/dice_button.png")
dice_button = pygame.transform.scale(dice_button_image,
                                     (img_data["dice_button"]["width"],
                                      img_data["dice_button"]["height"]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    # adding game elements to screen
    screen.blit(background, img_data["background"]["pos"])
    screen.blit(field, img_data["field"]["pos"])
    screen.blit(dice_table, img_data["dice_table"]["pos"])
    screen.blit(dice_button, img_data["dice_button"]["pos"])

    pygame.display.flip()

pygame.quit()
