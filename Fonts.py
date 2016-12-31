import pygame, sys, colorsys

pygame.init()
pygame.font.init()

try:
    screen = pygame.display.set_mode((800, 600), 0, 32)
except pygame.error():
    print("something")
    print(pygame.error)
    exit()


my_font = pygame.font.Font('my.otf' ,32)
new_surface = my_font.render("What's the fuck !!!", True, (0, 0, 0), (255, 255, 255))
pygame.image.save(new_surface,"cus.jpg")