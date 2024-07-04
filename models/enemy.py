import random

import pygame

from models.bullet import Bullet
from settings.settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()

        self.enemy_images = [
            pygame.image.load("assets/images/enemy1.png").convert_alpha(),
            pygame.image.load("assets/images/enemy2.png").convert_alpha(),
            pygame.image.load("assets/images/enemy3.png").convert_alpha()
        ]

        self.image = random.choice(self.enemy_images)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-2, 2])
        self.speed_y = self.rect.height * 0.9
        self.bullet_group = bullet_group

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > getGameWidth():
            self.speed_x = -self.speed_x
            self.rect.y += self.speed_y

        if random.random() < 0.001:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 'down', 'enemy')
        self.bullet_group.add(bullet)
