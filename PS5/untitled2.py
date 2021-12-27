#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:01:58 2019

@author: ariakillebrew
"""

def isCollapsible(word):
    
    for i in range(len(word)):
        word = word - word[i] 
        print(word)
        word = word + word[i]           
    