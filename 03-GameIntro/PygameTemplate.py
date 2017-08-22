import pygame

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

size = width, height = 800, 50

screen = pygame.display.update(size)

clock = pygame.time.Clock()
FPS = 50

game = True

while game:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    clock.tick(FPS)

quit()
