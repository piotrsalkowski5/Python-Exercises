import pygame,sys
from pygame.locals import *
background_image = 'jaguar.jpg'
mouse_motion_image = 'zloty.jpg'

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Images")

background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_motion_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor,(x,y))
    screen.set_clip(0,0,400,400)

    pygame.display.update()