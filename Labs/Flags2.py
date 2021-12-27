# -*- coding: utf-8 -*-

from pgl import GWindow, GRect, GOval

GW_WIDTH = 600
GW_HEIGHT = 400
RADIUS = 100

def DrawJapanFlag():
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    background = GRect(0, 0, GW_WIDTH, GW_HEIGHT)
    background.setFillColor("White")
    background.setFilled(True)
    
    sun = GOval(GW_WIDTH//2 - RADIUS, GW_HEIGHT//2 - RADIUS, 2*RADIUS, 2*RADIUS)
    sun.setFilled(True)
    sun.setColor("red")
    
    gw.add(background)
    gw.add(sun)
    
    def doSomething(e):
        x = e.getX()
        y = e.getY()
        thing = gw.getElementAt(x,y)
        if thing == background:
            thing.setFillColor("green")
        
    gw.addEventListener("mousedown", doSomething)
    
    
if __name__ == "__main__":
    DrawJapanFlag()