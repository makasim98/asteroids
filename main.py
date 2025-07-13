import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    display = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

       display.fill(color="black")
       pygame.display.flip()

if __name__ == "__main__":
    main()
