import pygame

class SpriteSheet:
    def __init__(self, image_path):
        self.sheet = pygame.image.load(image_path).convert_alpha()
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite
        
    def get_sprite_strip(self, x, y, width, height, frames):
        sprites = []
        for i in range(frames):
            sprites.append(self.get_sprite(x + (width * i), y, width, height))
        return sprites 