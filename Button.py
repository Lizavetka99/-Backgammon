import pygame
from image_settings import images_data as img_data


class Button:
    def __init__(self, image, name):
        self.texture = pygame.transform.scale(image,
                                     (img_data[name]["width"],
                                      img_data[name]["height"]))
        self.pos = img_data[name]["pos"]
        self.rect = self.texture.get_rect()
        self.rect.x = img_data[name]["pos"][0]
        self.rect.y = img_data[name]["pos"][1]

    def is_clicked(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print("нажали")