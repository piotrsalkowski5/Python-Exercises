import pygame, sys

background_image = "jaguar.jpg"
SCREEN_SIZE = (640,480)
message = "  Demonstarcja scrollera na ekranie biblioteki pygame  "
clock = pygame.time
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

font = pygame.font.SysFont("arial",80)
text_surface = font.render(message,True,(0,0,255))

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height())/2

background = pygame.image.load(background_image).convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))

    x -= 1
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x,y))
    screen.blit(text_surface, (x+text_surface.get_width(),y))
    clock.wait(10)
    pygame.display.update()