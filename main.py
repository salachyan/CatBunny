import os
import random
import subprocess
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
pygame.display.set_caption("CatBunny's Hop Adventure")

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (3600, 600))

background_pos1 = [0, 0]
background_pos2 = [3600, 0]

background_speed = 2.5

blocks = []  # Store active blocks
block_spawn_time = 0
block_spawn_interval = random.randint(1000, 2500)  # between 1 and 3 seconds
block_image = pygame.image.load('block.png')
block_width, block_height = block_image.get_size()
block_speed = 5

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
catbunny_pos_y = HEIGHT - 200

ground = HEIGHT - 260



carrot1_image = pygame.image.load('carrot$.png')
carrot1_image = pygame.transform.scale(carrot1_image, (30, 40))
carrot1_pos = [5, 0]

wizard_image = pygame.image.load('wizard.png')
wizard_image = pygame.transform.scale(wizard_image, (100, 200))

fireball_image = pygame.image.load('fireball.png')
fireball_image = pygame.transform.scale(fireball_image, (20, 20))

# Wizard position
wizard_pos = [850, 300]

# Fireball data
fireballs = []
fireball_speed = 5
fireball_chance = 0.01

# Load the Carrot Image & Set its Position:
carrot_image = pygame.image.load('carrot.png')
carrot_image = pygame.transform.scale(carrot_image, (50, 80))
carrot_pos = [WIDTH, random.randint(0, HEIGHT - carrot_image.get_height())]
carrot_speed = 5

# Collision Detection and Score Management Initialization:
score = 0

font = pygame.font.SysFont(None, 36)

# Jumping variables
jump = False
gravity = 2
jump_force = -25
velocity = 10

def generate_random_carrot_position():
    new_x = random.randint(600, WIDTH - carrot_image.get_width())
    new_y = random.randint(50, 400)
    return (new_x, new_y)

carrot_pos = generate_random_carrot_position()

clock = pygame.time.Clock()
FPS = 30

# Pause button
go_button_image = pygame.image.load('go.png')
go_button_image = pygame.transform.scale(go_button_image, (90, 90))
pause_button_image = pygame.image.load('pause.png')
pause_button_image = pygame.transform.scale(pause_button_image, (90, 90))

paused = False
button_rect = pause_button_image.get_rect(topleft=(910, -20))  # Assuming you want it at the same position


