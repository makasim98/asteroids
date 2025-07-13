import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    display = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    init_x, init_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    player = Player(init_x, init_y)
    asteroid_field = AsteroidField()

    while True:
        # Check for inputs
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

        # Update Screen
        display.fill(color="black")
        updatable.update(dt)
        for member in drawable:
            member.draw(display)

        for asteroid in asteroids:

            if asteroid.colides_with(player):
                print("Game Over!")
                return

            for shot in shots:
                if asteroid.colides_with(shot):
                    asteroid.split()
                    shot.kill()


        # Show next frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
