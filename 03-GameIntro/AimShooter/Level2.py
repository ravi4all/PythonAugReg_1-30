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

zombie_1 = pygame.image.load("images/zombie_1.gif")
zombie_2 = pygame.image.load("images/zombie_2.png")
zombie_3 = pygame.image.load("images/zombie_3.png")
zombie_4 = pygame.image.load("images/zombie_4.png")

zombieList = [zombie_1, zombie_2, zombie_3, zombie_4]

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

def score(c):
    font = pygame.font.Font('font_1.otf', 50)
    text = font.render("Score : "+str(c), True, yellow)
    screen.blit(text, (10,10))
    file = open('score.txt','w')
    file.write(str(c))

def main():
    zombie_x = random.randint(0,width-200)
    zombie_y = random.randint(0,height-200)
    zombieImage = random.choice(zombieList)

    zombieScaleX = 130
    zombieScaleY = 180

    gun_y = height/2+30

    counter = 0
    clicked = 0

    seconds = 30
    pygame.time.set_timer(USEREVENT + 1, 1000)

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
                if rect_1.colliderect(rect_2):
                    clicked += 1
                    screen.blit(bloodImage, (mouse_pos_x - 50, mouse_pos_y - 50))
                    zombieImage = pygame.transform.scale(zombieImage, (zombieScaleX, zombieScaleY))
                    zombieScaleX -= 10
                    zombieScaleY -= 10
                    if clicked == 3:
                        zombie_x = random.randint(0,width-200)
                        zombie_y = random.randint(0,height-200)
                        zombieImage = random.choice(zombieList)
                        counter += 1
                        clicked = 0
                        zombieScaleX = 100
                        zombieScaleY = 150

            elif event.type == pygame.MOUSEBUTTONUP:
                gun_y = height/2+30

        if seconds == -1:
            gameOver(counter)

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        screen.blit(zombieImage, (zombie_x, zombie_y))
        screen.blit(pointer, (mouse_pos_x - 50, mouse_pos_y - 50))
        screen.blit(gunImage, (mouse_pos_x,gun_y))

        rect_1 = pygame.Rect(mouse_pos_x-50, mouse_pos_y-50, pointer.get_width(), pointer.get_height())

        rect_2 = pygame.Rect(zombie_x, zombie_y, zombie_1.get_width(), zombie_1.get_height())

        score(counter)
        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

    quit()

# main()
