import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))


rock = pygame.image.load('Assets/Images/spaceEffects_008.png')
rock = pygame.transform.scale_by(rock, 0.2)
background = pygame.Surface((WIDTH, HEIGHT))

num_rocks= 55
for r in range(num_rocks):
    background.blit(rock, (randint(0,WIDTH), randint(0, HEIGHT)))

screen.blit(background, (0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    clock.tick()
    pygame.display.flip()