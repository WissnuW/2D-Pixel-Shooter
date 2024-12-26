# Sprite dimensions
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32

# Animation frames
PLAYER_ANIMATIONS = {
    'idle': {
        'row': 0,
        'frames': 4,
        'duration': 200  # milliseconds per frame
    },
    'run': {
        'row': 1,
        'frames': 6,
        'duration': 100
    },
    'jump': {
        'row': 2,
        'frames': 2,
        'duration': 150
    },
    'fall': {
        'row': 2,
        'frames': 2,
        'start_frame': 2,
        'duration': 150
    },
    'shoot': {
        'row': 3,
        'frames': 3,
        'duration': 100
    }
} 