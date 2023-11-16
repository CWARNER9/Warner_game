import pygame
from random import randint
from Ship import SpaceShip
from Enemy import Enemy
from Missile import Missile

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

num_enemy = 7
my_ship = SpaceShip(screen)
ship_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()

ship_group.add(my_ship)
[enemy_group.add(Enemy(screen)) for n in range(num_enemy)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_ship.velocity += 3
                if my_ship.velocity == 0:
                    my_ship.velocity +=3
            if event.key == pygame.K_LEFT:
                my_ship.velocity -= 3
                if my_ship.velocity == 0:
                    my_ship.velocity -=3
            if event.key == pygame.K_UP:
                if len(missile_group) < 5:
                    missile_group.add(Missile(my_ship.rect.midtop, enemy_group))
            if my_ship.velocity >= 3:
                my_ship.velocity = 3
            if my_ship.velocity <= -3:
                my_ship.velocity = -3
            if my_ship.rect.x == 800:
                my_ship.velocity = 0
            if my_ship.rect.x == 200:
                my_ship.velocity = 0
    enemy_group.update()
    ship_group.update()
    missile_group.update()
    screen.blit(background, (0, 0))
    ship_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()