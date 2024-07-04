import pygame
from models.player import Player
from models.enemy import Enemy
from views.game_view import GameView


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.view = GameView(screen)
        self.player = Player(self.view)
        self.enemies = pygame.sprite.Group()
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

            self.player.update()
            self.player.bullets.update()
            self.enemies.update()
            self.enemy_bullets.update()

            self.handle_collisions()

            self.view.draw(self.player, self.enemies, self.enemy_bullets, self.score)

            clock.tick(60)

    def handle_collisions(self):
        # Vérification des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(self.player.bullets , self.enemies, False, False)
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
