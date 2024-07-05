import pygame.sprite

from models.baseEnemy import BaseEnemy


class EnemyRed(BaseEnemy):
    def __init__(self, x: int | float, y: int | float, bullets: pygame.sprite.Group) -> None:
        BaseEnemy.__init__(self, x, y, bullets, pygame.image.load("assets/images/enemy_red.png").convert_alpha() )
        self.score = 500
