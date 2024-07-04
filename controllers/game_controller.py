import pygame, random

from models.bullet import Bullet
from models.enemy import Enemy
from models.heart import Heart
from models.player import Player
from settings.settings import *
from views.game_view import GameView


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.player = Player()
        self.hearts = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.view = GameView(screen)

        self.score = 0
        self.game_state = "start"

        self.create_hearts(3)
        self.create_enemies()

    def create_hearts(self, number) -> None:
        self.hearts.empty()
        for i in reversed(range(number)):
            heart = Heart()
            heart.rect.x = self.view.screen.get_size()[0] - (Heart.base_size * (i + 1) + 10)
            heart.rect.y = 20
            self.hearts.add(heart)

    def create_enemies(self):
        self.enemies.empty()
        for i in range(3):
            for j in range(8):
                enemy = Enemy(100 + j * 60, 50 + i * 40, self.enemy_bullets)
                self.enemies.add(enemy)

    def reset_game(self):
        self.player = Player()
        self.bullets.empty()
        self.enemy_bullets.empty()
        self.score = 0
        self.create_hearts(3)
        self.create_enemies()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    setGameWidth(event.w)
                    setGameHeight(event.h)
                    self.screen = pygame.display.set_mode((getGameWidth(), getGameHeight()), pygame.RESIZABLE)
                    self.view.screen = self.screen
                    self.player.resize()
                    for heart in self.hearts:
                        heart.resize()
                    self.create_hearts(self.hearts.sprites().__len__())
                elif event.type == pygame.KEYDOWN:
                    if self.game_state == "start" and event.key == pygame.K_RETURN:
                        self.game_state = "playing"
                    elif (self.game_state == "game_over" or self.game_state == "victory") and event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.game_state = "playing"
                    elif self.game_state == "playing" and event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top, 'up', 'player')
                        self.bullets.add(bullet)

            if self.game_state == "playing":

                for enemy in self.enemies.sprites():
                    if random.random() < 0.001:
                        bullet = Bullet(enemy.rect.centerx, enemy.rect.bottom, 'down', 'enemy')
                        self.enemy_bullets.add(bullet)

                self.player.update()
                self.enemies.update()
                self.bullets.update()
                self.enemy_bullets.update()

                self.handle_collisions()

                self.view.draw(self.player, self.enemies, self.bullets, self.enemy_bullets, self.hearts, self.score)

            elif self.game_state == "start":
                self.view.draw_start_screen()
            elif self.game_state == "game_over":
                self.view.draw_game_over_screen(self.score)
            elif self.game_state == "victory":
                self.view.draw_victory_screen(self.score)

            clock.tick(60)

    def handle_collisions(self):
        # Vérification des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for bullet, enemies in collisions.items():
            self.score += 100

        # Vérification des collisions entre les ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.lose_heart()
            for enemy in pygame.sprite.spritecollide(self.player, self.enemies, False):
                enemy.kill()

        # Vérification des collisions entre les projectiles ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemy_bullets):
            self.lose_heart()
            for bullet in pygame.sprite.spritecollide(self.player, self.enemy_bullets, False):
                bullet.kill()

        # S'il n'y a plus d'ennemi, la partie est fini
        if self.game_state == "playing" and not self.enemies:
            self.game_state = "victory"

    def lose_heart(self):
        if self.hearts:
            heart = self.hearts.sprites()[-1]
            heart.kill()
        if not self.hearts:
            self.game_state = "game_over"
