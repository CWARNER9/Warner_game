import pygame
import random

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/spaceShips_009.png')
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 600
        self.velocity = 0


    def update(self):
        self.rect.x += self.velocity
        self.border()
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def border(self, screen):
        if self.rect.x > screen.get_width -100:
            self.velocity = -0.1

