# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:52:49 2018

@author: XIN
"""
import random

def gen_1D(n):
    return [random.uniform(0,10) for _ in range(n)]

def merge(A, B):
    lA = len(A)
    lB = len(B)
    if lA == 0:
        return B
    if lB == 0:
        return A
    res = []
    iA = 0
    iB = 0
    while iA < lA and iB < lB:
        if A[iA] <= B[iB]:
            res.append(A[iA])
            iA += 1
        else:
            res.append(B[iB])
            iB += 1
    if iA == lA:
        res += B[iB:]
    else:
        res += A[iA:]
    return res

def merge_sort(array):
    l = len(array)
    if l <= 1:
        return array
    else:
        array_A = merge_sort(array[:l//2])
        array_B = merge_sort(array[l//2:])
        array = merge(array_A, array_B)
        return array
    
#a = gen_1D(100)
#print(merge_sort(a))    