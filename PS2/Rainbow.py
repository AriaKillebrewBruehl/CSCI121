# -*- coding: utf-8 -*-

from pgl import GWindow, GOval, GRect


GWINDOW_WIDTH = 700
GWINDOW_HEIGHT = 500
colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Cyan")

def background():
    
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    rect = GRect(-10, -10, 720, 520)
    rect.setColor("cyan")
    rect.setFilled(True)
    gw.add(rect)
  

    for i in range(8):
        arc = GOval(-100, 100 + 30*i, 900, 500)
        arc.setFilled(True)
        arc.setColor(colors[i])
        gw.add(arc)
    

    
if __name__ == "__main__":
    background()
    
    
    
