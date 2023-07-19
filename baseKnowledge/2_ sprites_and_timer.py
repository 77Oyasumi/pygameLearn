import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General Setup
pygame.init()
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

# Game Screen
screen_width = 1280
screen_height= 720
screen = pygame.display.set_mode((screen_width, screen_height))

crosshair = Crosshair(50, 50, 100, 100,(255, 255, 255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255,105,180))
    current_time = pygame.time.get_ticks()

    if current_time - button_press_time > 2000:
        screen.fill((0, 0, 0))
    
    crosshair_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)