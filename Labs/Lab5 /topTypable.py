#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:18:55 2019

@author: ariakillebrew
"""
def isInTop(letter):
    return letter in "qwertyuiop"

def topTypable(word):
    
    if len(word) == 0:
        print("True")
    else:
        cutoff = word[0]
        rest_of_word = word[1:]
        if isInTop(cutoff):
            topTypable(rest_of_word)
        else:
            print("False") 
        
        
def checkchar(letter):
    if letter == "[":
        lb += 1 
    if letter == "]":
        rb += 1 
        
def isBalanced(word):
    
    if len(word) == 0 and lb == rb:
        print("True")
    else:
        cutoff = word[0]
        rest_of_word = word[1:]
        checkchar(cutoff)
        