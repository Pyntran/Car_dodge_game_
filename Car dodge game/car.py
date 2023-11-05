import pygame
from game_variable import red_car


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


class PlayerCar(Vehicle):
    def __init__(self, x, y):
        image = red_car
        super().__init__(image, x, y)
