import pygame
from .constants import *

class UI:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font(None, 20)
        
    def draw_health_bar(self, surface):
        # Health bar background
        pygame.draw.rect(surface, (60, 60, 60), 
                        (10, 10, 100, 10))
        
        # Health bar
        health_width = (self.player.health / self.player.max_health) * 100
        pygame.draw.rect(surface, (220, 40, 40), 
                        (10, 10, health_width, 10))
        
    def draw_weapon_info(self, surface):
        weapon_text = f"Weapon: {self.player.current_weapon.type}"
        text_surf = self.font.render(weapon_text, True, WHITE)
        surface.blit(text_surf, (10, 25))
        
    def draw(self, surface):
        self.draw_health_bar(surface)
        self.draw_weapon_info(surface) 