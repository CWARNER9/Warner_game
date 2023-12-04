import pygame
import random
class Boss(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/enemyBlack5.png')
        self.image = pygame.transform.scale_by(self.image, 3.)
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = -400
        self.screen = screen
    def update(self):
        self.rect.y += self.speed
        if self.rect.y == 10:
            self.speed = 0


