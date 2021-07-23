import sys, pygame
from snekset import Settings 
from food import food
pygame.font.init()

#checking for keyboard events 
def check_for_events(settings, screen, snake):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        if settings.direction != 'UP':
          settings.change_to = 'DOWN'
      elif event.key == pygame.K_UP:
        if settings.direction != 'DOWN':
          settings.change_to = 'UP'  
      elif event.key == pygame.K_RIGHT:
        if settings.direction != 'LEFT':
          settings.change_to = 'RIGHT'
      elif event.key == pygame.K_LEFT:
        if settings.direction != 'RIGHT':
          settings.change_to = 'LEFT'

#updating the snake
def update_snake(snake, food, settings, game_window):
  #caution - don't go out of frame!
  if(snake.rect[0].right >= settings.framex):
    game_over(settings,game_window)

  if(snake.rect[0].left <= 0):
    game_over(settings,game_window)

  if(snake.rect[0].top <= 0):
    game_over(settings,game_window)

  if(snake.rect[0].bottom >= settings.framey):
    game_over(settings,game_window)

  #eating
  if(abs((food[len(food)-1].rect.centery - snake.rect[0].centery)) < 10 and abs((food[len(food)-1].rect.centerx - snake.rect[0].centerx)) < 10):
    snake.grow(settings)
    settings.food_spawn = False
    settings.score = len(food)


  #for movememt 
  if(settings.change_to == settings.direction):
    if(settings.direction == 'RIGHT'):
        snake.moveright()
    elif(settings.direction == 'LEFT'):
        snake.moveleft()
    elif(settings.direction == 'UP'):
        snake.moveup()
    elif(settings.direction == 'DOWN'):
        snake.movedown()    
  #change direction
  else:
    if settings.change_to == 'RIGHT':
    	if settings.direction != 'LEFT':
    	 snake.turnright()
    	 settings.direction = settings.change_to

    elif settings.change_to == 'LEFT':
      if settings.direction != 'RIGHT':
    	  snake.turnleft()
    	  settings.direction = settings.change_to

    elif settings.change_to == 'UP':
      if settings.direction != 'DOWN':
    	  snake.turnup()
    	  settings.direction = settings.change_to

    elif settings.change_to == 'DOWN':
      if settings.direction != 'UP':
    	  snake.turndown()
    	  settings.direction = settings.change_to


def create_food(settings,game_window,snake_food):
  if(settings.food_spawn == False):
    snake_food.append(food(settings,game_window))
    settings.food_spawn = True 


def game_over(settings,game_window):

  font = pygame.font.Font('freesansbold.ttf', 50)
  font2 = pygame.font.Font('freesansbold.ttf', 25)
  text = font.render('Game Over', True, (82, 255, 51))
  sc = str(settings.score)
  sc = 'The score is ' + sc 
  scoretext = font2.render(sc, True, (168, 255, 153))
  text_rect = text.get_rect()
  scoretext_rect = scoretext.get_rect()
  text_x = game_window.get_width() / 2 - text_rect.width / 2
  text_y = game_window.get_height() / 2 - text_rect.height / 2
  scoretext_x = game_window.get_width() / 2 - scoretext_rect.width / 2
  scoretext_y = game_window.get_height() / 2 - scoretext_rect.height / 2 - 40
  game_window.blit(text,[text_x,text_y])
  game_window.blit(scoretext,[scoretext_x,scoretext_y])
  pygame.display.flip()
  pygame.time.delay(3000)
  sys.exit()


def update_screen(settings,snake,snake_food,game_window):
  game_window.fill((0,0,0))
  snake.makesnek(settings)
  snake_food[len(snake_food)-1].make_food()
  show_score(settings,game_window)
  pygame.display.flip()


def show_score(settings,game_window):
  font = pygame.font.Font('freesansbold.ttf', 20)
  sc = str(settings.score)
  sc = 'The score is ' + sc 
  scoretext = font.render(sc,True,(75, 142, 250))
  x = 20
  y = 10
  game_window.blit(scoretext,[x,y])





