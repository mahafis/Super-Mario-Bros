import os
import random

PATH = os.getcwd()
RESOLUTION_W = 1280
RESOLUTION_H = 720
GROUND = 585

class Creature:
    
    def __init__(self, x, y, r, img, slice_w, slice_h, num_slices):
        self.x = x
        self.y = y
        self.r = r
        self.g = GROUND
        self.vx = 0
        self.vy = 1
        self.img = loadImage(PATH + "/images/" + img)
        self.slice_w = slice_w
        self.slice_h = slice_h
        self.num_slices = num_slices
        self.slice = 0
        self.dir = RIGHT
    
    def gravity(self):
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            if self.y + self.r + self.vy > self.g:
                self.y = self.g - self.r
                self.vy = 0
    
    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy
    
    def display(self):
        self.update()
        # fill(255,0,0)
        # circle(self.x, self.y, self.r * 2)
        if self.dir == RIGHT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2, self.slice_w, self.slice_h, self.slice * self.slice_w, 0, (self.slice + 1) * self.slice_w, self.slice_h )
        elif self.dir == LEFT:
            image(self.img, self.x - self.slice_w//2, self.y - self.slice_h//2, self.slice_w, self.slice_h, (self.slice + 1) * self.slice_w, 0, self.slice * self.slice_w, self.slice_h )
                        
class Mario(Creature):
    
    def __init__(self, x, y, r):
        Creature.__init__(self, x, y, r, "mario.png", 100, 70, 11)
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}

    def update(self):
        self.gravity()
    
        if self.key_handler[LEFT] == True:
            self.vx = -7
            self.dir = LEFT
        elif self.key_handler[RIGHT] == True:
            self.vx = 7
            self.dir = RIGHT
        else:
            self.vx = 0
        
        if self.key_handler[UP] == True and self.y + self.r == self.g:
            self.vy = -10
        
        if frameCount % 5 == 0 and self.vx != 0 and self.vy == 0: 
            self.slice = (self.slice + 1) % self.num_slices
        elif self.vx == 0:
            self.slice = 3
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x - self.r < 0:
            self.x = self.r

class Game:
    
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Mario(100, 100, 35)
    
    def display(self):
        noStroke()
        fill(0,125,0)
        rect(0, self.g, self.w, self.h - self.g)
        
        self.mario.display()

def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    background(255,255,255)
    
def draw():
    background(255,255,255)
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.mario.key_handler[UP] = True
        
def keyReleased():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = False  
    elif keyCode == UP:
        game.mario.key_handler[UP] = False  
    
game = Game(RESOLUTION_W, RESOLUTION_H, GROUND)
