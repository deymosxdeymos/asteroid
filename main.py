import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Your Game Title")

    # Create groups for managing game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the containers for the Player class
    Player.containers = (updatable, drawable)

    # Set the containers for the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set the containers for the AsteroidField class
    AsteroidField.containers = (updatable,)

    # Set the containers for the Shot class
    Shot.containers = (shots, updatable, drawable)


    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        # 1. Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()


        # 2. Update Game Logic
        updatable.update(dt)

        # 3. Collision Detection

        # Player vs. Asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
                break # Exit the asteroid loop since the game is over

        if not running: # If the game is over, break the main loop as well
            break

        # Shots vs. Asteroids
        for shot in shots:
            # Use a copy of the asteroids group for iteration in case elements are removed
            for asteroid in list(asteroids):
                if shot.collides_with(asteroid):
                    # If a collision occurs, kill the shot and split the asteroid
                    shot.kill()
                    asteroid.split() # Call the new split method
                    break # A shot can only hit one asteroid at a time, move to the next shot


        # 4. Draw Everything
        screen.fill((0, 0, 0))  # Fill with black

        for obj in drawable:
            obj.draw(screen)

        # 5. Update the Display
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()

