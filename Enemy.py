import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/enemyBlack1.png')
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.speed = random.randint(-5,5)
        self.rect = self.image.get_rect()
        self.x = random.randint(100, 900)
        self.rect.y = random.randint(100, 400)
        self.screen = screen
        self.dead_timer = 0
    def update(self):
        self.x += self.speed
        if self.speed == 0:
            self.speed = random.randint(-4,4)
        if self.x < 20:
            self.speed = self.speed*-1
        if self.x > 960:
            self.speed = self.speed*-1
        self.rect.x = self.x