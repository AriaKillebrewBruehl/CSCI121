#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:45:36 2019

@author: ariakillebrew
"""
from pgl import GWindow, GOval 

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300

TIME_STEP = 20
DELTA_SIZE = 1

def growingCircle():
    def createNew():
        nonlocal circle, desiredSize, currentSize 
        r = 50
        x = 100
        y = 100 
        circle = GOval(x, y, 0, 0)
        circle.setFilled(True)
        circle.setColor("red")
        desiredSize = 2 * r
        currentSize = 0 
        return circle 
    
    def step():
        nonlocal circle, desiredSize, currentSize
        if currentSize < desiredSize:
            currentSize += DELTA_SIZE
            x = circle.getX() - DELTA_SIZE/2
            y = circle.getY() - DELTA_SIZE/2
            circle.setBounds(x, y, currentSize, currentSize)
            
        elif currentSize == desiredSize:
            timer.stop()
            
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    desiredSize = 0 
    currentSize = 0 
    circle = None 
    timer = gw.setInterval(step, TIME_STEP)
    
    
if __name__ == "__main__":
    growingCircle()