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
from Laser import Laser
from Boss import Boss
from Biglaser import Biglaser
pygame.init()
clock = pygame.time.Clock()

# Screen dimensions
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initializing the number of enemies
num_lat_enemy = 10
num_vert_enemy = 20
# Calling the classes to define each ship
your_ship = SpaceShip2(screen)
my_ship = SpaceShip(screen)
enemy = Enemy(screen)
venemy = VEnemy(screen)
boss = Boss(screen)
# Initializing groups
ship_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()

# Adding sprites to their respective groups
ship_group.add(my_ship, your_ship)
[enemy_group.add(Enemy(screen)) for n in range(num_lat_enemy)]
[enemy_group.add(VEnemy(screen)) for n in range(num_vert_enemy)]
boss_group.add(boss)

# Creating menu text and background
background = create_background(screen)
in_game_font = pygame.font.SysFont('freesansbold', 30)
menu_font = pygame.font.SysFont('freesansbold', 50)
title_font = pygame.font.SysFont('freesansbold', 100)
# Add cool music
music = pygame.mixer.music.load("Assets/Sounds/summervibe.mp3")
hits = 0
pygame.mixer.music.play(4, True, 0)
game_start = False
running = True
while running:
    if len(laser_group) < 2:
        for enemy in enemy_group:
            number = randint(0,5)
            if number == 1:
                laser_group.add(Laser(enemy.rect.midbottom, SpaceShip))
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
                if len(missile_group) < 4:
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
                if len(missile_group) < 4:
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
    Title = title_font.render("SPACE FIGHTERZ", 1, (128, 0, 0))
    singleplayer = menu_font.render('Single Player', 1, (0, 0, 255))
    multiplayer = menu_font.render('Multiplayer', 1, (255, 0, 0))
    rect_1 = singleplayer.get_rect()
    rect_2 = multiplayer.get_rect()
    rect_1.centerx = 445
    rect_1.centery = 315
    rect_2.centerx = 465
    rect_2.centery = 415
    screen.blit(Title, (200, 50))
    screen.blit(singleplayer, (360, 300))
    screen.blit(multiplayer, (385, 400))
    # Menu actions
    mouse = pygame.mouse.get_pos()
    if rect_1.collidepoint(mouse):
        if pygame.mouse.get_pressed()[0]:
            your_ship.kill()
            game_start = True

    if rect_2.collidepoint(mouse):
        if pygame.mouse.get_pressed()[0]:
            game_start = True

    if game_start == True:
        screen.blit(background, (0, 0))
        enemy_group.update()
        ship_group.update(enemy_group, laser_group, screen)
        missile_group.update()
        laser_group.update()
        enemy_group.draw(screen)
        ship_group.draw(screen)
        missile_group.draw(screen)
        laser_group.draw(screen)
    if my_ship.lives ==  0:
        game_start = False
        screen.blit(background, (0, 0))
        pygame.mixer.music.stop()
        game_over = menu_font.render('Game Over :(', 1, (255, 0, 0))
        screen.blit(game_over, (360, 350))
    if your_ship.lives == 0:
        game_start = False
        screen.blit(background, (0, 0))
        pygame.mixer.music.stop()
        game_over = menu_font.render('Game Over :(', 1, (255, 0, 0))
        restart = menu_font.render('restart', 1, (0, 0, 255))
        screen.blit(game_over, (360, 350))
    # Brings out the boss
    if len(enemy_group) == 0:
        boss_group.update()
        boss_group.draw(screen)
        if len(laser_group) < 2:
            for boss in boss_group:
                number = randint(0, 10)
                if number == 1:
                    laser_group.add(Biglaser(boss.rect.midbottom, SpaceShip))
    if pygame.sprite.groupcollide(missile_group, boss_group, True, False,):
        hits += 1
    if hits == 40:
        boss.kill()
    if len(boss_group) == 0:
        game_start = False
        screen.blit(background, (0, 0))
        pygame.mixer.music.stop()
        Win = title_font.render('WINNER!!', 1, (0, 255, 0))
        screen.blit(Win, (340, 320))
    # Run at 60 fps
    clock.tick(60)
    pygame.display.flip()
pygame.quit()