import pygame
pygame.init()

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
        self.dead_time = 0
        self.lives = 3

    def update(self, enemy_group, laser_group, screen):
        self.rect.x += self.velocity
        self.border()
        self.crash(enemy_group)
        self.shot(laser_group)
        if self.dead_time and (pygame.time.get_ticks() - self.dead_time>500):
            self.image = pygame.image.load('Assets/Images/spaceShips_009.png')
            self.image = pygame.transform.scale_by(self.image, 0.5)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()
            self.rect.x = screen.get_width() / 2
            self.rect.y = 600
            self.velocity = 0
            self.dead_time = 0
            self.lives -= 1
            return self.lives

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def border(self):
        if self.rect.x > 940:
            self.velocity = -0.2
        if self.rect.x < 20:
            self.velocity = 0.2

    def boom(self):
        self.image = pygame.image.load('Assets/Images/explosion1.png')
        self.dead_time = pygame.time.get_ticks()
        self.velocity = 0
    def crash(self, enemy_group):
         crash_sound = pygame.mixer.Sound("Assets/Sounds/mixkit-8-bit-bomb-explosion-2811.wav")
         hit = pygame.sprite.spritecollideany(self, enemy_group)
         if hit:
             self.boom()
             pygame.mixer.Sound.play(crash_sound)

    def shot(self, laser_group):
         crash_sound = pygame.mixer.Sound("Assets/Sounds/mixkit-8-bit-bomb-explosion-2811.wav")
         hit = pygame.sprite.spritecollideany(self, laser_group)
         if hit:
             self.boom()
             pygame.mixer.Sound.play(crash_sound)

