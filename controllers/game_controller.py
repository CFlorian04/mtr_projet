import random

from models.bullet import Bullet
from models.enemy import Enemy
from models.player import Player
from settings.settings import *
from sounds.sounds import *
from views.game_view import GameView


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.view = GameView(screen)
        self.player = Player(self.view)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.score = 0
        self.game_state = "start"
        self.game_difficulty = self.score // 100
        self.spawn_timer = 0  # Timer pour le réapparition des ennemis

        self.create_enemies()

        play_background_music()

    def create_enemies(self):
        self.enemies.empty()
        for i in range(3):
            for j in range(10):
                enemy = Enemy(j * getGameWidth() / 10, i * getGameHeight() / 10, self.enemy_bullets)
                self.enemies.add(enemy)

    def reset_game(self):
        self.player = Player(self.view)
        self.enemy_bullets.empty()
        self.score = 0
        self.game_difficulty = 0
        self.create_enemies()

    def spawn_random_enemy(self):
        if len(self.enemies) >= 50:
            return

        enemy = None
        max_attempts = 10  # Nombre maximal de tentatives pour trouver une position
        for _ in range(max_attempts):
            x = random.randint(0, getGameWidth() - Enemy(0, 0, pygame.sprite.Group()).rect.width)
            y = random.randint(0, getGameHeight() // 10)
            enemy = Enemy(x, y, self.enemy_bullets)

            if not pygame.sprite.spritecollideany(enemy, self.enemies):
                break
            enemy = None

        if enemy:
            self.enemies.add(enemy)

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
                elif event.type == pygame.KEYDOWN:
                    if self.game_state == "start" and event.key == pygame.K_RETURN:
                        self.game_state = "playing"
                    elif (
                            self.game_state == "game_over" or self.game_state == "victory") and event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.game_state = "playing"

            if self.game_state == "playing":

                # Plus la difficulté augmente plus les ennemis ont de chance de spawner
                self.spawn_timer += 1
                timer = 120 - (0.5 * self.game_difficulty)
                # Valeur minimum pour le timer
                timer = timer if timer >= 20 else 20
                # print(f"Respawn Time : {timer}")
                if self.spawn_timer >= timer:
                    self.spawn_random_enemy()
                    self.spawn_timer = 0

                # Plus la difficulté augmente plus les ennemis ont de chance de tirer
                for enemy in self.enemies.sprites():
                    shot_luck = 0.001 + (self.game_difficulty / 100000)
                    # print(f"Shot Luck : {shot_luck}")
                    if random.random() < shot_luck:
                        # Un ennemi tire
                        bullet = Bullet(enemy.rect.centerx, enemy.rect.bottom, 'down', 'enemy')
                        self.enemy_bullets.add(bullet)
                        play_enemy_laser()

                self.player.update()
                self.enemies.update()
                self.enemy_bullets.update()

                self.handle_collisions()

                self.view.draw(self.player, self.enemies, self.enemy_bullets, self.score)

            elif self.game_state == "start":
                self.view.draw_start_screen()
            elif self.game_state == "game_over":
                self.view.draw_game_over_screen(self.score)
            elif self.game_state == "victory":
                self.view.draw_victory_screen(self.score)

            clock.tick(60)

    def handle_collisions(self):
        # Vérification des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(self.player.bullets, self.enemies, True, False)
        for bullet, enemies in collisions.items():
            self.score += 100
            self.game_difficulty = self.score // 100
            next(iter(enemies)).kill()
            play_enemy_explosion()

        # Vérification des collisions entre les ennemis et le joueur
        collisions = pygame.sprite.spritecollide(self.player, self.enemies, True)
        if collisions:
            self.__playerHitEvent()

        # Vérification des collisions entre les projectiles ennemis et le joueur
        if pygame.sprite.spritecollideany(self.player, self.enemy_bullets):
            self.__playerHitEvent()
            for bullet in pygame.sprite.spritecollide(self.player, self.enemy_bullets, False):
                bullet.kill()

        # Vérification des collisions entre ennemis
        # self.handle_enemy_collisions()

        # S'il n'y a plus d'ennemi, la partie est finie
        # if self.game_state == "playing" and not self.enemies:
        #    self.game_state = "victory"

    # Todo: Ne fonctionne pas : À regarder
    def handle_enemy_collisions(self):
        for enemy1 in self.enemies:
            for enemy2 in self.enemies:
                if enemy1 != enemy2 and pygame.sprite.collide_rect(enemy1, enemy2):
                    # Collision détectée entre deux ennemis
                    enemy1.speed_x = -enemy1.speed_x
                    enemy2.speed_x = -enemy2.speed_x

    def __playerHitEvent(self) -> None:
        self.player.hit()
        if not self.player.hitPoints:
            self.player.kill()
            self.enemies.empty()
            self.enemy_bullets.empty()
            self.game_state = 'game_over'
