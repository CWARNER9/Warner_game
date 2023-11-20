import pygame
import random
class VEnemy(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/spaceStation_001.png')
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.speed = 3
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(-5000, -500)
        self.screen = screen

    def update(self):
        self.rect.y += self.speed
