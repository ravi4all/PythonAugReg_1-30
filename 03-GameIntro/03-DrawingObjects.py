import pygame

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0

screen = pygame.display.set_mode((800,500))

game = True

while game:
    
    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            quit()

##    screen,color,[x,y,width,height]
    pygame.draw.rect(screen, red, [10,10,100,100])

##    screen, color, (x,y), radius
    pygame.draw.circle(screen, green, (200,140), 50)

    pygame.display.update()

##quit()
