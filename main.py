import pygame 
from pygame.locals import *
from math import sin


pygame.init()

screenWidth = 400
screenHeight = 400
screen_size  = screenWidth,screenHeight
game_window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("TEST")

bg_size = bg_width,bg_height = 800,800

background = pygame.Surface(bg_size)
wall = pygame.Surface(bg_size)



clock = pygame.time.Clock()
time_passed = 0

class Player():
  def __init__(self,x,y):
    self.Image = pygame.image.load("myAvatar.png").convert()
    self.Image = pygame.transform.scale(self.Image,(20,20))
    self.rect = self.Image.get_rect()
    self.rect.x = 200
    self.rect.y = 200
  
  def getX(self):
    return self.rect.x

  def getY(self):
    return self.rect.y

  def handle_keys(self, width, height):
      key = pygame.key.get_pressed()
      dist = 2 

      if key[K_LEFT] and self.rect.x > 0: 
            self.rect.x -= 500 * time_passed
      
      if key[K_RIGHT] and self.rect.x < width -20:
            self.rect.x += 500 * time_passed
         
      if key[K_UP] and self.rect.y > 0:
        self.rect.y -= 500 * time_passed
      
      if key[K_DOWN] and self.rect.y < height -20:
        self.rect.y += 500 * time_passed

  def update(self, screen):
    pass

  def draw(self, game_window):
    game_window.blit(self.Image, (int(self.rect.x), int(self.rect.y)))
   





class Map():
  def __init__(self):
    self.Image = pygame.image.load("testbackground.jpg").convert()
    self.Image = pygame.transform.scale(self.Image,(800,800))

    self.rect = self.Image.get_rect()
    self.x = 0
    self.y = 0

  def draw(self,background):
    background.blit(self.Image, (0,0))

class Walls():
  def __init__(self):
    self.Image = pygame.image.load("Walls.png").convert()
    self.Image = pygame.transform.scale(self.Image,(800,800))

    self.rect = self.Image.get_rect()
    self.x = 0
    self.y = 0

  def draw(self,wall):
    wall.blit(self.Image, (0,0))




class Camera(object):
	def __init__(self, width, height):
		self.rect = pygame.Rect(0,0, width, height)
		self.width = width
		self.height = height
		
	def update(self, target):
		x = target.rect.x - int(screenWidth/2)
		y = target.rect.y - int(screenHeight/2)

		x = max(0, x) 
		y = max(0, y)
	
		x = min((bg_width-screenWidth), x)
		y = min((bg_height-screenHeight), y)
		
		self.rect = pygame.Rect(x, y, self.width, self.height)



		















player = Player(200,200)
camera = Camera(screenWidth,screenHeight)
map = Map()
walls = Walls()

leave = False
while not leave:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() 
      running = False
      continue
  
  player.handle_keys(bg_width, bg_height)

  map.draw(background)

  walls.draw(wall)

  player.update(background)
  player.draw(background)

  camera.update(player)


  game_window.blit(background, (0,0), camera.rect)

  player.rect.clamp_ip(background.get_rect())

  pygame.display.update()
  pygame.display.flip()

  time_passed = clock.tick() / 1000

  
pygame.quit()
quit()
