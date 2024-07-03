import pygame


class GameView:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 30)

    def draw(self, player, enemies, bullets, enemy_bullets, hearts, score: int) -> None:
        self.screen.fill((7, 15, 43))
        self.screen.blit(player.image, player.rect)
        self.screen.blit(self.font.render(f"Score: {score}", 1, (255, 255, 255) ),
                         (10, 30, 100, 100) )
        for enemy in enemies:
            self.screen.blit(enemy.image, enemy.rect)
        for bullet in bullets:
            self.screen.blit(bullet.image, bullet.rect)
        for bullet in enemy_bullets:
            self.screen.blit(bullet.image, bullet.rect)
        for heart in hearts:
            self.screen.blit(heart.image, heart.rect)
        pygame.display.flip()
