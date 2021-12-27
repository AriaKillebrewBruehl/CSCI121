#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:57:53 2019

@author: ariakillebrew
"""
def removeReps(word):
    if len(word) == 1:
        return word
    else:
        cutoff = word[0]
        rest_of_word = word[1:]
        what_they_got_back = removeReps(rest_of_word)
        if cutoff ==  what_they_got_back[0]:
            return what_they_got_back 
        else:
            return cutoff + what_they_got_back 