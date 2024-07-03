import pygame


class Heart(pygame.sprite.Sprite):
    base_size = 32

    def __init__(self) -> None:
        super().__init__()
        self.__full = True

        self.__fullImg = pygame.image.load('assets/images/coeur_plein.png')
        self.__emptyImg = pygame.image.load('assets/images/coeur_vide.png')
        self.rect = self.image.get_rect()

    @property
    def image(self) -> pygame.image:
        return pygame.transform.scale(self.__fullImg if self.__full else self.__emptyImg,
                                      (self.base_size, self.base_size))

    @property
    def full(self) -> bool:
        return self.__full

    @full.setter
    def full(self, b: bool) -> None:
        if not isinstance(b, bool):
            raise TypeError(f"Expected bool got {type(b).__name__}")
        self.__full = b
