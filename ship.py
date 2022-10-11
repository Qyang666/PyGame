import pygame
from pygame.sprite import Sprite

#create ship class
class Ship(Sprite):

    ## initialize the ship and set its starting position
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen= screen

        # initialize the ship and set its starting position 
        self.ai_settings = ai_settings

        #load the ship image and get its rect
        self.image=pygame.image.load('ship.bmp')

        # rect is to treat the ship as rectangular 
        self.rect = self.image.get_rect()

        #get the screen rectangular 
        self.screen_rect = screen.get_rect()

        #make sure that the ship's center x = the screen's center x
        self.rect.centerx = self.screen_rect.centerx

        #make sure the ship's bottom y = the screen's bottom y 
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center 
        self.center=float(self.rect.centerx)

        self.moving_right = False
        self.moving_left= False


    def update(self):
        """Update the ship's position based on the movement flag.""" 
        # if press right button while the ship is not on the edge of the right screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        # if press left while the ship is not on the edge of the left screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #make sure that the ship's center moves along with user's commands
        self.rect.centerx = self.center
    


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 

    def center_ship(self):
           """Center the ship on the screen."""
           self.center = self.screen_rect.centerx
    

        