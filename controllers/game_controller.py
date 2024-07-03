import pygame
from models.player import Player
from models.enemy import Enemy
from models.bullet import Bullet
from views.game_view import GameView

class GameController:
    def __init__(self, screen: pygame.Surface):
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.view = GameView(screen)

        self.score = 0

        self.create_hearts()
        self.create_enemies()

    def create_enemies(self):
        for i in range(5):
            for j in range(8):
                enemy = Enemy(100 + j * 60, 50 + i * 40)
                self.enemies.add(enemy)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top, 'up', 'player')
                        self.bullets.add(bullet)

            self.player.update()
            self.enemies.update()
            self.bullets.update()
            self.enemy_bullets.update()

            self.handle_collisions()

            self.view.draw(self.player, self.enemies, self.bullets, self.enemy_bullets, self.hearts, self.score)

            clock.tick(60)

    def handle_collisions(self):
        # Vérification des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for bullet, enemy in collisions.items():
            self.score += 100
            bullet.kill()

        # Vérification des collisions entre les ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            print("Player hit by enemy!")

        # Vérification des collisions entre les projectiles ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemy_bullets):
            print("Player hit by enemy bullet!")
