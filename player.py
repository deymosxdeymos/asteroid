import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0.0  # New timer variable, starts at 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Only shoot if the cooldown timer is zero or less
        if self.shoot_cooldown_timer <= 0:
            # Create a new shot at the player's current position
            new_shot = Shot(self.position.x, self.position.y)

            # Calculate the shot's velocity in the direction the player is facing
            forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
            new_shot.velocity = forward_vector * PLAYER_SHOOT_SPEED

            # Reset the cooldown timer
            self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Decrease the shoot cooldown timer
        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt
            # Ensure the timer doesn't go below zero
            if self.shoot_cooldown_timer < 0:
                self.shoot_cooldown_timer = 0

        # Call the parent update
        super().update(dt)
