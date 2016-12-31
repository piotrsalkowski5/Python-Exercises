background_image = 'jaguar.jpg'
sprite_image = 'zloty.jpg'

import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image)

x = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,100))
    x += 10
    if x>640.:
        x -= 640.
    pygame.display.update()