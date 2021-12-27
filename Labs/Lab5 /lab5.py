#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:09:48 2019

@author: ariakillebrew
"""
'''
def removeVowels(s):
    newstr = ""
    
    for i in range(len(s)):
        if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u" and s[i] != "y":
            newstr =  newstr + s[i]
            
    print(newstr)      


def removeVowels(s):
    paper = ""
    for i in range(len(s)):
       letter = s[i]
       if not isVowel(letter):
           paper = paper + letter 
           
    return paper 
    
def isVowel(letter):
    return letter in aeiouy
'''

def removeVowels(word):
    if len(word) == 0"
        return ""
    else:
        cutoff = word[0]
        rest_of_word = word[1:]
        what_they_got_back = removeVowels(rest_of_word)
        if isVowels
    