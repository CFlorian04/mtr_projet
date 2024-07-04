import pygame
from settings.settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction='up', type='player'):
        super().__init__()
        self.image = pygame.image.load(
            "assets/images/player_laser.png").convert_alpha() if type == 'player' else pygame.image.load(
            "assets/images/enemy_laser.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y if direction == 'up' else y - self.rect.height

        self.bullet_speed = getGameHeight()/150

        self.speed_y = -self.bullet_speed if direction == 'up' else self.bullet_speed

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > getGameHeight():
            self.kill()
