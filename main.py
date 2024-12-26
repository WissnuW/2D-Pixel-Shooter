import pygame
import sys
import os
from scripts.game import Game
from scripts.constants import *

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        # Setup display dengan resolusi pixel art yang bagus
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
        pygame.display.set_caption("Pixel Shooter")
        
        # Setup scaling untuk pixel art yang lebih tajam
        self.display = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        
        self.clock = pygame.time.Clock()
        self.game = Game(self.display)
        
    def run(self):
        while True:
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.game.handle_events(event)
            
            # Update
            self.game.update(current_time)
            
            # Draw
            self.display.fill(BACKGROUND_COLOR)
            self.game.draw()
            
            # Scale the display to the screen
            scaled_surf = pygame.transform.scale(self.display, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(scaled_surf, (0, 0))
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = GameManager()
    game.run()
