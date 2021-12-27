#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:30:11 2019

@author: ariakillebrew
"""
import math
from pgl import GWindow, GPolygon  

# Constants 
GWINDOW_WIDTH = 600               # Width of the graphics window
GWINDOW_HEIGHT = 600              # Height of the graphics window
N_STEPS = 100 

TIME_STEP = 20 

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow

def growingRose(xp, yp, n):
     
    desiredR = 100 
    currentR = 1
    Rose = None 
    x = GWINDOW_WIDTH * xp 
    y = GWINDOW_HEIGHT * yp
    DELTA_SIZE = .5
    ROTATE = 0 
    
        
    def drawRose(x, y, currentR, n):
        nonlocal desiredR, Rose, ROTATE  
        theta = 0
        Rose = GPolygon()
        while theta < 10*math.pi:
            r = currentR * math.cos(n * theta + ROTATE)
            vx = r * math.cos(theta)
            vy = r * math.sin(theta)
            Rose.addVertex(vx, vy)
            theta += 10*math.pi/300
            
        desiredR = 100
        gw.add(Rose, x, y) 
    def step():
        nonlocal currentR, desiredR, Rose, DELTA_SIZE, ROTATE
        if currentR == 1:
            DELTA_SIZE = 1         
        elif currentR == desiredR:
            DELTA_SIZE = -1
            
        currentR += DELTA_SIZE
        ROTATE += .0625 
        gw.remove(Rose)
        drawRose(x, y, currentR, n)
            
    timer = gw.setInterval(step, TIME_STEP)  
 
def Roses():
    growingRose(1/4, 1/4, 1/5)
    growingRose(2/4, 2/4, 2/5)
    growingRose(3/4, 3/4, 3/5)
    
if __name__ == "__main__":
    Roses()