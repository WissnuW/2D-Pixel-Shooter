import pygame
from .constants import *

class Background:
    def __init__(self):
        self.layers = []
        self.setup_layers()
        
    def setup_layers(self):
        # Layer 1: Far background (mountains)
        far_bg = {
            'surface': self.create_layer((70, 100, 150)),
            'scroll_speed': 0.1
        }
        
        # Layer 2: Middle background (hills)
        mid_bg = {
            'surface': self.create_layer((60, 80, 120)),
            'scroll_speed': 0.3
        }
        
        # Layer 3: Near background (trees)
        near_bg = {
            'surface': self.create_layer((50, 60, 90)),
            'scroll_speed': 0.5
        }
        
        self.layers = [far_bg, mid_bg, near_bg]
        self.scroll = 0
        
    def create_layer(self, color):
        surface = pygame.Surface((VIRTUAL_WIDTH * 2, VIRTUAL_HEIGHT))
        surface.fill(color)
        # Add some random elements to make it more interesting
        for _ in range(20):
            x = random.randint(0, surface.get_width())
            y = random.randint(0, surface.get_height())
            size = random.randint(10, 30)
            shade = random.randint(-20, 20)
            new_color = tuple(max(0, min(255, c + shade)) for c in color)
            pygame.draw.rect(surface, new_color, (x, y, size, size))
        return surface
        
    def update(self, player_dx):
        self.scroll -= player_dx
        
    def draw(self, surface):
        for layer in self.layers:
            # Calculate position based on scroll and speed
            x = -(self.scroll * layer['scroll_speed']) % VIRTUAL_WIDTH
            surface.blit(layer['surface'], (x, 0))
            surface.blit(layer['surface'], (x + VIRTUAL_WIDTH, 0)) 