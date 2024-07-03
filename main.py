import pygame
from controllers.game_controller import GameController

GAME_WIDTH = 800
GAME_HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Space Invader")

    controller = GameController(screen)
    controller.run()

    pygame.quit()


if __name__ == "__main__":
    main()
