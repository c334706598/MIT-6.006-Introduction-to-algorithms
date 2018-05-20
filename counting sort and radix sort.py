# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:22:23 2018

@author: XIN
"""
import random

def counting_sort(array, key):
    MAX = max(key)
    L = [[] for _ in range(MAX+1)]
    output = []
    for j in range(len(array)):
        L[key[j]].append(array[j])
    for i in range(MAX+1):
        output.extend(L[i])
    return output
    
#a = [x for x in range(10)]
#print(a)
#k = [10-x for x in range(10)]
#print(counting_sort(a, k))
    
def radix_sort(array, base):
    i = 1
    while True:
        key = [(x%(base**i))//(base**(i-1)) for x in array]
        if any(key):
            array = counting_sort(array, key)
            i += 1
        else:
            break
    return array

#a = [int(random.uniform(0,100)) for _ in range(100)]
#print(a)
#print(radix_sort(a, 2))
        
        
    
    
        
    
    