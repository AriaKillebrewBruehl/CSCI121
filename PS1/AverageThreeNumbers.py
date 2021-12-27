#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:32:24 2019

@author: ariakillebrew
"""



def AverageThreeNumbers():
    
    print("This program averages three numbers.")
    
    a = float(input("Enter n1? "))
    b = float(input("Enter n2? "))
    c = float(input("Enter n3? "))

    avg = str((a+b+c)/3)
    
    print("The average is " + avg)

if __name__ == "__main__":
    AverageThreeNumbers()