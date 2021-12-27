#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:00:56 2019

@author: ariakillebrew
"""

def binarySearch(value, array, p1, p2):
    
    mid = (p1 + p2)//2
    if p1 <= p2 and p1 < len(array):
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            p2 = mid - 1
            return binarySearch(value, array, p1, p2)
        else:
            p1 = mid + 1
            return binarySearch(value, array, p1, p2)
    else:
        return -1


