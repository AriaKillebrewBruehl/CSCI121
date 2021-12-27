# -*- coding: utf-8 -*-


def raiseToPower(x, k):
    if k == 0:
        return 1 
    elif k % 2 == 0:
        return raiseToPower(x, k//2)**2
    elif k % 2 == 1: 
        return x * raiseToPower(x, k//2)**2
