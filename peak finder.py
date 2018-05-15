# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:00:49 2018

@author: XIN
"""

import random
import operator

def gen_1D(n):
    return [random.uniform(0,10) for _ in range(n)]

#print(gen_1D(10))
    
def peak_finder_1D(array):
    if len(array) == 1:
        return 0
    
    l = len(array)


#        
#a = gen_1D(10)
#index, value = max(enumerate(a), key=operator.itemgetter(1))
#print(index, value)
#print(a)
#print(peak_finder_1D(a))
            
def gen_2D(n):
    return [[random.uniform(0,10) for col in range(n)] for row in range(n)]

#print(gen_2D(10))

def find_max(array):
    ind, val = max(enumerate(array), key=operator.itemgetter(1))
    return ind, val

def peak_finder_2D(matrix):
    if len(matrix) == 1:
        return 0, find_max(matrix[0])
    
    l = len(matrix)
    index, value = find_max(matrix[l//2])
    if l//2 == 0:
        if  value >= matrix[1][index]:
            return 0, index
        else:
            return 1 + peak_finder_2D(matrix[1:])[0], peak_finder_2D(matrix[1:])[0]
    elif l//2 == l-1:
        if value >= matrix[l-2][index]:
            return l-1, index
        else:
            return peak_finder_2D(matrix[:l-1])
    else:
        if value >= matrix[l//2-1][index] and value >= matrix[l//2+1][index]:
            return l//2, index
        elif value < matrix[l//2-1][index]:
            return peak_finder_2D(matrix[:l//2])
        else:
            return l//2 + 1 + peak_finder_2D(matrix[l//2+1:])[0], peak_finder_2D(matrix[l//2+1:])[1]
        
#b = gen_2D(10)
#print(b)
#i,j = peak_finder_2D(b)
#print(find_max(b[0]))    
#print(b[i][j])
#print(b[i-1][j])
#print(b[i+1][j])
#print(b[i][j-1])    
#print(b[i][j+1])        