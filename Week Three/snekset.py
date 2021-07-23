import pygame  

class Settings():
	def __init__(self):
		self.framex = 720
		self.framey = 480

		self.direction = 'RIGHT'
		self.change_to = self.direction

		self.score = 0 

		self.food_pos = [0,0]
		self.food_spawn = True

		self.snake_block_x = 10
		self.snake_block_y = 10
		self.snake_pos = [100, 50]
		self.snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

		self.food_width = 10
		self.food_height = 10
		self.food_color = (100,0,0)

		self.game_over = False 

		self.score_pos = [500,500]
		self.score_color = (100,0,0)
		self.score_font = pygame.font.SysFont('Comic Sans MS',10)