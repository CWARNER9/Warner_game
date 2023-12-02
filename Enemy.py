import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/enemyBlack1.png')
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.speed = 0
        self.rect = self.image.get_rect()
        # Increases size of rect so hitbox is bigger
        self.pseudo_rect = self.rect.inflate(10, 10)
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(100, 400)
        self.screen = screen
    def update(self):
        self.rect.x += self.speed
        if self.speed == 0:
            self.speed = random.randint(-4,4)
        if self.rect.x < 20:
            self.speed = self.speed*-1
        if self.rect.x > 960:
            self.speed = self.speed*-1




