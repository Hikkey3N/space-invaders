import pygame
import os

class Invader:
    def __init__(self, type, x, y):
        # Construct the relative path to the invader images
        base_path = os.path.dirname(os.path.abspath(__file__))  # Path to the current file's directory
        image_path_base = os.path.join(base_path, rf"..\Assets\Sprites\Invaders\space_{type}1.png")
        image_path_shoot = os.path.join(base_path, rf"..\Assets\Sprites\Invaders\space_{type}2.png")
        image_path_explode = os.path.join(base_path, r"..\Assets\Sprites\Invaders\space__0009_EnemyExplosion.png")

        image_path_bullet1 = os.path.join(base_path, rf"..\Assets\Sprites\Projectiles\Projectile{type}_1.png")
        image_path_bullet2 = os.path.join(base_path, rf"..\Assets\Sprites\Projectiles\Projectile{type}_2.png")
        image_path_bullet3 = os.path.join(base_path, rf"..\Assets\Sprites\Projectiles\Projectile{type}_3.png")
        image_path_bullet4 = os.path.join(base_path, rf"..\Assets\Sprites\Projectiles\Projectile{type}_4.png")

        # Load the images and resize them if necessary
        self.image_base = pygame.transform.scale(pygame.image.load(image_path_base), (20, 20))
        self.image_shoot = pygame.transform.scale(pygame.image.load(image_path_shoot), (20, 20))
        self.image_explode = pygame.transform.scale(pygame.image.load(image_path_explode), (25, 25))

        self.bullets = [
            pygame.transform.scale(pygame.image.load(image_path_bullet1), (5, 15)),
            pygame.transform.scale(pygame.image.load(image_path_bullet2), (5, 15)),
            pygame.transform.scale(pygame.image.load(image_path_bullet3), (5, 15)),
            pygame.transform.scale(pygame.image.load(image_path_bullet4), (5, 15))
        ]


         # Initialize state variables
        self.current_image = self.image_base
        self.x = x
        self.y = y
        self.health = 1
        self.bullet_speed = 0.2
        self.shooting_freq = 2  # Seconds between shots
        self.last_shot_time = 0

        # Bullets fired by invader
        self.bullet_list = []

        # Timer for changing back the image
        self.shoot_animation_time = 0.5
        self.shoot_start_time = None

        # Bullet animation management
        self.bullet_animation_time = 0.1  # Time between bullet image changes
        self.last_bullet_change_time = 0  # Time of last bullet image change
        self.bullet_image_index = 0  # Index of the current bullet image

    def draw(self, screen):
        # Draw the current image of the invader
        screen.blit(self.current_image, (self.x, self.y))

        # Draw bullets fired by the invader
        for bullet in self.bullet_list:
            screen.blit(bullet['image'], (bullet['x'], bullet['y']))

    def shoot(self):
        # Shoot a bullet if enough time has passed
        current_time = pygame.time.get_ticks() / 1000  # Convert to seconds
        if current_time - self.last_shot_time >= self.shooting_freq:
            self.last_shot_time = current_time
            self.current_image = self.image_shoot  # Change to shooting image
            self.shoot_start_time = current_time  # Set start time for shoot animation

            bullet = {
                'image': self.bullets[self.bullet_image_index],  # Select current bullet image
                'x': self.x + self.image_base.get_width() // 2 - 5,  # Center bullet on invader
                'y': self.y + self.image_base.get_height()
            }
            self.bullet_list.append(bullet)

    def update_bullets(self):
        # Update bullet positions
        for bullet in self.bullet_list:
            bullet['y'] += self.bullet_speed
        # Remove bullets that go off screen
        self.bullet_list = [bullet for bullet in self.bullet_list if bullet['y'] < 720]

        # Update bullet images
        self.animate_bullets()

    def animate_bullets(self):
        current_time = pygame.time.get_ticks() / 1000  # Convert to seconds

        # Check if it's time to change the bullet image
        if current_time - self.last_bullet_change_time >= self.bullet_animation_time:
            self.last_bullet_change_time = current_time
            self.bullet_image_index = (self.bullet_image_index + 1) % len(self.bullets)  # Cycle through bullet images

            # Update all bullets' images to the new one
            for bullet in self.bullet_list:
                bullet['image'] = self.bullets[self.bullet_image_index]

    def update(self, screen):
        self.draw(screen)
        self.update_bullets()

        # Check if the shoot animation time has passed
        if self.shoot_start_time is not None:
            current_time = pygame.time.get_ticks() / 1000  # Convert to seconds
            if current_time - self.shoot_start_time >= self.shoot_animation_time:
                self.current_image = self.image_base  # Change back to normal image
                self.shoot_start_time = None  # Reset the shoot start time