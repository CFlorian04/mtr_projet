import pygame
from settings.settings import *

from models.heart import Heart
from models.bullet import Bullet
from views.game_view import GameView


class Player(pygame.sprite.Sprite):
    def __init__(self, view: GameView) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = getGameWidth()/2
        self.rect.bottom = int(getGameHeight() - getGameHeight()/30)
        self.speed_x = 0
        self.max_speed = getGameWidth()/100
        self.acceleration = self.max_speed/20
        self.deceleration = self.acceleration
        
        self.__view = view

        self.__bullets = pygame.sprite.Group()

        self.__hitPoints = 3
        self.__hearts: dict[int, Heart] = {}
        self.__heartsSpriteGroup = pygame.sprite.Group()
        self.__create_hearts()

        self.__lastFired = pygame.time.get_ticks()  # Doc: msec
        self.__fireRate = 1000 / 5  # Doc: 5 tirs max par seconde

        # Doc: Initialise à fire rate + 1 pour qu'il puisse tirer dès le départ
        self.__cooldown = self.__fireRate + 1

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

        tick = pygame.time.get_ticks()
        self.__cooldown = tick - self.__lastFired

        # Doc: ne pourra pas tirer tant que le cooldown n'est pas passé
        if keys[pygame.K_SPACE] and self.__cooldown > self.__fireRate:
            self.__lastFired = tick
            self.__cooldown = 0
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
