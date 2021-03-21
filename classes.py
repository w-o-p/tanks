import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, side, *group):
        super().__init__(*group)
        if side == 1:
            self.static = pygame.image.load('imgs/tank1_static.png')
            self.fire_img = pygame.image.load('imgs/tank1.png')
        else:
            self.static = pygame.image.load('imgs/tank2_static.png')
            self.static = pygame.transform.flip(self.static, True, False)
            self.fire_img = pygame.image.load('imgs/tank2.png')
            self.fire_img = pygame.transform.flip(self.fire_img, True, False)
        self.alkoharch = pygame.image.load('imgs/alkash.png')

        self.image = self.static
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def fire(self):
        self.image = self.fire_img

    def update(self):
        pass
