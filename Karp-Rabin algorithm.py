# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:23:39 2018

@author: XIN
"""

class rollingHash(object):
    def __init__(self):
        self.value = 0
        self.base = 26
        self.p = 10529
        self.size = 0
        
    def append(self, char):
        self.value = (self.value*self.base + (ord(char)-ord('a'))) % self.p
        self.size += 1
    
    def skip(self, char):
        self.value = (self.value - (ord(char)-ord('a'))*(self.base**(self.size-1) % self.p)) % self.p
        self.size -= 1
        

def Karp_Rabin(s, t):
    rs = rollingHash()
    rt = rollingHash()
    res = []
    for c in s:
        rs.append(c)
#    print(rs.value)    
    for c in t[:len(s)]:
        rt.append(c)
#        print(rt.value)

    if rs.value == rt.value:
#        print(rt.value)       
        res.append(0)
    for i in range(len(s), len(t)):
        rt.skip(t[i-len(s)])
        rt.append(t[i])
#        print(rt.value)
        if rs.value == rt.value:
            res.append(i-len(s)+1)
    return res

import random
import string
import re

if __name__ == '__main__':
    s = 'aab'
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(1000000))
    
    ans = Karp_Rabin(s,t)
    a = []
    for x in ans:
        a.append(t[x:x+len(s)])
    
    count = 0
    for x in a:
        if x == s:
            count += 1
        
    b = re.findall(s,t)
    print(len(b)-count)

    