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
| Add a scoring system | Planned |
| Implement multiple lives and respawning | Planned |
| Add an explosion effect for the asteroids | Planned |
| Add acceleration to the player movement | Planned |
| Make the objects wrap around the screen instead of disappearing | Planned |
| Add a background image | Planned |
| Create different weapon types | Planned |
| Make the asteroids lumpy instead of perfectly round | Planned |
| Make the ship have a triangular hit box instead of a circular one | Planned |
| Add a shield power-up | Planned |
| Add a speed power-up | Planned |
| Add bombs that can be dropped | Planned |

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
