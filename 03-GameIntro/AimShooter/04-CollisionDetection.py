import pygame

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

size = width, height = 1000, 600

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 100

img = pygame.image.load("images/aim_pointer.png")

img_1 = pygame.image.load("images/aim_pointer.png")

img_1_x = 0
img_2_x = height

game = True

while game:

    screen.fill(red)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

    # screen.blit(img, (img_1_x, 400))
    # screen.blit(img_1,(img_2_x, 0))

    img_1_x += 5
    img_2_x -= 5

    img_rect_1 = pygame.draw.rect(screen, blue, (img_1_x, 300, 50, 50))
    img_rect_2 = pygame.draw.rect(screen, blue, (img_2_x, 300, 50, 50))

    if img_rect_1.colliderect(img_rect_2):
        print("Collision detection")

    pygame.display.update()
    clock.tick(FPS)

quit()
