import pygame
import math
from scripts.constants import *
from scripts.spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, collision_sprites):
        super().__init__(groups)
        
        # Animation setup
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.state = 'idle'
        
        # General setup
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = self.rect.inflate(-10, -10)
        
        # Movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 5
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False
        self.facing_right = True
        
        # Limits
        self.terminal_velocity = 15  # Maximum falling speed
        self.min_y = 0  # Top of screen
        self.max_y = VIRTUAL_HEIGHT - self.rect.height  # Bottom of screen
        self.min_x = 0  # Left of screen
        self.max_x = VIRTUAL_WIDTH - self.rect.width  # Right of screen
        
        # Collision
        self.collision_sprites = collision_sprites
        
    def import_assets(self):
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}
        sprite_sheet = SpriteSheet('assets/images/player/player_sheet.png')
        
        # Load animations from sprite sheet
        for action, data in PLAYER_ANIMATIONS.items():
            row = data['row']
            frames = data['frames']
            start_frame = data.get('start_frame', 0)
            
            animation = sprite_sheet.get_sprite_strip(
                start_frame * SPRITE_WIDTH,
                row * SPRITE_HEIGHT,
                SPRITE_WIDTH,
                SPRITE_HEIGHT,
                frames
            )
            self.animations[action] = animation
            
    def constrain_position(self):
        # Constrain horizontal position
        if self.rect.left < self.min_x:
            self.rect.left = self.min_x
            self.pos.x = self.rect.x
        elif self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.pos.x = self.rect.x
            
        # Constrain vertical position
        if self.rect.top < self.min_y:
            self.rect.top = self.min_y
            self.pos.y = self.rect.y
            self.direction.y = 0
        elif self.rect.bottom > self.max_y:
            self.rect.bottom = self.max_y
            self.pos.y = self.rect.y
            self.direction.y = 0
            self.on_ground = True
            
    def get_state(self):
        # Determine animation state
        if self.direction.y < 0:
            self.state = 'jump'
        elif self.direction.y > 1:
            self.state = 'fall'
        else:
            if self.direction.x != 0:
                self.state = 'run'
            else:
                self.state = 'idle'
                
    def animate(self, dt):
        animation = self.animations[self.state]
        
        # Loop over frame index
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
            
        # Set the rect
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        else:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
            
    def input(self):
        keys = pygame.key.get_pressed()
        
        # Movement input
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
            
        # Jump input
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.direction.y = self.jump_power
            self.on_ground = False
            
    def apply_gravity(self, dt):
        # Apply gravity
        self.direction.y += self.gravity * dt
        
        # Limit falling speed
        if self.direction.y > self.terminal_velocity:
            self.direction.y = self.terminal_velocity
            
        # Update position
        self.pos.y += self.direction.y * dt
        self.rect.y = round(self.pos.y)
        
    def move(self, dt):
        # Horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        
    def update(self, dt, current_time):
        self.input()
        self.move(dt)
        self.apply_gravity(dt)
        self.constrain_position()
        self.get_state()
        self.animate(dt)
