import pygame
from .constants import *
from .player import Player
from .enemy import Enemy
from .background import Background
from .particle import ParticleSystem
from .ui import UI

class Game:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_groups()
        self.setup_level()
        self.background = Background()
        self.particle_system = ParticleSystem()
        self.ui = UI(self.player)
        
        # Load sounds
        self.sounds = {
            'shoot': pygame.mixer.Sound('assets/sounds/sfx/shoot.wav'),
            'hit': pygame.mixer.Sound('assets/sounds/sfx/hit.wav'),
            'jump': pygame.mixer.Sound('assets/sounds/sfx/jump.wav'),
            'pickup': pygame.mixer.Sound('assets/sounds/sfx/pickup.wav')
        }
        
        # Background music
        pygame.mixer.music.load('assets/sounds/music/background.wav')
        pygame.mixer.music.play(-1)
        
    def setup_groups(self):
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        
    def setup_level(self):
        # Create player
        self.player = Player(
            VIRTUAL_WIDTH // 4,
            VIRTUAL_HEIGHT - 100,
            [self.all_sprites],
            self.collision_sprites
        )
        
        # Create ground (temporary)
        ground = pygame.sprite.Sprite(self.collision_sprites)
        ground.image = pygame.Surface((VIRTUAL_WIDTH, 20))
        ground.image.fill((100, 100, 100))
        ground.rect = ground.image.get_rect(bottom=VIRTUAL_HEIGHT)
        ground.hitbox = ground.rect
        
    def handle_events(self, event):
        # Handle any game-specific events here
        pass
        
    def update(self, current_time):
        # Update all game objects
        dt = 1
        self.all_sprites.update(dt, current_time)
        
        # Check for collisions
        self.check_collisions()
        
        self.background.update(self.player.direction.x * self.player.speed)
        self.particle_system.update(dt, current_time)
        
    def check_collisions(self):
        # Player with enemies
        for enemy in self.enemy_sprites:
            if enemy.hitbox.colliderect(self.player.hitbox):
                self.player.take_damage(enemy.damage, pygame.time.get_ticks())
                
        # Bullets with enemies
        for bullet in self.bullet_sprites:
            hits = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False)
            for enemy in hits:
                enemy.take_damage(bullet.damage)
                bullet.kill()
                
    def draw(self):
        # Draw background
        self.background.draw(self.display_surface)
        
        # Draw sprites
        self.all_sprites.draw(self.display_surface)
        
        # Draw particles
        self.particle_system.draw(self.display_surface)
        
        # Draw UI
        self.ui.draw(self.display_surface)
