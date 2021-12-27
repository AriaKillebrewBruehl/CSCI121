#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:16:31 2019

@author: ariakillebrew
"""

def isCollapsable(word):
    if len(word) == 1 and  isEnglishWord(word):
        return True 
    for i in range(len(word)):
        if isEnglishWord(word):
            return True
        word = word - word[i] 
    else:
        return False