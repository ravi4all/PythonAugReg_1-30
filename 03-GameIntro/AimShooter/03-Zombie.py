import pygame
import random

pygame.init()
pygame.mixer.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

size = width, height = 1000, 500

screen = pygame.display.set_mode(size)

pointer = pygame.image.load("images/aim_pointer.png")
zombie_1 = pygame.image.load("images/zombie_1.gif")

gun_shot = pygame.mixer.Sound("sounds/gunShot.wav")

zombie_x = random.randint(0,width-200)
zombie_y = random.randint(0,height-200)

clock = pygame.time.Clock()
FPS = 50

game = True

while game:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            gun_shot.play()

    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

    screen.blit(zombie_1, (zombie_x, zombie_y))
    screen.blit(pointer, (mouse_pos_x - 50, mouse_pos_y - 50))

    pygame.display.update()
    clock.tick(FPS)

quit()
