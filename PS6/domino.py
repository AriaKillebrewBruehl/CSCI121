# -*- coding: utf-8 -*-

class Domino:
    def __init__(self, ls, rs):
        self.leftside = ls
        self.rightside = rs
        
    def getLeftDots(self):
        return self.leftside

    def getRightDots(self):
        return self.rightside    
    
    def __str__(self):
        return str(self.leftside) + "-" + str(self.rightside) 

def fullSet():
    for i in range(7):
        dominos = []
        for j in range(i, 7):
            dominos.append(str(Domino(i, j)))
        line = " ".join(dominos)
        print(line)
        
if __name__ == "__main__":
    fullSet()