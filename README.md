

# 2D Pixel Shooter Game (Work in Progress)

A simple 2D pixel-style shooter game built with Python and Pygame. This project is currently in development and only has basic player movement and animation systems implemented.

## Project Status: 25% Complete

### What's Working
- Basic player movement system
- Simple physics (gravity and jumping)
- Sprite sheet generation
- Player animation states (idle, run, jump, fall)
- Screen boundary collision
- Basic debug information display

### What's Missing (75%)
1. Core Game Features (40% remaining)
   - Weapon system and shooting mechanics
   - Enemy AI and spawning system
   - Collision detection for combat
   - Health and damage system
   - Score system

2. Graphics and Animation (15% remaining)
   - Professional sprite sheets
   - Particle effects
   - Background graphics
   - UI elements
   - Animation polish

3. Audio (10% remaining)
   - Sound effects
   - Background music
   - Audio manager

4. Game Systems (10% remaining)
   - Save/Load system
   - Menu interface
   - Pause system
   - Settings configuration

### Areas Needing Improvement
1. Code Structure
   - Better organization of game states
   - Improved error handling
   - More comprehensive documentation
   - Code optimization

2. Physics System
   - More precise collision detection
   - Better jump mechanics
   - Platform interaction

3. Animation System
   - Smoother transitions between states
   - More animation frames
   - Better sprite management

4. Performance
   - Frame rate optimization
   - Memory management
   - Resource loading

### Known Issues
1. Player Movement
   - Jump physics needs fine-tuning
   - Movement can feel rigid
   - Screen boundary collision needs smoothing

2. Animation
   - Limited animation frames
   - Basic sprite implementation
   - Missing transition animations

3. Technical
   - Debug information needs cleanup
   - Code structure needs optimization
   - Missing error handling in some areas

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
