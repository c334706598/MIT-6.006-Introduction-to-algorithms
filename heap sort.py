# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:02:17 2018

@author: XIN
"""
import random

class heap:
    def __init__(self, array):
        self.data = self.build_max_heap(array)
    
    def max_heapify(self, array, i):
        l = len(array)
        if 2*i > l-1:
            pass
        elif 2*i == l-1:
            if array[i] < array[2*i]:
                array[i], array[2*i] = array[2*i], array[i]
        else:
            if array[i] > max(array[2*i], array[2*i+1]):
                pass
            else:
                if array[2*i] < array[2*i+1]:
                    array[i], array[2*i+1] = array[2*i+1], array[i]
                    self.max_heapify(array, 2*i+1)
                else:
                    array[i], array[2*i] = array[2*i], array[i]
                    self.max_heapify(array, 2*i)
            
                    
    def build_max_heap(self, array):
        length = len(array)
        array = [0] + array
        i = length // 2
        while i > 0:
            self.max_heapify(array, i)
            i -=1
        return array
    
    def extract_max(self):
        if len(self.data) == 1:
            return None
        if len(self.data) == 2:
            temp = self.data[-1] 
            self.data = self.data[:-1]
            return temp
        else:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            temp = self.data[-1]
            self.data = self.data[:-1]
            self.max_heapify(self.data, 1)
            return temp
        

def gen_1D(n):
    return [random.uniform(0,10) for _ in range(n)]

def heap_sort(array):
    l = len(array)
    if l <= 1:
        return array
    else:
        res = []
        h = heap(array)
        for i in range(l):
            res.append(h.extract_max())
        return res
            
#a = gen_1D(50)
#print(a)
#print(heap(a).data)
#print(heap_sort(a))    
        
    