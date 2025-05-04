import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Your Game Title") # Add a window title

    # Create a Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        # 1. Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update Game Logic
        # We'll add player movement logic here later.
        player.update(dt) # Call the player's update method

        # 3. Draw Everything
        screen.fill((0, 0, 0))  # Fill with black

        # Draw the player
        player.draw(screen) # Call the player's draw method

        # 4. Update the Display
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()

