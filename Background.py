import pygame
from random import randint




def Background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    color = (0,0,0)
    screen.fill(color)
    pygame.display.flip()