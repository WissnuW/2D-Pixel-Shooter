import pygame
import math
import random
from .constants import *
from .bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_type, player, *groups):
        super().__init__(*groups)
        
        # Enemy type and properties
        self.enemy_type = enemy_type
        self.settings = ENEMY_TYPES[enemy_type]
        
        # Setup sprite
        self.animations = self.load_animations()
        self.frame_index = 0
        self.animation_speed = 0.15
        
        self.image = self.animations['idle'][0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -10)
        
        # Movement
        self.pos = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = self.settings['speed']
        
        # Combat
        self.health = self.settings['health']
        self.damage = self.settings['damage']
        self.player = player
        
        # AI state
        self.state = 'idle'
        self.detection_radius = 150
        self.attack_radius = 50
        
        # Shooting (for shooter type)
        if enemy_type == 'shooter':
            self.last_shot_time = 0
            self.can_shoot = True
            
    def load_animations(self):
        animations = {
            'idle': [],
            'move': [],
            'attack': []
        }
        
        # Temporary animation (replace with actual sprites)
        temp_surf = pygame.Surface((32, 32))
        if self.enemy_type == 'walker':
            temp_surf.fill((255, 0, 0))  # Red
        elif self.enemy_type == 'shooter':
            temp_surf.fill((255, 100, 0))  # Orange
        else:  # boss
            temp_surf.fill((150, 0, 0))  # Dark red
            
        animations['idle'].append(temp_surf)
        animations['move'].append(temp_surf)
        animations['attack'].append(temp_surf)
        
        return animations
        
    def get_player_distance_direction(self):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(self.player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
            
        return (distance, direction)
        
    def get_state(self):
        distance = self.get_player_distance_direction()[0]
        
        if distance <= self.attack_radius:
            self.state = 'attack'
        elif distance <= self.detection_radius:
            self.state = 'move'
        else:
            self.state = 'idle'
            
    def actions(self, dt):
        if self.state == 'attack':
            if self.enemy_type == 'shooter':
                self.shoot()
            else:
                # Melee enemies continue moving in attack state
                self.direction = self.get_player_distance_direction()[1]
                
        elif self.state == 'move':
            self.direction = self.get_player_distance_direction()[1]
            
        else:  # idle
            self.direction = pygame.math.Vector2()
            
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.settings['fire_rate']:
            self.last_shot_time = current_time
            
            # Get direction to player
            _, direction = self.get_player_distance_direction()
            angle = math.atan2(direction.y, direction.x)
            
            # Create bullet
            Bullet(
                self.rect.center,
                angle,
                self.damage,
                5,  # bullet speed
                self.groups()[0]  # add to same group as enemy
            )
            
    def move(self, dt):
        # Update position
        self.pos += self.direction * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.hitbox.centery = round(self.pos.y)
        self.rect.center = self.hitbox.center
        
    def animate(self, dt):
        current_animation = self.animations[self.state]
        
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(current_animation):
            self.frame_index = 0
            
        self.image = current_animation[int(self.frame_index)]
        
        # Flip sprite based on movement direction
        if self.direction.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
            
    def die(self):
        # Add death animation or particles here
        self.kill()
        
    def update(self, dt, current_time):
        self.get_state()
        self.actions(dt)
        self.move(dt)
        self.animate(dt)
