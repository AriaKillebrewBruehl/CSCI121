# -*- coding: utf-8 -*-
from pgl import GWindow, GOval, GRect, GLabel, GLine # Import pgl objects 
import random # Import random 


# Constants 
GWINDOW_WIDTH = 700               # Width of the graphics window
GWINDOW_HEIGHT = 500              # Height of the graphics window
PLAYER_WIDTH = 20
DORM_WIDTH = 200
DORM_HEIGHT = 100 
ROOF_HEIGHT = 50
DOOR_HEIGHT = (DORM_HEIGHT)/3
DOOR_WIDTH = DOOR_HEIGHT/2
CAT_WIDTH = 15
NUM_CAT = 20 
NUM_TREES = 5
TREE_MAX_WIDTH = 20
TREE_MIN_WIDTH = 10
TREE_MAX_HEIGHT = 50
TREE_MIN_HEIGHT = 10 


# Derived Constants
D_X = (GWINDOW_WIDTH - DORM_WIDTH)/2
D_Y = (GWINDOW_HEIGHT - DORM_HEIGHT)/2

# Variable creation
player = None
cat = None
tree = None

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow 

def createPlayer():
    global player
    
    player = GOval(PLAYER_WIDTH/2, PLAYER_WIDTH/2, PLAYER_WIDTH, PLAYER_WIDTH)
    player.setFilled(True)
    player.setColor("red")
    gw.add(player)
    
def createDorm():
    
    gw.add(GLine(D_X + DORM_WIDTH/2, D_Y - ROOF_HEIGHT, D_X, D_Y))
    gw.add(GLine(D_X + DORM_WIDTH/2, D_Y - ROOF_HEIGHT, D_X + DORM_WIDTH, D_Y))
    gw.add(GRect(D_X, D_Y, DORM_WIDTH, DORM_HEIGHT))
    gw.add(GRect(D_X + (DORM_WIDTH - DOOR_WIDTH)/2, D_Y + DORM_HEIGHT - DOOR_HEIGHT, DOOR_WIDTH, DOOR_HEIGHT))
    
def createCat():
    global cat 
    
    for i in range(NUM_CAT):
        cat = GOval(random.randrange(GWINDOW_WIDTH - CAT_WIDTH), random.uniform(0, (GWINDOW_HEIGHT - DORM_HEIGHT - ROOF_HEIGHT)/2), CAT_WIDTH, CAT_WIDTH)
        cat.setFilled(True)
        cat.setColor("blue")
        gw.add(cat)

def createTree():
    global Tree
    
    tree = GRect(50, 50, random.uniform(TREE_MIN_WIDTH, TREE_MAX_WIDTH), random.uniform(TREE_MIN_HEIGHT, TREE_MAX_HEIGHT))
    tree.setFilled(True)
    tree.setColor("brown")
    gw.add(tree)
    
    
def addObstacles():
    createCat()
    createDorm()
    createTree()
    
def mouseMotion(e): # Move player with mouse 
    global player 
    
    lastX = e.getX()
    lastY = e.getY()
    player.setLocation(lastX, lastY)
    
    if e.getX() < 0:
        player.setLocation(0, lastY)
        
    elif e.getX() > (GWINDOW_WIDTH - PLAYER_WIDTH) :
        player.setLocation(GWINDOW_WIDTH - PLAYER_WIDTH, lastY)   
        
def movePlayer():
    
    gw.addEventListener("mousemove", mouseMotion)

if (__name__ == "__main__"):
    createPlayer()
    movePlayer()
    addObstacles()
    
    
