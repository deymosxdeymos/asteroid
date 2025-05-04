import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # Keep rotation within 0-360 degrees (optional but good practice)
        self.rotation %= 360

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left (reverse dt)
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt)

        # Call the parent update (which currently does nothing in the base)
        super().update(dt)
