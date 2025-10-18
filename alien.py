# ...existing code...
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        """Initialize an alien and set its starting position."""
        super().__init__()  # <-- do NOT pass ai_game here

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Try to load an image, fall back to a simple surface if it fails
        try:
            self.image = pygame.image.load('images/alien.bmp').convert_alpha()
        except Exception:
            self.image = pygame.Surface((40, 30))
            self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        # Start each new alien near the top-left (adjust as needed)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
# ...existing code...