while True:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Variables
    on_block = False

    # Check if catbunny lands on a block or falls off a block
    for block in blocks:
        block_rect = pygame.Rect(block[0], block[1], block_width, block_height)
        
        # Check if catbunny's bottom collides with the block
        if block_rect.collidepoint(catbunny_rect1.midbottom) and velocity >= 0:
            on_block = True
            catbunny_pos_y = block_rect.top - catbunny_rect1.height + 30  # Add your desired offset here
            velocity = 0
            break
        
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jump = True
                velocity = jump_force
        # Handle the button click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                paused = not paused

    
    # STEP 3: Pause game logic when paused
    if not paused:
        catbunny_rect = pygame.Rect(catbunny_pos_x-100, catbunny_pos_y, new_width, new_height)
        carrot_rect = pygame.Rect(carrot_pos[0], carrot_pos[1], 20, 30)

        if catbunny_rect.colliderect(carrot_rect):
            score += 1
            carrot_pos = generate_random_carrot_position()
            
        # Check if score is 10 right after updating it
        if score == 5:
            subprocess.Popen(["python3", "winpage.py"])
            exit(1)
            

        # Always apply gravity
        catbunny_pos_y += velocity
        
        # Check if CatBunny goes over the top boundary
        if catbunny_pos_y < -50:
            velocity = 0  # Reset the velocity so it starts descending immediately


        if jump:
            velocity += gravity
            if catbunny_pos_y >= ground:
                catbunny_pos_y = ground
                jump = False
                velocity = 0

        fireball_rect = pygame.Rect(carrot_pos[0], carrot_pos[1], 20, 30)

        # Check for collision between catbunny and fireballs:
        catbunny_rect = pygame.Rect(catbunny_pos_x-100, catbunny_pos_y, new_width, new_height)
        
        for fireball in fireballs:
            fireball_rect = pygame.Rect(fireball[0], fireball[1], 20, 20)
            if catbunny_rect.colliderect(fireball_rect):
                score -= 1  # Decrement the score
                if score < 0:
                    score = 0  # Ensure score doesn't go below 0
                fireballs.remove(fireball)  # Remove the fireball



        if random.random() < fireball_chance:
            fireball_start_pos = [wizard_pos[0], wizard_pos[1] + wizard_image.get_height() // 2]
            fireballs.append(fireball_start_pos)

        fireballs = [fireball for fireball in fireballs if fireball[0] + fireball_image.get_width() > 0]

        # Move fireballs to the left
        for fireball in fireballs:
            fireball[0] -= fireball_speed
        
        # below lines are block FUCK BLOCKS FUCK FUCK FUCK
        
        current_time = pygame.time.get_ticks()
        if current_time > block_spawn_time + block_spawn_interval:
            new_block_pos_x = WIDTH
            new_block_pos_y = random.randint(100, 350)

            blocks.append([new_block_pos_x, new_block_pos_y])
            block_spawn_time = current_time
            block_spawn_interval = random.randint(2000, 4000)


        catbunny_rect1 = pygame.Rect(catbunny_pos_x+30, catbunny_pos_y, new_width, new_height)

        # Check if catbunny lands on a block or falls off a block
        # Move all blocks to the left
        for block in blocks:
            block[0] -= block_speed  # move the block leftwards


        # If not on a block and below ground, place catbunny on the ground
        if not on_block and catbunny_pos_y >= ground:
            catbunny_pos_y = ground
            velocity = 0

            
        # above lines are block FUCK BLOCKS FUCK FUCK FUCK

        if current_time - last_frame_time > frame_duration:
            current_frame = (current_frame + 1) % len(frames)
            last_frame_time = current_time

        carrot_pos = (carrot_pos[0] - carrot_speed, carrot_pos[1])
        if carrot_pos[0] < -carrot_image.get_width():
            carrot_pos = list(generate_random_carrot_position())
            carrot_pos[1] = random.randint(0, HEIGHT - 300 - carrot_image.get_height())

        background_pos1[0] -= background_speed
        background_pos2[0] -= background_speed
        if background_pos1[0] < -3600:
            background_pos1[0] = 3600
        if background_pos2[0] < -3600:
            background_pos2[0] = 3600

        scroll_speed = 5
        platform_pos1_x -= scroll_speed
        platform_pos2_x -= scroll_speed

        if platform_pos1_x <= -platform_image.get_width():
            platform_pos1_x = platform_image.get_width()
        if platform_pos2_x <= -platform_image.get_width():
            platform_pos2_x = platform_image.get_width()

        screen.blit(background_image, background_pos1)
        screen.blit(background_image, background_pos2)
        screen.blit(platform_image, (platform_pos1_x, HEIGHT - platform_image.get_height()-40))
        screen.blit(platform_image, (platform_pos2_x, HEIGHT - platform_image.get_height()-40))
        screen.blit(wizard_image, wizard_pos)


        for block in blocks:
            screen.blit(block_image, (block[0], block[1]))
        
        blocks = [block for block in blocks if block[0] + block_width > 0]
        
        for fireball in fireballs:
            screen.blit(fireball_image, fireball)

        screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
        screen.blit(carrot_image, carrot_pos)
        
        screen.blit(carrot1_image, carrot1_pos)
        
        # Display the score
        font = pygame.font.SysFont(None, 36)  # Use the default font with size 36
        score_text = font.render(f"{score}", True, (255, 255, 255))  # Render the score text in white
        screen.blit(score_text, (40, 10))  # Draw the score text at the top-left corner of the screen

        screen.blit(pause_button_image, button_rect.topleft)

        pygame.display.flip()

    else:
        screen.blit(background_image, background_pos1)
        screen.blit(background_image, background_pos2)
        screen.blit(platform_image, (platform_pos1_x, HEIGHT - platform_image.get_height()-80))
        screen.blit(platform_image, (platform_pos2_x, HEIGHT - platform_image.get_height()-80))
        screen.blit(wizard_image, wizard_pos)


        for block in blocks:
            screen.blit(block_image, (block[0], block[1]))
        
        blocks = [block for block in blocks if block[0] + block_width > 0]
        
        for fireball in fireballs:
            screen.blit(fireball_image, fireball)

        screen.blit(frames[current_frame], (catbunny_pos_x, catbunny_pos_y))
        screen.blit(carrot_image, carrot_pos)
        
        screen.blit(carrot1_image, carrot1_pos)
        
        # Display the score
        font = pygame.font.SysFont(None, 36)  # Use the default font with size 36
        score_text = font.render(f"{score}", True, (255, 255, 255))  # Render the score text in white
        screen.blit(score_text, (40, 10))  # Draw the score text at the top-left corner of the screen

        screen.blit(go_button_image, button_rect.topleft)
        pygame.display.flip()
