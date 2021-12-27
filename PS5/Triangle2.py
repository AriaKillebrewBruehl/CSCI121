#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:11:45 2019

@author: ariakillebrew
"""
from pgl import GPolygon, GWindow, GCompound
import  math 

GWINDOW_WIDTH = 600
GWINDOW_HEIGHT = 600

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

def drawTriangle(edge, x, y, whole):
    
    tri = GPolygon()
    tri.addVertex(x,y)
    tri.addVertex(x + edge, y)
    tri.addVertex(x + edge/2, y - edge*math.sqrt(3)/2)
    whole.add(tri)  
    
def createSierpinskiTriangle(size,order):
    whole = GCompound()
    
    def createTriangle(size, order, dx, dy):
        if order == 0:
           drawTriangle(size, dx, dy, whole)
        else:
           createTriangle(size/2, order - 1, dx + size/4, dy - size/4*math.sqrt(3)) 
           createTriangle(size/2, order - 1, dx, dy)
           createTriangle(size/2, order - 1, dx + size/2, dy)
           
    createTriangle(size, order, 0, 0)
    gw.add(whole, (GWINDOW_WIDTH - size)/2, (GWINDOW_HEIGHT + size * math.sqrt(3)/2)/2)  
    
if __name__ == "__main__":
    
    createSierpinskiTriangle(size, order)
  
