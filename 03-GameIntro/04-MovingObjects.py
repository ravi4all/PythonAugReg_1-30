import pygame

pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0

screen = pygame.display.set_mode((800,500))

game = True

rect_x = 0
rect_y = 0

move_x = 0
move_y = 0

while game:
    
    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x += 10

##    screen,color,[x,y,width,height]
    pygame.draw.rect(screen, red, [rect_x,rect_y,100,100])

##    screen, color, (x,y), radius
##    pygame.draw.circle(screen, green, (200,140), 50)

    rect_x += move_x

    pygame.display.update()

##quit()
