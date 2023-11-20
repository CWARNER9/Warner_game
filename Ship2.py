import pygame


class SpaceShip2(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Assets/Images/playerShip1_blue.png')
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width()/2) - 100
        self.rect.y = 600
        self.velocity = 0


    def update(self):
        self.rect.x += self.velocity
        self.border()
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def border(self):
        if self.rect.x > 940:
            self.velocity = -0.2
        if self.rect.x < 20:
            self.velocity = 0.2
