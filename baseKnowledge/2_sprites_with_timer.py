import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("baseKnowledge/material/gunshot.wav")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height= 720
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("baseKnowledge/material/shooting-gallery-pack/PNG/Stall/bg_red.png")
background = pygame.transform.scale(background, (1280, 720))
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair("baseKnowledge/material/shooting-gallery-pack/PNG/HUD/crosshair_outline_large.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("baseKnowledge/material/shooting-gallery-pack/PNG/Objects/target_colored.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    while pygame.sprite.spritecollide(new_target, target_group, False):
        new_target.rect.center = (random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

# Timer
current_time = 0
button_press_time = 0
is_timer_running = False
font = pygame.font.Font(None, 36)
result_font = pygame.font.Font(None, 72)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_timer_running:
                # Start the timer when the first target is hit
                is_timer_running = True
                button_press_time = pygame.time.get_ticks()
            crosshair.shoot()

    # Check if all targets are gone
    if not target_group:
        # Stop the timer when all targets are gone
        is_timer_running = False
        final_time_text = result_font.render(f"Final Time: {seconds}.{milliseconds:03d} seconds. Press R to play again.", True, (255, 255, 255))
        screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 - final_time_text.get_height() // 2))


    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    # Draw the timer on the screen if it's running
    if is_timer_running:
        current_time = pygame.time.get_ticks() - button_press_time
        seconds = current_time // 1000
        milliseconds = current_time % 1000
        timer_text = font.render(f"Time: {seconds}.{milliseconds:03d} seconds", True, (255, 255, 255))
        screen.blit(timer_text, (20, 20))
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_r and not is_timer_running and not target_group:
            # Restart the game when 'R' key is pressed and there are no targets left
            target_group.empty()
            for target in range(20):
                new_target = Target("baseKnowledge/material/shooting-gallery-pack/PNG/Objects/target_colored.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
                while pygame.sprite.spritecollide(new_target, target_group, False):
                    new_target.rect.center = (random.randrange(0, screen_width), random.randrange(0, screen_height))
                target_group.add(new_target)

         

    clock.tick(60)