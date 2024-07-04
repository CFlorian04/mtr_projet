import pygame
from settings.settings import *
from controllers.game_controller import GameController

def main():
    pygame.init()
    screen = pygame.display.set_mode((getGameWidth(), getGameHeight()), pygame.RESIZABLE)
    pygame.display.set_caption("Space Invader")

    controller = GameController(screen)
    controller.run()

    pygame.quit()

if __name__ == "__main__":
    main()
