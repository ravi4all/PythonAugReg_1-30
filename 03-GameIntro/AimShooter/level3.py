import pygame
from pygame.locals import *
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

pointer = pygame.image.load("images/aim_2.png")
gunImage = pygame.image.load("images/gun_1.png")

zombie_1 = pygame.image.load("images/big_zombie.png")

backgroundImage = pygame.image.load("images/background.png")
bloodImage = pygame.image.load("images/zombie_blood.png")

gun_shot = pygame.mixer.Sound("sounds/gunShot.wav")

clock = pygame.time.Clock()
FPS = 50


def gameOver(counter):
    font = pygame.font.Font(None, 80)
    font_2 = pygame.font.Font('font_1.otf', 50)
    seconds_display = font.render("Game Over", 1, yellow)
    scoreDisplay = font_2.render("Total Score is : "+str(counter), True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(seconds_display, (width/2 - 100, 100))
        screen.blit(scoreDisplay, (width/2-200, 250))

        pygame.display.update()

def timer(seconds):
    font = pygame.font.Font(None, 46)
    seconds_display = font.render("Time Left: " + str(seconds), 1, yellow)
    screen.blit(seconds_display, (width-300, 10))


def main():

    gun_y = height/2+30
    counter = 0
    seconds = 30
    pygame.time.set_timer(USEREVENT + 1, 1000)
    zombieHealth = 300

    game = True
    while game:

        screen.fill(white)
        screen.blit(backgroundImage, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun_shot.play()
                gun_y -= 40

            elif event.type == pygame.MOUSEBUTTONUP:
                gun_y = height/2+30

        if seconds == -1:
            gameOver(counter)

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        screen.blit(zombie_1, (width/2 - 175,10))
        screen.blit(pointer, (mouse_pos_x - 50, mouse_pos_y - 50))
        screen.blit(gunImage, (mouse_pos_x,gun_y))

        pygame.draw.rect(screen, green, [5,5,zombieHealth,10])

        rect_1 = pygame.Rect(mouse_pos_x-50, mouse_pos_y-50, pointer.get_width(), pointer.get_height())

        rect_2 = pygame.Rect(width/2 - 175,10, zombie_1.get_width(), zombie_1.get_height())

        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

    quit()

main()
