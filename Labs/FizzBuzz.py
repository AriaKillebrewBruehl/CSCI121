#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:16:27 2019

@author: ariakillebrew
"""


def fizzbuzz(k):
    for i in range(1,k+1):
        if i%3 == 0 and i%5 ==0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")

        else:
            print(i)
            
def redux(k):
    for i in range(1,k+1):
        
        if i%3 == 0 and i%5 ==0:
            print("fizzbuzz")
        elif i%10 == 3 and i//10 == 5:
            print("fizzbuzz")
        elif i%10 == 5 and i//10 == 3:
            print("fizzbuzz")
            
            
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
            
            
        elif i == 3:
            print("fizz")
        elif i == 5:
            print("buzz")
        elif i%10 == 3:
            print("fizz")
        elif i%10 == 5:
            print("buzz")
        
            
        else:
            print(i)
    
def fizzy(num):
    return (num % 3 == 0 or num // 10 == 3 or num % 10 == 3)

def buzzy(num):
    return (num % 5 == 0 or num // 10 == 5 or num % 10 == 5)      


def redux2(num):
    for i in range(1, num+1):
        if fizzy(num) and buzzy(num):
            print("fizzbuzz")
        elif buzzy(num):
            print("buzz")
        elif fizzy(num):
            print("fizz")
        else:
            print(num)
    
        
def fizzy2(num):
    return fuzzy(num, 3)

def buzzy2(num):
    return fuzzy(num, 5)      
def fuzzy(num, d):
    return (num % d == 0 or num // 10 == d or num % 10 == d)     
        
        
        
def fizzbuzz2(k):
    
    num = 0
    while num <= k:
        
        
        if num%3 == 0 and num%5 ==0:
            print("fizzbuzz")
        elif num%3 == 0:
            print("fizz")
        elif num%5 == 0:
            print("buzz")
        else:
            print(num)
            
        num += 1 
        

if __name__ == "__main__":
    fizzbuzz2(50)
    
            
        
        
        
