#imports the modules needed
import pygame
from pygame.locals import*
from math import sin
import sys


#initiates the pygame modue
pygame.init()


#sets the screen dimensions

screenWidth = 740
screenHeight = 600
screen_size  = screenWidth,screenHeight
game_window = pygame.display.set_mode((screenWidth,screenHeight))
#names the window
pygame.display.set_caption("TEST")

#sets the size of the background
bg_size = bg_width,bg_height = 1500,1500

#makes the background a surface for the game
background = pygame.Surface(bg_size)

#creates the clock (fps)
clock = pygame.time.Clock()
time_passed = 0











#creates the class player
class Player():
    #contructs the class with the given variables. Gives the player object these variables.
    def __init__(self,the_map,x,y):
        self.the_map = the_map
        self.image = pygame.image.load("DoomguyUp.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.armour = 0

    #returns the value of x
    def getX(self):
        return self.rect.x
    #returns the value of y
    def getY(self):
        return self.rect.y

    def get_rect(self):
        return self.rect

    #this procedure is used to detect the keys pressed
    def handle_keys(self, width, height,game_window,enemy):
        #creates the key variabe to detect the key
        key = pygame.key.get_pressed()

        

        #this checks if the
        if key[K_a] and self.rect.x > 0  :
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1:
                self.rect.y += 20
                self.move(0,0)
            else:
                self.move(-1, 0)
            self.image = pygame.image.load("DoomguyLeft.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)
        if key[K_d] and self.rect.x < width -20:
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1:
                self.rect.y -= 20
                self.move(0,0)
            else:
                self.move(1, 0)
            self.image = pygame.image.load("DoomguyRight.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)
        if key[K_w] and self.rect.y > 0:
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1:
                self.rect.x += 20
                self.move(0,0)
            else:
                self.move(0,-1)
            self.image = pygame.image.load("DoomguyUp.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)
        if key[K_s] and self.rect.y < height -20 :
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1:
                self.rect.x -= 20
                self.move(0,0)
            else:
                self.move(0,1)
            self.image = pygame.image.load("DoomguyDown.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)
        


    def move(self, dx, dy):
        movex = int(500 * time_passed * dx)
        movey = int(500 * time_passed * dy)

        if self.rect.right + movex >bg_width or self.rect.x + movex < 0:
            return
        if self.rect.bottom + movey > bg_height or self.rect.y + movey < 0:
            return

        collision_rect = pygame.Rect(self.rect.x + movex, self.rect.y + movey, self.rect.width, self.rect.height)


        if self.move_okay(collision_rect):
            self.rect.x += movex
            self.rect.y += movey

    def move_okay(self, rect):
        for x in range(rect.x, rect.x + rect.width):
            for y in range(rect.y, rect.y + rect.height):
                if self.the_map.image.get_at((x,y)) == (0,0,0):
                    return False
        
        
                    
        return True

    def update(self, screen):
        pass

    def draw(self, game_window):
        game_window.blit(self.image, self.rect)



class Enemy():
        #contructs the class with the given variables. Gives the player object these variables.
    def __init__(self,the_map,x,y):
        self.the_map = the_map
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def draw(self, game_window):
        game_window.blit(self.image, self.rect)
    



class Map():
    def __init__(self):
        self.image = pygame.image.load("testbackground.jpg").convert()
        self.image = pygame.transform.scale(self.image,(1500,1500))

        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0


    def draw(self,background):
        background.blit(self.image, (0,0))


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

camera = Camera(screenWidth,screenHeight)
the_map = Map()
player = Player(the_map, 700, 900)
enemy = Enemy(the_map,700,700)








running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue


    the_map.draw(background)

    player.handle_keys(bg_width, bg_height,game_window,enemy)
    camera.update(player)

    player.draw(background)
    enemy.draw(background)

    print((enemy.get_rect()).colliderect(player.get_rect()))
        


    game_window.blit(background, (0,0), camera.rect)

    player.rect.clamp_ip(background.get_rect())

    pygame.display.update()

    time_passed = clock.tick() / 1000



