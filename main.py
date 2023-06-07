import pygame, sys
from settings import *
from level import Level

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
background_image = pygame.image.load("background_image.jpg")
screenUpdate = pygame.transform.scale(background_image, (screen_width,screen_height))
level = Level(level_map, screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(screenUpdate, (0,0))
    level.run()
    pygame.display.update()
    clock.tick(60)

    