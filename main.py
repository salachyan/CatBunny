import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLUE WAFFLE")

new_width = 350
new_height = 150
frame_count = len([name for name in os.listdir('catbunny') if os.path.isfile(os.path.join('catbunny', name))])
frames = [pygame.transform.scale(pygame.image.load(os.path.join('catbunny', f'frame{i}.png')), (new_width, new_height)) for i in range(1, frame_count + 1)]

current_frame = 0
frame_duration = 70
last_frame_time = pygame.time.get_ticks()

catbunny_pos_x = WIDTH // 2 - new_width // 2
catbunny_pos_y = HEIGHT - 300

ground = HEIGHT - 300

# Jumping variables
jump = False
gravity = 1
jump_force = -20
velocity = 0

clock = pygame.time.Clock()  # Initialize the clock object
FPS = 60  # Set the desired frames per second

while True:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not jump:
                jump = True
                velocity = jump_force

    if jump:
        catbunny_pos_y += velocity
        velocity += gravity
        if catbunny_pos_y >= ground:
            catbunny_pos_y = ground
            jump = False
            velocity = 0

    # Animation frame update
    current_time = pygame.time.get_ticks()
    if current_time - last_frame_time > frame_duration:
        current_frame = (current_frame + 1) % len(frames)
        last_frame_time = current_time

    screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
    pygame.display.flip()


