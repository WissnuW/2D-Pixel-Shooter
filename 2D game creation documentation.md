

# 2D Pixel Shooter Game (Work in Progress)

A simple 2D pixel-style shooter game built with Python and Pygame. This project is currently in development and only has basic player movement and animation systems implemented.

## Project Structure
```
gameV2/
├── assets/
│   └── images/
│       └── player/
│           ├── player_sheet.png (auto-generated)
│           └── player_data.py
├── scripts/
│   ├── constants.py
│   ├── player.py
│   ├── spritesheet.py
│   └── create_player_sprite.py
└── test_player.py
```

## Features Currently Implemented
- Basic player movement system
- Simple physics (gravity and jumping)
- Sprite sheet generation
- Player animation states (idle, run, jump, fall)
- Screen boundary collision
- Basic debug information display

## Controls
- Left/Right Arrow or A/D: Move horizontally
- Space or Up Arrow: Jump

## Requirements
- Python 3.x
- Pygame

## Installation
1. Clone this repository
2. Install Pygame:
```bash
pip install pygame
```

3. Run the test file:
```bash
python test_player.py
```

## File Descriptions
- `constants.py`: Contains game constants and configurations
- `player.py`: Player class with movement and animation logic
- `spritesheet.py`: Handles sprite sheet loading and manipulation
- `create_player_sprite.py`: Generates basic player sprite sheet
- `test_player.py`: Test environment for player mechanics

## Current Status
This project is still in early development. Future features planned:
- Weapon system
- Enemy AI
- Level design
- Sound effects and music
- Score system
- Menu interface
- Multiple weapons
- Power-ups

## Contributing
Feel free to contribute to this project. As this is a work in progress, there are many areas that can be improved and expanded upon.

## Note
This is an educational project and is currently incomplete. Many features are still in development, and the current implementation is basic and meant for testing purposes.

## License
MIT License

## Author
Wisnu Wardhana

---
Last Updated: 26/12/2024
