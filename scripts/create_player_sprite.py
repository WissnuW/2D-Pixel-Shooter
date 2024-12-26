import pygame
import math
import os
from scripts.constants import *  # Ubah dari 'constants' menjadi 'scripts.constants'

def create_player_sprite():
    # Pastikan folder exists
    os.makedirs('assets/images/player', exist_ok=True)
    
    # Create sprite sheet surface
    sheet_width = SPRITE_WIDTH * 6  # Maximum frames needed
    sheet_height = SPRITE_HEIGHT * 4  # Number of animations
    sheet = pygame.Surface((sheet_width, sheet_height), pygame.SRCALPHA)
    
    # Colors
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (100, 100, 255)
    
    # Draw idle animation (row 0)
    for i in range(4):
        surf = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT), pygame.SRCALPHA)
        # Body
        pygame.draw.rect(surf, BLUE, (8, 8, 16, 20))
        # Head
        pygame.draw.circle(surf, LIGHT_BLUE, (16, 8), 6)
        # Slight bobbing animation
        y_offset = [0, -1, 0, 1][i]
        sheet.blit(surf, (i * SPRITE_WIDTH, 0 + y_offset))
    
    # Draw run animation (row 1)
    for i in range(6):
        surf = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT), pygame.SRCALPHA)
        # Body
        pygame.draw.rect(surf, BLUE, (8, 8, 16, 20))
        # Head
        pygame.draw.circle(surf, LIGHT_BLUE, (16, 8), 6)
        # Legs animation
        leg_offset = math.sin(i * math.pi/3) * 4
        pygame.draw.rect(surf, BLUE, (12, 28, 4, 4 + leg_offset))
        pygame.draw.rect(surf, BLUE, (20, 28, 4, 4 - leg_offset))
        sheet.blit(surf, (i * SPRITE_WIDTH, SPRITE_HEIGHT))
    
    # Save the sprite sheet
    pygame.image.save(sheet, 'assets/images/player/player_sheet.png')
    print("Player sprite sheet created successfully!")

if __name__ == "__main__":
    pygame.init()
    create_player_sprite()
    pygame.quit() 