import pygame, sys

class GameView:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, player, enemies, bullets, enemy_bullets):
        self.screen.fill((0, 0, 0))
        self.screen.blit(player.image, player.rect)
        for enemy in enemies:
            self.screen.blit(enemy.image, enemy.rect)
        for bullet in bullets:
            self.screen.blit(bullet.image, bullet.rect)
        for bullet in enemy_bullets:
            self.screen.blit(bullet.image, bullet.rect)
        pygame.display.flip()
