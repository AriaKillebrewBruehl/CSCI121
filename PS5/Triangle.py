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

def drawTriangle(edge, dx, dy, whole):
    
    tri = GPolygon()
    x = - edge/2
    y = edge / (2 * math.sqrt(3))
    print(x, y)
    tri.addVertex(x,y)
    tri.addPolarEdge(edge, 0)
    tri.addPolarEdge(edge, 120)
    tri.addPolarEdge(edge, -120)
    whole.add(tri, dx - edge/2, dy - edge *(math.sqrt(3)/2))
    

    
def createSierpinskiTriangle(size,order):
    whole = GCompound()
    def createTriangle(size, order, dx, dy):
        if order == 0:
           drawTriangle(size, dx, dy, whole)
           
        else:
           createTriangle(size/2, order - 1, dx, 300) #dy - 4/(math.sqrt(3) * size)
           createTriangle(size/2, order - 1, dx - size/4, dy + 4*math.sqrt(3)/size - 2 * (4/(math.sqrt(3) * size)))
           createTriangle(size/2, order - 1, dx + size/4, dy + 4*math.sqrt(3)/size - 2 * (4/(math.sqrt(3) * size)))
    createTriangle(size, order, 0, 0)
    gw.add(whole, GWINDOW_WIDTH/2,GWINDOW_HEIGHT/2)  
    
if __name__ == "__main__":
    createSierpinskiTriangle(300, 2)
    #whole = GCompound()
    #drawTriangle(50, 0, 0, whole)
    #gw.add(whole, 300, 300)
    
    
