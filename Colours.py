import pygame, random

pygame.init()

screen = pygame.display.set_mode((640,480))
all_colours = pygame.Surface((4096,4096),24)

for r in range(256):
    print(r+1)
    x = (r&15)*256
    y = (r>>4)*256
    for g in range(256):
        for b in range(256):
            all_colours.set_at((x+g, y+b),(r,g,b))
pygame.image.save(all_colours, "allcolours.bmp")