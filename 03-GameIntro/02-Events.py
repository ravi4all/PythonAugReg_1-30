import pygame

pygame.init()

white = 255,255,255

screen = pygame.display.set_mode((800,500))

game = True

while game:
    
    screen.fill(white)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game = False
            quit()

    pygame.display.update()

##quit()
