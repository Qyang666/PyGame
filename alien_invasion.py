import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship
    ship = Ship(ai_settings, screen)
    #Make a group pf bullets
    bullets= Group()
    #make a group of aliens
    aliens= Group()
    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        #Make the aliens move 
        gf.update_aliens(ai_settings, aliens)
        ## update images on the screen and flip to the new screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
