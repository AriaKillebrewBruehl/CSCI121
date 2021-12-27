# -*- coding: utf-8 -*-

from pgl import GWindow, GOval, GLabel

GW_WIDTH = 600
GW_HEIGHT = 400

def write(s):
    import sys
    sys.stdout.write(str(s))   

def FizzbuzzTheExperience():
    aria = 1
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    fizzbutton = GOval(100, 150, 100, 100)
    fizzbutton.setFilled(True)
    gw.add(fizzbutton)
    fizztext = GLabel("fizz", 140, 210)
    gw.add(fizztext)
    
    buzzbutton = GOval(400, 150, 100, 100)
    buzzbutton.setFilled(True)
    gw.add(buzzbutton)
    buzztext = GLabel("buzz", 430, 210)
    gw.add(buzztext)
    
    
    def fizz(num):
        if num % 3 == 0:
            fizzbutton.setColor("red")
            write('fizz')
            
    def buzz(num):
        if num % 5 == 0:
            buzzbutton.setColor("orange")
            write('buzz')
            
    def count(num):
        if num % 3 != 0 and num%5 != 0:
            write(num)
    
    def step():
        nonlocal aria 
        fizzbutton.setColor("black")
        buzzbutton.setColor("black")
        fizz(aria)
        buzz(aria)
        count(aria)
        print("")
        aria += 1
    
   
    timer = gw.setInterval(step, 1000)
    
if __name__ == "__main__":
    FizzbuzzTheExperience()
        
        