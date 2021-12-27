#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:16:31 2019

@author: ariakillebrew
"""
from english import isEnglishWord

def isCollapsible(word):
    
    if len(word) == 1 and isEnglishWord(word):
        return True 
    else:
        for i in range(len(word)):
            word = word[:i]+ word[i+1:]  
            if isEnglishWord(word):
                if isCollapsible(word): 
                    return True      
            word = word[:i]+ word[i:]         
    return False 