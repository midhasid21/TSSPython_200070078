import pygame, sys, time, random
from snekset import Settings
from snek import Snek 
from food import food 
import game as gm 

#init font
pygame.font.init()

#init pygame
pygame.init()

#make settings object 
settings = Settings()

#make the frame
game_window = pygame.display.set_mode((settings.framex, settings.framey))
pygame.display.set_caption('Snake Eater')

#make the snake object
snake = Snek(settings, game_window)

#make the snake food object array (a list - what is that?!)
snake_food = [food(settings,game_window)]

#clock to control speed of the game
clk = pygame.time.Clock()


#main loop
while True:
    gm.create_food(settings,game_window,snake_food)
    gm.check_for_events(settings, game_window, snake)
    gm.update_snake(snake, snake_food, settings,game_window)
    gm.update_screen(settings,snake,snake_food,game_window)
    
    # To set the speed of the screen
    clk.tick(25)