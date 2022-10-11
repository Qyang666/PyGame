#import modules 
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

        #Make the aliens move 
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        ## update images on the screen and flip to the new screen
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            
run_game()
