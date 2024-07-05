import pygame.sprite

from models.baseEnemy import BaseEnemy


class EnemyGreen(BaseEnemy):
    def __init__(self, x: int | float, y: int | float, bullets: pygame.sprite.Group) -> None:
        BaseEnemy.__init__(self, x, y, bullets, pygame.image.load("assets/images/enemy_green.png").convert_alpha() )
