import pygame


class Missile(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_group):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/spaceMissiles_040.png')
        self.image = pygame.transform.scale_by(self.image, 0.7)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 8
        self.enemy_group = enemy_group
    def update(self):
        self.rect.y -= self.velocity
        if self.rect.y < 10:
            self.kill()

