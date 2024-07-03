import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-2, 2])
        self.speed_y = 10

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed_x = -self.speed_x
            self.rect.y += self.speed_y
