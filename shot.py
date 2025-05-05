import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: int, y: int):
        # Call the parent class's constructor with the shot radius
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        # Draw the shot as a white filled circle
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self, dt: float):
        # Move the shot in a straight line
        self.position += self.velocity * dt

        # Call the parent update
        super().update(dt)
