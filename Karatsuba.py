# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:44:54 2018

@author: XIN
"""

### Newton's method: x_i+1 = x_i - f(x_i)/f'(x_i)
### To find the square root of a: x_i+1 = 1/2 * (x_i + a/x_i)
import time
import matplotlib.pyplot as plt

def mul(a, b):
    la = len(a)         ### O(1)
    lb = len(b)         ### O(1)
    n = 1
    while 2**n < len(a) or 2**n < len(b):      ###
        n += 1           
    
    a = '0'*(2**n-la) + a        ### O(n)
    b = '0'*(2**n-lb) + b        ### O(n)

    if len(a) <= 2 and len(b) <= 2:
        return str(int(a)*int(b))
    else:
        a0 = low(a)
        a1 = high(a)
        b0 = low(b)
        b1 = high(b)
        c0 = mul(a0, b0)
        c2 = mul(a1, b1)
#        print(mul(add(a0, a1), add(b0, b1)))
#        print('c0=',c0)
#        print('c2=',c2)
        c1 = minus(minus(mul(add(a0, a1), add(b0, b1)), c0), c2)
        c2 = c2 + '0' * 2**n
        c1 = c1 + '0' * 2**(n-1)
        return add(add(c2, c1), c0)
        

def high(a):
    l = len(a)
    return a[:l//2]

def low(a):
    l = len(a)
    return a[l//2:]

def trim(string):
    p = 0
    l = len(string)
    while p < l:
        if string[p] == '0':
            p += 1
        else:
            break
    if p == l:
        return '0'
    else:
        return string[p:]
        

def add(a, b):
###    return str(int(a)+int(b))  ### This is not linear time !!!    
### the following is linear complexity
    
    a = trim(a)
    b = trim(b)    
        
    _sum = ''
    la = len(a)
    lb = len(b)
    l = min(la, lb)
    if la < lb:  # switch a and b so that a is always no shorter than b
        a, b = b, a
        la, lb = lb, la
        
    carry = 0
    for i in range(l):
        temp = (int(a[~i]) + int(b[~i]) + carry)
        digit = temp % 10
        carry = temp // 10
        _sum += str(digit)
        
    while i < la-1:
        if carry == 0:
            _sum += a[:~i][::-1]
            break
        else:
            i += 1
            temp = int(a[~i]) + carry
            digit = temp % 10
            carry = temp // 10
            _sum += str(digit)
    
    if carry == 1:
        _sum += '1'
        
    return _sum[::-1]
                
#print(add('1233123'))

def minus(a, b):
    ### assuming here a is always larger than b, all the operation is defined on the positive integers
    ### linear time complexity
    a = trim(a)
    b = trim(b)    
    
    diff = ''
    l = len(b)
    carry = 0
#    print('a=', a)
#    print('b=', b)
#    
    for i in range(l):
        digit_a = int(a[~i])
        digit_b = int(b[~i])
        if digit_a - carry >= digit_b:
            diff += str(digit_a - carry - digit_b)
            carry = 0
        else:
            diff += str(digit_a + 10 - carry - digit_b)
            carry = 1
            
    while carry == 1:
        i += 1
        digit_a = int(a[~i])
        if digit_a == 0:
            diff += '9'
            carry = 1
        else:
            diff += str(digit_a - carry)
            carry = 0
        
    diff += a[:~i][::-1]
        
    return diff[::-1]
            
    


#a = '12345567881231231123131333132313888'
#b = '12333456677123123113131131331238888'
#print(Karatsuba_mul(a,b)=='152263526617648095227423243968516371732477105725680661152537128076544')
    
### Newton's Method for computing R/b
### f(x) = 1/x - b/R,   f'(x) = -1/x^2
### x_i+1 = 2x_i - bx_i^2/R

def divide(a,b):
    l = 2 * max(len(a), len(b))
#    print(l)
    ans = '1'
    while True:
        temp1 = ans
        temp2 = mul(mul(ans, ans), b)
        if len(temp2) > l:
            ans = minus(mul(ans,'2'), temp2[:-l])
        else:
            ans = mul(ans,'2')
        if temp1 == ans:
            break
    return mul(a, ans)[:-l]
        
    
#print(divide('1000','25'))    
    
     
def root(int1, digit):
    d = int(digit)
    int1 = int1 + '0'*(2*d)
    root = '1'
    while True:
        temp1 = root
        root = divide(add(root, divide(int1, root)), '2')
        if root == temp1:
            break
    return root[:-d] + '.' + root[-d:]

x = []
t = []

#for i in range(5):
#    t1 = time.time()    
#    print(root('2', str(i+1)))
#    t2 = time.time()
#    x.append(i+1)
#    t.append(t2-t1)

for i in range(10):
    
    int1 = '1'*10*2**i
    int2 = '2'*10*2**i
    
    t1 = time.time()    
    mul(int2, int1)
    t2 = time.time()
    print(i)
    print(t2-t1)
    x.append(i)
    t.append(t2-t1)

plt.plot(x, t)
print(t)
    
#print(root('2','5'))    

### mul time complexity test result O(n^(1.854)) worse than expected O(n^(1.585))