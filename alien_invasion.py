#import modules 
import pygame
from settings import Settings
from pygame.sprite import Group
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button

#start a game
def run_game():
    # Initialize game and 
    pygame.init()
    # create screen 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # add screen caption
    pygame.display.set_caption("Alien Invasion")
    #add a button
    play_button = Button(ai_settings, screen, "Play")

    ## Create an instance to store game statistics.
    stats = GameStats(ai_settings)
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
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            
        #Make the aliens move 
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        ## update images on the screen and flip to the new screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
