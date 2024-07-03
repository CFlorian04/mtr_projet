import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction='up'):
        super().__init__()
        self.image = pygame.image.load("assets/images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y if direction == 'up' else y - self.rect.height
        self.speed_y = -5 if direction == 'up' else 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()
