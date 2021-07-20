#imports the modules needed
import pygame
import os
from pygame.locals import*
import math
import sys


#initiates the pygame modue
pygame.init()



#sets the screen dimensions

screenWidth = 740
screenHeight = 600
screen_size  = screenWidth,screenHeight
#os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
#, pygame.NOFRAME
game_window = pygame.display.set_mode((screenWidth,screenHeight))
#names the window
pygame.display.set_caption("TEST")

#sets the size of the background
bg_size = bg_width,bg_height = 2000,2000

#makes the background a surface for the game
background = pygame.Surface(bg_size)

#creates the clock (fps)
clock = pygame.time.Clock()
Otherclock = pygame.time.Clock()
time_passed = 0




black   = (0,0,0)
bRed = (136,8,8)
white  = (255,255,255)
label = (130, 132, 135)
error = (209, 13, 13)



titleFont  = "AmazDooMLeft.ttf"
titleFont=pygame.font.Font(titleFont,70)

bFont  = "Retro.ttf"
bFont=pygame.font.Font(bFont,40)









def formatText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj,textrect)
     




def death():
    running = False
    click = False
    while not running:
            
                
                
        mx, my = pygame.mouse.get_pos()


        pauseBack = pygame.image.load("pauseBackground.png").convert_alpha()
        pauseBack= pygame.transform.scale(pauseBack,(740,600))
        pauseBack.set_alpha(50)
        formatText('You are DEAD!', bFont, bRed, game_window,screenWidth/2-100 , 140)

        pygame.display.update()
        clock.tick(60)





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
        


    def updateHealth(self,game_window):
        #formatText(str(self.health), bFont, bRed, game_window,50 , 50)
        if self.health > 100:
            self.health = 100
        if self.armour > 100:
            self.armour = 100
        if self.armour < 0:
            self.armour = 0
        
        if self.health == 0:
            death()
        

    def getHealth(self):
        return self.health

    def getArmour(self):
        return self.armour
        
        
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
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1 and enemy.get_death() == False:
                if self.armour > 0:
                    self.armour -= 2
                else:
                    self.health -= 1
                self.move(2,0)

            else:
                if key[K_LSHIFT]:
                    self.move(-2,0)
                else:
                    self.move(-1, 0)
            self.image = pygame.image.load("DoomguyLeft.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)



        if key[K_d] and self.rect.x < width -20:
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1 and enemy.get_death() == False:
                if self.armour > 0:
                    self.armour -= 2
                else:
                    self.health -= 1
                self.move(-2,0)
            else:
                self.move(1, 0)
            self.image = pygame.image.load("DoomguyRight.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)


        if key[K_w] and self.rect.y > 0:
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1 and enemy.get_death() == False:
                if self.armour > 0:
                    self.armour -= 2
                else:
                    self.health -= 1
                self.move(0,2)
            else:
                self.move(0,-1)
            self.image = pygame.image.load("DoomguyUp.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)


        if key[K_s] and self.rect.y < height -20 :
            if (enemy.get_rect()).colliderect(player.get_rect()) == 1 and enemy.get_death() == False:
                if self.armour > 0:
                    self.armour -= 2
                else:
                    self.health -= 1
                self.move(0,-2)
            else:
                self.move(0,1)
            self.image = pygame.image.load("DoomguyDown.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))
            game_window.blit(self.image, self.rect)
        


    def move(self, dx, dy):
        #sets the moxe x and y values
        movex = int(500 * time_passed * dx)
        movey = int(500 * time_passed * dy)

        #This is checking if the move values are greater or less than the size of the game window. Stopping the player from being able to move off the screen.
        if self.rect.right + movex >bg_width or self.rect.x + movex < 0:
            return
        if self.rect.bottom + movey > bg_height or self.rect.y + movey < 0:
            return

        #This is now creation a collision check. By adding the new x an y coordiantes of the player and the with and height of the player.
        collision_rect = pygame.Rect(self.rect.x + movex, self.rect.y + movey, self.rect.width, self.rect.height)

        #this now calls the function move okay to check if it should move the player.
        if self.move_okay(collision_rect):
            #Changes the players x and y coordinates allowing them to move. 
            self.rect.x += movex
            self.rect.y += movey

    def move_okay(self, rect):
        #This is now using the collision rect values. 
        #This is now looping through the x and y coordinats around the player. 
        for x in range(rect.x, rect.x + rect.width):
            for y in range(rect.y, rect.y + rect.height):
                #checks if at those x and y coordinates on the map have the colour black.
                if self.the_map.image.get_at((x,y)) == (0,0,0):
                    #if so it returns false stopping the player from moving.
                    return False
        
        
        #if not it'll return true and then allow the player ot move to it's new position.        
        return True

    def update(self, screen):
        pass

    def draw(self, game_window):
        #formatText(str(self.health), bFont, bRed, game_window,700 , 900)
        game_window.blit(self.image, self.rect)


class Pointer():
    def __init__ (self,x,y):
        self.image = pygame.image.load("crosshair.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect

    def get_x (self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image


    def draw(self,game_window):
        self.rect.center = pygame.mouse.get_pos()
        #game_window.blit(self.image,self.rect)
        
        
    def collision(self,enemy,camera):
        click = False
        enemy_collision_rect  = camera.update_rect(enemy)
        if enemy_collision_rect.colliderect(self.rect) and enemy.get_death() == False:
            self.image = pygame.image.load("crosshairActive.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(40,40))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            if click:
                enemy.hit()
                enemy_health = enemy.get_health()
                print(enemy_health)
                
            
        else:
            self.image = pygame.image.load("crosshair.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(40,40))
        
   
class Bullet:
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((10, 4)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 2

    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)  







class Enemy():
        #contructs the class with the given variables. Gives the player object these variables.
    def __init__(self,the_map,x,y):
        self.the_map = the_map
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.death = False

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y
    
    def get_health(self):
        return self.health

    def get_death(self):
        return self.death

    def hit(self):
        self.health -=10


    def draw(self, game_window):
        
        game_window.blit(self.image, self.rect)

    def enemyAlive(self):
        if self.health <= 0:
            self.death = True
            self.image = pygame.image.load("EnemyDead.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(80,80))

    


class PickUp():
    def __init__(self,type,x,y):
        self.type = type.lower()
        self.taken = False
        self.image = pygame.image.load("empty.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    
    def get_rect(self):
        return self.rect


    def draw(self,game_window):
        if self.taken == True:
            self.image = pygame.image.load("empty.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(30,30))
        else:
            if self.type == "armour":
                self.image = pygame.image.load("armour.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(30,30))


        game_window.blit(self.image,self.rect)


    def pick(self,player):
     
        if (player.get_rect()).colliderect(self.get_rect()) == 1 and self.taken == False:
            player.armour += 5
            self.taken = True
            















#makes the class map
class Map():
    #constructs the object
    def __init__(self):
        #loads the image used for the back
        self.image = pygame.image.load("testbackground.jpg").convert()
        #resizes the image
        self.image = pygame.transform.scale(self.image,(2000,2000))

        #Gets the rect values for the image
        self.rect = self.image.get_rect()
        #sets the x and y position on the game window
        self.x = 0
        self.y = 0

    #blits the background image on to the screen in the position 0,0
    def draw(self,background):
        background.blit(self.image, (0,0))


#makes the camera class
class Camera(object):
    #constructs the camera objeect
    def __init__(self, width, height):
        #Sets the rect value of the camera.(position)
        self.rect = pygame.Rect(0,0, width, height)
        #sets the width and height of the camera the same as the game window
        self.width = width
        self.height = height
    
    #This updates the camera object
    def update(self, target):
        #it sets the position of the camera to the players x and y values subtracting half the width and height of the game window. 
        x = target.rect.x - int(screenWidth/2)
        y = target.rect.y - int(screenHeight/2)

        #this sets the max position the camera can go to stop it going off the screen. 
        x = max(0, x)
        y = max(0, y)
        #This is the same as the max values. So the camera can never leave the map. 
        x = min((bg_width-screenWidth), x)
        y = min((bg_height-screenHeight), y)

        #Sets the new rect position of the camera. 
        self.rect = pygame.Rect(x, y, self.width, self.height)


    def update_rect(self, target):
	    x = target.rect.x - self.rect.x
	    y = target.rect.y - self.rect.y
	    updated_rect = pygame.Rect(x, y, target.rect.width, target.rect.height)
	    return updated_rect

camera = Camera(screenWidth,screenHeight)
the_map = Map()
player = Player(the_map, 700, 900)
enemy = [(Enemy(the_map,1298,1472)),(Enemy(the_map,800,800))]
pointer = Pointer(0,0)
pickup = [(PickUp("armour",700,800)),(PickUp("armour",1692,1463))]


bullets = []
pos = (250, 250)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == MOUSEBUTTONDOWN:
        
            bullets.append(Bullet(*pos))


    the_map.draw(background)

    for bullet in bullets[:]:
        bullet.update()
        if not game_window.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)

  
        
    mx, my = pygame.mouse.get_pos()

 
    

    for p in pickup:
        p.pick(player)
    player.updateHealth(game_window)
    for e in enemy:
        player.handle_keys(bg_width, bg_height,game_window,e)
    camera.update(player)

    for p in pickup:
        p.draw(background)
    

    player.draw(background)
    for bullet in bullets:
        print(bullets)
        bullet.draw(game_window)

   


    for e in enemy:
        e.enemyAlive()


    for e in enemy:
        e.draw(background)

   


  

    pointer.draw(background)
    for e in enemy:
        pointer.collision(e,camera)
    

    
    
    game_window.blit(background, (0,0), camera.rect)

    player.rect.clamp_ip(background.get_rect())

    game_window.blit(pointer.get_image(),pointer.get_rect())
   
    formatText(("Health: "+ str(player.getHealth())), bFont, bRed, game_window,50 , 50)
    
    formatText(("Armour: "+ str(player.getArmour())), bFont, bRed, game_window,50 , 100)

    pygame.display.update()
      

    time_passed = clock.tick() / 1000



