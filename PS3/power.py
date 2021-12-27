# -*- coding: utf-8 -*-


def raiseToPower(x, k):
    if k == 0:
        return 1 
    else: 
        return x * raiseToPower(x, k-1)
