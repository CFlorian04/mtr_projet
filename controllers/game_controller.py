import pygame
from models.heart import Heart
from models.player import Player
from models.enemy import Enemy
from models.bullet import Bullet
from views.game_view import GameView


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.view = GameView(screen)
        self.player = Player(self.view)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.score = 0

        self.create_enemies()

    def create_enemies(self):
        for i in range(3):
            for j in range(8):
                enemy = Enemy(100 + j * 60, 50 + i * 50)
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

            self.view.draw(self.player, self.enemies, self.bullets, self.enemy_bullets, self.score)

            clock.tick(60)

    def handle_collisions(self):
        # Vérification des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, False, False)
        for bullet, enemies in collisions.items():
            self.score += 100
            if bullet.alive():
                bullet.kill()
                next(iter(enemies)).kill()  # Sélection le premier ennemi parmi ceux trouvés, et le tue

        # Vérification des collisions entre les ennemis et le joueur
        collisions = pygame.sprite.spritecollide(self.player, self.enemies, True)
        if collisions:
            self.player.hit()
            if not self.player.hitPoints:
                self.player.kill()  # Todo: remove from screen

        # Vérification des collisions entre les projectiles ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemy_bullets):
            print("Player hit by enemy bullet!")
