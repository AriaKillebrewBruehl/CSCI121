# -*- coding: utf-8 -*-

from pgl import GWindow, GRect, GOval 

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400


def DrawBangladeshFlag():
    
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    rect = GRect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    rect.setFilled(True)
    rect.setColor("ForestGreen")
    gw.add(rect)
    

    circ = GOval(200, 100, 200, 200)
    circ.setFilled(True)
    circ.setColor("DarkRed")
    gw.add(circ)
    
def DrawLibyaFlag():
    
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

    gw.add(createBackground("Green"))
    
def DrawJapanFlag():
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    circ = GOval(200, 100, 200, 200)
    circ.setFilled(True)
    circ.setColor("DarkRed")
    gw.add(circ)
  

def createBackground(color):
    
    background = GRect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    background.setFilled(True)
    background.setColor(color)
    
    return background

def createSun(color):
    
    sun_radius = WINDOW_HEIGHT//5
    sun = GOval(WINDOW_WIDTH//2 - sun_radius, WINDOW_HEIGHT//2-sun_radius, 
                sun_radius*2, sun_radius*2)
    sun.setColor(color)
    sun.setFilled(True)
    
    return sun 
    

def DrawPalauFlag():
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

    gw.add(createBackground("cyan"))
    gw.add(createSun("yellow"))
    
 
    
def DrawMaldivesFlag():
    sun_radius = WINDOW_HEIGHT//5
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    gw.add(createBackground("Crimson"))
    
    rect = GRect(WINDOW_WIDTH//8, WINDOW_HEIGHT//8, 3*WINDOW_WIDTH//4, 3*WINDOW_HEIGHT//4)
    rect.setColor("darkgreen")
    rect.setFilled(True)
    gw.add(rect)
    
    gw.add(createSun("white"))
    
    circ=GOval(WINDOW_WIDTH//2 - (sun_radius-20), WINDOW_HEIGHT//2-(sun_radius), 
                sun_radius*2, sun_radius*2)
    circ.setColor("darkgreen")
    circ.setFilled(True)
    gw.add(circ)


def createRect(x, y, w, h, color):
    
    rect = GRect(x, y, w, h)
    rect.setFilled(True)
    rect.setColor(color)
    
    return rect
    
def DrawArtsakhFlag():
    gw = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    gw.add(createRect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT//3, "red"))
    gw.add(createRect(0, WINDOW_HEIGHT//3, WINDOW_WIDTH, WINDOW_HEIGHT//3, "blue"))
    gw.add(createRect(0, 2*WINDOW_HEIGHT//3, WINDOW_WIDTH, WINDOW_HEIGHT//3, "yellow"))
    
    for i in range(5):
         gw.add(createRect(, 0, WINDOW_WIDTH, WINDOW_HEIGHT//3, "red"))
        
    
if __name__ == "__main__":
    DrawArtsakhFlag()
