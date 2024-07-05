import random

import pygame

from settings.settings import *


class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group: pygame.sprite.Group, image: pygame.Surface):
        super().__init__()

        self.score = 100

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 2
        self.speed_y = self.rect.height * 0.9
        self.bullet_group = bullet_group

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > getGameWidth():
            self.speed_x = -self.speed_x
            self.rect.y += self.speed_y

    def inverseSpeed(self):
        # print(self.speed_x)
        self.speed_x = -self.speed_x
