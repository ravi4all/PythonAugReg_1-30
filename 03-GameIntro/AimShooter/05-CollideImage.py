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
zombie_2 = pygame.image.load("images/zombie_2.png")
zombie_3 = pygame.image.load("images/zombie_3.png")
zombie_4 = pygame.image.load("images/zombie_4.png")

zombieList = [zombie_1, zombie_2, zombie_3, zombie_4]

backgroundImage = pygame.image.load("images/background.png")
bloodImage = pygame.image.load("images/zombie_blood.png")

gun_shot = pygame.mixer.Sound("sounds/gunShot.wav")

clock = pygame.time.Clock()
FPS = 50

def main():
    zombie_x = random.randint(0,width-200)
    zombie_y = random.randint(0,height-200)
    zombieImage = random.choice(zombieList)
    game = True
    while game:

        screen.fill(white)
        screen.blit(backgroundImage, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun_shot.play()
                if rect_1.colliderect(rect_2):
                    screen.blit(bloodImage, (mouse_pos_x, mouse_pos_y))
                    zombie_x = random.randint(0,width-200)
                    zombie_y = random.randint(0,height-200)
                    zombieImage = random.choice(zombieList)

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        screen.blit(zombieImage, (zombie_x, zombie_y))
        screen.blit(pointer, (mouse_pos_x - 50, mouse_pos_y - 50))

        rect_1 = pygame.Rect(mouse_pos_x-50, mouse_pos_y-50, pointer.get_width(), pointer.get_height())

        rect_2 = pygame.Rect(zombie_x, zombie_y, zombie_1.get_width(), zombie_1.get_height())

        pygame.display.update()
        clock.tick(FPS)

    quit()

main()
