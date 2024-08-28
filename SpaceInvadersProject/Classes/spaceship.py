import pygame
import os

class Spaceship:
    def __init__(self, x, y):
        # Construct the relative path to the spaceship image
        base_path = os.path.dirname(os.path.abspath(__file__))  # Path to the current file's directory
        image_path = os.path.join(base_path, r"..\Assets\Sprites\SpaceShip\spaceship.png")

        # Scale the image the the proper size and load the image
        spaceship_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(spaceship_image, (40, 40))
        

        # Set position and speed
        self.x = x
        self.y = y
        self.speed = 1

        # Default lifes = 3
        self.life_left = 3
        

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
