# -*- coding: utf-8 -*-
import math 
from pgl import GWindow, GPolygon

class GRegularPolygon(GPolygon):
    
    def __init__(self, num_sides, radius):
        GPolygon.__init__(self)
        dx = -radius
        dy = 0
        self.addVertex(dx, dy)
        da = 360 / num_sides
        edge = math.sin(da/2 * math.pi/180) * radius * 2
        angle = 0
        for i in range(num_sides):
            self.addPolarEdge(edge, angle)
            angle -= da


def drawPolygon(sides, size):
    gw = GWindow(500, 500)
    regualrPolygon = GRegularPolygon(sides, size)
    gw.add(regualrPolygon, 250, 250)

if __name__ == "__main__":
    drawPolygon(200, 30)