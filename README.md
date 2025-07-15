# Asteroids

A project in the curriculum of [Boot.dev](https://www.boot.dev) to practice Python OOP principles. It's a simple game made using the Pygame package. 

## Current fuctionality
* Auto spawning of asteroids
* Player movement using WASD and shooting with SPACEBAR
* Player death on asteroid collision
* Asteroid splitting Big -> Medium -> Small

## Posible Additions:
| Feature | Status |
| :------ | :----: |
| Add a scoring system | N/A |
| Implement multiple lives and respawning | N/A |
| Add an explosion effect for the asteroids | N/A |
| Add acceleration to the player movement | N/A |
| Make the objects wrap around the screen instead of disappearing | N/A |
| Add a background image | N/A |
| Create different weapon types | N/A |
| Make the asteroids lumpy instead of perfectly round | N/A |
| Make the ship have a triangular hit box instead of a circular one | N/A |
| Add a shield power-up | N/A |
| Add a speed power-up | N/A |
| Add bombs that can be dropped | N/A |

## How to run the game:
### Prerequesites
- Python 3 installed
- UV package manager installed

### Install
1. Clone the ```main``` branch of the project repository
2. Create a VENV for the uv project and activate it
    1. Create a VENV with ```uv venv``` when inside project directory
    2. Activate the virtual environment with ```source .venv/bin/activate```
3. Running the game with ```uv run main.py``` will automatically install all required packages before running the game.
