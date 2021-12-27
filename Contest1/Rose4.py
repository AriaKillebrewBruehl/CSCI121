#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:30:11 2019

@author: ariakillebrew
"""
import math, random
from pgl import GWindow, GPolygon, GRect, GLine, GLabel, GArc 

# Constants 
GWINDOW_WIDTH = 1000               # Width of the graphics window
GWINDOW_HEIGHT = 600              # Height of the graphics window
TIME_STEP = 50 
BOX_WIDTH = 2 * GWINDOW_WIDTH/3
BOX_HEIGHT = GWINDOW_HEIGHT/8
LIP = BOX_WIDTH/40
numflowers = 0



gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create GWindow

def background():
    sky = GRect(0, 0, GWINDOW_WIDTH, 4 * GWINDOW_HEIGHT/5) # Create sky 
    sky.setFilled(True)
    sky.setColor("deepskyblue")
    gw.add(sky)
    grass = GRect(0, 4 * GWINDOW_HEIGHT/5, GWINDOW_WIDTH, GWINDOW_HEIGHT) # Create grass
    grass.setFilled(True)
    grass.setColor("darkgreen")
    gw.add(grass)    
    box = GRect(GWINDOW_WIDTH/6, 3*GWINDOW_HEIGHT/4, BOX_WIDTH, BOX_HEIGHT) # Create box 
    box.setFilled(True)
    box.setColor("darkgoldenrod")
    gw.add(box)
    lip = GRect(GWINDOW_WIDTH/6 - LIP/2, 3*GWINDOW_HEIGHT/4, BOX_WIDTH + LIP, LIP/2) # Add lip to box 
    lip.setFilled(True)
    lip.setColor("saddlebrown")
    gw.add(lip)
    msg = GLabel("Polar Python Plants!") # Add upper message 
    msg.setFont("25pt 'Courier'")
    x = GWINDOW_WIDTH/6 + (BOX_WIDTH - msg.getWidth())/2
    y = 3*GWINDOW_HEIGHT/4 + LIP + msg.getAscent()
    gw.add(msg, x, y)
    msg2 = GLabel("Click to Plant Flower!") # Add lower message 
    msg2.setFont("12pt 'Courier'")
    x = GWINDOW_WIDTH/6 + (BOX_WIDTH - msg2.getWidth())/2
    y = msg.getY() + 1.5*msg2.getAscent()
    gw.add(msg2, x, y)
    
    tag = GLabel("Created by Aria Killebrew Bruehl with tutoring from Henry Lideman") # Add lower message 
    tag.setFont("7pt 'Courier'")
    y = GWINDOW_HEIGHT - tag.getAscent()
    gw.add(tag, 5, y)
    
    
    
  
        
def growingRose(e):
    global numflowers 
    
    if GWINDOW_WIDTH/6 <= e.getX() <= 5*GWINDOW_WIDTH/6 and 75 <= e.getY() <= 3*GWINDOW_HEIGHT/5: # If the mouse is above flower bed
        numflowers +=  1 
        
        if numflowers < 8:    
            
            desiredR = 75 
            currentR = 1
            Rose = None 
            x = e.getX() # Position flower at mouseX, mouseY
            y = e.getY()
            DELTA_SIZE = .5
            ROTATE = 0 
            n = int(e.getX() // 50) # Number of flower petals based on mouse position
            if n == 5:
                n = 6
            
            colors = ["red", "pink", "lightcoral", "salmon", "orchid","fuchsia", "darkviolet", "rebeccapurple" ,"mediumorchid", "mediumvioletred", "blueviolet", "orangered"]
            color = random.choice(colors)   
            stemcolors = ["darkgreen", "green", "forestgreen", "limegreen", "springgreen", "greenyellow"]
            stemcolor = random.choice(stemcolors)
            
            stem = GRect(x - 1, y, 2, 3*GWINDOW_HEIGHT/4 - y - 1) # Add stem for flower 
            stem.setFilled(True)
            stem.setColor(stemcolor)
            gw.add(stem)
            
            LEAF_SIZE = random.uniform(60, 100) # Add leafs for flower 
            LEAF_Y = y + random.uniform(stem.getHeight()/5, stem.getHeight()/2)
            Rleafcolor = random.choice(stemcolors)
            leafR = GArc(x - LEAF_SIZE/2, LEAF_Y, LEAF_SIZE, LEAF_SIZE, random.uniform(30, 60), random.uniform(-50, -15))
            leafR.setFilled(True)
            leafR.setColor(Rleafcolor)
            gw.add(leafR)
            Lleafcolor = random.choice(stemcolors)
            leafL = GArc(x - LEAF_SIZE/2, LEAF_Y, LEAF_SIZE, LEAF_SIZE, random.uniform(120, 185), random.uniform(15, 50))
            leafL.setFilled(True)
            leafL.setColor(Lleafcolor)
            gw.add(leafL)
            
            
            
            
            def drawRose(x, y, currentR, n):
                nonlocal desiredR, Rose, ROTATE  
                theta = 0
                Rose = GPolygon()
                while theta < 10*math.pi: # Create polar curve 
                    r = currentR * math.cos(n/5 * theta + ROTATE)
                    vx = r * math.cos(theta)
                    vy = r * math.sin(theta)
                    Rose.addVertex(vx, vy)
                    theta += 10*math.pi/300
                    
                desiredR = 75
                Rose.setFilled(True)
                Rose.setColor(color)
                gw.add(Rose, x, y) 
            def step(): # Grow/rotate flower 
                nonlocal currentR, desiredR, Rose, DELTA_SIZE, ROTATE
                if currentR == 1:
                    DELTA_SIZE = 1         
                elif currentR == desiredR:
                    DELTA_SIZE = -1
                    
                currentR += DELTA_SIZE
                ROTATE += .0625 
                gw.remove(Rose)
                drawRose(x, y, currentR, n)
                    
            timer = gw.setInterval(step, TIME_STEP)  
            
        if numflowers > 8:
            msg3 = GLabel("You're garden is too crowded! No more flowers can be added!")
            msg3.setFont("20pt 'Courier'")
            x = (GWINDOW_WIDTH - msg3.getWidth())/2
            y = (GWINDOW_HEIGHT - msg3.getAscent())
            gw.add(msg3, x, y)
            
def Roses():
    global numflowers 
    
    background() # Add sky, grass, box
    gw.addEventListener("click", growingRose) # Add rose on click 
    
    
if __name__ == "__main__":
    Roses()