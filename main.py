import pygame

from controllers.game_controller import GameController
from settings.settings import *


def main():
    pygame.init()
    # Création de la fenetre en RESIZEABLE
    screen = pygame.display.set_mode((getGameWidth(), getGameHeight()), pygame.RESIZABLE)
    pygame.display.set_caption("Space Invader")

    # Création du game controller
    controller = GameController(screen)
    controller.run()

    pygame.quit()


if __name__ == "__main__":
    main()
