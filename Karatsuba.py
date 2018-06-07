# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:44:54 2018

@author: XIN
"""

### Newton's method: x_i+1 = x_i - f(x_i)/f'(x_i)
### To find the square root of a: x_i+1 = 1/2 * (x_i + a/x_i)

def mul(a, b):
    la = len(a)
    lb = len(b)
    n = 1
    while 2**n < len(a) or 2**n < len(b):
        n += 1
    
    a = '0'*(2**n-la) + a
    b = '0'*(2**n-lb) + b 

    if len(a) <= 4 and len(b) <= 4:
        return str(int(a)*int(b))
    else:
        a0 = low(a)
        a1 = high(a)
        b0 = low(b)
        b1 = high(b)
        c0 = mul(a0, b0)
        c2 = mul(a1, b1)
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

def add(a, b):
    return str(int(a)+int(b))

def minus(a, b):
    return str(int(a)-int(b))


#a = '12345567881231231123131333132313888'
#b = '12333456677123123113131131331238888'
#print(Karatsuba_mul(a,b)=='152263526617648095227423243968516371732477105725680661152537128076544')
    
### Newton's Method for computing R/b
### f(x) = 1/x - b/R,   f'(x) = -1/x^2
### x_i+1 = 2x_i - bx_i^2/R

def divide(a,b):
    l = len(a)
    R = '1'+'0'*l
    ans = '1'
    while True:
        temp = ans
        ans = minus(mul(ans,'2'), mul(mul(ans, ans), b)[-l])
        if temp == ans:
            break
    return ans
        
    
print(divide('123333','23'))    
    
    
    
    
#def root(a, d):
#    A = str(a)
#    A = A + '0'*(2*d)
#    while True:
#        x = divide(add(x, divide(A, x)), 2)
    
