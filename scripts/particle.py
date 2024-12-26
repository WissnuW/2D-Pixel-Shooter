import pygame
import random
import math

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, color, velocity, lifetime, size, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        
        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(velocity)
        self.lifetime = lifetime
        self.spawn_time = pygame.time.get_ticks()
        self.alpha = 255
        
    def update(self, dt, current_time):
        # Move particle
        self.velocity.y += 0.1 * dt  # Gravity
        self.pos += self.velocity * dt
        self.rect.center = self.pos
        
        # Fade out
        age = current_time - self.spawn_time
        self.alpha = 255 * (1 - age / self.lifetime)
        self.image.set_alpha(self.alpha)
        
        if age > self.lifetime:
            self.kill()

class ParticleSystem:
    def __init__(self):
        self.particles = pygame.sprite.Group()
        
    def create_particles(self, pos, color, count=5):
        for _ in range(count):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(1, 3)
            velocity = (math.cos(angle) * speed, math.sin(angle) * speed)
            lifetime = random.randint(300, 500)
            size = random.randint(2, 4)
            
            Particle(pos, color, velocity, lifetime, size, self.particles)
            
    def update(self, dt, current_time):
        self.particles.update(dt, current_time)
        
    def draw(self, surface):
        self.particles.draw(surface) 