import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        # 1. Handle Events (like closing the window - we'll add this later)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # 2. Update Game Logic (e.g., move characters - we'll add this later)
    # ...

    # 3. Draw Everything
    screen.fill((0, 0, 0))  # Fill with black
    # You would draw your game elements here
    # ...

    # 4. Update the Display (call this last!)
    pygame.display.flip()
    dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
