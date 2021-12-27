# -*- coding: utf-8 -*-

def slytherinAnswer():
    return 1729

def enigmaAnswer():
    return 64 

def enigma():
    def puzzle(x):
        def riddle(y):
            return 2 * x - y 
        return riddle 
    x = 10 
    y = 37
    f = puzzle(y)
    return f(x)