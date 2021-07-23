import pygame
import random

class food():
	def __init__(self,settings,screen):
		self.game_window = screen
		self.rect = pygame.Rect(0, 0, settings.food_width, settings.food_height)
		self.rect.centerx = random.randint(10, settings.framex-10)
		self.rect.centery = random.randint(10, settings.framey-10)
		self.color = settings.food_color 

	def make_food(self):
		pygame.draw.rect(self.game_window, self.color, self.rect)