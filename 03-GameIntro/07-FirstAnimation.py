import pygame
import random

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,blue,green,yellow]

size = width, height = 800, 500

screen = pygame.display.set_mode(size)
pygame.display.set_caption("FirstAnim")

clock = pygame.time.Clock()
FPS = 10

rect_x = 0
rect_y = 0

game = True

while game:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

##    for i in range(50):
##        rect_x = random.randint(0, width)
##        rect_y = random.randint(0, height)
##        rand_color = random.choice(colors)
##        pygame.draw.rect(screen, rand_color,[rect_x, rect_y,50,50])

    move_x = random.randint(0,1)
    move_y = random.randint(0,1)
    for i in range(50):
        rect_x = random.randint(0, width)
        rect_y = random.randint(0, height)
        rand_color = random.choice(colors)
        pygame.draw.rect(screen, rand_color,[rect_x, rect_y,50,50])

##        rect_x += move_x
##        rect_y += move_y

    if rect_x >= width-100 or rect_x < 0:
        move_x = 0

    if rect_y >= height-100 or rect_y < 0:
        move_y = 0
    

    pygame.display.update()
    clock.tick(FPS)

quit()
