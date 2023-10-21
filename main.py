import os
import random
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

    screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
    screen.blit(carrot_image, carrot_pos)
    
    text = font.render(f'Score: {score}', True, (0, 0, 0))  # Black color for the text
    screen.blit(text, (10, 10))  # Display the score in the top-left corner

    pygame.display.flip()


