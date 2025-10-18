import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

        # Keep ship within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)