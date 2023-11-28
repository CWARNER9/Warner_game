import pygame
from random import randint


def create_background(screen):
    WIDTH = 1000
    HEIGHT = 700
    rock = pygame.image.load('Assets/Images/spaceEffects_008.png')
    rock = pygame.transform.scale_by(rock, 0.2)
    background = pygame.Surface((WIDTH, HEIGHT))
    num_rocks = 55
    for r in range(num_rocks):
        background.blit(rock, (randint(0, WIDTH), randint(0, HEIGHT)))
    return background
