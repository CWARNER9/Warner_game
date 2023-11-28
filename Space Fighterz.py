# Import pygame and the classes
# Add Score, Sound effects, Music, collisions, lives
import pygame
from random import randint
from Ship import SpaceShip
from Enemy import Enemy
from Missile import Missile
from Ship2 import SpaceShip2
from VEnemy import VEnemy
from Menu_background import create_background
pygame.init()
clock = pygame.time.Clock()

# Screen dimensions
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initializing the number of enemies
num_lat_enemy = 8
num_vert_enemy = 15

# Calling the classes to define each ship
your_ship = SpaceShip2(screen)
my_ship = SpaceShip(screen)

# Initializing groups
ship_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()

# Adding sprites to their respective groups
ship_group.add(my_ship, your_ship)
[enemy_group.add(Enemy(screen)) for n in range(num_lat_enemy)]
[enemy_group.add(VEnemy(screen)) for n in range(num_vert_enemy)]

# Creating menu text and background
background = create_background(screen)
menu_font = pygame.font.SysFont('freesansbold', 100)


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
            if my_ship.rect.x == 980:
                my_ship.velocity = 0
            if my_ship.rect.x == 50:
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
                your_ship.velocity = -0.5
            if your_ship.rect.x == 150:
                your_ship.velocity = 0.5
    # Checking for collisions between the missiles and the enemies
    collision = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)

    # Blitting the background/menu so they show up as the game runs
    screen.blit(background, (0, 0))
    font_surface = menu_font.render('START', 1, (0, 0, 255))
    screen.blit(font_surface, (390, 300))
    # calling update functions for each group
    enemy_group.update()
    ship_group.update()
    missile_group.update()

    # Drawing the groups to the screen
    ship_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)

    # Run at 60 fps
    clock.tick(60)
    pygame.display.flip()
pygame.quit()