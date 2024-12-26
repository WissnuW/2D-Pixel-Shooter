# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
VIRTUAL_WIDTH = 320
VIRTUAL_HEIGHT = 180
FPS = 60

# Sprite settings
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32

# Colors
BACKGROUND_COLOR = (20, 20, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_SPEED = 3
PLAYER_JUMP_POWER = -8
GRAVITY = 0.4
MAX_FALL_SPEED = 10

# Weapon settings
WEAPON_TYPES = {
    'pistol': {
        'damage': 10,
        'fire_rate': 200,  # milliseconds
        'bullet_speed': 8,
        'spread': 2
    },
    'shotgun': {
        'damage': 8,
        'fire_rate': 800,
        'bullet_speed': 7,
        'spread': 15,
        'pellets': 5
    },
    'rifle': {
        'damage': 15,
        'fire_rate': 100,
        'bullet_speed': 10,
        'spread': 5
    }
}

# Enemy settings
ENEMY_TYPES = {
    'walker': {
        'health': 30,
        'speed': 1,
        'damage': 10,
        'score': 100
    },
    'shooter': {
        'health': 20,
        'speed': 2,
        'damage': 5,
        'fire_rate': 1000,
        'score': 150
    },
    'boss': {
        'health': 200,
        'speed': 1.5,
        'damage': 20,
        'fire_rate': 500,
        'score': 1000
    }
}

# Player Animation Data
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