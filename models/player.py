import pygame

from models.heart import Heart
from models.bullet import Bullet
from views.game_view import GameView


class Player(pygame.sprite.Sprite):
    def __init__(self, view: GameView) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speed_x = 0
        self.acceleration = 0.2
        self.max_speed = 5
        self.deceleration = 0.2

        self.__view = view

        self.__bullets = pygame.sprite.Group()

        self.__hitPoints = 3
        self.__hearts: dict[int, Heart] = {}
        self.__heartsSpriteGroup = pygame.sprite.Group()
        self.__create_hearts()

    def __create_hearts(self) -> None:
        for i in reversed(range(self.__hitPoints)):
            heart = Heart()
            heart.rect.x = self.__view.screen.get_size()[0] - (Heart.base_size * (i+1) + 10)
            heart.rect.y = 20
            self.__heartsSpriteGroup.add(heart)
            self.__hearts[i + 1] = heart

    def hit(self) -> None:
        if self.__hitPoints:
            self.__hearts[self.__hitPoints].full = False
            self.__hitPoints -= 1

    @property
    def hitPoints(self) -> int:
        return self.__hitPoints

    @property
    def bullets(self) -> pygame.sprite.Group:
        return self.__bullets

    @property
    def hearts(self) -> pygame.sprite.Group:
        return self.__heartsSpriteGroup

    def update(self) -> None:
        if not self.hitPoints:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet = Bullet(self.rect.centerx, self.rect.top, 'up', 'player')
            self.__bullets.add(bullet)

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
