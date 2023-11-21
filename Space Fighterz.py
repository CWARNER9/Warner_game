# Import pygame and the classes
import pygame
from random import randint
from Ship import SpaceShip
from Enemy import Enemy
from Missile import Missile
from Ship2 import SpaceShip2
from VEnemy import VEnemy
pygame.init()
clock = pygame.time.Clock()
# Screen dimensions
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# These rocks make the background "stars"
rock = pygame.image.load('Assets/Images/spaceEffects_008.png')
rock = pygame.transform.scale_by(rock, 0.2)
background = pygame.Surface((WIDTH, HEIGHT))
# The random functions place the rocks randomly over the screen
num_rocks= 55
for r in range(num_rocks):
    background.blit(rock, (randint(0,WIDTH), randint(0, HEIGHT)))

screen.blit(background, (0,0))
# Initializing the number of enemies and adding them to their respective sprite groups
num_lat_enemy = 8
num_vert_enemy = 15
your_ship = SpaceShip2(screen)
my_ship = SpaceShip(screen)
ship_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()

ship_group.add(my_ship, your_ship)
[enemy_group.add(Enemy(screen)) for n in range(num_lat_enemy)]
[enemy_group.add(VEnemy(screen)) for n in range(num_vert_enemy)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Code for red ship actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_ship.velocity += 4
                if my_ship.velocity == 0:
                    my_ship.velocity +=4
            if event.key == pygame.K_LEFT:
                my_ship.velocity -= 4
                if my_ship.velocity == 0:
                    my_ship.velocity -=4
            if event.key == pygame.K_UP:
                if len(missile_group) < 8:
                    missile_group.add(Missile(my_ship.rect.midtop, enemy_group))
            if my_ship.velocity >= 4:
                my_ship.velocity = 4
            if my_ship.velocity <= -4:
                my_ship.velocity = -4
            if my_ship.rect.x == 800:
                my_ship.velocity = 0
            if my_ship.rect.x == 200:
                my_ship.velocity = 0
        # Code for blue ship actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                your_ship.velocity += 4
                if your_ship.velocity == 0:
                    your_ship.velocity +=4
            if event.key == pygame.K_a:
                your_ship.velocity -= 4
                if your_ship.velocity == 0:
                    your_ship.velocity -=4
            if event.key == pygame.K_w:
                if len(missile_group) < 8:
                    missile_group.add(Missile(your_ship.rect.midtop, enemy_group))
            if your_ship.velocity >= 4:
                your_ship.velocity = 4
            if your_ship.velocity <= -4:
                your_ship.velocity = -4
            if your_ship.rect.x == 800:
                your_ship.velocity = 0
            if your_ship.rect.x == 200:
                your_ship.velocity = 0
    # Calling the update functions from respective classes to make the game run how it is supposed to
    enemy_group.update()
    ship_group.update()
    missile_group.update()
    screen.blit(background, (0, 0))
    ship_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    # Run at 60 fps
    clock.tick(60)
    pygame.display.flip()
pygame.quit()