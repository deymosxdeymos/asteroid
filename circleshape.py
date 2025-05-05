import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        # For collision detection (CircleShape's 'rect' is based on its circle)
        # This is a common way to represent collision bounds for sprites in Pygame
        self.rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        # Update the rect position to match the current position
        self.rect.center = (int(self.position.x), int(self.position.y))
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        # Calculate the distance between the centers of the two circles
        distance = self.position.distance_to(other.position)

        # Check if the distance is less than or equal to the sum of their radii
        if distance <= self.radius + other.radius:
            return True
        else:
            return False
