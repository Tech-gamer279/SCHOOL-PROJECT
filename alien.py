import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Repesents a single alien in the fleet."""

    def _init_(self, ai_game):
        """Initialize the aliens"""
        super()._init_()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)