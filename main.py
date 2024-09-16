import pygame
import Screen

pygame.init()
background = pygame.image.load("Assets/field.jpg")

screen = Screen.Screen()
while True:
    screen.screen.blit(background, (0, 0))

