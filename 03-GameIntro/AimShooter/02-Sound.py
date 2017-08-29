import pygame

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

gun_shot = pygame.mixer.Sound("sounds/gunShot.wav")


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

    screen.blit(pointer, (mouse_pos_x - 50, mouse_pos_y - 50))

    pygame.display.update()
    clock.tick(FPS)

quit()
