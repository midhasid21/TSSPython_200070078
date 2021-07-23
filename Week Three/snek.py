import pygame, sys

class Snek():

    def __init__(self, settings, game_window):
        self.game_window = game_window
        self.settings = settings
        self.rect = []
        for i in range(3):
            self.rect.append(pygame.Rect(100 -10*i,50,settings.snake_block_x,settings.snake_block_y))
        self.color = (0,200,0)

    def makesnek(self,settings):

            for i in range(len(list(self.rect))):
                pygame.draw.rect(self.game_window, self.color, self.rect[i])

    def grow(self, settings):
    	k = len(list(self.rect))
    	x = self.rect[k-1].centerx
    	y = self.rect[k-1].centery
    	if settings.direction == 'RIGHT':
    		self.rect.append(pygame.Rect(x-5 ,y-5,10, 10))
    	if settings.direction == 'LEFT':
    		self.rect.append(pygame.Rect(x+5 ,y-5,10, 10))
    	if settings.direction == 'UP':
    		self.rect.append(pygame.Rect(x - 5 ,y + 5 ,10, 10))
    	if settings.direction == 'DOWN':
    		self.rect.append(pygame.Rect(x,y - 5,10, 10))
    
    def moveright(self):
    	for i in range(len(list(self.rect))):
    		#pygame.time.delay(100)
    		self.rect[i].x += 10

    def moveleft(self):
    	for i in range(len(list(self.rect))):
    		#pygame.time.delay(100)
    		self.rect[i].x -= 10

    def moveup(self):
    	for i in range(len(list(self.rect))):
    		#pygame.time.delay(100)
    		self.rect[i].y -= 10

    def movedown(self):
    	for i in range(len(list(self.rect))):
    		#pygame.time.delay(100)
    		self.rect[i].y += 10

    def turnright(self):
        x = self.rect[0].centerx
        y = self.rect[0].centery
        l = len(list(self.rect))
        for i in range(l):
            self.rect[i].centery = y
            self.rect[i].centerx = x + (l - i - 1)*10

    def turnleft(self):
        x = self.rect[0].centerx
        y = self.rect[0].centery
        l = len(list(self.rect))
        for i in range(l):
            self.rect[i].centery = y
            self.rect[i].centerx = x - (l - i - 1)*10

    def turnup(self):
        x = self.rect[0].centerx
        y = self.rect[0].centery
        l = len(list(self.rect))
        for i in range(l):
            self.rect[i].centerx = x
            self.rect[i].centery = y - (l - i - 1)*10

    def turndown(self):
        x = self.rect[0].centerx
        y = self.rect[0].centery
        l = len(list(self.rect))
        for i in range(l):
            self.rect[i].centerx = x
            self.rect[i].centery = y + (l - i - 1)*10

        