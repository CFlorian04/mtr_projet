import pygame


class GameView:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.update_fonts()
        self.menu_background = pygame.image.load("assets/images/background_menu.jpg").convert()
        self.game_background = pygame.image.load("assets/images/background_game.jpg").convert()

    def update_fonts(self):
        screen_width, screen_height = self.screen.get_size()
        self.font_size = screen_height // 20
        self.large_font_size = screen_height // 12
        self.font = pygame.font.SysFont("monospace", self.font_size)
        self.large_font = pygame.font.SysFont("monospace", self.large_font_size)

    def draw_background(self, background):
        # Pour que le background soit sûr toute la fenêtre
        scaled_background = pygame.transform.scale(background, self.screen.get_size())
        self.screen.blit(scaled_background, (0, 0))

    def draw(self, player, enemies, enemy_bullets, score: int) -> None:
        self.draw_background(self.game_background)
        self.screen.blit(player.image, player.rect)
        score_text = self.font.render(f"Score: {score}", 1, (255, 255, 255))
        self.screen.blit(score_text, (10, 30))
        for enemy in enemies:
            self.screen.blit(enemy.image, enemy.rect)
        for bullet in player.bullets:
            self.screen.blit(bullet.image, bullet.rect)
        for bullet in enemy_bullets:
            self.screen.blit(bullet.image, bullet.rect)
        for heart in player.hearts:
            self.screen.blit(heart.image, heart.rect)
        pygame.display.flip()

    def draw_start_screen(self) -> None:
        # Écran menu du jeu
        self.draw_background(self.menu_background)
        title_text = self.large_font.render("Space Invader", True, (255, 255, 255))
        start_text = self.font.render("Press ENTER to Start", True, (255, 255, 255))
        self.screen.blit(title_text,(self.screen.get_width() // 2 - title_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(start_text,(self.screen.get_width() // 2 - start_text.get_width() // 2, self.screen.get_height() // 2))
        pygame.display.flip()

    def draw_game_over_screen(self, score: int) -> None:
        # Écran de défaite
        self.draw_background(self.menu_background)
        game_over_text = self.large_font.render("Game Over", True, (255, 0, 0))
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        restart_text = self.font.render("Press ENTER to Restart", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(score_text,(self.screen.get_width() // 2 - score_text.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, self.screen.get_height() * 2 // 3))
        pygame.display.flip()

    def draw_victory_screen(self, score: int) -> None:
        # Écran de victoire
        self.draw_background(self.menu_background)
        game_over_text = self.large_font.render("Victory", True, (0, 255, 0))
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        restart_text = self.font.render("Press ENTER to Restart", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(score_text,(self.screen.get_width() // 2 - score_text.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, self.screen.get_height() * 2 // 3))
        pygame.display.flip()
