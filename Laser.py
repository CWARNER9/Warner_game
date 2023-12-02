import pygame
import pygame.sprite


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, ship_group):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/laserGreen04.png')
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 4
        self.ship_group = ship_group
    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > 700:
            self.kill()
        if self.rect.y < 100:
            self.kill()
