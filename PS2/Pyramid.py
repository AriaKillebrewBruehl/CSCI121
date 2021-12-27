# -*- coding: utf-8 -*-

from pgl import GWindow, GRect


GWINDOW_WIDTH = 700
GWINDOW_HEIGHT = 500
BRICKS_IN_BASE = 20
BRICK_WIDTH = 30
BRICK_HEIGHT = 15 
OFFSET = (GWINDOW_WIDTH - (BRICK_WIDTH * BRICKS_IN_BASE))//2
BASE_HEIGHT = GWINDOW_HEIGHT - (GWINDOW_HEIGHT - (BRICK_HEIGHT * BRICKS_IN_BASE))//2


gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

def drawBrick(x, y):
    
    brick = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
    
    return brick 

def drawRow(y, n): 
    
    for i in range(n):
        newbrick = drawBrick(OFFSET + (BRICKS_IN_BASE-n)*BRICK_WIDTH//2 + BRICK_WIDTH*i, y)
        
        gw.add(newbrick) 
        

def drawPyramid():
    
    for i in range(BRICKS_IN_BASE):
        drawRow(BASE_HEIGHT - BRICK_HEIGHT*i, BRICKS_IN_BASE-i)


if __name__ == "__main__":
    drawPyramid() 
          
