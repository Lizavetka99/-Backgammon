import random, pygame, image_settings

class Dice:
    is_throw = False
    dice_textures = []
    for i in range(1, 7):
        image = pygame.image.load(f"Assets/dice/{i}.png")
        dice_textures.append(pygame.transform.scale(image, (50, 50)))
    x_pos_1 = image_settings.images_data["dice_table"]["width"]//2
    x_pos_2 = image_settings.images_data["dice_table"]["width"]//4
    y_pos_1 = image_settings.images_data["dice_table"]["height"]//2
    y_pos_2 = image_settings.images_data["dice_table"]["height"]//4

    @staticmethod
    def throw():
        Dice.is_throw = True
        value = random.randint(0, 5)
        return Dice.dice_textures[value], value