#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:50:55 2019

@author: ariakillebrew
"""

from pgl import GWindow, GOval, GRect, GLabel, GLine # Import pgl objects 
import random # Import random 


# Constants 
GWINDOW_WIDTH = 500               # Width of the graphics window
GWINDOW_HEIGHT = 700              # Height of the graphics window
STAR_MAX_W = 1
STAR_MIN_W = 5
NUM_STARS = 1
HOLE_W = 20

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow 

def addStars():
    for i in range(NUM_STARS):
        sx = random.uniform(10, (GWINDOW_WIDTH - HOLE_W)/2)
        sy = random.uniform((GWINDOW_HEIGHT-GWINDOW_WIDTH)/2, GWINDOW_HEIGHT- (GWINDOW_HEIGHT-GWINDOW_WIDTH)/2)
        r = random.uniform(STAR_MIN_W, STAR_MAX_W)
        star = GOval(sx, sy, r, r)
        star.setFilled(True)
        star.setColor("blue")
        
        gw.add(star)
        
def blackHole():
    hole = GOval((GWINDOW_WIDTH - HOLE_W)/2, (GWINDOW_HEIGHT - HOLE_W)/2, HOLE_W, HOLE_W)
    hole.setFilled(True)
    hole.setColor("darkblue")
    gw.add(hole)

def step():
    
    
      
if __name__ == "__main__":
    addStars()
    blackHole()