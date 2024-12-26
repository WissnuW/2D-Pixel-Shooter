import pygame
from .constants import *

class Pickup(pygame.sprite.Sprite):
    def __init__(self, pos, pickup_type, *groups):
        super().__init__(*groups)
        self.pickup_type = pickup_type
        
        # Setup sprite
        self.image = pygame.Surface((16, 16))
        if pickup_type == 'health':
            self.image.fill((0, 255, 0))  # Green for health
        elif pickup_type == 'ammo':
            self.image.fill((255, 255, 0))  # Yellow for ammo
        
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-4, -4)
        
        # Floating animation
        self.y_offset = 0
        self.float_speed = 0.05
        self.original_y = pos[1]
        
    def update(self, dt, current_time):
        # Floating animation
        self.y_offset = math.sin(current_time * self.float_speed) * 5
        self.rect.y = self.original_y + self.y_offset 