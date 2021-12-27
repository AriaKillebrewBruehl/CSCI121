#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:05:17 2019

@author: ariakillebrew
"""
from pgl import GWindow, GOval

GW_W = 600
GW_H = 600
F_W = 100
EYE_S = 20
MOUTH_S = 30
def face():
    gw = GWindow(GW_W, GW_H)
    face = GOval((GW_W - F_W)/2, (GW_H - F_W)/2, F_W, F_W)
    face.setFilled(True)
    face.setColor("yellow")
    gw.add(face)
    
    eye = GOval((GW_W - F_W)/2 + EYE_S, GW_H/2 - EYE_S, EYE_S, EYE_S)
    eye.setFilled(True)
    eye.setColor("blue")
    gw.add(eye)
    eye2 = GOval((GW_W - F_W)/2  + F_W - EYE_S*2, GW_H/2 - EYE_S, EYE_S, EYE_S)
    eye2.setFilled(True)
    eye2.setColor("blue")
    gw.add(eye2)


    mouth = GOval((GW_W - MOUTH_S)/2, GW_H/2 + MOUTH_S/2, MOUTH_S, MOUTH_S)
    mouth.setFilled(True)
    mouth.setColor("red")
    gw.add(mouth)
    
    
if __name__ == "__main__":
    face()