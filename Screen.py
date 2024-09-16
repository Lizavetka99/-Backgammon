import pygame

# SCREEN SETTINGS
WIDTH = 800
HEIGHT = 800
BACKGROUND = "Assets/field.jpg"

class Screen:
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.\
            scale(self.background, (WIDTH, HEIGHT))