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
        self.screen_width = 800
        self.screen_height = 600
        self.ship = Ship(self)
        
    def run_game(self):
        """Starts the loop for the game."""
        while True:
            self.check_events()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.rect.x += 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Stop moving the ship to the right
                    self.ship.moving_right = False

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()