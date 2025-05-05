import pygame
import random  # Import the random module
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )

    def update(self, dt: float):
        self.position += self.velocity * dt
        # Update the rect position to match the current position
        self.rect.center = (int(self.position.x), int(self.position.y))
        # Call the parent update
        super().update(dt)

    def split(self):
        # Immediately kill the current asteroid
        self.kill()

        # If it's a small asteroid, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Otherwise, spawn 2 new smaller asteroids

        # Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # Calculate the new velocities by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Rotate and scale up
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Rotate and scale up

        # Compute the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroids at the current position
        # The Asteroid class's containers are set in main, so they are added to groups automatically
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
