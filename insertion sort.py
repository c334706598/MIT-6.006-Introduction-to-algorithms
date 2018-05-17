# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:07:58 2018

@author: XIN
"""
import random

def gen_1D(n):
    return [random.uniform(0,10) for _ in range(n)]

def find_position(sorted_array, num):
    l = len(sorted_array)
    if l == 1:
        if sorted_array[0] <= num:
            return 1
        else:
            return 0
    if sorted_array[l//2] == num:
        return l//2 + 1
    elif sorted_array[l//2] < num:
        return l//2 + find_position(sorted_array[l//2:], num)
    else:
        return find_position(sorted_array[:l//2], num)

def swap_to_position(sorted_array, p_i, p_f):
    if p_f >= p_i:
        pass
    else:
        while p_i > p_f:
            sorted_array[p_i], sorted_array[p_i-1] = sorted_array[p_i-1], sorted_array[p_i]
            p_i -= 1
        

def Insertion_sort(array):
    l = len(array)
    if l <= 1:
        return array
    i = 1
    while i <= l-1:
        p = find_position(array[:i], array[i])
        swap_to_position(array, i, p)
        i += 1
    return array
                
#a = gen_1D(20)
#a.sort()
#print(a)
#print(find_position(a, 5))
#swap_to_position(a,9,1)
#print(Insertion_sort(a))


    
    
    
