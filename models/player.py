import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speed_x = 0
        self.acceleration = 0.2
        self.max_speed = 5
        self.deceleration = 0.2

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x -= self.acceleration
        if keys[pygame.K_RIGHT]:
            self.speed_x += self.acceleration
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
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
