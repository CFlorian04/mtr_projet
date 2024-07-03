import pygame
from settings.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = getGameWidth()/2
        self.rect.bottom = int(getGameHeight() - getGameHeight()/30)
        self.speed_x = 0
        self.max_speed = getGameWidth()/100
        self.acceleration = self.max_speed/20
        self.deceleration = self.acceleration

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] | keys[pygame.K_q]:
            self.speed_x -= self.acceleration
        if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            self.speed_x += self.acceleration
        if not (keys[pygame.K_LEFT] | keys[pygame.K_q]) and not (keys[pygame.K_RIGHT] | keys[pygame.K_d]):
            if self.speed_x > 0:
                self.speed_x -= self.deceleration
                if self.speed_x < 0:
                    self.speed_x = 0
            elif self.speed_x < 0:
                self.speed_x += self.deceleration
                if self.speed_x > 0:
                    self.speed_x = 0

        if self.speed_x > self.max_speed:
            self.speed_x = self.max_speed
        if self.speed_x < -self.max_speed:
            self.speed_x = -self.max_speed

        self.rect.x += self.speed_x

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = 0
        if self.rect.right > 800:
            self.rect.right = 800
            self.speed_x = 0
