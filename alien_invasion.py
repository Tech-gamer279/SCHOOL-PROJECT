import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    # Create the game window
    self.screen = pygame.display.set_mode((
        self.settings.screen_width,
        self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    self.ship = Ship(self)

def check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

def run_game(self):
    """Starts the loop for the game."""
    while True:
        self.check_events()
        self.ship.update()  # Add this line to update ship position
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        self.clock.tick(60)