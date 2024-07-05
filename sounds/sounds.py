import os

import pygame


def play_intro_music() -> None:
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join('assets/sounds/intro_music.wav'))
    pygame.mixer.music.play(-1)

def play_background_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join('assets/sounds/gameplay.wav'))
    pygame.mixer.music.play(-1)


def play_player_explosion():
    sound = pygame.mixer.Sound(os.path.join('assets/sounds/player_explosion.wav'))
    pygame.mixer.Sound.play(sound)


def play_enemy_explosion():
    sound = pygame.mixer.Sound(os.path.join('assets/sounds/enemy_explosion.wav'))
    pygame.mixer.Sound.play(sound)


def play_player_laser():
    sound = pygame.mixer.Sound(os.path.join('assets/sounds/player_laser.wav'))
    pygame.mixer.Sound.play(sound)


def play_enemy_laser():
    sound = pygame.mixer.Sound(os.path.join('assets/sounds/enemy_laser.wav'))
    pygame.mixer.Sound.play(sound)
