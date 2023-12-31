import pygame
import random
from random import randint
class VEnemy(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/spaceStation_001.png')
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.speed = 1
        self.rect = self.image.get_rect()
        # Increases size of rect so hitbox is bigger
        self.pseudo_rect = self.rect.inflate(10, 10)
        self.rect.x = randint(100, 900)
        self.rect.y = randint(-1500, -500)
        self.screen = screen
        self.dead_time = 0
    def update(self):
        self.rect.y += self.speed
        if self.rect.y == 300:
            self.speed = 0
        if self.rect.y == 900:
            self.kill()

    def reset(self):
        self.rect.x = randint(100, 900)
        self.rect.y = randint(-2000, -500)