class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600  # Smaller width
        self.screen_height = 400  # Smaller height
        self.bg_color = (230, 230, 230)

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        # Ship settings
        self.ship_speed = 1.5