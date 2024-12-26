import pygame
import math
from .constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, damage, speed, *groups):
        super().__init__(*groups)
        
        # Bullet appearance
        self.image = pygame.Surface((4, 4))
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect(center=pos)
        
        # Movement
        self.speed = speed
        self.direction = pygame.math.Vector2(
            math.cos(angle) * self.speed,
            math.sin(angle) * self.speed
        )
        self.pos = pygame.math.Vector2(pos)
        
        # Properties
        self.damage = damage
        self.lifetime = 1000  # milliseconds
        self.spawn_time = pygame.time.get_ticks()
        
    def update(self, dt, current_time):
        # Move bullet
        self.pos += self.direction * dt
        self.rect.center = self.pos
        
        # Check lifetime
        if current_time - self.spawn_time > self.lifetime:
            self.kill()
            
        # Check if bullet is off screen
        if not (-50 <= self.rect.x <= VIRTUAL_WIDTH + 50 and
                -50 <= self.rect.y <= VIRTUAL_HEIGHT + 50):
            self.kill()
