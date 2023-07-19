import pygame, sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1920
screen_height= 1080
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick(60)