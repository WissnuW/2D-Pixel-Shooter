import pygame
from .constants import *
from .bullet import Bullet
import math

class Weapon:
    def __init__(self, weapon_type, player):
        self.type = weapon_type
        self.player = player
        self.settings = WEAPON_TYPES[weapon_type]
        
        # Shooting properties
        self.last_shot_time = 0
        self.can_shoot = True
        
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.settings['fire_rate']:
            self.last_shot_time = current_time
            
            # Get mouse position for direction
            mouse_pos = pygame.mouse.get_pos()
            # Convert screen coordinates to virtual coordinates
            mouse_x = mouse_pos[0] * (VIRTUAL_WIDTH / SCREEN_WIDTH)
            mouse_y = mouse_pos[1] * (VIRTUAL_HEIGHT / SCREEN_HEIGHT)
            
            # Calculate direction
            start_pos = self.player.rect.center
            dx = mouse_x - start_pos[0]
            dy = mouse_y - start_pos[1]
            angle = math.atan2(dy, dx)
            
            # Create bullets based on weapon type
            if self.type == 'shotgun':
                self.shoot_shotgun(start_pos, angle)
            else:
                self.shoot_single(start_pos, angle)
                
    def shoot_single(self, start_pos, angle):
        # Add random spread
        spread = math.radians(self.settings['spread'])
        final_angle = angle + random.uniform(-spread, spread)
        
        Bullet(
            start_pos,
            final_angle,
            self.settings['damage'],
            self.settings['bullet_speed'],
            self.player.groups()[0],
            self.player.bullet_sprites
        )
        
    def shoot_shotgun(self, start_pos, angle):
        for _ in range(self.settings['pellets']):
            spread = math.radians(self.settings['spread'])
            final_angle = angle + random.uniform(-spread, spread)
            
            Bullet(
                start_pos,
                final_angle,
                self.settings['damage'],
                self.settings['bullet_speed'],
                self.player.groups()[0],
                self.player.bullet_sprites
            )
            
    def update(self):
        # Update weapon position to follow player
        pass
