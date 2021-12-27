#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:30:11 2019

@author: ariakillebrew
"""
import math
from pgl import GWindow, GOval, GPolygon  

# Constants 
GWINDOW_WIDTH = 700               # Width of the graphics window
GWINDOW_HEIGHT = 500              # Height of the graphics window
R_TOTAL = GWINDOW_WIDTH / 2 
N_STEPS = 100 

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow 


def drawRose(e):
    #nonlocal currentR, desiredR
    theta = 0
    Rose = GPolygon()
    X_LOCATION = e.getX()
    Y_LOCATION = e.getY()
    
    while theta < 2*3.14:
        #currentR = R_TOTAL * math.cos(4 * theta)
        #desiredR
        r = 100 * math.cos(6 * theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        Rose.addVertex(x, y)

        theta += 2*3.14/1000
    
    Rose.setFilled(True)
    Rose.setColor("pink")
    gw.add(Rose, X_LOCATION, Y_LOCATION) 
    
def drawRose2():
    #nonlocal currentR, desiredR
    theta = 0
    Rose2 = GPolygon()
    while theta < 2*3.14:
        #currentR = R_TOTAL * math.cos(4 * theta)
        #desiredR
        r = 75 * math.cos(4 * theta + 3.14/4)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        Rose2.addVertex(x, y)

        theta += 2*3.14/1000
    
    Rose2.setFilled(True)
    Rose2.setColor("lightblue")
    gw.add(Rose2, GWINDOW_WIDTH/2, GWINDOW_HEIGHT/2)
    
def addRoses():

    gw.addEventListener("click", drawRose)
    
if __name__ == "__main__":
    addRoses()
        
        
        
    