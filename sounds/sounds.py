import os

import pygame


def play_background_music():
    music = pygame.mixer.music.load(os.path.join('assets/sounds/game.wav'))
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