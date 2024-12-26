import pygame
import sys
import os
from scripts.player import Player
from scripts.constants import *
from scripts.create_player_sprite import create_player_sprite

class PlayerTest:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Player Test")
        self.clock = pygame.time.Clock()
        
        # Buat sprite sheet jika belum ada
        if not os.path.exists('assets/images/player/player_sheet.png'):
            create_player_sprite()
        
        # Setup test environment
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        # Buat ground
        self.create_ground()
        
        # Buat player
        self.player = Player(
            SCREEN_WIDTH // 4,
            SCREEN_HEIGHT - 150,
            [self.all_sprites],
            self.collision_sprites
        )
        
    def create_ground(self):
        ground = pygame.sprite.Sprite(self.collision_sprites)
        ground.image = pygame.Surface((SCREEN_WIDTH, 40))
        ground.image.fill((100, 100, 100))
        ground.rect = ground.image.get_rect(bottom=SCREEN_HEIGHT)
        ground.hitbox = ground.rect
        
    def run(self):
        while True:
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Update
            self.all_sprites.update(1, current_time)
            
            # Draw
            self.screen.fill((50, 50, 50))  # Dark gray background
            
            # Draw sprites
            self.collision_sprites.draw(self.screen)
            self.all_sprites.draw(self.screen)
            
            # Draw debug info
            self.draw_debug_info()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
    def draw_debug_info(self):
        font = pygame.font.Font(None, 24)
        debug_info = [
            f"Position: {self.player.rect.center}",
            f"Velocity Y: {self.player.direction.y:.2f}",
            f"On Ground: {self.player.on_ground}",
            f"State: {self.player.state if hasattr(self.player, 'state') else 'N/A'}"
        ]
        
        for i, text in enumerate(debug_info):
            surf = font.render(text, True, (255, 255, 255))
            self.screen.blit(surf, (10, 10 + i * 25))

if __name__ == "__main__":
    test = PlayerTest()
    test.run() 