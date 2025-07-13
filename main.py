import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    display = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    init_x, init_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    player = Player(init_x, init_y)

    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

        display.fill(color="black")
        player.update(dt)
        player.draw(display)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
