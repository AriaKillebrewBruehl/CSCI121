#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:30:11 2019

@author: ariakillebrew
"""
import math
from pgl import GWindow, GPolygon  

# Constants 
GWINDOW_WIDTH = 700               # Width of the graphics window
GWINDOW_HEIGHT = 500              # Height of the graphics window
R_TOTAL = GWINDOW_WIDTH / 2 
N_STEPS = 100 

TIME_STEP = 20 



def growingRose():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow 
    desiredR = 100 
    currentR = 1
    Rose = None 
    x = GWINDOW_WIDTH/2
    y = GWINDOW_HEIGHT/2
    DELTA_SIZE = 1
    ROTATE = 0 
    
        
    def drawRose(x, y, currentR):
        nonlocal desiredR, Rose, ROTATE 
        theta = 0
        Rose = GPolygon()
        while theta < 2*math.pi:
            r = currentR * math.cos(4 * theta + ROTATE)
            vx = r * math.cos(theta)
            vy = r * math.sin(theta)
            Rose.addVertex(vx, vy)
    
            theta += 2*math.pi/1000
        desiredR = 100
        gw.add(Rose, x, y) 
    def step():
        nonlocal currentR, desiredR, Rose, DELTA_SIZE, ROTATE 
        if currentR == 1:
            DELTA_SIZE = 1
            
        elif currentR == desiredR:
            DELTA_SIZE = -1
            
        currentR += DELTA_SIZE
        ROTATE += .25 
        gw.remove(Rose)
        drawRose(x, y, currentR)
    drawRose(x, y, currentR)        
    timer = gw.setInterval(step, TIME_STEP)  
    
if __name__ == "__main__":
    growingRose()
        
        
        
    