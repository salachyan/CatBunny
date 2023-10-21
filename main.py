import os
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600

# Colors
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLUE WAFFLE")

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (3600, 600))  # Preserve the original size as it's designed for this resolution

background_pos1 = [0, 0]  # This starts at the left edge of the screen
background_pos2 = [3600, 0]  # This starts just off the right edge of the screen, given the width of the background image

background_speed = 2.5 # Adjust this value for desired background scroll speed

platform_image = pygame.image.load('platform.png')
platform_pos1_x = 0
platform_pos2_x = platform_image.get_width()

new_width = 350
new_height = 150
frame_count = len([name for name in os.listdir('catbunny') if os.path.isfile(os.path.join('catbunny', name))])
frames = [pygame.transform.scale(pygame.image.load(os.path.join('catbunny', f'frame{i}.png')), (new_width, new_height)) for i in range(1, frame_count + 1)]

current_frame = 0
frame_duration = 50
last_frame_time = pygame.time.get_ticks()

catbunny_pos_x = 40
catbunny_pos_y = HEIGHT - 300

ground = HEIGHT - 300

# Load the Carrot Image & Set its Position:
carrot_image = pygame.image.load('carrot.png')  # Load the carrot image
carrot_image = pygame.transform.scale(carrot_image, (100, 100))
carrot_pos = [WIDTH, random.randint(0, HEIGHT - carrot_image.get_height())]
carrot_speed = 5  # Initialize carrot speed

# Collision Detection and Score Management Initialization:
score = 0  # Initial score

font = pygame.font.SysFont(None, 36)  # Choose a font and size for displaying score.

# Jumping variables
jump = False
gravity = 2
jump_force = -30
velocity = 10

clock = pygame.time.Clock()  # Initialize the clock object
FPS = 30  # Set the desired frames per second

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

 # Check for collision between catbunny and carrot:
    catbunny_rect = pygame.Rect(catbunny_pos_x, catbunny_pos_y, new_width, new_height)
    carrot_rect = pygame.Rect(carrot_pos[0], carrot_pos[1], carrot_image.get_width(), carrot_image.get_height())

    if catbunny_rect.colliderect(carrot_rect):
        score += 1  
        carrot_pos = [random.randint(0, WIDTH - carrot_image.get_width()), random.randint(0, HEIGHT - carrot_image.get_height())]  # Move the carrot to a new random position
        
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
        
     # Update carrot's position
    carrot_pos[0] -= carrot_speed
    # If the carrot is completely off the screen to the left
    if carrot_pos[0] < -carrot_image.get_width():
        carrot_pos[0] = WIDTH 
        carrot_pos[1] = random.randint(0, HEIGHT - 300 - carrot_image.get_height()) 


    # Update the background positions
    background_pos1[0] -= background_speed
    background_pos2[0] -= background_speed

    # If the first background is completely off the screen to the left
    if background_pos1[0] < -3600:
        background_pos1[0] = 3600  # Reposition it to the right of the second background

    # If the second background is completely off the screen to the left
    if background_pos2[0] < -3600:
        background_pos2[0] = 3600  # Reposition it to the right of the first background

    scroll_speed = 5  # Adjust this value as needed
    platform_pos1_x -= scroll_speed
    platform_pos2_x -= scroll_speed

    if platform_pos1_x <= -platform_image.get_width():
        platform_pos1_x = platform_image.get_width()

    if platform_pos2_x <= -platform_image.get_width():
        platform_pos2_x = platform_image.get_width()
        
    # Draw the backgrounds
    screen.blit(background_image, background_pos1)
    screen.blit(background_image, background_pos2)
    screen.blit(platform_image, (platform_pos1_x, HEIGHT - platform_image.get_height()-80))
    screen.blit(platform_image, (platform_pos2_x, HEIGHT - platform_image.get_height()-80))
    
    screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
    screen.blit(carrot_image, carrot_pos)
    
    text = font.render(f'Score: {score}', True, (0, 0, 0))  # Black color for the text
    screen.blit(text, (10, 10))  # Display the score in the top-left corner

    pygame.display.flip()


