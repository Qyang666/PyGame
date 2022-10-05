import pygame

class Ship():

    ## initialize the ship and set its starting position
    def __init__(self,ai_settings,screen):
        self.screen= screen
        # initialize the ship and set its starting position 
        self.ai_settings = ai_settings
        self.image=pygame.image.load('ship.bmp')
        #Start each new ship at the bottom center of the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #ect taks only integer so have to do some adjustments
        #to store the ship's position accurately, we need a new attribute center
        self.center=float(self.rect.centerx)
         # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Continuous movement flag 
        self.moving_right = False
        self.moving_left= False


    def update(self):
        """Update the ship's position based on the movement flag.""" 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 

    def center_ship(self):
           """Center the ship on the screen."""
           self.center = self.screen_rect.centerx