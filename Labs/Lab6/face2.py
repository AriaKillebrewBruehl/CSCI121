#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:28:35 2019

@author: ariakillebrew
"""

from pgl import GWindow, GOval, GCompound
GWINDOW_WIDTH = 600
GWINDOW_HEIGHT = 400
diameter = 100
gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

def filledCircle(x, y, diameter, color):
    circle = GOval(x, y, diameter, diameter)
    circle.setFilled(True)
    circle.setFillColor(color)
    return circle

def createFace(gw, diameter):
    face = GCompound()
    head = filledCircle(-diameter//2, -diameter//2, diameter, "yellow")
    face.add(head)
    mouth = filledCircle(-diameter/10, diameter/8, diameter/5, "black")
    face.add(mouth)
    lefteye = filledCircle(-diameter/4, -diameter/4, diameter/8, "blue")
    face.add(lefteye)
    righteye = filledCircle(diameter/8, -diameter/4, diameter/8, "blue")
    face.add(righteye)
    return face 
    
def faces():
    
    for i in range(-2, 3):
        face = createFace(gw, diameter)
        gw.add(face, GWINDOW_WIDTH/2, GWINDOW_HEIGHT/2)
        face.movePolar(diameter * (i), 45)
        face = createFace(gw, diameter)
        gw.add(face, GWINDOW_WIDTH/2, GWINDOW_HEIGHT/2)
        face.movePolar(diameter * (i), 135)
        

        
if __name__ == "__main__":
    faces()
    