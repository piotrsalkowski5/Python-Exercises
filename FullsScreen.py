import pygame, sys

background_Image = 'jaguar.jpg'
pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
background = pygame.image.load(background_Image).convert()
fullscreen = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen == True:
                    screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.RESIZABLE | pygame.NOFRAME, 32)
                else:
                    screen = pygame.display.set_mode((800, 600), 0, 32)



    screen.blit(background,(0,0))
    pygame.display.update()

