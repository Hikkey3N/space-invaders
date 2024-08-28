import pygame
import sys
from Classes.spaceship import Spaceship
from Classes.invader import Invader


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Invaders')


# Create objects
spaceship = Spaceship(620, 650)
invader = Invader('C', 620, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move_left()
    if keys[pygame.K_RIGHT]:
        spaceship.move_right()

    # # Move the invader
    # invader.move()
    # if invader.x <= 0 or invader.x >= 640 - invader.image.get_width():
    #     invader.reverse_direction()

    # Make the invader shoot
    invader.shoot()  # Invader attempts to shoot based on its shooting frequency
    invader.update_bullets()  # Update the position of invader's bullets

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the spaceship and invader
    spaceship.draw(screen)
    invader.update(screen)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()

