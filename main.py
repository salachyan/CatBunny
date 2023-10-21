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

block_image = pygame.image.load('block.png')
block_pos = [WIDTH // 2, HEIGHT - 350]  # Adjust this position based on where you want the block to appear initially.
block_chance = 0.005  # Adjust this value to control frequency. The higher, the more frequent.
blocks = []  # List to store the position of each block.
block_speed = 5  # Speed at which blocks move to the left.
block_pos_x = random.randint(0, WIDTH - block_image.get_width()) 
block_pos_y = random.randint(HEIGHT - block_image.get_height() - 150, HEIGHT - block_image.get_height())



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

wizard_image = pygame.image.load('wizard.png')
wizard_image = pygame.transform.scale(wizard_image, (100, 200))

fireball_image = pygame.image.load('fireball.png')
fireball_image = pygame.transform.scale(fireball_image, (20, 20))

# Wizard position
wizard_pos = [WIDTH - wizard_image.get_width(), 250]

# Fireball data
fireballs = []
fireball_speed = 5
fireball_chance = 0.02  # The chance on each frame for the wizard to shoot a fireball

# Load the Carrot Image & Set its Position:
carrot_image = pygame.image.load('carrot.png')  # Load the carrot image
carrot_image = pygame.transform.scale(carrot_image, (50, 80))
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

def on_block(catbunny_rect, blocks):
    for block in blocks:
        block_rect = pygame.Rect(block[0], block[1], block_image.get_width(), block_image.get_height())
        if catbunny_rect.colliderect(block_rect):
            return True
    return False

def generate_random_carrot_position():
    new_x = random.randint(600, WIDTH - carrot_image.get_width())
    new_y = random.randint(50, 300)  # Ensure the carrot is above the character
    return (new_x, new_y)

carrot_pos = generate_random_carrot_position()

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
    carrot_rect = pygame.Rect(carrot_pos[0], carrot_pos[1], 20, 30)

    if catbunny_rect.colliderect(carrot_rect):
        score += 1  
        carrot_pos = generate_random_carrot_position()  # Move the carrot to a new random position

    # Check for collision with block
    for block in blocks:
        block_rect = pygame.Rect(block[0], block[1], block_image.get_width(), block_image.get_height())
        if catbunny_rect.colliderect(block_rect) and velocity > 0:  # Check if the cat is descending onto the block
            catbunny_pos_y = block[1] - catbunny_rect.height
            velocity = 0
            jump = False

    # Check if the cat is on any block
    if not on_block(catbunny_rect, blocks):
        # Move the cat down with gravity if it's not on a block and not jumping
        catbunny_pos_y += gravity

    if jump:
        catbunny_pos_y += velocity
        velocity += gravity
        if catbunny_pos_y >= ground:
            catbunny_pos_y = ground
            jump = False
            velocity = 0
    
    # Randomly shoot a fireball
    if random.random() < fireball_chance:
        fireball_start_pos = [wizard_pos[0], wizard_pos[1] + wizard_image.get_height() // 2]
        fireballs.append(fireball_start_pos)

    # Move fireballs to the left
    for fireball in fireballs:
        fireball[0] -= fireball_speed

    # Remove fireballs that are off-screen
    fireballs = [fireball for fireball in fireballs if fireball[0] + fireball_image.get_width() > 0]

    if random.random() < block_chance:
        new_block_pos = [WIDTH, HEIGHT - 350]  # Adjust the height value if necessary.
        blocks.append(new_block_pos)

    for block in blocks:
        block[0] -= block_speed

    blocks = [block for block in blocks if block[0] + block_image.get_width() > 0]

    # Animation frame update
    current_time = pygame.time.get_ticks()
    if current_time - last_frame_time > frame_duration:
        current_frame = (current_frame + 1) % len(frames)
        last_frame_time = current_time
        
     # Update carrot's position
    carrot_pos = (carrot_pos[0] - carrot_speed, carrot_pos[1])
    # If the carrot is completely off the screen to the left
    if carrot_pos[0] < -carrot_image.get_width():
        carrot_pos = list(generate_random_carrot_position())
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
    
    # Draw the wizard and fireballs
    screen.blit(wizard_image, wizard_pos)
    for fireball in fireballs:
        screen.blit(fireball_image, fireball)
        
    for block in blocks:
        screen.blit(block_image, block)

    screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
    screen.blit(carrot_image, carrot_pos)
    
    text = font.render(f'Score: {score}', True, (0, 0, 0))  # Black color for the text
    screen.blit(text, (10, 10))  # Display the score in the top-left corner

    pygame.display.flip()


