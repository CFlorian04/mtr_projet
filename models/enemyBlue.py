import pygame.sprite

from models.baseEnemy import BaseEnemy


class EnemyBlue(BaseEnemy):
    def __init__(self, x: int | float, y: int | float, bullets: pygame.sprite.Group) -> None:
        BaseEnemy.__init__(self, x, y, bullets, pygame.image.load("assets/images/enemy_blue.png").convert_alpha() )
        self.score = 250
