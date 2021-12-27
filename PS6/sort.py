# -*- coding: utf-8 -*-

def insertionSort(L, k):
    wontord = L[k:]
    willord = L[:k]
    
    for i in range(k):
        for j in range(i, 0, -1):
            if willord[j] < willord[j - 1]:
                willord[j], willord[j - 1] = willord[j - 1], willord[j]
            else:
                break
            
    return willord + wontord

