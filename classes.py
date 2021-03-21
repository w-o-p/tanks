import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, side, *group):
        super().__init__(*group)
        if side == 1:
            self.static = pygame.image.load('imgs/tank1_static.png')
            self.static.set_colorkey('white')
            self.fire_img = pygame.image.load('imgs/tank1.png')
            self.fire_img.set_colorkey('white')
        else:
            self.static = pygame.image.load('imgs/tank2_static.png')
            self.static = pygame.transform.flip(self.static, True, False)
            self.static.set_colorkey('white')
            self.fire_img = pygame.image.load('imgs/tank2.png')
            self.fire_img = pygame.transform.flip(self.fire_img, True, False)
            self.fire_img.set_colorkey('white')

        self.image = self.static
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def fire(self):
        self.image = self.fire_img

    def gunpoint_down(self):
        self.image = self.static

    def update(self):
        pass


class Harch(pygame.sprite.Sprite):
    def __init__(self, x, y, side, *group):
        super().__init__(*group)
        self.image = pygame.image.load('imgs/alkash.png')
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side
        self.x = 0

    def update(self):
        self.x += 0.5
        self.rect = self.rect.move(25 * self.side, self.x ** 2 - 3 * self.x)
