# ГЛАВНЫЙ ФАЙЛ
from classes import Tank
import pygame

pygame.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
DINO_COLOR = (83, 83, 83)

color = (255, 255, 255)
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
screen.fill(color)
score = 0
clock = pygame.time.Clock()
f1 = pygame.font.Font(None, 60)
f1.set_italic(True)
f2 = pygame.font.Font(None, 18)

turn = 1

all_sprites = pygame.sprite.Group()

t1 = Tank(100, 100, 1, all_sprites)
t2 = Tank(400, 100, 2, all_sprites)

background_color = (255, 255, 255)
text_color = (255, 255, 255)

# если надо до цикла отобразить объекты на экране
screen.fill('black')

# главный цикл
if __name__ == '__main__':
    while True:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_e:
                    if turn == 1:
                        t1.fire()
                        turn += 1
                    else:
                        t2.fire()

        # --------
        # изменение объектов и многое др.
        # --------
        screen.fill(background_color)

        all_sprites.draw(screen)
        all_sprites.update()

        # обновление экрана
        pygame.display.update()
